"""Emit judgment-ready surface lists for Task 5."""
import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def load_chunks(base_dir, cat, max_n=30):
    rows = []
    for n in range(1, max_n+1):
        p = Path(base_dir) / cat / f"chunk_{n:03d}.jsonl"
        if not p.exists(): break
        for line in p.read_text(encoding="utf-8").splitlines():
            rows.append(json.loads(line))
    return rows

def fmt(r):
    sc = r["bucket_scores"]
    desc = (r.get("description","") or "")[:70].replace("\n"," ")
    return f"{r['stars']:>7}  {r['full_name']:<48}  {desc}  [A:{sc['apparatus']} W:{sc['workflow']} C:{sc['cool']}]"

# ---- COOL: full list (all 459) ----
print("=" * 100)
print("COOL — FULL LIST (all candidates, stars desc)")
print("=" * 100)
cool = load_chunks("chunks-v0.3", "cool")
for i, r in enumerate(cool, 1):
    print(f"{i:>3}. {fmt(r)}")
print(f"\n[COOL total: {len(cool)}]")

# ---- WORKFLOW: full list (all 554) ----
print("\n" + "=" * 100)
print("WORKFLOW — FULL LIST (all candidates, stars desc)")
print("=" * 100)
wf = load_chunks("chunks-v0.3", "workflow")
for i, r in enumerate(wf, 1):
    print(f"{i:>3}. {fmt(r)}")
print(f"\n[WORKFLOW total: {len(wf)}]")

# ---- APPARATUS: delta only (exclude v0.2 chunks 001-004 = top 400) ----
# Load v0.2 apparatus chunks 001-004 repo names
v2_judged = set()
for n in range(1, 5):
    p = Path(f"chunks-v0.2/chunk_apparatus_{n:03d}.jsonl")
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            v2_judged.add(r["full_name"])

print(f"\n[Apparatus: v0.2 judged set (chunks 001-004): {len(v2_judged)} repos]")

apparatus = load_chunks("chunks-v0.3", "apparatus")
delta = [r for r in apparatus if r["full_name"] not in v2_judged]

print("\n" + "=" * 100)
print(f"APPARATUS — DELTA ONLY (v0.3 candidates NOT in v0.2 chunks 001-004), stars desc")
print("=" * 100)
for i, r in enumerate(delta, 1):
    print(f"{i:>3}. {fmt(r)}")
print(f"\n[APPARATUS delta total: {len(delta)} (of {len(apparatus)} total v0.3 apparatus candidates)]")
