# Task: Generate Research Ideas in RO/DRO

The purpose is not to generate many superficial combinations. The goal is to identify a modeling primitive whose absence creates a real operational and mathematical gap.

## Step I1 — Start from a failure mode, not a technique

Collect concrete failures such as exogenously fixed uncertainty geometry, costly/endogenous information treated as free, estimated prediction coefficients treated as known, residual ambiguity robustified while parameter uncertainty is ignored, transport geometry that ignores credible structural knowledge, multistage models that are theoretically strong but unusable computationally, iid guarantees applied to trajectory data, or guarantees with oracle constants.

## Step I2 — Identify the missing primitive

Examples include decision-dependent information, learned uncertainty geometry, structured/knowledge-guided transport, joint parameter and residual ambiguity, dependent-data calibration, target-oriented fragility, endogenous robustness budgets, or nonlinear/multistage recourse with exploitable exact structure.

Do not combine primitives arbitrarily. Each added primitive must be operationally motivated.

## Step I3 — Find the mathematical obstruction

A strong theory paper usually creates a nontrivial obstruction: decision-dependent nonanticipativity, decision-dependent ambiguity, failed conjugate reformulations, bilinearity/nonconvexity, uniform control over a learned class, dependent samples invalidating iid concentration, or infinite-dimensional recourse.

If no meaningful obstruction appears, the idea may be an application rather than a methods contribution.

## Step I4 — Search for a structural escape hatch

Look for separability, monotonicity, perspective/conjugate identities, polyhedral/extreme-point geometry, low-rank/block/diagonal parameterization, saddle structure, conditional independence, martingale/mixing concentration, K-adaptability, convexifying reparameterizations, or invariant geometry.

## Step I5 — Predict the theorem package

Before developing the idea, write the likely stack: model equivalence/reformulation; tractability/algorithm; finite-sample or asymptotic guarantee; and structural/managerial comparative statics if relevant. If all are immediate corollaries, novelty is weak.

## Step I6 — Adversarial novelty search

Use current literature and search by both application and primitive. Actively try to kill the idea before investing in it.

## Step I7 — Feasibility filter

Score theoretical novelty, proof feasibility, computational feasibility, data/experiment feasibility, and operational relevance separately. A high-novelty idea without a plausible proof route is high-risk, not ready.

## Output

For each surviving idea provide a one-sentence problem, missing primitive, nearest literature, mathematical obstruction, proposed structural result, likely statistical result, computational route, decisive experiment, and main risk that could kill the paper.
