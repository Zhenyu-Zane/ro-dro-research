# Case: Contextual Robust Optimization

**Source:** Xun Zhang, Qinshen Tang, Zhi Chen, Li Chen, *Managing Inventory and Pricing with Contextual Robust Optimization*.

## Research pattern

Jointly treats uncertainty in estimated prediction parameters, ambiguity in residual distributions, decision-dependent prediction through pricing, and recourse through emergency ordering. It targets finite-sample performance and asymptotic optimality, making it a useful stress test for layered uncertainty.

## Researcher lessons

- Model parameter uncertainty and residual ambiguity as distinct layers.
- A guarantee can create a substitution/tradeoff between robustness radii; this is substantive only if proved rather than tuned heuristically.
- Economic structure can serve both interpretation and regularization.

## Auditor lessons

- Verify whether parameter confidence regions are conditional on realized covariates/prices and whether residual concentration uses independent errors.
- Track how estimated parameters alter empirical residual distributions.
- Check radius computability versus unknown tail proxies.
- An affine-recourse SDP lower bound is an approximation unless equality is proved.
- In asymptotic optimality, parameter-set and ambiguity-radius shrinkage must jointly imply convergence to the true problem.

## Stress test

Construct separate parameter and residual good events, combine their probabilities, and audit whether the robust objective is a valid high-confidence bound on true performance.
