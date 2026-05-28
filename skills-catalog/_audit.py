import json
from pathlib import Path

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load v0.2 sets (name → primary_hint)
v2_bucket = {}
for n in range(1, 21):
    p = Path(f"chunks-v0.2/chunk_apparatus_{n:03d}.jsonl")
    if not p.exists(): break
    for line in p.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        v2_bucket[r["full_name"]] = "apparatus"

for line in Path("chunks-v0.2/chunk_workflow_001.jsonl").read_text(encoding="utf-8").splitlines():
    r = json.loads(line)
    v2_bucket[r["full_name"]] = "workflow"

for line in Path("chunks-v0.2/chunk_cool_001.jsonl").read_text(encoding="utf-8").splitlines():
    r = json.loads(line)
    v2_bucket[r["full_name"]] = "cool"

print(f"v0.2 total mapped: {len(v2_bucket)}")

# Load v0.3 cool
v3_cool = []
for n in range(1, 10):
    p = Path(f"chunks-v0.3/cool/chunk_{n:03d}.jsonl")
    if not p.exists(): break
    for line in p.read_text(encoding="utf-8").splitlines():
        v3_cool.append(json.loads(line))
print(f"v0.3 cool: {len(v3_cool)}")

# Load v0.3 workflow
v3_workflow = []
for n in range(1, 10):
    p = Path(f"chunks-v0.3/workflow/chunk_{n:03d}.jsonl")
    if not p.exists(): break
    for line in p.read_text(encoding="utf-8").splitlines():
        v3_workflow.append(json.loads(line))
print(f"v0.3 workflow: {len(v3_workflow)}")

# COOL audit
cool_was_cool = [r for r in v3_cool if v2_bucket.get(r["full_name"]) == "cool"]
cool_buried_apparatus = [r for r in v3_cool if v2_bucket.get(r["full_name"]) == "apparatus"]
cool_buried_workflow  = [r for r in v3_cool if v2_bucket.get(r["full_name"]) == "workflow"]
cool_new = [r for r in v3_cool if r["full_name"] not in v2_bucket]

print("\n=== COOL CROSS-CLASSIFICATION AUDIT ===")
print(f"v0.3 cool total:            {len(v3_cool)}")
print(f"was already cool in v0.2:   {len(cool_was_cool)}")
print(f"BURIED in v0.2 apparatus:   {len(cool_buried_apparatus)}")
print(f"buried in v0.2 workflow:    {len(cool_buried_workflow)}")
print(f"new (not in v0.2):          {len(cool_new)}")

# Top 30 buried cool by stars
top30_buried_cool = sorted(cool_buried_apparatus + cool_buried_workflow,
                           key=lambda r: -r["stars"])[:30]
print("\nTop 30 buried-cool rows (stars | repo | 1-liner | scores):")
for r in top30_buried_cool:
    sc = r["bucket_scores"]
    desc = (r.get("description","") or "")[:60].replace("\n"," ")
    print(f"  {r['stars']:>6}  {r['full_name']:<45}  [{desc}]  A:{sc['apparatus']} W:{sc['workflow']} C:{sc['cool']}")

# WORKFLOW audit
wf_was = [r for r in v3_workflow if v2_bucket.get(r["full_name"]) == "workflow"]
wf_buried_apparatus = [r for r in v3_workflow if v2_bucket.get(r["full_name"]) == "apparatus"]
wf_buried_cool      = [r for r in v3_workflow if v2_bucket.get(r["full_name"]) == "cool"]
wf_new              = [r for r in v3_workflow if r["full_name"] not in v2_bucket]

print("\n=== WORKFLOW CROSS-CLASSIFICATION AUDIT ===")
print(f"v0.3 workflow total:         {len(v3_workflow)}")
print(f"was already workflow in v0.2:{len(wf_was)}")
print(f"BURIED in v0.2 apparatus:    {len(wf_buried_apparatus)}")
print(f"buried in v0.2 cool:         {len(wf_buried_cool)}")
print(f"new (not in v0.2):           {len(wf_new)}")

# Top 20 buried workflow by stars
top20_buried_wf = sorted(wf_buried_apparatus + wf_buried_cool,
                         key=lambda r: -r["stars"])[:20]
print("\nTop 20 buried-workflow rows (stars | repo | 1-liner | scores):")
for r in top20_buried_wf:
    sc = r["bucket_scores"]
    desc = (r.get("description","") or "")[:60].replace("\n"," ")
    print(f"  {r['stars']:>6}  {r['full_name']:<45}  [{desc}]  A:{sc['apparatus']} W:{sc['workflow']} C:{sc['cool']}")
