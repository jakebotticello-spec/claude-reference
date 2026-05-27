# Freeze Pipeline Spec — apparatus

*file: Freeze_Pipeline_Spec_v1.md · v1 · apparatus S11 · 2026-05-27*
*all decisions in this doc were frozen during apparatus S11, post-export-verification, pre-implementation*

---

## 1. Purpose

Take an Anthropic conversation export and produce a sealed, scrubbed, retrievable snapshot keyed by `(snapshot-id · conv_uuid · msg_uuid)` with the message tree intact. Every later layer of apparatus (substrate, retrieval, per-project anchors) consumes the output of this pipeline. Append-only at snapshot granularity; new exports add new snapshots, never overwrite.

This spec covers Stages 0–4 of the pipeline. It does NOT cover the substrate choice (NEXT MOVE #3 in the v4 anchor), the retrieval interface, the export-cadence helper (#6), or the cross-export uuid-stability check (#8). Those consume this pipeline's output, they don't change its shape.

---

## 2. Inputs — what the pipeline assumes about the export

Current verified shape, as of S11:

· `conversations.json` is the single export file. No sibling files in the bundle observed (S2-confirmed + S11-re-confirmed).
· 294 conversations in the existing archive · 22,801 messages · 67,275 content blocks.
· Conversation object keys: `uuid`, `name`, `summary`, `created_at`, `updated_at`, `account` (object with `uuid` only), `chat_messages` (array of message objects). 7 keys, all present on 294/294.
· Message object keys: `uuid`, `sender` ("human"|"assistant"), `text`, `content` (list of block objects), `created_at`, `updated_at`, `parent_message_uuid`, `attachments`, `files`. 9 keys, all present on 22,801/22,801. No optional fields.
· Root sentinel: messages with no parent use `parent_message_uuid = 00000000-0000-4000-8000-000000000000`. Sentinel value, not null.
· `chat_messages` is a TREE, not a list. Multiple messages can share a parent (branched conversations). The pipeline preserves the tree as-is.
· Content block types observed (5): `text` (28767), `thinking` (13393), `tool_use` (12612), `tool_result` (12489), `token_budget` (14).
· Thinking-block shape: `{type, thinking (str), summaries (list), start_timestamp, stop_timestamp, cut_off, truncated, alternative_display_type, flags, signature}`. `signature` is null in export (stripped); the rest are populated.

If a future export shape changes any of the above (new sibling file, new block type, new field on any object), the pipeline must surface the change rather than silently absorb it — see §6, schema drift.

---

## 3. Outputs — what the pipeline produces

For each snapshot processed, a directory under `apparatus-archive/snapshots/`:

```
snapshots/
  baseline-{YYYY-MM-DD}-{sha256[:8]}/    ← initial backfill snapshot (run once)
    raw.json                              ← full conversations.json, sealed read-only
    manifest.json                         ← snapshot metadata (see §5.1)
    scrub-v1/                             ← scrubbed view under v1 regex set
      conversations.scrubbed.json
      scrub-audit.jsonl
      verify.log
      records.ndjson
    scrub-v2/                             ← generated later if regex set evolves
      ...
  delta-{YYYY-MM-DD}-{sha256[:8]}/        ← daily delta snapshot
    raw.json                              ← just new uuids since last snapshot, sealed
    manifest.json
    scrub-v1/
      conversations.scrubbed.json
      scrub-audit.jsonl
      verify.log
      records.ndjson
  delta-{YYYY-MM-DD}-{sha256[:8]}/
    ...
  ledger.jsonl                            ← append-only registry of all snapshots
```

Two snapshot types: `baseline-` (the one-time full ingest of the existing archive) and `delta-` (every export after that). Same internal structure for both — the only difference is whether `raw.json` is the full export or a uuid-filtered slice.

---

## 4. Stages

### Stage 0 — Pre-implementation probes

Four small probes against the existing archive must close before Stage 1 implementation begins. Each follows the protocol used for the S11 thinking-block probe: sanitized skeletons only (length placeholders for string values; never actual content; uuids only as references).

· **0.1 Non-thinking block field shapes.** One sanitized skeleton each for `text`, `tool_use`, `tool_result`, `token_budget`. Full key set, type per value, length placeholders. **`tool_result` is the prime cred vector — its shape directly affects scrub correctness.**
· **0.2 Attachments and files.** Find conversations with non-empty `attachments` and non-empty `files` on at least one message. Sample one of each. Key question: **is file content inlined in the export, referenced by handle, or both?** This determines whether the scrub-walk needs to descend into them.
· **0.3 Summaries entry shape.** One sanitized skeleton of a single entry from a thinking block's `summaries` list. Field set, types, length placeholders.
· **0.4 Token-budget block shape.** 14 instances across the archive — what are they? Single sanitized skeleton.
· **0.5 Field-semantics characterization for `name` and `summary`.** Sample a handful of conversations: how often is each field populated, how often empty, observable signs of user-rename vs model-authorship (e.g., does `summary` tend to read as descriptive prose while `name` reads as title-cased keywords). This is the last hedge on the floor-scoping decision — even though both are dropped at ingest under the corrected S11 floor rule, characterizing their actual semantics confirms the symmetric-drop is correct and lets future-Claude resist any "but `name` is more durable" re-litigation.

If any probe surfaces something architecturally unexpected (a new content type, an inlined-file path nobody saw, a field shape that breaks the scrub-walk model), the spec gets a v2 before Stage 1 proceeds.

### Stage 1 — Freeze

Action sequence:

1. Compute the snapshot's content (see §4.1.1 baseline vs §4.1.2 delta).
2. Compute snapshot-id: `{baseline|delta}-{YYYY-MM-DD}-{sha256[:8]}`. Date is the export's mtime. Hash is the first 8 hex of the sha256 of the snapshot's content. Both included so a same-day re-export produces a distinct id and cannot collide silently.
3. Create the snapshot directory.
4. Write `raw.json` containing the snapshot's content. Set the file read-only (chmod 0444 or platform equivalent). After this, the file is never opened for write again.
5. Write `manifest.json`:
   ```
   {
     snapshot_id, type ("baseline"|"delta"),
     source_export_path, source_export_mtime, source_export_sha256_full,
     raw_sha256_full, raw_byte_size,
     conv_count, message_count, content_block_count,
     prior_snapshot_id (null for baseline; the last snapshot in the ledger for delta),
     frozen_at
   }
   ```
6. Append to `snapshots/ledger.jsonl`.

After Stage 1, `raw.json` inside the snapshot dir is the authoritative input to every downstream stage. The original export file outside the snapshots tree may be deleted at user discretion — the freeze is what matters.

#### 4.1.1 Baseline content

The very first run. `raw.json` contains the full export verbatim. Used once, against the existing 366MB archive.

#### 4.1.2 Delta content

Every subsequent run. The pipeline:

· Builds a set of every `(conv_uuid, msg_uuid)` already present in any prior snapshot (read from each prior snapshot's `raw.json`, or from a cached uuid index built incrementally — see §6 performance).
· Reads the new export.
· Filters: only conversations and messages whose `msg_uuid` is NOT in the prior set are included in the delta.
· If a conversation has any new messages, the conversation header (`uuid`, `name`, `summary`, `created_at`, `updated_at`, `account`) is included alongside the new messages.
· `raw.json` contains the resulting filtered structure — same JSON shape as the full export, just narrower.

**The filter is uuid-based, never date-based.** Date is not used as a filter, hint, or proxy. UUIDs are intrinsic to messages and survive any backdating, dormancy, or skipped-export edge cases. (Considered using date as a performance hint during S11 spec — rejected as a second mechanism doing the same job, an unnecessary drift surface.)

### Stage 2 — Scrub

**Walk model: type-agnostic recursive descent over the JSON.** For every string value at any depth — message text, content-block fields, summaries, attachments, files, conv-level fields — run the cred regex set against it.

**Why type-agnostic:** the S10 cred scan worked this way (CC noted at S11: "content was JSON-serialized before regex application"). It's also forward-compatible — if Anthropic adds a new block type, the scrub still catches creds inside it. A type-aware scrub creates blind spots whenever the schema evolves.

**Cred regex set v1 (initial):**

· RTSP with embedded auth: `rtsp://[^:\s]+:[^@\s]+@`
· Postgres/Supabase conn strings: `postgres(ql)?://[^:\s]+:[^@\s]+@`
· OpenAI keys: `sk-[A-Za-z0-9_-]{20,}` (excluding `sk-ant-` matches — those are below)
· Anthropic keys: `sk-ant-[A-Za-z0-9_-]{20,}`
· Stripe secret/restricted: `(sk|rk)_live_[A-Za-z0-9]{20,}` (publishable `pk_live_` keys are NOT secret material and not redacted by default)

The set is extensible. New patterns are added when discovered. Adding a pattern does NOT modify any sealed scrubbed file — see §4.2.1 versioning.

**Redaction format:** substring replacement.
`[REDACTED:{cred_class}:{conv_uuid}:{msg_uuid}:{block_index}]`

Class is preserved (downstream context: "this was a postgres conn string" is useful metadata). Value is gone. Pointers preserve the audit correlation.

**Audit log** (`scrub-audit.jsonl`, append-only during the run):
```
{timestamp, cred_class, conv_uuid, msg_uuid, block_index, char_offset_in_block, original_length}
```
Never the value. Original length captured so analytical questions like "how big was the leak" can be answered without re-exposure.

#### 4.2.1 Scrub versioning

The scrub regex set IS versioned. When the set evolves, sealed snapshots get re-scrubbed under the new version as an overlay — never in-place.

Process when adding pattern set v2:
1. For each existing snapshot directory: create `scrub-v2/` alongside the existing `scrub-v1/`.
2. Re-run Stages 2, 3, 4 against `raw.json` under the v2 pattern set, writing results into `scrub-v2/`.
3. `scrub-v1/` remains sealed and queryable; `scrub-v2/` becomes the new default for retrieval.
4. The retrieval layer is told which scrub-version is current.

This preserves append-only (no scrubbed file ever mutates) while letting the regex set evolve. The original sealed `raw.json` is the true floor; scrubbed views are versioned interpretations of it.

Pointers carry scrub-version only when ambiguous: `(snapshot-id, conv_uuid, msg_uuid)` against the current scrub-version is sufficient until a re-scrub is in progress. Cross-version pointer comparison adds `scrub-version` to the tuple.

### Stage 3 — Verify-clean

Re-run the full cred regex set against `scrub-vN/conversations.scrubbed.json`.

**Pass:** zero hits across the entire file. Write `verify.log`:
```
{passed: true, scrub_version, scanned_bytes, scanned_strings,
 regex_hits_per_class: {RTSP: 0, postgres: 0, openai: 0, anthropic: 0, stripe: 0}}
```
Proceed to Stage 4.

**Fail:** any hit. **Hard stop.** Move the scrubbed file to `quarantine/{snapshot-id}/scrub-vN/` for forensic review. Write `verify.log` with the failing pattern + count + first few sanitized pointer references (uuids only, never the matched value). **Do NOT proceed to Stage 4.** The regex must be extended and Stage 2 re-run, or the input must be repaired, before ingest can occur.

**Why a hard stop, not a warning:** an immutable store with a cred in it is an immortal leak. The whole point of scrub-at-freeze is that you don't ingest unless you've proven clean. The scrub regex is by definition the same set used at Stage 2 and Stage 3, so a Stage 3 hit means a Stage 2 implementation bug — that needs fixing, not warning past.

### Stage 4 — Ingest

Per-message record written to `records.ndjson` (one JSON object per line, append-only during the run):

```
{
  snapshot_id, scrub_version,
  conv_uuid, conv_name,
  msg_uuid, parent_message_uuid,
  sender, created_at, updated_at,
  text, content_blocks,
  attachments, files,
  is_root  // true when parent_message_uuid == 00000000-0000-4000-8000-000000000000
}
```

Per-conversation header written first per conv (one line per conv):
```
{
  record_type: "conversation_header",
  snapshot_id, scrub_version,
  conv_uuid,
  created_at, updated_at, account_uuid,
  message_count, has_branches  // any msg that is parent to ≥2 children
}
```

**Conversation-level `name` and `summary` are BOTH dropped at ingest.** Both fields are user-affected and not stable model-authored evidence: `name` is the user-renameable sidebar title (Jake renames every session); `summary` is model-generated and may evolve. Neither qualifies as floor; both fail symmetric application of the floor rule. Carrying either would treat session-affected metadata as evidence — a category error. Human-readable labels at retrieval are derived from the message stream itself, or live in per-project anchors. See §5.

**Order:** conversations written in `created_at` order; within each conversation, messages in `created_at` order. **Branches preserved** — every node lands as its own record with its real `parent_message_uuid`. No flattening, no branch selection.

**Sealing:** after Stage 4 completes for a given scrub-version, the `scrub-vN/` directory contents are set read-only. New scrub versions get their own directory; existing ones are never modified.

---

## 5. Invariants (load-bearing)

These are the rules the pipeline enforces, not just intentions. A violation here is an architectural bug.

· **5.1 Original export is preserved.** `raw.json` inside any snapshot dir is read-only after Stage 1.
· **5.2 Append-only at snapshot granularity.** Sealed snapshots never mutate. Regex updates create new scrub-versions, not patched files.
· **5.3 The message stream is floor.** Every user message and every assistant message is preserved verbatim through scrub and ingest. The scrub redacts cred *substrings* within content; it never discards a message, never modifies a message uuid, never alters parent-child structure. User messages and assistant messages are equal floor citizens.
· **5.4 Floor scope: per-message content yes, conv-level mutable metadata no.** Per-message content (text, content blocks, attachments, files, timestamps, uuids, sender) IS floor. Conversation-level metadata that's user-affected — both `name` (user-renameable title) and `summary` (model-generated, may evolve) — is NOT floor. Both are dropped at ingest. Conversation headers carry only stable structural data (uuids, timestamps, counts, branch-bool). Human-readable labels live at retrieval time, derived from the message stream, or in per-project anchors — not in snapshot headers.
· **5.5 Scrub walks all strings recursively.** Type-agnostic. Future-proof against schema evolution.
· **5.6 Verify is a hard gate.** No cred in the scrubbed file, or no ingest from that scrub run.
· **5.7 Branches preserved.** `chat_messages` is a tree; the parent chain is verbatim.
· **5.8 Pointer is `(snapshot-id, conv_uuid, msg_uuid)`.** All three needed — snapshot-id because exports accumulate; conv+msg uuids because they're the intrinsic addresses. Scrub-version added only when cross-version comparison is in scope.
· **5.9 The filter at delta-build is uuid-based, never date-based.** Date is not a filter, not a hint, not a proxy.
· **5.10 The audit log is the only place that knows redactions existed.** The scrubbed file knows class; the audit log knows position. Neither knows the value.

---

## 6. Implementation notes

· **Language: Python.** Standard library + `re` is sufficient. No DB dependency, no third-party deps at this layer.
· **Idempotency:** re-running on the same export must produce the same snapshot-id (deterministic from mtime + content sha256) and must refuse to overwrite a sealed snapshot. Detect by checking the ledger; refuse with an explicit error.
· **Performance:** the existing 366MB archive parses in seconds. The cred scrub regex against ~283MB of content (the JSON-serialized content total) is single-pass. No optimization needed at v1.
· **UUID index for delta filtering:** read each prior snapshot's `raw.json` and build the seen-uuids set at delta-run time. If this becomes slow as snapshots accumulate, cache an incremental index — but defer the optimization until measured. (Likely never necessary; uuid sets are tiny relative to content.)
· **Schema drift:** if the parser encounters a field or block type not in this spec's known set (§2), it surfaces a warning + writes a `schema-drift.jsonl` entry inside the snapshot dir. Stages 2–4 continue (the type-agnostic scrub still walks strings). A schema-drift warning is a signal to update the spec, not a hard stop.
· **Testing:** initial baseline run against the existing 366MB archive should produce: 1 baseline snapshot, scrub-v1 with audit showing 97 RTSP + 55 postgres + 6 OpenAI redactions (S10 cred-scan counts), verify-clean PASS, records.ndjson containing 22,801 message records + 294 conversation headers.

---

## 7. What this spec deliberately does not cover

Out of scope for this artifact. Each lives behind its own seam in the pipeline.

· **Substrate choice** (NEXT MOVE #3). The `records.ndjson` is the substrate-agnostic handoff. Supabase, memvid, claude-mem's rig — any of them ingests from ndjson. Substrate decision is downstream.
· **Retrieval interface.** Substrate-dependent.
· **Export-cadence helper** (NEXT MOVE #6). Wraps Stage 1 (watch Downloads folder, trigger pipeline) but doesn't change pipeline behavior.
· **Cross-export uuid stability check** (NEXT MOVE #8). Done at next natural export by diffing a known message across two snapshots. Design absorbs both outcomes via snapshot-id.
· **Anchor/graveyard capture format.** Contextual-commits adopted at S10; orthogonal to this pipeline.
· **Per-project anchor passes** (NEXT MOVE #7). Build on top of ingested records; not part of the freeze pipeline itself.

---

## 8. Change log

· v1 · 2026-05-27 · apparatus S11 · initial freeze. Folded: S11 export verification (5 block types confirmed, thinking-block schema confirmed, conv-level fields identified as user-affected non-floor); delta-ingest via pure uuid-diff (date dropped as filter mechanism); scrub versioning via overlay (`scrub-vN/` dirs under each snapshot); floor-rule clarified (message stream is floor; conv-level mutable metadata is not; user messages and assistant messages equal). **Pre-commit correction:** initial draft of this spec carried `conv_name` in headers as a mutable index hint while dropping `summary` — inverted field semantics (the actively user-mutated field is `name`, not `summary`). Caught by peer-instance review of the S11 ignition prompt before bundle reached the repo. Symmetric drop landed: both `name` and `summary` out. Added Stage 0 probe 0.5 (field semantics) to close the residual hedge. Pre-Stage-1 work blocked on §4 Stage 0 probes (now five).

---

*Anchored 2026-05-27 by apparatus S11 (Jake + orchestrator-Claude). The spec is product of the S11 export-verification probes (thinking-in-export closed; content-block-type enumeration in hand) and the S11 redirect-correction work on the pipeline architecture (delta-ingest, versioned scrub, floor-rule scoping). It supersedes the chat-only "spec v1" sketched at S11 turn 9 — that draft contained a floor-rule bug (would have implicated user messages) and a date-as-filter hint (redundant with uuid-diff); both fixed here. The v4 anchor's NEXT MOVE #2 is satisfied by this spec for the architecture; implementation is gated on Stage 0 probes.*
