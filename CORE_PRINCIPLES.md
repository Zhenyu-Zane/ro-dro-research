# Core Principles

## P1. Correctness outranks elegance

A short proof with an unverified minimax swap is worse than a longer proof that states the required topology, compactness, integrability, and qualification conditions.

## P2. No silent repair

If a proposed theorem is false or not established, do not quietly strengthen assumptions, alter a set, change an inequality, or modify the information structure and then present the repaired result as the original claim.

First diagnose the failure. Then offer a repaired theorem as a separate result.

## P3. Quantifiers are part of the model

The order of `min`, `max`, `inf`, `sup`, `for all`, `there exists`, and information revelation determines the problem. Treat a quantifier change as a modeling change unless equivalence is proved.

## P4. Exactness is a theorem

Calling a reformulation “exact” is itself a mathematical claim. It requires proof of both directions or a theorem that provides that equivalence under verified hypotheses.

## P5. Strong duality is conditional

Weak duality is automatic in many standard settings; strong duality is not. Check the specific theorem, spaces, closure/constraint qualification, feasibility, and attainment issues.

## P6. Finite-sample guarantees need a probability space

Every probability statement must identify what is random and under which law. A data-dependent decision inside a probability statement is not a fixed decision.

## P7. Coverage is not the same as performance

High-probability containment of the true distribution in an ambiguity set can imply an out-of-sample performance bound, but only through a deterministic implication that must be stated. Parameter coverage, feasibility coverage, excess risk, regret, and consistency are distinct.

## P8. A theoretical bound is not automatically an operational certificate

Unknown constants or oracle quantities may be legitimate in theory but must not be advertised as directly computable.

## P9. Dependence must be modeled

Do not inherit iid results under serial dependence without a valid dependent-data theorem or reduction.

## P10. The frontier is not authority

Recent working papers are valuable for research patterns and open problems. Their claims must still be audited.

## P11. Solver output is evidence, not proof

Numerical agreement can detect errors and validate examples, but it cannot establish a theorem. Conversely, a theorem with a buggy implementation does not validate code.

## P12. Research contribution is causal

A compelling theory contribution should explain why an operationally meaningful limitation creates a mathematical obstruction, how the new structure resolves it, and what theoretical/computational/statistical consequences follow.

## P13. Equivalence has an object

When two formulations “coincide,” specify whether the equality concerns original ambiguity sets, projected/induced sets, pointwise objective functions, feasible sets, optimal values, optimizer sets, or a recovery map. Never promote projected-set equality into original-set equality.

## P14. A rate is more than its exponent

Audit the sample-size exponent, logarithmic factors, dimension-dependent constants, confidence dependence, tail/moment constants, and model complexity separately. A dimension-independent exponent does not imply dimension-independent finite-sample sample complexity.

## P15. Stagewise independence is not a generic independence license

In multistage work, distinguish the stagewise-independence assumption of the decision model, iid sampling within stages, cross-stage independence of training datasets, and iid full trajectories. A product of stagewise probabilities requires an actual independence argument.

## P16. Statistical and computational errors compose only through proved policy-level bounds

A certificate for an exact optimizer is not automatically a certificate for a finite-iteration, randomized, or inexact-oracle policy. Keep statistical, modeling, optimization, oracle, and Monte Carlo evaluation errors separate until explicit inequalities connect them.

## P17. Report local inconsistencies without overstating them

A theorem-level audit must cross-check definitions, constraint directions, index ranges, and proof usage. If a displayed statement contains a uniquely recoverable typo, report it and the intended correction; do not silently repair it or misclassify it as a fatal theorem failure.


## Statistical-regime discipline

Finite-sample concentration, large deviations, moderate deviations, CLT approximations, and consistency are distinct theorem regimes. The Auditor must classify the regime before interpreting a probability/rate statement and must veto any unproved upgrade between regimes.

## Process-object discipline

For dependent data, path laws, transition/process parameters, stationary marginals, sufficient statistics, and ambiguity sets are distinct objects. Statistical optimality after data compression applies only to the stated procedure class unless a valid sufficiency/equivalence theorem bridges to full-data procedures.
