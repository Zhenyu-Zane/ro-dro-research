# Case: Knowledge-Guided Wasserstein DRO

**Source:** Wang et al., *Knowledge-Guided Wasserstein Distributionally Robust Optimization*.

## Research pattern

Shows that the transportation cost can encode external knowledge and induce structured regularization.

## Researcher lessons

- A transport cost is a model of plausible distribution shift, not a neutral metric choice.
- Prior knowledge can constrain or penalize transport in selected directions.
- Regularization equivalence is useful for interpretation and tractability but is tied to specific losses and costs.

## Auditor lessons

- Verify that the transport cost satisfies the strong-duality theorem assumptions; it need not itself be a metric.
- Check hard-constraint limits such as $\lambda\to\infty$.
- Multiple prior directions can collapse perturbations if they span feature space.
- A smaller ambiguity set does not automatically preserve finite-sample coverage.

## Stress test

Given external predictors that alter transport cost, characterize ambiguity-set inclusion and identify assumptions needed for valid coverage.
