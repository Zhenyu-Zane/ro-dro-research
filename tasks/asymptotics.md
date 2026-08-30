# Task: Consistency, Large Deviations, and Asymptotic Optimality

## Step A-1 — Classify the asymptotic regime

Before proving anything, fill `templates/deviation_regime_ledger.md` and run `auditor/deviation_regime_auditor.md`. Distinguish LLN/consistency, CLT/local asymptotics, moderate deviations, and large deviations. A theorem about one regime cannot be silently upgraded to another.

For dependent trajectories, also fill `templates/process_randomness_map.md` and run `auditor/process_law_auditor.md`.

## Step A0 — Define the limiting population problem

State the true problem and its optimal value/set of optimizers.

## Step A1 — Identify converging ingredients

Possible objects include estimator $\widehat{\bm\theta}_S$, empirical/reference distribution $\widehat{\mathbb P}_S$, ambiguity/uncertainty set, robust objective functions, feasible sets, optimal values, and optimizers.

Do not jump from parameter consistency directly to decision optimality.

## Step A2 — Choose the convergence route

Examples: uniform law of large numbers, epi-convergence, set convergence, stability/sensitivity, compactness plus uniform convergence, Borel–Cantelli from summable finite-sample failures, or continuous mapping. State the exact theorem used.

## Step A3 — Identifiability/nondegeneracy

Check whether the data identify the true parameter/model. For regression-like models, rank/eigenvalue conditions often matter.

## Step A4 — Shrinking-set logic

If robustness radii shrink with $S$, prove: the true object is eventually included with the required probability/almost surely; the diameter or relevant discrepancy shrinks; and the robust objective converges to the population objective.

## Step A5 — Optimizers

Optimal-value convergence does not imply optimizer convergence without additional structure. If only objective convergence is established, do not claim decision consistency.

## Step A6 — Almost sure versus in probability

Keep the mode of convergence explicit. A high-probability bound with $\delta_S$ can yield eventual almost-sure statements only if failure probabilities are summable and the event structure supports the argument.

## Auditor checks

Check hidden compactness/coercivity, uniqueness, interchange of limit and optimization, convergence of random feasible sets, dependence of contexts/decision sets on $S$, and misuse of asymptotic normality.

## Step A7 — Large-deviation proofs

When the theorem uses an LDP, write the upper and lower inequalities explicitly. The upper bound applies to the closure of the bad event; the lower bound applies to its interior. If a Pareto/minimax optimality proof needs the LDP lower bound, verify that the constructed witness is genuinely an interior point.

Record the LDP speed $b_S$ and rate function $I$. Interpret a target $r$ as an exponential-rate budget unless a separate finite-sample theorem gives it another operational meaning.

## Step A8 — Compression and statistical optimality

If a procedure depends only on a statistic, distinguish optimality in the restricted statistic-based class from optimality over arbitrary raw-data procedures. Run `auditor/sufficiency_compression_auditor.md` before claiming the second. An LDP for the statistic is not by itself a no-loss theorem.
