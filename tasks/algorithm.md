# Task: Algorithm Design

## 1. Start from the audited formulation

Do not design an algorithm around an unaudited reformulation.

## 2. Classify the computational object

- convex finite-dimensional;
- conic;
- mixed-integer;
- bilinear/nonconvex;
- semi-infinite;
- infinite-dimensional;
- decomposition-friendly;
- multistage policy optimization.

## 3. Algorithm choice

Possible routes:

- off-the-shelf conic solver;
- bisection;
- cutting plane / constraint generation;
- column-and-constraint generation;
- Benders/decomposition;
- K-adaptability;
- sample/scenario approximation;
- stochastic/online first-order method;
- DC/nonconvex algorithm;
- global optimization.

Explain why the method matches the structure.

## 4. Guarantee taxonomy

State whether the algorithm provides:

- exact optimum;
- global optimum under finite termination;
- $\epsilon$-optimality;
- lower/upper bounds;
- stationary point only;
- heuristic solution.

Never call a local method exact unless a global argument exists.

## 5. Complexity

Report complexity in terms of meaningful dimensions: samples, uncertainty dimension, decision dimension, stages, candidate policies $K$, cone dimensions, and scenarios/cuts.

## 6. Numerical certification

Track primal/dual bounds or original/reformulated objective values when available. Solver tolerance is not proof of mathematical equality.

## 7. Statistical-certificate inheritance

If the model has a finite-sample/out-of-sample theorem, do not assume the algorithmic output inherits it. Run `auditor/statistical_computational_composition_auditor.md` whenever the theorem is for an exact optimizer but the algorithm returns an $\varepsilon$-optimal, finite-iteration, randomized, or inexact-oracle policy.

For dynamic methods such as DDP/SDDP, report separately the first-stage objective gap, feasibility/nonanticipativity of the induced policy, quality/direction of cost-to-go bounds, exactness of stage oracles, and whether a policy-level robust upper bound exists.
