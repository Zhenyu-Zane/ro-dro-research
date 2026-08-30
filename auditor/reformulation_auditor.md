# Reformulation Auditor

## A. Semantic preservation

- Are the same decisions optimized?
- Is the same uncertainty represented?
- Is the information timing unchanged?
- Are feasibility conventions unchanged?
- Are support constraints preserved?

## B. Quantifier audit

Write the quantifier string for original and reformulated models.

Examples:

`min_x sup_P` is not automatically interchangeable with `sup_P min_x`.

`min_x max_z min_y` is not equivalent to choosing a function $y(z)$ unless nonanticipativity/measurability and policy construction are handled correctly.

## C. Equivalence object and value-versus-solution audit

First read `auditor/equivalence_object_auditor.md`. Identify the exact object being equated.

Identify which is proved:

- same feasible set;
- same optimal value;
- mapping between optimizers;
- one-way recovery only.

Do not infer optimizer equivalence from value equivalence.

### Proof-route neutrality

Do not mechanically demand strong duality if the claimed equivalence is proved by another exact route, such as a direct lifting/projection construction, perturbation identity, coupling argument, extreme-point characterization, or algebraic bijection. Audit the proof route actually used. If duality or minimax is used anywhere, then invoke the corresponding specialized auditor.

## D. Infinite-dimensional to finite-dimensional audit

Check whether the finite representation relies on:

- compact support;
- lower/upper semicontinuity;
- growth control;
- Slater/interiority;
- finite support of reference distribution;
- polyhedral/conic representability;
- saddle structure.

## E. Bound direction

For every relaxation/restriction, derive the direction from first principles.

For minimization:

- restricting feasible decisions raises the optimum;
- relaxing constraints lowers the optimum.

For inner maximization, directions reverse appropriately. Track nested problems carefully.

## F. Attainment

If an argmin/argmax is used, verify existence. Otherwise use inf/sup.

## G. Boundary multipliers

Check cases where dual/radius variables equal zero. Perspective/conjugate formulas often require explicit conventions at zero.

## H. Final verdict

PASS requires both semantic and mathematical equivalence under stated conditions.
