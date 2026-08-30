# Case: Predict, Optimize, Satisfice, Then Fortify

**Source:** Sim, Tang, Zhou, Zhu, *The Analytics of Robust Satisficing: Predict, Optimize, Satisfice, Then Fortify*, Operations Research.

## Research pattern

Combines prediction with robust decision making and separates ambiguity in prediction residuals from estimation uncertainty in prediction coefficients. It also develops statistical justification and tractable special cases involving recourse and decision-dependent prediction.

## Researcher lessons

- Decompose uncertainty before robustifying it; “prediction uncertainty” is too broad when coefficients and residuals behave differently.
- Residual-based ambiguity sets inherit data dependence from estimated prediction models.
- A second robustification layer is substantive only if it handles an uncertainty source not already absorbed by the first.

## Auditor lessons

- Track whether residuals are computed at true or estimated coefficients.
- Check inequalities transferring distance between predicted empirical distributions into coefficient-distance bounds.
- For dependent samples, audit the exact probability theorem rather than importing iid Wasserstein concentration.
- Distinguish statistical motivation of a target from a finite-sample operational certificate.

## Stress test

Rebuild the randomness map for residual-based robustness with estimated coefficients and identify every interaction between estimation and distributional error.
