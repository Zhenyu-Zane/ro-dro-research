# Dependent-Process Statistical Map

This note is a routing map, not a substitute for original probability theorems. For a concrete proof, cite and verify the original theorem.

## 1. First question: finite-sample or asymptotic?

Dependent-data tools split into distinct families.

### Finite-sample / non-asymptotic

Possible routes include martingale inequalities, mixing inequalities, Markov-chain concentration, spectral-gap/log-Sobolev bounds, regeneration methods, and blocking arguments. Their constants can depend on mixing times, spectral gaps, drift/minorization constants, or initialization.

Do not assume these constants are known or estimable.

### Large deviations

For Markov or autoregressive processes, an LDP can identify the exponentially optimal shape of a data-driven ambiguity set. The resulting rate function need not be a conventional probability metric and may be nonconvex in the model parameter.

An LDP is asymptotic and does not by itself give a finite-sample confidence radius.

### Consistency/ergodic arguments

Ergodic theorems can justify convergence of empirical statistics while providing no non-asymptotic error probability.

## 2. Theorem-condition map

For each cited result record:

- process class;
- stationarity requirement;
- initialization requirement;
- mixing/ergodicity assumptions;
- boundedness or moment/tail assumptions;
- statistic to which it applies;
- finite-sample or asymptotic nature;
- speed/rate/constants;
- whether the result is uniform in parameters.

## 3. DRO implication

Only after the probabilistic theorem is established may it be converted into a robust guarantee. State the deterministic implication separately:

`statistical good event -> true parameter/process lies in ambiguity set -> robust objective bounds true risk`.

If the first arrow is only asymptotic, the final guarantee is only asymptotic unless an independent non-asymptotic result is supplied.
