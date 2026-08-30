# Task: Derive and Verify a Reformulation

This workflow is mandatory for every nontrivial claim of equivalence, exactness, strong duality, or finite-dimensional reduction.

Read `auditor/reformulation_auditor.md`, `auditor/duality_minimax_auditor.md` if needed, and `templates/reformulation_ledger.md`.

## Gate R0 — Normalize the original problem

Write the original problem exactly once with decision variables/spaces, random/uncertain variables/support, uncertainty/ambiguity set, objective/constraints, quantifier order, information structure, and infeasibility/infinite-value conventions. Do not begin algebra before R0 is stable.

## Gate R1 — Identify the nature/adversary subproblem

For DRO, fix the outer decision and isolate the worst-case expectation/risk problem. For multistage RO, isolate alternating decision/nature moves and nonanticipativity. State whether the inner optimum is attained or only a supremum/infimum.

## Gate R2 — Name the equivalence object and build the ledger

State whether the claim concerns original sets, projected/induced sets, pointwise objectives, feasible sets, optimal values, optimizer sets, or a recovery map. Read `auditor/equivalence_object_auditor.md`.

Represent the derivation as `P0 -> P1 -> ... -> PK`. For each arrow record transformation, implication direction, theorem/identity, qualification conditions, and preservation of feasible sets, values, and optimizers.

## Gate R3 — Audit duality/interchange

If using Lagrangian/Fenchel/conic/generalized-moment duality or minimax, state primal/dual spaces, establish weak duality, identify the exact strong-duality theorem, map every hypothesis, check closure/semicontinuity/Slater/interiority/compactness as applicable, and distinguish zero gap from primal/dual attainment.

## Gate R4 — Convert semi-infinite constraints

Identify the exact device: conjugate, support function, perspective, dual norm, S-lemma, conic duality, extreme-point reduction, finite-support theorem, K-adaptability lifting, enumeration/partition, or another exact device. State any qualification condition.

## Gate R5 — Establish both directions

For equivalence, prove original feasible -> reformulated feasible with same value and reformulated feasible -> original feasible with same value. If only optimal values match, say so. If only a bound is proved, label its direction.

Do not require duality when an exact direct construction, projection identity, coupling, perturbation identity, or other route establishes both directions. Audit the route actually used.

## Gate R6 — Convexity and solver class

Check objective/constraint convexity, cone representability, bilinear/nonconvex terms, integer variables, and growth with samples/scenarios/stages. State the final class: LP, SOCP, SDP, exponential cone, MILP/MICP, finite bilinear/nonconvex program, etc.

## Gate R7 — Sanity checks

Test at least three of zero radius, single sample, singleton support, one-dimensional uncertainty, no recourse, full/no information revelation, linear loss, or a known closed-form special case. When possible, numerically compare original and reformulated tiny instances.

## Gate R8 — Independent Auditor

The Auditor reconstructs the key equality independently and returns one verdict from `VETO_POLICY.md`.

## Required final language

Use “exactly equivalent under Assumptions ...”, “safe conservative approximation because ...”, “provides a lower/upper bound ...”, or “not established as equivalent; the gap is ...”. Never use “equivalent” as shorthand for “similar.”
