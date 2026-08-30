# Case: Data-Driven Uncertainty Sets

**Source:** Lou et al., *Data-Driven Uncertainty Sets*.

## Research pattern

Treats RO uncertainty-set geometry as an estimand learned directly from data and connects geometric complexity to finite-sample reliability.

## Researcher lessons

- Separate estimable geometry parameters (center, scale, orientation, asymmetry) from robustness/coverage level.
- Parameterization complexity matters statistically as well as computationally.
- Invariance to unit changes/transformations is a meaningful property.
- Structured lower-dimensional sets can trade flexibility for finite-sample stability.

## Auditor lessons

- Uniform convergence over learned set parameters requires a controlled parameter class and complexity argument.
- Reparameterization can restore convexity but introduce nonsingularity/boundedness assumptions.
- Check existence when volume can collapse to zero.
- A finite-sample coverage claim must specify how approximate population deviation control translates to robust feasibility.

## Stress test

For a learned ellipsoidal or component-wise uncertainty set, derive a uniform finite-sample bound valid for the data-selected geometry, not merely a fixed geometry.
