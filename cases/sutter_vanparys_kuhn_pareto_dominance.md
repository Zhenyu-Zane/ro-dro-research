# Case: Sutter–Van Parys–Kuhn Pareto Dominance

**Source:** Tobias Sutter, Bart Van Parys, Daniel Kuhn, *A Pareto Dominance Principle for Data-Driven Optimization*, Operations Research 72(5):1976–1999 (2024).

## Why this case matters

This external theorem-level stress test covers dependent-process data, large-deviation principles, parametric/process ambiguity, and statistical optimality/Pareto dominance.

## Audit findings

### Core theorem chain — PASS

The main logic is coherent under the stated regular large-deviation assumptions, including the distinct roles of closure in the LDP upper bound and interior in the LDP lower bound.

### LDP is not a finite-sample guarantee

A statement of the form

$$
\limsup_{S\to\infty}\frac1S\log\mathbb P[\mathcal E_S^c]\le-r
$$

controls an asymptotic exponential rate. It does not imply $\mathbb P[\mathcal E_S]\ge1-e^{-rS}$ for every finite $S$ without an additional non-asymptotic theorem. This motivated `auditor/deviation_regime_auditor.md`.

### Process ambiguity is not marginal ambiguity

For Markov/autoregressive data, the relevant statistic and rate function can live in transition/process-parameter space. A conditional-relative-entropy rate function must not be relabeled as a KL ball on one-period marginals unless an equivalence is proved. This motivated `auditor/process_law_auditor.md`.

### Compression-class optimality versus no-loss sufficiency

An LDP-admitting statistic can support optimality among statistic-based procedures without proving that compression loses no information relative to arbitrary raw-data procedures. A separate sufficiency/equivalence bridge is required. This motivated `auditor/sufficiency_compression_auditor.md`.

## General lesson

For dependent data, classify the theorem regime first, map the process-law object carefully, and always state the procedure class over which statistical optimality is proved.
