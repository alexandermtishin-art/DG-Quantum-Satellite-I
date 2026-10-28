# Target-relative sufficiency: explicit test

The relevant notion of sufficiency is **indexed by the physical target**. Let \(C\) be an admissible controller history, \(Q(C)\) a retained description and \(F(C)\) a designated response or computable physical-control functional. Then a unique predictor \(f\) with \(F=f\circ Q\) exists precisely if \(F\) is constant on each fiber of \(Q\).

## Spectral example (published pulse family)

Within the cosine-ramp flat-top envelope family described in Tishin, *Next Materials* 13 (2026) 103674, choose total time \(T\), area \(\theta\), ramp time \(\tau\), and evaluation frequency \(\alpha\). A pulse is fully specified by \((T,\theta,\tau,\text{shape})\), subject to \(0<2\tau<T\). For the spectral functional

\[
F_\alpha[C]=\int_0^T\Omega_C(t)e^{i2\pi\alpha t}\,dt,
\]

the coarse control \(Q_{\rm pulse}=(T,\theta)\) is not sufficient: equal-area and equal-duration ramp choices can have distinct Fourier responses. The refinement \(Q_{\rm spec}=(T,\theta,\tau,\alpha,\text{shape})\) *is* sufficient to compute this specified Fourier integral. This is a complete analytic input description, not a claim of a minimal unique summary (the integral itself would also be sufficient).

In that published family, for \(|\alpha|=0.310\) cycles/ns and \(T=60\) ns, \(\tau_1=1.5/|\alpha|\simeq4.83871\) ns corresponds to an exact envelope spectral zero; \(\tau_2=2/|\alpha|\simeq6.45161\) ns does not. Both can be normalized to the same \(\theta=\pi/2\).

**Proven task:** differing Fourier functionals show loss of waveform/spectral information from a coarse control summary.

**Not proven task:** they do *not* alone imply distinct measured leakage **probabilities** on any IBM device. A physical transition model, pulse transfer function, instrument and calibration remain additional input.

## Three levels for the actual archived IBM control

- \(Q_0\): backend/qubit, depth, SX count and nominal shared calibration; omits ordered phases.
- \(Q_1\): additionally specifies ordered nominal RZ/SX history; distinguishes A and B but does not predict errors by label alone.
- \(Q_2\): additionally requires executed waveforms, physical noise/drive law, calibrations and readout; this is a *required information interface*, not an experimentally certified sufficient reconstruction.

The published pulse family and the archived IBM Linear histories are different physical tests: no equivalence of their pulse shapes or mechanisms is implied. Finite counts do not prove exact response inequality absent statistical assumptions, and the fixed order A-before-B leaves drift confounding unresolved.

## Scientific novelty boundary

The factorisation criterion is standard mathematics. The spectral-null physics is already published. Their combination provides a **noncircular, precisely scoped physical example of a partial sufficiency hierarchy**, but not yet a new DG-specific predictive law or experimental demonstration of beyond-standard quantum mechanics.
