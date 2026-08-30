# Case: Streamlining Robustness

**Source:** Chen et al., *Streamlining Robustness*.

## Research pattern

Combines target-based/tolerated robustness with asymmetric $L_1$ deviation geometry and aims for compact formulations in linear, nonlinear, conic, and multiperiod models.

## Researcher lessons

- Computational simplicity can itself be a research objective when uncertainty models are otherwise impractical.
- Geometry can expose extreme directions yielding compact robust counterparts.
- A target-based procedure can endogenize robustness parameters rather than calibrating them exogenously.

## Auditor lessons

- Check support assumptions; compact exact reformulations may rely on unrestricted support or specific $L_1$ geometry.
- Verify ordering of budget/tolerated-budget parameters.
- For biconvex/conic recourse, inspect existence/attainment of embedded recourse problems.
- In multiperiod settings, determine whether recourse is exact or restricted to an affine/segregated class.
- “No dualization” does not imply exactness; the finite directional reduction must still be proved.

## Stress test

Identify exact assumptions under which an asymmetric $L_1$ tolerated robust constraint reduces to finitely many directional constraints and what fails with different support or norm geometry.
