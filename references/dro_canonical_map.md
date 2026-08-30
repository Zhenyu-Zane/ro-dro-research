# Canonical DRO Map

This map follows the conceptual organization of the supplied 2024 Kuhn–Shafiee–Wiesemann source manuscript. It is a navigation layer, not a replacement for checking the original theorem statement.

## 1. Ambiguity sets

Primary families:

- moment-based ambiguity sets;
- $\phi$-divergence ambiguity sets;
- optimal-transport / Wasserstein ambiguity sets;
- other structured ambiguity sets.

Research question: what distributional information is credible, and how does the chosen set encode it?

## 2. Topological properties and attainment

Before speaking about a “worst-case distribution,” check whether the supremum is attained. Compactness/tightness, closure, semicontinuity, and moment/tail conditions matter.

Do not use “worst-case distribution” when only a supremum over a non-attaining sequence is known. Say “worst-case value” or “asymptotically worst-case distributions” as appropriate.

## 3. Duality for worst-case expectations

Nature's subproblem has the generic form

$$
\sup_{\mathbb P\in\mathcal P}\mathbb E_{\mathbb P}[\ell(\tilde{\bm v})].
$$

The canonical proof strategy parameterizes the ambiguity set in a finite-dimensional way and uses convex-analytic duality. Strong duality depends on the exact ambiguity-set construction and qualification conditions.

## 4. Worst-case risk

When the objective is a law-invariant risk functional rather than an expectation, minimax interchange or optimized-certainty-equivalent representations can introduce an additional layer of conditions. Audit every interchange.

## 5. Analytical solutions

Closed-form worst-case bounds are special structures, not the default. Always verify the loss class and ambiguity-set assumptions before transplanting a formula.

## 6. Finite convex reformulations

The core workflow is:

1. dualize nature's infinite-dimensional problem;
2. represent the semi-infinite dual constraints by convex conjugates/support functions/perspectives or other exact finite devices;
3. verify the qualification conditions that convert inequalities to equalities;
4. combine the finite representation with the outer decision problem;
5. identify the final cone/program class.

A finite-dimensional representation can still be nonconvex. A convex representation can still require a nontrivial cone. “Finite” and “tractable” are not synonyms.

## 7. Regularization by robustification

DRO can induce regularization, but an observed regularizer-equivalence is a structural theorem that depends on the loss, transport cost/divergence, and support assumptions. Do not generalize an equivalence beyond its exact setting.

## 8. Numerical solution methods

When no compact finite reformulation is useful, tailored methods include scenario, cutting-plane, online/stochastic, and problem-specific algorithms. Algorithmic convergence and statistical guarantees are separate claims.

## 9. Statistical guarantees

Separate:

- excess risk and out-of-sample disappointment;
- asymptotic analyses;
- non-asymptotic finite-sample analyses.

For non-asymptotic analysis, distinguish ambiguity-set containment/measure concentration from generalization-bound approaches.

Moment-based ambiguity can remain structurally ambiguous even with exact low-order moments; do not automatically claim asymptotic recovery of the true stochastic program unless the ambiguity set shrinks in a way that identifies the true law.
