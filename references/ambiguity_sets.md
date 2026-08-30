# Ambiguity-Set Selection Guide

Use this guide to select a candidate ambiguity set. It is not a theorem sheet; verify exact formulas in original sources.

## Moment-based

Use when credible information is available about moments or generalized moments but the full distribution is not.

Strengths:
- interpretable moment information;
- often compatible with conic reformulations.

Risks:
- low-order moments may not identify the distribution;
- statistical consistency of the resulting DRO objective is not automatic;
- unbounded support can create attainment/integrability issues.

Audit:
- support assumptions;
- positive semidefiniteness/feasibility of moment matrices;
- generalized moment problem duality;
- Slater-type conditions;
- whether moments are known or estimated.

## $\phi$-divergence

Use when distributions share a common support/reference and likelihood-ratio deviations are meaningful.

Strengths:
- strong links to statistics and empirical likelihood;
- tractable finite-support formulations in many cases.

Risks:
- absolute-continuity/support restrictions can be consequential;
- empirical discrete reference laws may restrict which shifts are representable;
- asymptotic radius scaling matters.

Audit:
- direction of divergence;
- definition at zero probabilities;
- support matching;
- conjugate domain;
- radius scaling with sample size.

## Optimal transport / Wasserstein

Use when moving probability mass across the state space is meaningful and support mismatch should be allowed.

Strengths:
- natural geometry on outcomes/features;
- works with empirical reference distributions and continuous true laws;
- rich links to regularization and adversarial perturbations.

Risks:
- transport cost is a modeling primitive, not a neutral choice;
- generic finite-sample radii may suffer dimension dependence;
- worst-case expectation may be infinite without growth/tail control;
- decision-dependent or learned transport cost can complicate convexity and validity.

Audit:
- transport cost lower semicontinuity/coercivity as required;
- support constraints;
- growth of loss relative to transport cost;
- $p$ and cost-power convention;
- radius units/scaling;
- exact strong-duality theorem used.

## Hybrid/structured sets

Examples include sets with support, moments, conditional moments, structural shape restrictions, or knowledge-guided costs.

Use when the added information is genuinely defensible.

Audit whether the extra structure:

1. shrinks the ambiguity set in a valid way;
2. preserves containment/coverage of the true law;
3. changes duality or tractability;
4. introduces new tuning parameters or oracle information.
