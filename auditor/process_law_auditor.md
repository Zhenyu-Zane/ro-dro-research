# Process-Law Auditor

Use this auditor whenever training data form a trajectory, Markov chain, autoregressive process, time series, or another dependent stochastic process, or whenever ambiguity is placed on a process parameter rather than directly on a one-period distribution.

## 1. Build the process-law object map

Distinguish all of the following objects when they exist:

- observed trajectory $\tilde{\bm\xi}_{[S]}=(\tilde{\bm\xi}_1,\ldots,\tilde{\bm\xi}_S)$;
- finite-horizon path law $\mathbb P_{\bm\theta}^{(S)}$;
- infinite-process law $\mathbb P_{\bm\theta}$;
- model/process parameter $\bm\theta\in\Theta$;
- stationary marginal, invariant distribution, transition kernel, or stationary doublet distribution;
- statistic $\widehat{\bm S}_S=T_S(\tilde{\bm\xi}_{[S]})$;
- limiting statistic $\bm S_\infty(\bm\theta)$;
- rate function or discrepancy $I(\bm s,\bm\theta)$;
- decision risk $c(\bm x,\bm\theta)$;
- ambiguity set in **parameter/process-law space**.

Do not identify these objects merely because they parameterize one another.

## 2. Path law is not a one-step marginal

For dependent data,
\[
\mathbb P_{\bm\theta}^{(S)}
\]
is generally not the product of one-step marginals. A divergence/rate function for transition laws or stationary doublet distributions is not automatically the KL divergence or Wasserstein distance between one-period marginals.

If the ambiguity set is
\[
\{\bm\theta:I(\widehat{\bm S}_S,\bm\theta)\le r\},
\]
state explicitly that it is a **parametric/process ambiguity set** unless the paper proves an equivalent distribution-space representation.

## 3. Dependence assumptions

Record separately:

- stationarity;
- ergodicity;
- Markov order;
- mixing/geometric ergodicity if used;
- initialization assumptions;
- innovation structure for autoregressive models;
- whether training and future/test data come from the same process law;
- whether independent trajectories or one dependent trajectory are observed.

Ergodicity can justify consistency without supplying a finite-sample concentration inequality.

## 4. Statistical theorem route

Identify the exact route:

- Markov/trajectory concentration;
- spectral-gap or mixing inequality;
- martingale concentration;
- Gärtner–Ellis theorem;
- Donsker–Varadhan/Sanov-type LDP;
- explicit likelihood or exponential-family argument;
- another process-specific theorem.

Check every hypothesis of that theorem against the process model.

## 5. Boundary and closure

Process parameters often live in the interior of a simplex or stability region while robust ambiguity sets use its closure. Check:

- whether the rate/divergence is defined on $\Theta$ or $\operatorname{cl}\Theta$;
- whether a continuous extension exists;
- whether only a lower-semicontinuous extension exists;
- whether zero transition probabilities or stability-boundary parameters create infinite values;
- whether compactness/attainment relies on the extension.

Do not silently use continuity on the boundary when only lower semicontinuity is established.

## 6. Decision problem versus data process

The stochastic process generating the training data and the uncertainty entering the downstream decision problem need not be the same mathematical object. State how the estimated process parameter determines the risk $c(\bm x,\bm\theta)$.

## 7. Veto triggers

Veto or downgrade a theorem claim if it:

- treats a dependent path as iid without justification;
- replaces a path-law rate function with a marginal divergence by analogy;
- invokes an LDP without verifying the process-specific hypotheses;
- extends a result to boundary parameters without a valid extension argument;
- claims a finite-sample certificate from an asymptotic process LDP alone.
