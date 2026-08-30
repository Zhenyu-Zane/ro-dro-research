# Sufficiency and Compression Auditor

Use this auditor whenever raw training data are replaced by residuals, features, empirical moments, a sufficient statistic, a learned representation, or another compressed object and the paper claims optimality or “no information loss.”

## 1. Separate the procedure classes

Define explicitly:

- full-data procedures measurable with respect to the raw data $\tilde{\bm\xi}_{[S]}$;
- compressed procedures of the form $g_S(\widehat{\bm S}_S)$ for a statistic $\widehat{\bm S}_S$.

Optimality in the compressed class does **not** imply optimality in the full-data class.

## 2. What does the statistical theorem establish?

A statistic may be:

- consistent;
- asymptotically normal;
- LDP-admitting;
- sufficient;
- minimal sufficient;
- approximately sufficient.

These notions are not interchangeable. In particular, an LDP for a statistic may support an optimal DRO rule **among statistic-based procedures** without proving that compression is lossless.

## 3. No-loss claims require a bridge

A claim such as

> compressing the raw data incurs no loss of optimality

requires an explicit bridge from the full-data class to the compressed class. Typical bridges include:

- a sufficient-statistic factorization/conditional-law argument;
- an explicit equivalence theorem for the two meta-optimization problems;
- a Rao–Blackwell-type argument when the loss/criterion permits it;
- another theorem that shows full-data procedures cannot improve the criterion.

Consistency alone is insufficient.

## 4. Sufficiency must match the process family

For dependent data, verify sufficiency with respect to the **finite-horizon path-law family** $\{\mathbb P_{\bm\theta}^{(S)}:\bm\theta\in\Theta\}$, not merely a one-step marginal family.

Check whether sufficiency holds for every $S$, whether the statistic depends on initialization, and whether boundary parameters remain mutually absolutely continuous where the proof requires change of measure.

## 5. Scope of Pareto/statistical optimality

When a theorem proves Pareto dominance, minimax optimality, or statistical optimality, write the class over which dominance is established:

- all full-data predictors/prescriptors;
- only compressed/statistic-based ones;
- only a parametric family;
- only procedures satisfying a specified disappointment/rate constraint.

Never abbreviate a restricted-class result to “DRO is optimal” without the class and criterion.

## 6. Veto triggers

Veto “no information loss” if:

- the statistic is merely consistent;
- sufficiency is asserted for marginals but the data law is a dependent path law;
- the full-data and compressed procedure classes are not compared;
- the theorem establishes only asymptotic equality of one objective but prose claims finite-sample equivalence of procedures.
