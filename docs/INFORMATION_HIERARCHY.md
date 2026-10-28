# An explicit hierarchy of retained information

Let h denote a fully specified physical control-and-preparation history and let R_c(h) be the **true** response in an allowed continuation/instrument context c. The finite data are estimates, not exact R_c.

## Q0: coarse hardware metadata

Q0 records backend/qubit, k, number of nominal SX operations and selected shared device calibration metadata. Q0 deliberately **forgets ordering of phase controls**. At each fixed k the archive records two distinct histories A/B with the same Q0 but different finite-sample endpoint bit fractions. This is evidence against stable equal-response hypotheses under explicit sampling and drift controls, **not** a deterministic proof from noisy counts.

## Q1: ordered nominal control history

Q1 extends Q0 with the ordered RZ/SX instruction sequence and nominal target. It **distinguishes** A from B but does not, merely by including sequence labels, compute the physical response. Separating two histories is weaker than predicting their rates.

## Q2: physically calibrated realization

Q2 would additionally contain the executed scheduled waveforms, relevant coherent control errors, leakage channels, drift-aware calibration and instrument response. A device-specific dynamical law would then have to map these to outputs. Those complete data are not presently archived here; Q2 is a **proposed requirement**, not a demonstrated sufficient state.

## Mathematical criterion

For a fixed test family F, Q is exact-response sufficient if and only if

    Q(h)=Q(g) implies R_c(h)=R_c(g) for every c in F.

It is a standard factorisation condition. It does not follow that any finite set of existing IBM endpoint measurements exhausts all future contexts. Likewise an oriented tangent to an **already realised history** does not specify the physical generator for a *new* control command.

## Independent published physical example

For the two-timescale cosine-ramp pulses in Tishin, Next Materials 13 (2026) 103674, a pair of equal-duration, equal-area pulses can differ in their spectral Fourier response as the ramp time varies. Thus Qpulse=(total duration, pulse area) is insufficient for the **specified spectral functional**; adding ramp shape, ramp time and frequency can make that functional computable. The Fourier cancellation is published prior work and is not a newly measured hardware leakage zero. Relating the functional to leakage requires a physical response law.
