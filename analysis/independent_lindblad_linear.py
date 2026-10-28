#!/usr/bin/env python3
"""Frozen ideal-SX plus T1/T2 Lindblad comparator, independent of IBM count fitting."""
import csv
from pathlib import Path
import numpy as np
from scipy.linalg import expm

root = Path(__file__).resolve().parents[1]
T1, T2, tau = 368.9e-6, 226.7e-6, 32e-9
G1, Gphi = 1/T1, 1/T2-1/(2*T1)
X = np.array([[0,1],[1,0]],complex)
Z = np.diag([1.,-1.])
sm = np.array([[0,1],[0,0]],complex)
I = np.eye(2,dtype=complex)
H = np.pi/(4*tau)*X
L = -1j*(np.kron(I,H)-np.kron(H.T,I))
def dissipator(c):
    C=c.conj().T @ c
    return np.kron(c.conj(),c)-0.5*(np.kron(I,C)+np.kron(C.T,I))
L += G1*dissipator(sm)+(Gphi/2)*dissipator(Z)
E = expm(L*tau)
def run(seq,k):
    v=np.array([[1.,0.],[0.,0.]],complex).reshape(4,order="F")
    for _ in range(k):
        for phi in seq:
            a=np.deg2rad(phi)
            R=np.diag([np.exp(1j*a/2),np.exp(-1j*a/2)])
            rho=v.reshape((2,2),order="F")
            v=(R@rho@R.conj().T).reshape(4,order="F")
            v=E@v
            rho=v.reshape((2,2),order="F")
            v=(R.conj().T@rho@R).reshape(4,order="F")
    rho=v.reshape((2,2),order="F")
    return float(rho[1,1].real),float(np.trace(rho).real)
with (root/"data/linear_counts.csv").open(newline="") as f:
    raw=[{"k":int(r["k"]),"seq":r["history"],"counts":{"1":int(r["counts_1"])}} for r in csv.DictReader(f)]
records=[]
for k in (20,60):
    for name,seq in (("A",[270,0,0,270]),("B",[180,0,0,0])):
        p,trace=run(seq,k)
        obs=sum(r["counts"]["1"] for r in raw if r["k"]==k and r["seq"]==name)/120000
        modeled=0.002+0.996*p
        records.append(dict(k=k,history=name,pulse_count=4*k,sx_time_us=4*k*tau*1e6,model_pre_readout=p,model_with_symmetric_ro_0p002=modeled,observed_error=obs,obs_minus_model=obs-modeled,trace=trace))
path=root/"data/independent_lindblad_baseline_reproduced.csv"
with path.open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=records[0].keys());w.writeheader();w.writerows(records)
for row in records: print(row)
