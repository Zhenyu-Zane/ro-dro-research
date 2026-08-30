# Task: Formulate an RO/DRO Research Model

## Goal

Translate an operational decision problem into a coherent uncertainty model before attempting reformulation.

## Step 1 — Deterministic skeleton

Write decisions, objective, constraints, timing, interpretation, and feasible set without uncertainty. Separate true decisions from estimated inputs.

## Step 2 — Uncertainty decomposition

Create `object | meaning | observed when? | random/unknown? | data source | proposed uncertainty representation` and separate primitive uncertainty, parameter/estimation uncertainty, residual ambiguity, model misspecification, and information revelation.

## Step 3 — Information structure

For each stage, state what is known before the decision. If a decision affects what will be observed, explicitly model decision-dependent nonanticipativity rather than treating it as an ordinary decision-dependent uncertainty set.

## Step 4 — Paradigm selection

Explain why RO, DRO, robust satisficing, stochastic optimization, or a hybrid is appropriate. Reject unnecessary sophistication.

## Step 5 — Set design

For RO, specify center/location, geometry, scale/shape, budget, support, and data-driven estimation/calibration.

For DRO, specify reference distribution, ambiguity metric/constraints, support, radius/confidence parameter, and whether the set depends on decision, context, or estimated parameters.

## Step 6 — Well-posedness screen

Check nonempty feasible and ambiguity/uncertainty sets, finite objective or controlled extended-real interpretation, measurability, integrability, recourse feasibility, and compactness/coercivity if attainment will be used.

## Step 7 — Research delta

Write one sentence each for existing model, operational failure, missing modeling primitive, proposed new primitive, and mathematical difficulty it creates. If the mathematical obstruction is trivial, the theory contribution may be weak.

## Output

Return the formulation, uncertainty decomposition, information timeline, modeling rationale, assumptions, expected mathematical bottleneck, and nearest literature.
