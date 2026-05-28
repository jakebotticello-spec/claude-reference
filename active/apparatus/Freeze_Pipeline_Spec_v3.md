# Freeze Pipeline Spec — apparatus

*file: Freeze_Pipeline_Spec_v3.md · v3 · apparatus S13 · 2026-05-28*
*v1 was frozen at S11 close, post-export-verification. v2 incorporated S12's population-scale corrections from the safety + robustness probes against the full 366MB archive. v3 reconciles the spec text with what the S13 implementation actually landed: §4.0.5 ANSWERED (symmetric-drop ratified), §6 idempotency refined (dry-run exemption), §6 schema-drift coverage corrected to match the v1.0 code (type-level only). No architectural change — Stages 1–4 implemented from v2 with zero structural deviations; v3 is a fidelity pass on three text-level drifts.*

---

## 1. Purpose

Take an Anthropic conversation export and produce a sealed, scrubbed, retrievable snapshot keyed by `(snapshot-id · conv_uuid · msg_uuid)` with the message structure intact. Every later layer of apparatus (substrate, retrieval, per-project anchors) consumes the output of this pipeline. Append-only at snapshot granularity; new exports add new snapshots, never overwrite.

This spec covers Stages 0–4 of the pipeline. It does NOT cover the substrate choice (NEXT MOVE #3 in the v6 anchor), the retrieval interface, the export-cadence helper (#6), or the cross-export uuid-stability check (#8). Those consume this pipeline's output; they don't change its shape.

---

## 2. Inputs — what the pipeline assumes about the export

Current verified shape, population-scale, as of S12:

### 2.1 Top-level structure

· `conversations.json` is the single export file. No sibling files in the bundle (S2-confirmed + S11-re-confirmed + S12 safety probe re-confirmed).
· 294 conversations in the existing archive · 22,801 messages · 67,275 content blocks.
· Conversation object: 7 keys, all present on all 294 conversations. Keys: `uuid`, `name`, `summary`, `created_at`, `updated_at`, `account` (object with `uuid` only — no name or email), `chat_messages` (array of message objects).
· Message object: 9 keys, all present on all 22,801 messages, no optional fields. Keys: `uuid`, `sender` ("human"|"assistant"), `text`, `content` (list of content block objects), `created_at`, `updated_at`, `parent_message_uuid`, `attachments` (list), `files` (list).
· **`uuid` global uniqueness within archive: CONFIRMED.** 22,801/22,801 msg_uuids globally unique; 294/294 conv_uuids unique (S12 robustness probe Checks 1+2).

### 2.2 Tree-or-forest structure

· `chat_messages` is a **tree or forest** [S12 correction; was "tree" in v1]. Population breakdown (S12 robustness probe Check 3):
  - 282/294 conversations: single-rooted trees (the common case).
  - 9/294 conversations: forests with 2–6 sentinel roots each (parallel threads in the same conv). Largest: conv `b5cefa7c` with 6 roots.
  - 3/294 conversations: empty (0 messages — pipeline writes 0 records for these).
· Root sentinel: messages with no parent use `parent_message_uuid = 00000000-0000-4000-8000-000000000000`. Sentinel value, not null. All 304 root-position messages across all conversations use exactly this sentinel (S12 Check 4).
· Multiple messages can share a parent (branched conversations). The pipeline preserves the structure as-is.

### 2.3 Content block types — 5 enumerated, population-confirmed

Across 67,275 blocks (S11 + S12 Check 10):
· `text` (28,767) — visible text content. Field: `text` (str).
· `thinking` (13,393) — model reasoning. Schema: `{type, thinking (str), summaries (list), start_timestamp, stop_timestamp, cut_off (bool), truncated (bool), flags (null), alternative_display_type (null), signature}`.
· `tool_use` (12,612) — tool invocation. Schema: `{type, name (str), input (dict), display_content (object — see §2.4), integration_icon_url, integration_name, mcp_server_url, is_mcp_app, icon_name, message, approval_key (mostly null), context (null)}`.
· `tool_result` (12,489) — tool output. Schema: `{type, content (list — see §2.5 for item types), display_content (object — see §2.4), integration_icon_url, integration_name, mcp_server_url, is_mcp_app, icon_name, message, meta (null), structured_content (mostly null)}`.
· `token_budget` (14) — token-budget annotation. Schema: `{type, remaining (null)}`. Single field besides type.

No sixth content-block type exists at any frequency across the archive (S12 Check 10).

### 2.4 `display_content` cluster

[NEW IN v2 — not in S11 enumeration; surfaced by S12 robustness probe.]

Present on all 25,101 tool blocks (`tool_use` + `tool_result`). Object shape (fields appear conditionally):
· `json_block` (str up to 1,000,381 chars, 11,114 occurrences) — serialized JSON of tool output. **Cred vector — walked by scrub.** Always a string (never an object); scrub applies uniformly.
· `text` (str, 7,251 occurrences).
· `table` (list, 1,156 occurrences).
· `code` (str, 143 occurrences).
· `link` (dict, 154 occurrences) — contains `resource_type` and `subtitles` both 100% null (strip set).
· `content[]` (list of items, 925 occurrences) — display search results; sub-items have `icon_url` and `source` both 100% null (strip set).
· `filename`, `is_trusted`, `language` (minor fields).

### 2.5 `tool_result.content[]` item types

[NEW IN v2 — surfaced by S12 robustness probe Check 12.]

5 distinct item types across 18,667 items in tool_result content lists:
· `text` (64.9%) — `{type, text, url, title, uuid, metadata, ...}`. Max 1,000,381 chars in `text` field. Primary tool-output content vector inside tool_result.
· `knowledge` (21.8%) — web search results. Same shape as `text` plus `is_citable`, `is_missing`, `links[]`, `prompt_context_metadata`.
· `local_resource` (9.8%) — `{type, file_path, file_uuid, mime_type, name, uuid}`. **File references only, no inline binary content.** MIME types present (tar, PNG, SVG, PDF, STL, Word, zip, etc.) all appear as references; the binary itself is not in the export.
· `image` (3.4%) — `{type, file_uuid, uuid}`. UUID reference only.
· `image_gallery` (0.0%, very rare) — `{type, images[], is_expired, uuid}`.

### 2.6 Thinking-block `signature` field

[CORRECTED IN v2 — v1 claimed `signature` was null in export (stripped). S12 robustness probe Check 9 falsified at population scale.]

· Population: 8,087/13,393 thinking blocks (~60%) carry a non-null `signature`. ~40% are null.
· Length: range 196–211,384 chars, median ~1,092.
· Character class: 100% base64 charset (sampled byte-class: 38.8% lower / 44.4% upper / 13.3% digit / 3.5% `/+=`; 0% other). All observed signatures share an `E`-prefix pattern.
· Interpretation: cryptographic provenance metadata over the thinking content. Anthropic includes it in the export by design; treat as opaque base64 blob.
· Pipeline handling: walked by recursive scrub as a string. Regex set will not match (no cred-pattern matches base64-of-signature). No operational impact.

### 2.7 `summaries[]` entry shape

[NEW IN v2 — surfaced by S12 safety probe.]

Each entry in a thinking block's `summaries` list is a single-field dict: `{summary: str}`. No type field, no token markers.
· Lengths: 11–359 chars (median 64).
· List lengths per thinking block: 0–106 entries (median 2).

### 2.8 Attachments and files

[NEW IN v2 — surfaced by S12 safety probe.]

· `attachments[]`: 884 total objects. Each carries `extracted_content` (str up to 1,466,728 chars, median 10,922) — **inlined file text. Cred vector class.** Plus `file_name` (str, often empty), `file_size` (int), `file_type` (str). Scrub walks `extracted_content` via recursive descent.
· `files[]`: 4,102 total objects. Carries `file_uuid` (str, UUID, always 36 chars) + `file_name` (str, sometimes null). **Reference-only, no inline binary content.** Floor does NOT carry file bytes from this field.

### 2.9 MCP and tool metadata

[NEW IN v2 — surfaced by S12 robustness probe.]

Present on tool_use + tool_result blocks:
· `integration_icon_url`, `integration_name`, `mcp_server_url`, `is_mcp_app`, `icon_name`, `message` — MCP server metadata.
· `approval_key` (str, 81–84 chars, 13 non-null hits out of 12,612 tool_use blocks). **Benign** — clusters entirely on Google Calendar MCP per-operation auth (`create_event`, `list_calendars`, `list_events`, `update_event`). Not an Anthropic-internal identifier.
· `structured_content` (12,489 occurrences on tool_result, ~99.9% null). When non-null, Google Calendar API response data.

### 2.10 The 9-path strip set

[NEW IN v2 — surfaced by S12 safety probe Section 2.]

9 paths are 100% null across the full archive — Anthropic deliberately strips them. The apparatus principle is "we don't reconstruct what the export strips":
· `content[].flags` (all 67,275 blocks)
· `content[].alternative_display_type` (all 13,393 thinking blocks)
· `content[].context` (all 12,612 tool_use blocks)
· `content[].meta` (all 12,489 tool_result blocks)
· `content[].remaining` (all 14 token_budget blocks)
· `display_content.content[].icon_url` (4,155)
· `display_content.content[].source` (4,155)
· `display_content.link.resource_type` (154)
· `display_content.link.subtitles` (154)

### 2.11 Schema drift surface

If a future export shape changes any of §2.1–2.10 (new sibling file, new block type, new field on any object, new content-list item type), the pipeline must surface the change rather than silently absorb it — see §6, schema drift.

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
  ledger.jsonl                            ← append-only registry of all snapshots
```

Two snapshot types: `baseline-` (the one-time full ingest of the existing archive) and `delta-` (every export after that). Same internal structure for both — the only difference is whether `raw.json` is the full export or a uuid-filtered slice.

---

## 4. Stages

### Stage 0 — Pre-implementation probes

The original Stage 0 probe list (§4.0.1–§4.0.5) was substantially absorbed by S12's two pre-Stage-0 probes (safety + robustness), which ran broader sweeps and population-scale verifications.

· **§4.0.1 Non-thinking block field shapes** (text, tool_use, tool_result, token_budget) — **ANSWERED.** See `apparatus-scratch/robustness_probe_output.md` Checks 11–12 + the field-presence table in Check 6, supplemented by safety probe field-path inventory. Documented in §2.3 + §2.4 + §2.5.
· **§4.0.2 Attachments and files inline-vs-reference** — **ANSWERED.** See `apparatus-scratch/safety_probe_output.md`. Documented in §2.8.
· **§4.0.3 Summaries entry shape** — **ANSWERED.** See `apparatus-scratch/safety_probe_output.md`. Documented in §2.7.
· **§4.0.4 Token-budget block shape** — **ANSWERED.** Single field besides type: `remaining`, 100% null (strip set). Documented in §2.3 + §2.10.
· **§4.0.5 Field-semantics characterization for `name` and `summary`** — **ANSWERED (ratified S13).** See `apparatus-scratch/stage0_probe_output.md`. Findings: `name` 276/294 populated (median 33 chars, 97.1% title/fragment), `summary` 146/294 populated (median 2519 chars, 100% sentence-prose, never <700); both always-string never-null; 0 summary-only convs (name gates summary); summary population non-monotonic with message count (the "may evolve" property). The symmetric-drop decision is CONFIRMED — both fields are conv-level user-affected metadata, neither floor, neither derivable-without-itself; both dropped at ingest. The shape difference (fragment vs prose) is real but irrelevant to the floor-scoping rationale. No spec change resulted from §4.0.5 itself; the existing decision held at population scale.

If §4.0.5 surfaces something architecturally unexpected, the spec gets a v3 before Stage 1 proceeds. Otherwise Stage 1 opens at S13.

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

· Builds a set of every `(conv_uuid, msg_uuid)` already present in any prior snapshot (read from each prior snapshot's `raw.json`, or from a cached uuid index built incrementally).
· Reads the new export.
· Filters down to conversations + messages whose `(conv_uuid, msg_uuid)` is NOT in the seen set.
· `raw.json` for the delta snapshot contains only the new content. Same internal structure (conversations.json shape, just fewer rows).

**Filter is pure uuid-set-difference; date is never used as filter, hint, or proxy.** [Invariant 5.9.]

### Stage 2 — Scrub

Type-agnostic recursive descent over JSON strings. Walks every string value at every nesting depth — `chat_messages[].text`, `chat_messages[].content[].text`, `chat_messages[].content[].thinking`, `chat_messages[].content[].input.*`, `chat_messages[].content[].display_content.json_block`, `chat_messages[].content[].content[].text`, `chat_messages[].attachments[].extracted_content`, every other string-typed field at any depth.

The scrub never decides "this field is safe to skip." Future schema additions are walked automatically.

#### 4.2.1 Regex set v1 (locked at S12)

Pattern set:
· RTSP creds: `rtsp://[^/\s:]+:[^/\s@]+@`
· Postgres/Supabase conn strings: `postgres(ql)?://[^/\s:]+:[^/\s@]+@`
· OpenAI: `sk-[A-Za-z0-9_-]{20,}` (excluding `sk-ant-`)
· Anthropic: `sk-ant-[A-Za-z0-9_-]{20,}`
· Stripe live secret/restricted: `(sk|rk)_live_[A-Za-z0-9]{20,}`

Each match: replace the matched substring with a class token (`<RTSP_CRED_REDACTED>`, `<POSTGRES_CRED_REDACTED>`, `<OPENAI_KEY_REDACTED>`, `<ANTHROPIC_KEY_REDACTED>`, `<STRIPE_KEY_REDACTED>`) and append an audit entry to `scrub-audit.jsonl`:
```
{snapshot_id, scrub_version, conv_uuid, msg_uuid, json_path, pattern_class, redaction_token, original_length}
```
Audit knows the position + class + length; it never knows the value. The value is gone from disk after scrub.

#### 4.2.2 Scrub versioning

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

**Why a hard stop, not a warning:** an immutable store with a cred in it is an immortal leak. The whole point of scrub-at-freeze is that you don't ingest unless you've proven clean. S12's robustness probe found Anthropic API keys inside thinking blocks — without the proactive `sk-ant-` regex, those would have landed in the immutable corpus permanently. The proactive-patterns-beyond-observed-leaks principle is what's protecting us here.

### Stage 4 — Ingest

Per-message record written to `records.ndjson` (one JSON object per line, append-only during the run):

```
{
  snapshot_id, scrub_version,
  conv_uuid,
  msg_uuid, parent_message_uuid,
  sender, created_at, updated_at,
  text, content_blocks,
  attachments, files,
  is_root  // true when parent_message_uuid == 00000000-0000-4000-8000-000000000000
}
```

[v2 correction: `conv_name` removed from per-message record. v1 carried `conv_name` here while §5.4 invariant said both `name` and `summary` are dropped at ingest — that was a propagation miss from the S11 inversion correction, caught at S12 turn 8. Both fields now correctly dropped at every layer of ingest output.]

Per-conversation header written first per conv (one line per conv):
```
{
  record_type: "conversation_header",
  snapshot_id, scrub_version,
  conv_uuid,
  created_at, updated_at, account_uuid,
  message_count,
  has_branches,  // any msg that is parent to ≥2 children
  multi_root     // true if conv has >1 sentinel-root message (the 9/294 forest case)
}
```

[v2 addition: `multi_root` boolean. 9/294 convs in the existing archive have 2–6 sentinel roots; retrieval needs to know the conversation isn't a single linear thread to walk. Orthogonal to `has_branches` (a conv can be single-root with branches, multi-root without, or both).]

**Conversation-level `name` and `summary` are BOTH dropped at ingest.** Both fields are user-affected and not stable model-authored evidence: `name` is the user-renameable sidebar title (Jake renames every session); `summary` is model-generated and may evolve. Neither qualifies as floor; both fail symmetric application of the floor rule. Human-readable labels at retrieval are derived from the message stream itself, or live in per-project anchors. See §5.

**Order:** conversations written in `created_at` order; within each conversation, messages in `created_at` order. **Branches AND multi-root preserved** — every node lands as its own record with its real `parent_message_uuid`. No flattening, no branch selection, no root selection.

**Sealing:** after Stage 4 completes for a given scrub-version, the `scrub-vN/` directory contents are set read-only. New scrub versions get their own directory; existing ones are never modified.

---

## 5. Invariants (load-bearing)

These are the rules the pipeline enforces, not just intentions. A violation here is an architectural bug.

· **5.1 Original export is preserved.** `raw.json` inside any snapshot dir is read-only after Stage 1.
· **5.2 Append-only at snapshot granularity.** Sealed snapshots never mutate. Regex updates create new scrub-versions, not patched files.
· **5.3 The message stream is floor.** Every user message and every assistant message is preserved verbatim through scrub and ingest. The scrub redacts cred *substrings* within content; it never discards a message, never modifies a message uuid, never alters parent-child structure. User messages and assistant messages are equal floor citizens.
· **5.4 Floor scope: per-message content yes, conv-level mutable metadata no.** Per-message content (text, content blocks, attachments, files, timestamps, uuids, sender) IS floor. Conversation-level metadata that's user-affected — both `name` (user-renameable title) and `summary` (model-generated, may evolve) — is NOT floor. Both are dropped at ingest at every layer of output. Conversation headers carry only stable structural data (uuids, timestamps, counts, branch + multi-root flags). Human-readable labels live at retrieval time, derived from the message stream, or in per-project anchors — not in snapshot headers.
· **5.5 Scrub walks all strings recursively.** Type-agnostic. Future-proof against schema evolution. S12 finding: this design absorbed three new field clusters (`display_content`, MCP metadata, `attachments[].extracted_content`) without code change. The invariant proves itself in practice.
· **5.6 Verify is a hard gate.** No cred in the scrubbed file, or no ingest from that scrub run.
· **5.7 Branches AND multi-root preserved.** [v2 expansion of v1 5.7.] `chat_messages` is a tree or forest; both the parent chain and the multi-root case are preserved verbatim through ingest. `is_root` per-message + `multi_root` per-conv-header flag handle the structural variation.
· **5.8 Pointer is `(snapshot-id, conv_uuid, msg_uuid)`.** All three needed — snapshot-id because exports accumulate; conv+msg uuids because they're the intrinsic addresses. Population-validated at S12 (22,801/22,801 msg_uuids globally unique; 294/294 conv_uuids unique). Scrub-version added only when cross-version comparison is in scope.
· **5.9 The filter at delta-build is uuid-based, never date-based.** Date is not a filter, not a hint, not a proxy.
· **5.10 The audit log is the only place that knows redactions existed.** The scrubbed file knows class; the audit log knows position. Neither knows the value.
· **5.11 Sampling floor: field-population semantics claims require whole-archive scans.** [v2 addition.] Probes that characterize field presence, populate rate, value semantics, or population distribution use whole-archive scans, not N-of-5 samples. Five-sample probes are skeleton-shape probes only — adequate for "what fields exist on this block type" but inadequate for "how often is field X populated" or "what does field X look like across the population." The v5 anchor's `signature`-is-stripped claim was a five-sample coincidence on a ~60%-populated field; the same failure mode could land on any field below ~50% population. Cost of whole-archive scan on 366MB: seconds. Cost of a stable wrong answer in canon: high.

---

## 6. Implementation notes

· **Language: Python.** Standard library + `re` is sufficient. No DB dependency, no third-party deps at this layer.
· **Idempotency:** re-running on the same export must produce the same snapshot-id (deterministic from mtime + content sha256) and the **real run** must refuse to overwrite a sealed snapshot — detect by checking the ledger / snapshot-dir existence, refuse with an explicit error before any write. **Dry-run is exempt** [v3 / S13 v1.2 refinement]: a dry-run writes nothing, so there is no overwrite to guard; when a snapshot for the computed id already exists, dry-run prints an informational NOTE and still reports counts + snapshot-id rather than refusing. The no-overwrite guard protects the write path only; dry-run stays re-runnable against an existing baseline.
· **Performance:** the existing 366MB archive parses in seconds. The cred scrub regex against ~283MB of content (the JSON-serialized content total) is single-pass. No optimization needed at v1/v2.
· **UUID index for delta filtering:** read each prior snapshot's `raw.json` and build the seen-uuids set at delta-run time. If this becomes slow as snapshots accumulate, cache an incremental index — but defer the optimization until measured. (Likely never necessary; uuid sets are tiny relative to content.)
· **Schema drift:** the §2.11 drift *surface* is broad (new sibling file, new block type, new field on any object, new content-list item type). The **v1.0 implementation detects a subset of it: type-level drift only** — new content-block types and new `tool_result.content[]` item types, checked against the enumerated sets in §2.3 + §2.5. **Field-level additions on existing objects are NOT detected at v1.0** (a new field on an existing block would pass silently; the type-agnostic scrub still walks its strings, but no drift entry is written). On a detected type-level drift, the pipeline surfaces a warning + writes a `schema-drift.jsonl` entry inside the snapshot dir (real run only — dry-run surfaces the warning to stderr but has no snapshot dir to write into); Stages 2–4 continue (warn-not-stop). A schema-drift warning is a signal to update the spec, not a hard stop. **Field-level drift detection is a v1.1 expansion** (requires an allowlist of known fields per object type); until then, a field-level change relies on a human noticing at the next export — tracked as a downstream flag.
· **Testing (v2 baseline):** initial baseline run against the existing 366MB archive should produce: 1 baseline snapshot, scrub audit with **population-confirmed cred counts: 177 RTSP + 76 Postgres + 10 OpenAI + 10 Anthropic + 0 Stripe** (S12 robustness probe Check 5 — supersedes v1's S10-based "97 RTSP + 55 Postgres + 6 OpenAI" testing note, which undercounted by walking a narrower path set), verify-clean PASS, records.ndjson containing 22,801 message records + 294 conversation headers (with `multi_root = true` on 9 of those 294 + `message_count = 0` on 3 of them).

---

## 7. What this spec deliberately does not cover

Out of scope for this artifact. Each lives behind its own seam in the pipeline.

· **Substrate choice** (NEXT MOVE #3). The `records.ndjson` is the substrate-agnostic handoff. Choice gates on SCDD's Substrate_FaceOff_v1.md finalization + Continuous-Claude-v3 dual-gate read + seed-shape test. Substrate decision is downstream.
· **Retrieval interface.** Substrate-dependent.
· **Export-cadence helper** (NEXT MOVE #6). Wraps Stage 1 (watch Downloads folder, trigger pipeline) but doesn't change pipeline behavior.
· **Cross-export uuid stability check** (NEXT MOVE #8). Done at next natural export by diffing a known message across two snapshots. Design absorbs both outcomes via snapshot-id.
· **Anchor/graveyard capture format.** Contextual-commits adopted at S10; orthogonal to this pipeline.
· **Per-project anchor passes** (NEXT MOVE #7). Build on top of ingested records; not part of the freeze pipeline itself.

---

## 8. Change log

· **v3 · 2026-05-28 · apparatus S13 · post-implementation fidelity pass.** Stages 1–4 were implemented from v2 with ZERO architectural deviations (the frozen design proved correct under real code; baseline snapshot `baseline-2026-05-25-ae015455` acceptance-passed 9/9). v3 reconciles three text-level drifts between the spec and the landed code — no invariant moved, no stage redesigned:
  - **§4.0.5 RUNNING → ANSWERED.** §4.5 ratified at S13: symmetric-drop CONFIRMED for `name` + `summary` (population stats folded into §4.0.5). The decision held at population scale; §4.5 itself forced no spec change.
  - **§6 idempotency refined.** Added the dry-run exemption (v1.2 code behavior): dry-run writes nothing, prints an informational NOTE on an existing snapshot, stays re-runnable; the no-overwrite guard protects the real-run write path only.
  - **§6 schema-drift coverage corrected.** v2 text implied detection across the full §2.11 surface (incl. field-level additions); the v1.0 code detects type-level drift only (block types + content-list item types). Spec now states the actual coverage + flags field-level detection as a v1.1 expansion.
· **v2 · 2026-05-27 · apparatus S12 · post-robustness-probe correction.** Folded S12 safety + robustness + Stage 0 §4.5 probes against the full 366MB archive. Corrections:
  - **§2.6: `signature` field corrected.** v1 claimed null in export (stripped); falsified at population scale — populated on ~60% of thinking blocks, base64 cryptographic provenance metadata. Documented as opaque blob, treated by scrub as string.
  - **§2.2: tree-or-forest correction.** v1 said `chat_messages` is a tree; 9/294 convs are forests with 2–6 sentinel roots. Stage 4 conversation header gains `multi_root` boolean (§3 output + §4 Stage 4); invariant 5.7 expanded.
  - **§2.4 + §2.5 + §2.7 + §2.8 + §2.9 + §2.10: new field clusters documented.** `display_content` (~25K tool blocks, includes `json_block` cred vector), `tool_result.content[]` five item types, `summaries[]` entry shape, `attachments[].extracted_content` (inlined file text, cred vector), `files[]` (reference-only), MCP metadata, `approval_key` (benign Google Calendar MCP auth), `structured_content`, the 9-path strip set.
  - **§4 Stage 0 collapsed.** §4.0.1–§4.0.4 absorbed by S12 safety + robustness probes (output refs at `apparatus-scratch/safety_probe_output.md` and `robustness_probe_output.md`). §4.0.5 remains; running in CC at S12 close, output at S13 boot.
  - **§4 Stage 4 per-message record: `conv_name` dropped.** v1 carried it while §5.4 said `name` was dropped — propagation miss from S11 inversion correction caught at S12 turn 8.
  - **§4 Stage 4 conversation header: `multi_root` boolean added.** Multi-root convs need the structural flag.
  - **§5.7 expanded.** Branches AND multi-root preserved.
  - **§5.8 strengthened.** Pointer uniqueness population-validated; v5 "presumed" hedge dropped.
  - **§5.11 added.** Sampling-floor invariant — field-population-semantics claims require whole-archive scans. Derived from the `signature` drift error meta-lesson.
  - **§6 baseline counts corrected.** Stage 3 verify-gate baseline locked at population-confirmed counts (RTSP=177, Postgres=76, OpenAI=10, Anthropic=10, Stripe=0). v1's S10-based counts undercounted.

· **v1 · 2026-05-27 · apparatus S11 · initial freeze.** Folded S11 export verification (5 block types confirmed, thinking-block schema confirmed, conv-level summary identified as user-mutable session-state); delta-ingest via pure uuid-diff (date dropped as filter mechanism); scrub versioning via overlay (`scrub-vN/` dirs under each snapshot); floor-rule clarified (message stream is floor; mutable conv metadata is not; user messages and assistant messages equal). Pre-Stage-1 work blocked on §4 Stage 0 probes (four small, later five).

---

*Anchored v2 2026-05-27 by apparatus S12 (Jake + orchestrator-Claude). The spec is product of the S12 safety + robustness probes (population-scale verification against the full 366MB archive) following the S11 v1 initial freeze. Two architectural canon corrections landed (signature semantics + tree-vs-forest), three new field clusters documented, cred baseline population-validated, sampling-floor invariant added. The architecture survived all findings without code change — the type-agnostic recursive scrub absorbed every new field and every cred-vector class. Implementation gates on §4.0.5 output landing at S13.*
