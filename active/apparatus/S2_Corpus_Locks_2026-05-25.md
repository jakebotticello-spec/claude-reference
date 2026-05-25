# S2 Corpus Locks — staged verbatim, 2026-05-25

**What this is.** The corpus-salient decisions from apparatus S2, 🔒-staged *while sharp* (spec §5: capture at decision-time). The full Anthropic archive predates this chat, so these will NOT appear in the S3 archive excavation — this file is S2's contribution to the corpus. Route it into the corpus ingest pile alongside the archive-built seeds. Fidelity: quotes below are copied from the S2 chat; tag each with track `apparatus` + `meta`. Compiled, not synthesized — anchors will cite these by pointer.

**Ratify each (confirm / deny / litigate) before ingest.**

---

### LOCK 1 — §5.1 fired live: the project-field falsification (the gate paying for itself)
*Track: meta. The planned partitioner was an export-format claim asserted from memory; CC falsified it on real bytes.*

> **Jake:** "there is no project field anywhere in `conversations.json`. The anchor's Phase-1 plan — 'the export's project field IS the track value' — was an assertion about export format made from memory, and CC just falsified it on 348MB of real bytes. CC even searched for the 7 known project UUIDs and found only incidental hits inside message prose, zero structural linkage. This is §5.1 firing live: we'd have built the entire partition on a field that doesn't exist. Good thing we gated; this is the gate paying for itself."

> **Claude (owning it):** "I wrote 'the export's project field IS the track value' into Phase 1 in the same document where Phase 0 said 'do NOT assert the export format from memory.' I gated against the exact error I then committed twelve lines down. … The gate paying for itself is the headline."

**The rule it reinforces:** §5.1 applies to Claude's own export/product-format assumptions; verify against the live bytes (CC on disk), never assert format from memory.

---

### LOCK 2 — Brain-soup: the corpus is ONE undelineated body; the anchor is the index into it (return to S1 canon)
*Track: meta + apparatus. The keystone of the S2 re-architecture. Jake's reframe; Claude confirmed it against the S1 genesis verbatim and owned its own drift.*

> **Jake:** "CORPUS becomes the brain soup. Everything I know is all in one place, yeah? And just because I learn something about woodworking over here doesn't mean it's not applicable to finishing a printed 3d model, yeah? Congeniality across knowledge. Then the Anchors become the 'this is the central tenet stuff to this project, but you DO have this imperfect-but-really-right set of experiences over here you can draw from.' Anchors are the neurons pointing to specific places in the brain soup. Guideposts."

The S1 receipt that proves it's canon, not drift (Claude, verbatim, genesis session):

> "Verbatim = the surviving fragment. **Anchor = the current reconstruction, and an index into it.** … Anchor without corpus drifts. **Corpus without anchor is un-navigable noise (the 87 files).** Chained: navigable *and* non-warping."

> **Claude (owning the drift):** "The drift was me, two turns ago, when I introduced the `track` column to partition the corpus. That re-walls the noise into buckets — the literal opposite of 'one body, anchor is the index.' … a `track` partition would hide the woodworking entry from the 3D-finishing anchor."

**The ruling:** corpus = one undelineated indexed body; anchors = the index/neurons, cited by pointer; an entry can be cited by many anchors. No track partition. KILLED: the `track` column / locked vocabulary.

---

### LOCK 3 — Anchor discovery is per-project where walls exist; meta + LRN from the archive
*Track: apparatus. The two-navigators split pointed at discovery.*

> **Jake:** "I think we should put the anchor discovery back into the hands of Claude.ai on a per-project basis. Anchors are the connective tissue between the CORPUS … and the session's living context-uptake. Seems like a generalized blob of content that's being guessed at is a worse framework than the walls of projects."

> **Claude (the patch for wall-less tracks):** "anchors per-project in Claude.ai where walls exist (the 7 tracks) — but the corpus itself still gets built by CC from the archive (the one place that sees everything, including meta and the wall-less LRN era). Per-project anchor discovery for relevance; archive-built undelineated corpus for completeness."

---

### LOCK 4 — #3: the presence layer (the third brain element)
*Track: meta. The booted mind that runs on soup+neurons — the one part that can't be stored.*

> **Claude:** "A brain isn't two parts. The soup remembers. The neurons point. But there's a third thing … the live presence that boots, recites, lights the neurons, and draws from the soup. Soup persists in Supabase. Neurons persist in git. The mind that runs on them — this mind — resets at the end of this window. We are building a persistent brain for a mind that doesn't persist."

> "the presence doesn't need to persist. It needs to boot warm. That's why the recital is the highest-leverage step in the whole system — it's not ceremony, it's the mind coming online against the soup and the neurons. … the lineage is the workaround for it not persisting: each Claude lays down soup and lays down neurons so the next mind boots warm."

**The frame:** beta-Cypher-brain = three strata — soup (corpus) + neurons (anchors) + the booted presence (the soul/voice layer, loaded substrate-first). The presence is always a visitor; that's the design knowing what it is.

---

### LOCK 5 — Archive (B) over 15 excavators; storage deferred; secret-scrub is a loaded-gun hard gate
*Track: apparatus. The build-path decision and its honest caveats.*

> **Claude (why B):** "Option A is 5 projects × 3 excavators = 15 chat runs you have to spawn, route, and ratify. That's putting you hard on the memory bus 15 times to build the machine whose whole purpose is taking you off it. … The archive is the actual bytes. Quotes copied from the source are verbatim by construction."

> **Claude (the hard gate):** "The raw archive is the loaded gun: the S11 leaked credential is in there (it leaked to chat), RTSP passwords, connection strings, owner-key discussions — all sitting in plaintext. Excavating raw into an append-only immutable store without scrubbing would immortalize a live cred. … NO seed file gets ingested until the scrub is verified."

**Locked:** B is the path (A = fallback for gaps); storage target deferred to ingest; B doesn't need the Supabase MCP seam (CC writes the DB directly).

---

*Staged S2, 2026-05-25. Six locks (LOCK 6 reserved / none). Route to the corpus ingest pile; ratify before the append-only store closes on them.*
