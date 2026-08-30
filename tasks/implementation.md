# Task: Implement RO/DRO Models Reliably

## 1. Mathematical-to-code map

Create `mathematical object | code variable | dimension | bounds/domain | solver construct`.

## 2. Prefer audited finite formulations

Do not code a claimed equivalent model until its direction and conditions are verified.

## 3. Unit tests

At minimum test zero radius/nominal recovery where expected, one-sample and one-dimensional cases, a known closed form, infeasible case, boundary radius, and brute-force/scenario comparison on a tiny instance.

## 4. Solver validation

Record status, primal objective, dual bound if meaningful, MIP/nonconvex gap, constraint violation, and numerical tolerances.

## 5. Original versus reformulated validation

When possible, solve both representations on tiny instances and compare values and recovered decisions. A mismatch is a debugging alarm; a match is not a proof.

## 6. Reproducibility

Use fixed random seeds, versioned data-generation code, saved hyperparameters, explicit solver options, machine/time limits, and no hidden manual tuning.
