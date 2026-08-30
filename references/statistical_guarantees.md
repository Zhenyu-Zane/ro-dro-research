# Statistical Guarantee Taxonomy

A statistical theorem must first identify its target. Do not use “performance guarantee” as a catch-all.

## A. Parameter coverage

Typical target:

$$
\mathbb P^\star_S[\bm\theta^\star\in\widehat{\Theta}_S]\ge 1-\delta.
$$

This is not yet a guarantee about the robust decision unless a deterministic implication connects parameter containment to decision performance.

## B. Ambiguity-set coverage

Typical target:

$$
(\mathbb P^\star)^S[\mathbb P^\star\in\widehat{\mathcal P}_S]\ge 1-\delta.
$$

On the containment event, the worst-case objective bounds the true objective for every fixed feasible decision. This can yield a uniform statement if the containment event itself is independent of the selected decision.

## C. Feasibility guarantee

Typical target:

$$
\mathbb P^\star[f(\widehat{\bm x}_S,\tilde{\bm v})\le 0]\ge 1-\epsilon,
$$

possibly with outer confidence over training data. Distinguish the operational violation probability $\epsilon$ from confidence level $\delta$.

## D. Out-of-sample performance/disappointment

A high-probability bound comparing the true expected loss/reward of a data-dependent decision with a data-dependent robust certificate. Audit carefully which probability is over the training sample and whether the future observation is already integrated out in an expectation.

## E. Generalization/excess risk

Generalization gap concerns empirical/robust certificate versus population performance. Excess risk compares the selected decision with the population-optimal decision. They are different quantities and require different arguments.

## F. Regret

Specify the comparator and whether regret is pointwise, expected, high probability, cumulative, or instance-dependent.

## G. Consistency and asymptotic optimality

Consistency of an estimator/set does not automatically imply convergence of optimal decisions or objective values. Check epi-convergence/uniform convergence/compactness/identifiability or the specific theorem used.

## H. Finite-sample versus asymptotic

A theorem using $S\to\infty$, CLT approximations, asymptotic quantiles, or $o_p(1)$ is not a finite-sample theorem. A finite-sample theorem should state a bound valid for the stated finite $S$ under explicit assumptions.

## I. Theoretical guarantee versus operational certificate

Classify every constant as observable from data, known by design, user-chosen, estimated, unknown distributional primitive, or oracle quantity. A bound containing an unknown primitive can be mathematically valid but not directly computable.

## J. Multistage guarantees

For a multistage theorem, record both the **process law** and the **training-data law**. Stagewise independence of the optimization model is distinct from independence of empirical datasets used to build stagewise ambiguity sets. If a proof multiplies stagewise containment probabilities, cross-stage independence must be justified.

Also state whether performance is evaluated under a product of stagewise marginals, conditional transition kernels, or a dependent joint trajectory distribution.

## K. Statistical versus computational guarantees

A finite-sample theorem for the exact robust optimizer does not automatically apply to a finite-iteration or inexact-oracle solution. Certify the actual output by composing statistical containment/performance inequalities with a policy-level optimization certificate for the same candidate decision or policy.
