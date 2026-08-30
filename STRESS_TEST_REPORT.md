# Stress-Test Report

## Purpose

The skill is deliberately hardened against failure modes that are common in RO/DRO research but easy for language models to miss: invalid duality/minimax steps, overclaimed equivalence, pointwise-to-data-dependent statistical errors, oracle radii, dependence mismatches, theorem/algorithm scope drift, and asymptotic results mislabeled as finite-sample guarantees.

## A. Canonical DRO containment logic

Baseline test: Wasserstein ambiguity-set containment implies a deterministic bound on true performance for every decision on the containment event. The Auditor must still verify integrability, metric convention, concentration assumptions, and radius computability.

Result: core randomness-map and oracle-quantity workflows retained.

## B. Decision-dependent information discovery

Tested quantifier order, nonanticipativity, dynamic min–max–min–max formulations, and K-adaptability.

Result: information timing is treated as part of the model; dynamic equivalence requires an explicit policy recovery argument.

## C. Learned uncertainty-set geometry

Tested data-selected centers/scales/shapes and uniform finite-sample coverage over learned parameter classes.

Result: learned geometry requires complexity/uniformity control; reparameterization and invariance are audited separately from coverage.

## D. Layered parameter uncertainty plus residual ambiguity

Tested contextual models where coefficients and residual distributions are both uncertain.

Result: separate good events, observability of radii, and joint asymptotic shrinkage are mandatory.

## E. Knowledge-guided transport

Tested transport costs informed by external predictors and regularization equivalences.

Result: transport geometry is recognized as a modeling primitive; smaller ambiguity sets do not automatically preserve coverage.

## F. Dependent samples

Tested attempts to transplant iid Wasserstein concentration to dependent trajectories.

Result: direct reuse is vetoed; a dependence-class-specific theorem or justified reduction is required.

## G. Wu–Li–Mao external theorem-level test

Source: *On Generalization and Regularization via Wasserstein Distributionally Robust Optimization*, Management Science (2026).

Key hardening:

- distinguish equality of projected/induced ambiguity sets from equality of original sets;
- identify the provenance of uniformity rather than mechanically applying a union bound;
- decompose statistical rates into sample exponent, logs, dimension in constants, confidence, and nuisance parameters;
- audit the proof route actually used rather than forcing all exactness through strong duality.

This produced `equivalence_object_auditor.md` and `rate_anatomy.md`.

## H. Zhang–Sun external multistage test

Source: *On Distributionally Robust Multistage Convex Optimization: Data-Driven Models and Performance*, INFORMS Journal on Optimization (2026).

Key hardening:

- within-stage iid is not cross-stage independence;
- stagewise-independent optimization models do not automatically describe dependent trajectory evaluation;
- product good-event probabilities require justified event independence;
- exact-policy statistical theorems do not automatically certify finite-iteration DDP policies;
- local theorem/definition typos must be reported without being inflated into fatal failures.

This produced multistage, statistical–computational composition, and internal-consistency auditors.

## I. Sutter–Van Parys–Kuhn external dependent-process test

Source: *A Pareto Dominance Principle for Data-Driven Optimization*, Operations Research (2024).

Key hardening:

- large-deviation principles are asymptotic exponential-rate results, not generic finite-sample confidence inequalities;
- Markov/autoregressive process ambiguity must not be confused with one-period marginal ambiguity;
- closure/interior roles in LDP upper/lower bounds are checked explicitly;
- optimality among statistic-based procedures is weaker than no-loss optimality over all raw-data procedures unless a sufficiency/equivalence bridge is proved.

This produced deviation-regime, process-law, and sufficiency/compression auditors.

## Maturity assessment

V1.3 is considered structurally mature for research use. V1.3.1 changes packaging/discovery rather than mathematical logic: `SKILL.md` remains the single provider-neutral source of truth, while Claude/OpenAI repository pointers and progressive disclosure make the same skill easier to invoke without duplicating instructions.

The intended failure mode for an uncovered theorem class is **NOT ESTABLISHED + retrieve the appropriate original theorem**, not analogy-based improvisation.
