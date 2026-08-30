# Case: Wu–Li–Mao Generalization and Regularization

**Source:** Wu, Q., Li, J. Y.-M., Mao, T., *On Generalization and Regularization via Wasserstein Distributionally Robust Optimization*, Management Science 72(7):6104–6119 (2026), DOI `10.1287/mnsc.2023.03895`.

## Why this case matters

This external theorem-level stress test combines projection-based Wasserstein generalization, exact regularization equivalence, and claims about avoiding the classical curse of dimensionality.

## Audit findings

### Projection/reformulation — PASS

The key equivalence concerns **projected/induced ambiguity sets under the affine decision rule**, not equality of the original Wasserstein and max-sliced Wasserstein balls. This motivated `auditor/equivalence_object_auditor.md`.

### Finite-sample generalization — PASS, but not automatically operational

Uniformity comes from a common containment/projection event rather than a union bound over decisions. Some radius constants depend on unknown distributional moments, so the result is a theoretical finite-sample guarantee unless those primitives are known or validly bounded from data.

### Curse-of-dimensionality wording — qualified

The sample-size exponent can avoid the classical Wasserstein dimension dependence while constants still depend on dimension. Therefore “dimension-free exponent” must not be upgraded to “dimension-free finite-sample sample complexity.” This motivated `templates/rate_anatomy.md`.

### Exact regularization equivalence — PASS

The proof route is not merely a generic strong-duality invocation; projection and perturbation identities can establish exactness directly. This motivated proof-route-neutral reformulation auditing.

## General lesson

When a paper says two DRO models “coincide,” identify the exact object and decision class. When it says “curse-free,” decompose the rate before accepting the prose.
