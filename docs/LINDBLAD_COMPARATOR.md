# Reproducing the independent simplified Lindblad comparator

Install `numpy` and `scipy`. From repository root run:

```
python analysis/independent_lindblad_linear.py
```

Reads `data/linear_result.json`, writes `data/independent_lindblad_baseline_reproduced.csv`.

Frozen inputs: T1=368.9 µs, T2=226.7 µs, SX time=32 ns, computational ground preparation, 4 nominal SX per repeat, A virtual-RZ phase list [270,0,0,270] degrees and B=[180,0,0,0], ideal resonant SX Hamiltonian, constant Markovian amplitude damping and pure dephasing, hypothetical symmetric readout misclassification rate 0.002. Counts **do not enter fitting**.

Results for observed-error probability: A20=0.0070558671; B20=0.0065192713; A60=0.0170141357; B60=0.0154344600.

These are conditional model outcomes, not certified hardware predictions. The T1/T2 snapshot was taken the day before Linear; executed IBM pulse-level schedules, coherent control error, leakage, device drift and contemporaneous calibration are not recovered. The actual gate-error metric is not a rigorous pulse-error bound. The comparator's wrong-sign A/B contrast establishes inadequacy of this limited model, not quantum theory or DG.
