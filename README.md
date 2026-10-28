# DG Quantum Satellite I

**Predictive Sufficiency and Physical Direction in Distinguishability Geometry: A Single-Qubit Realization**

Research and reproducibility repository for a manuscript under revision (28 October 2026). **Not an experimental demonstration of a novel DG-specific force or quantum evolution law.**

## Research question

What information does Distinguishability Geometry (DG) retain about a physical history, and what further physical assumptions are needed to predict a real qubit's response? The manuscript separates (i) future-response sufficiency of a coarse description, (ii) closure of its reduced dynamics, (iii) locally observable physical directions, and (iv) device-specific quantitative response laws.

## Public evidence

- `data/linear_counts.csv`: directly archived IBM Quantum Linear run, qubit 141; job `d9vavtl0vrcc73bp0ueg`. Twenty-four 20,000-shot records, six paired blocks at each depth k=20 and 60.
- `analysis/analyze_linear.py`: pure Python, standard-library-only reanalysis; block contrasts and conditional t intervals.
- `docs/INFORMATION_HIERARCHY.md`: precise meaning and evidentiary status of Q0 → Q1 → Q2.
- `docs/PROVENANCE_AND_LIMITS.md`: what was and was not retained.
- `docs/REFERENCES.md`: published prior results and conceptual boundaries.

Run `python analysis/analyze_linear.py` from the repo root. No IBM credentials are required.

## Important limits

Recorded A/B contrasts are descriptive experimental facts. Six blocks do **not** license treating all 120,000 shots per condition as independent experimental replications. Fixed order of execution may confound sequence effects with drift. A comparator based on earlier, noncontemporaneous T1/T2 calibrations is a **conditional simplified model**, not a certified hardware error bound. Full executed pulse-level schedules and contemporaneous calibration snapshots have not been established.

The qualitative DG operational precursor used in some examples should not be confused with the published DG v59 operational quotient, which is defined using outcome statistics.

## Status and reuse

This is a **revision-stage** reproducibility archive, not a frozen journal-accepted artifact. Public files include no unpublished collaborator reviews or internal revision history. Published AMT and transmon papers are referenced by DOI, not redistributed.

Cite the manuscript version and date alongside any reused dataset. No explicit reuse license is granted here; please contact the author for permissions beyond standard GitHub viewing.
