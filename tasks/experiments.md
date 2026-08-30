# Task: Design Numerical Experiments

## Objective

Experiments should test the theoretical mechanism, not merely show that a new method wins on average.

## Required experiment families

### 1. Structural sanity

Use small instances with known or brute-force solutions to validate the formulation/reformulation.

### 2. Mechanism experiment

Vary the parameter that activates the proposed mechanism, such as ambiguity radius, parameter-uncertainty radius, information-discovery budget, robustness target, transport-cost knowledge weight, uncertainty-set geometry, or dependence strength. The response should match the theorem or conceptual mechanism.

### 3. Nearest baselines

Include the model obtained by removing each new ingredient separately: empirical/estimate-then-optimize, classical RO, standard DRO, residual-only DRO, parameter-only RO, standard K-adaptability, vanilla Wasserstein DRO, or robust satisficing as appropriate.

### 4. Statistical calibration

If a finite-sample theorem is claimed, simulate empirical coverage/disappointment across sample sizes and confidence levels. Do not claim theorem validation merely because average performance is good.

### 5. Misspecification

Stress heavy tails, distribution shift, incorrect support, noisy prior knowledge, weak covariates, dependent samples, and nonlinear DGPs when a linear model is fitted.

### 6. Computational scaling

Report time, memory, optimality gap, iteration count, and failure rate as relevant. If the theorem is for an exact optimizer but experiments use early termination, random/inexact stage oracles, heuristics, or approximate dynamic programming, report that implementation regime explicitly.

### 7. Process mismatch and theorem scope

For multistage models, state whether training/evaluation paths are stagewise independent, Markov, mixing, or generally dependent. If a stagewise-independent model is deliberately tested on dependent paths, label it model-misspecification/robustness evidence rather than theorem validation.

### 8. Real data

Use real data to demonstrate operational relevance, but do not infer causal managerial mechanisms unless the empirical design supports causality.

## Reporting

Separate statistical uncertainty, operational magnitude, computational advantage, theoretical coverage, and qualitative mechanism.
