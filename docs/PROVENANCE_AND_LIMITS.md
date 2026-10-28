# Provenance, reproducibility and inference limits

- Source: archived `linear_result(1).json` and `linear_spec(1).json`, IBM job `d9vavtl0vrcc73bp0ueg`, physical qubit 141.
- Acquisition: six fixed-order blocks of A20,B20,A60,B60, 20,000 shots per row, for 24 total rows. `data/linear_counts.csv` preserves the raw count pairs, block labels, depths and order shown in the source.
- The stored endpoint error for even k equals fraction of bit 1. Both available Linear depths are even.
- For k=20: A 2732/120000, B 4284/120000; B-A = 0.0129333333.
- For k=60: A 4733/120000, B 13306/120000; B-A = 0.0714416667.
- All 12 observed paired contrasts are positive. Conditional two-sided sign-test p = 2/2^6 = 0.03125 **per depth**, assuming independent exchangeable block-signs.
- Student t(5) intervals using six contrasts: k20 [0.0103487,0.0155179], k60 [0.0699585,0.0729248]. These ignore correlated and systematic drift.
- Fixed A-before-B ordering may align with temporal drift. The dataset alone cannot eliminate this nuisance or establish causal phase-order effects.
- A stored notebook was reported to include a program generating four SX per repeat with virtual RZ differences, but no independently verifiable device-executed pulse schedule and full time-matched calibration is published in this repository.
- A 13 August 2026 snapshot was reported as T1=368.9 microseconds, T2=226.7 microseconds and SX duration 32 ns for qubit 141; the Linear job was 14 August. Snapshot values are not run-time guaranteed error bounds.
- Earlier independent simplified T1/T2 comparator predictions (conditional on its implementation): B-A approximately -0.00054 for k=20, -0.00158 for k=60. Neither is a DG prediction. Full simulator dependencies/assumptions need publication before numerical independent verification of this comparator can be claimed.
- Other IBM archives (evenscan/finescan) are excluded from this release because their executable provenance and/or raw counts have not been sufficiently established.
- There is no raw hardware measurement of Next Materials spectral zero in this archive.

Research data are disclosed solely to support verification of recorded outputs. Publication of these counts is not a guarantee of run reproducibility on changed quantum hardware.
