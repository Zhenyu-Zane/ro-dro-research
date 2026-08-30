# Task: Derive a Finite-Sample / Statistical Guarantee

## Step F-1 — Exclude purely asymptotic substitutes

Before starting a finite-sample proof, run the classification in `auditor/deviation_regime_auditor.md`. A large-deviation, moderate-deviation, CLT, or consistency result is not a finite-sample certificate unless it comes with an explicit non-asymptotic remainder bound that yields the claimed probability for the stated sample size.

For dependent trajectories, a process LDP or ergodic theorem is not a substitute for a finite-sample mixing/Markov/martingale concentration theorem.

Always read `references/statistical_guarantees.md`, `auditor/statistical_auditor.md`, `auditor/oracle_quantity_auditor.md`, and `templates/randomness_map.md`; add the multistage and statistical–computational modules when triggered.

## Step S0 — State the target theorem before choosing a concentration inequality

Examples: parameter-region coverage, ambiguity-set containment, robust-feasibility probability, out-of-sample expected performance, out-of-sample disappointment, excess risk, or regret. Write the target event mathematically.

## Step S1 — Build the randomness map

Identify the training sample $\mathcal D_S$, its joint law, empirical distributions/estimators, data-dependent sets and optimizer, future/test variables, contexts/conditioning variables, and outer probability measure. If using regression residuals, state whether they are computed with true or estimated parameters.

## Step S2 — Separate deterministic implication from probabilistic event

A clean DRO proof often has: define a good event $\mathcal E_S$; prove deterministically that on $\mathcal E_S$ the robust objective/constraint dominates true performance; then lower-bound $\Pr(\mathcal E_S)$.

## Step S3 — Match dependence assumptions

Classify the sample as iid, independent non-identical, conditionally independent, martingale, mixing, Markov, trajectory, or clustered/block dependent. Use a theorem valid for that class. If none is available, return **NOT ESTABLISHED** rather than reusing an iid result.

## Step S4 — Tail/moment assumptions

State exactly what is required: bounded support, moments, sub-Gaussian/sub-exponential/light-tailed behavior, Lipschitz loss, bounded envelope, etc. Verify the current model satisfies it.

## Step S5 — Uniformity and provenance

If the decision is selected after seeing the same data, a fixed-$\bm x$ inequality may be insufficient. Establish a uniform event, a containment event that protects all decisions, sample splitting, a complexity-based bound, stability, or another valid mechanism. Record why uniformity holds.

## Step S6 — Multistage joint-event architecture and multiple uncertainty layers

For multistage results, distinguish model stagewise independence from training-sample independence. A product of stagewise event probabilities requires cross-stage independence; within-stage iid alone is insufficient. State whether evaluation is under product marginals or the true joint trajectory law.

For parameter uncertainty plus residual ambiguity, identify separate good events, account for dependence, combine them validly, avoid double-counting estimation error, and state any radius tradeoff.

## Step S7 — Rate anatomy

Use `templates/rate_anatomy.md`. Separate sample-size exponent, logs, dimension dependence in exponent and constants, confidence dependence, units, unknown tail/moment constants, decision-class complexity, metric/order dependence, and whether the rate is an upper bound, lower bound, minimax, or heuristic.

## Step S8 — Oracle audit

Classify every theorem input as `observable | known by design | tuning | estimated | unknown primitive | oracle`. Do not call a result fully data-driven when an operationally unavailable primitive remains.

## Step S9 — Calibration versus theorem

Separate a radius chosen for theoretical confidence from a radius chosen by cross-validation. Cross-validation does not automatically inherit the theoretical coverage probability.

## Step S10 — Statistical–computational composition

If the theorem is for an exact policy but implementation is approximate, finite-iteration, randomized, or inexact-oracle, separate statistical, modeling, optimization, oracle, and Monte Carlo errors. Inheritance requires policy-level inequalities for the actual output.

## Step S11 — Stress tests

At minimum examine small $S$, large dimension, singular empirical covariance, heavy tails, dependence, misspecified support, weak/negative side information, zero radius, and extreme confidence $\delta$.

## Step S12 — Auditor verdict

The Auditor checks from the probability space upward. If the bounded event is ambiguous, veto the claim.

## Required output

Return the exact target guarantee, randomness map, assumptions, proof architecture, theorem-condition map, rate/constants, oracle table, Auditor verdict, and precise scope of what is established.
