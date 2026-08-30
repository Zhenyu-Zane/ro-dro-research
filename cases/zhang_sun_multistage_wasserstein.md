# Case: Zhang–Sun Multistage Wasserstein DR-MCO

**Source:** Shixuan Zhang and Xu Andy Sun, *On Distributionally Robust Multistage Convex Optimization: Data-Driven Models and Performance*, INFORMS Journal on Optimization 8(2):120–140 (2026).

## Why this case matters

This external stress test combines multistage Wasserstein DRO, finite-dimensional dual recursion, stagewise finite-sample guarantees, and DDP computation.

## Audit findings

### Finite-dimensional stagewise reformulation — PASS

The proof carefully connects Wasserstein couplings, conditional measures, dualization, and pointwise supremum representations. Attainment/approximation issues are handled through the actual proof route rather than assumed away.

### Finite-sample theorem — PASS WITH EXPLICIT CONDITIONS

The proof multiplies stagewise good-event probabilities. That product requires independence of the stage-specific empirical datasets/events. Within-stage iid sampling alone does not imply cross-stage independence.

If cross-stage independence is unavailable, a valid joint argument such as Bonferroni/union bound or process-specific concentration is needed. This motivated `auditor/multistage_statistical_auditor.md`.

### Theorem DGP versus experiment DGP

A stagewise-independent model can be evaluated empirically on dependent sample paths as a misspecification/robustness experiment, but the stagewise-independent theorem does not automatically certify that regime.

### Exact optimizer versus finite-iteration DDP

A statistical theorem for the exact robust policy does not automatically transfer to a finite-iteration or inexact-oracle policy. This motivated `auditor/statistical_computational_composition_auditor.md`.

### Internal consistency

The stress test also found a local index/constraint-direction inconsistency in an appendix definition whose intended correction was recoverable from surrounding proof usage. This motivated `auditor/internal_consistency_auditor.md` and the rule not to overstate a typo as a fatal theorem failure.

## General lesson

In multistage DRO, explicitly separate process assumptions, training-data sampling architecture, joint good-event calculations, and the policy actually returned by the algorithm.
