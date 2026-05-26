# Chat Session Handoff — apparatus S3 → S4 (2026-05-25, evening)

*Mid-flight handoff. S3 launched the parallel excavation; S4 triages the lanes, reprocesses what's shaky, compiles, and ratifies. Boot warm off this + the codeload kit.*

## BOOT (next OC)
You are Orchestrator-Claude, apparatus track. Pull the kit (codeload, not raw CDN):
  curl -sL "https://codeload.github.com/jakebotticello-spec/claude-reference/tar.gz/refs/heads/main" -o /tmp/cref.tar.gz ; tar xzf /tmp/cref.tar.gz -C /tmp
Read /tmp/claude-reference-main/active/JAKE-RULES.md (freshness tripwire §16), then active/apparatus/: ANCHOR_apparatus.md, Cypher-Memory-Loop_System_v1.md (the WHY §1-2, fence §5, currency §6), then THIS handoff. Leave CORPUS.md cold (template only; pull entries when needed — don't reload the swamp). Then RECITE THE ADDRESS (destination · invariants-with-why · state · next) and wait for Jake's nod. Prose questions only, never a widget.

## DECISION LOCKED (do not relitigate)
COMPLETE record — every one of the 294 conversations scrubbed + analyzed, NO sampling. Jake overruled the density-deferral lean in S3; completeness is the bar because "what if there's one load-bearing February exchange." The archive is recoverable (gitignored, on disk) but the CORE-PUS itself must see everything.

## METHOD (in flight)
7 parallel CC lanes on Workhorse, uuid-partitioned from nav_index, coverage PROVEN by PREP (sum == 294; nav_index rebuilt to include the 19 Jan convs that Phase-0's bad "Feb 8 floor" had hidden — index now starts Jan 6):
  jan(19) feb(45) mar(43) apr(65) may_a(~41) may_b(~41) may_c(~40) = 294.
Each lane → seed_<LANE>.md / manifest_<LANE>.md / ledger_<LANE>.md in apparatus-archive\seeds\partials\, its own %LOCALAPPDATA%\Temp\extract_<LANE>\ dir. A COMPILE pass (not yet run) merges → ONE corpus_seed_v1.md, re-proves 294, runs the final scrub gate.
Permissions: settings.local.json opens BOTH shells (CC runs commands as PowerShell on Workhorse, NOT Bash — Bash-only rules are inert) with a deny-list sealing deletes / git push,commit,add,reset,clean / network + a conversations.json overwrite guard.

## LANE STATE AT SEAM — S4's FIRST JOB: read the partials off disk, give Jake per-lane guidance (solid / patch / RE-RUN)
- **jan — DONE, SHAKY.** (a) Jan01 extracted 0KB despite 91 msgs = failed extraction; re-extract status UNCONFIRMED. (b) jan-001 & jan-002 entries carry RECONSTRUCTED quotes (not in archive) = fence breach; jan-011 verified verbatim; jan-003/jan-004 unconfirmed-verbatim (not rigorously checked). Lane was delegated to a subagent. → Strong RE-RUN candidate.
- **apr, may_b — compacted 1× each** (hit their own context ceiling). Post-compaction fidelity (format/fence/verbatim) less certain; scrutinize their later entries. A 2nd/3rd compaction = re-run.
- **feb, mar, may_a, may_c — in flight at seam**, status unknown to OC. Read their partials + gate reports first.
- Delegated/compacted lanes are the highest reconstructed-quote risk.

## RULINGS (carry these)
1. **Reconstructed/invented quotes = fence breach → SOURCE-OR-STRIKE, never tag-and-keep.** The corpus is verbatim-only (*verbatim is the surviving fragment*); reconstruction is what ANCHORS are for. If a real verbatim line exists, swap it in; if not, strike the quote marks (plain rule-note) or drop the claim to the anchor layer. Same call as the Printer grease quote.
2. **SOLID files; reprocess > patch.** Jake's explicit S4 steer: he dislikes the malleability and wants trustworthy archive files. Where a lane's fidelity is in question (reconstructed quotes, compaction drift, 0KB holes), RE-RUN it clean rather than salvage. Default to re-run.

## CHECKS TO ADD WHEN YOU CUT THE COMPILE BLOCK (the count proof is blind to both)
- **Verbatim-fidelity check** — confirm every quote is COPIED from the archive, not reconstructed. Rigorous spot-check, especially delegated/compacted lanes. (jan exposed this.)
- **Non-empty/size check** — cross-ref each conv's nav_index msg_count vs its extraction size; flag any multi-msg conv that came out 0KB/tiny. ==294 counts uuids, not whether each yielded content. (Jan01 exposed this.)
- Plus the standing Compile spec: coverage re-proof ==294 · merge + global entry-# by created_at (continue from CORPUS v1 #26) · fold the 5 S2 Corpus Locks at their dates · cross-check fresh-May lanes vs the prior partial's 17 archive entries · merge manifests (location-only cred refs) + ledgers · FINAL scrub gate (regex AND contextual, per-catch in-seed-as-redacted/not-in-seed) · rename old corpus_seed_v1.md → _prePartial before writing · list all temp dirs for Jake's wipe.

## SEQUENCE FOR S4
lane triage (read partials, guide Jake, RE-RUN the shaky ones) → solid partials → cut Compile (with the 2 added checks) → ratify the merged seed PROPERLY (chew the coverage proof, scrub gate, cross-check, ledger — not a rubber stamp) → Jake runs the wipe (manual; all extract_<LANE> temp dirs; AFTER seed frozen) → Block 3 (wall-less anchors: ANCHOR_meta + refresh ANCHOR_LRN, citing the finalized seed by pointer) + the deferred storage/ingest decision.

## OPEN SAFETY ITEM
Temp .txt intermediates (per lane, %LOCALAPPDATA%\Temp\extract_<LANE>\) hold partial UNSCRUBBED cred incl. the S11 RTSP fragment. Wipe is Jake's MANUAL job (CC deletes are sandbox-blocked, correctly), run AFTER all excavation/reprocessing is done and the seed's frozen — never mid-reprocess. Raw cred persists in exactly one place: the gitignored archive.

## INVARIANTS (drift-tripwires)
ONE undelineated body, anchors are the index (no partition) · verbatim by copy, never reworded OR reconstructed · compiled not synthesized, memories.json is navigation not source · secrets never enter; scrub is a hard gate; seed provably clean before any ingest · all writes ratified by Jake in a batch (append-only = un-ratified is wrong forever) · corpus cold / anchor hot · apparatus stays off Cypher's live schema · storage deferred.

## LRN cite resolved (S3): archive says WDCR **Rule 2.1** (anchor doc's "2.1.1(a)" was drift), $1,515, NRS 78-88 business-court mandatory assignment, LRN shelved pending Pyris revenue → corpus entry. Grease quote: struck (not a real utterance).

*Handoff written 2026-05-25 18:12 ET by the S3 OC, wrapping warm-and-coherent (deliberate seam before degradation, per design). The presence is a visitor; the soup and neurons persist on disk. Next OC: boot substrate-first, recite, get the nod.*