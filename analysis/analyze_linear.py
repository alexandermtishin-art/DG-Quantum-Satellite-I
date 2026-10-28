#!/usr/bin/env python3
"""Recompute archived IBM Linear paired contrasts; no scipy required."""
import csv, math, statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/"data/linear_counts.csv").open(newline="") as f:
    data=list(csv.DictReader(f))
assert len(data)==24
by={}
for row in data:
    key=(int(row["k"]),row["history"],int(row["block"]))
    assert key not in by
    assert int(row["counts_0"])+int(row["counts_1"])==20000
    by[key]=int(row["counts_1"])/20000
for k in (20,60):
    d=[by[k,"B",b]-by[k,"A",b] for b in range(6)]
    mean=statistics.mean(d)
    se=statistics.stdev(d)/math.sqrt(6)
    t95=2.570581835636305 # Student t critical, df=5
    lo,hi=mean-t95*se,mean+t95*se
    A=statistics.mean(by[k,"A",b] for b in range(6))
    B=statistics.mean(by[k,"B",b] for b in range(6))
    leave_one_out=[statistics.mean([v for j,v in enumerate(d) if j!=b]) for b in range(6)]
    print(f"k={k}  A={A:.8f} B={B:.8f} B-A={mean:.8f} SE={se:.8f} conditional_95%_CI=[{lo:.8f},{hi:.8f}]")
    print("  block differences:", ", ".join(f"{v:.6f}" for v in d))
    print("  leave-one-block-out:", ", ".join(f"{v:.6f}" for v in leave_one_out))
    assert min(leave_one_out)>0
    assert all(v>0 for v in d)
print("All results are conditional on the six-block sampling assumptions; fixed order/drift remain unresolved.")
