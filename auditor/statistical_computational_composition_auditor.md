# Auditor: Statistical–Computational Guarantee Composition

Use this module whenever a statistical guarantee is stated for an optimization model that is solved approximately, iteratively, heuristically, or with inexact oracles.

The central rule is:

> **A finite-sample theorem for an exact robust optimizer does not automatically certify the policy returned by a finite-iteration algorithm. Statistical error and optimization error must be composed explicitly.**

## 1. Separate the error layers

At minimum distinguish:

1. **statistical error** — estimation/ambiguity-set error caused by finite data;
2. **modeling error** — mismatch between the modeled uncertainty process and the true process;
3. **optimization error** — suboptimality relative to the exact robust problem;
4. **oracle error** — inexact subproblem, separation, integration, or adversarial oracle;
5. **Monte Carlo evaluation error** — finite test-sample error in reported experiments.

Never report one of these as if it controls the others.

## 2. Identify the exact theorem object

Record whether the statistical theorem is proved for:

- the exact robust optimal value;
- the exact robust optimal decision/policy;
- every robust-feasible decision/policy;
- a certificate evaluated at an arbitrary candidate decision.

This determines whether an approximate algorithm can inherit the theorem directly.

## 3. Determine what the algorithm guarantees

Classify the algorithmic output:

- exact optimum;
- $\varepsilon$-optimal objective value;
- primal feasible policy with an upper bound;
- lower bound only;
- stationary point;
- heuristic/finite-iteration policy;
- inexact-oracle solution.

An $\varepsilon$-optimal first-stage objective statement may be insufficient to bound the realized cost of the induced policy unless a policy-level robust-cost inequality is also available.

## 4. Compose only proved inequalities

A valid composition may look like

$$
R_{\mathbb P^\star}(\widehat\pi)
\le R_{\rm robust}(\widehat\pi)
\le V_{\rm robust}^\star+\varepsilon
$$

on a high-probability containment event. Both inequalities must be proved for the **same candidate policy** $\widehat\pi$.

Do not infer the first inequality merely because it holds for the exact robust optimizer. Do not infer the second from a lower bound on $V_{\rm robust}^\star$.

## 5. Dynamic algorithms require policy certification

For DDP/SDDP, Benders-type dynamic methods, K-adaptability, or approximate dynamic programming, check separately:

- first-stage optimality gap;
- quality of cost-to-go approximations;
- feasibility/nonanticipativity of the induced policy;
- upper versus lower policy bounds;
- exactness of stage oracles;
- termination criterion.

If random sampling or inexact subproblem steps violate the assumptions of the convergence theorem, classify the implementation guarantee separately from the ideal algorithm guarantee.

## 6. Experiment reporting

When numerical evaluation uses a finite test set, distinguish the sample mean from the true expected cost. If a confidence interval is required, account for Monte Carlo error separately.

## 7. Verdict rules

- **PASS** — statistical and computational guarantees are linked by explicit policy-level inequalities.
- **PASS WITH EXPLICIT CONDITIONS** — composition works after adding a stated optimization/feasibility certificate.
- **NOT ESTABLISHED** — exact-model theorem and approximate algorithm are both individually valid, but no theorem connects them.
- **FAIL** — a lower bound, stationarity result, or heuristic output is incorrectly presented as inheriting an exact finite-sample certificate.
