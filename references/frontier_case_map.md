# Frontier Case Map

The supplied representative projects are used as research-pattern case studies.

| Case | Research pattern | Primary audit lesson |
|---|---|---|
| Robust Satisficing | New target-oriented robustness criterion / fragility | New criterion must be separated from classical RO/DRO and axiomatized carefully |
| Predict, Optimize, Satisfice, Then Fortify | Prediction + residual ambiguity + coefficient estimation uncertainty | Separate sources of uncertainty and do not let data-dependence disappear in guarantees |
| Data-Driven Uncertainty Sets | Learn uncertainty-set geometry directly from data | Finite-sample guarantee depends on class complexity and parameterization |
| Decision-Dependent Information Discovery | Decisions alter what is observed and when | Quantifier order and nonanticipativity are central; dynamic equivalence must be proved |
| Contextual Robust Optimization | Parameter uncertainty + residual ambiguity + decision-dependent prediction | Layered uncertainty can create coupled radii and tractability/statistical tradeoffs |
| Knowledge-Guided WDRO | Prior knowledge modifies transport geometry | Transport cost is a modeling choice; regularizer equivalence is setting-specific |
| Streamlining Robustness | Tolerated/globalized robustness + asymmetric L1 geometry + multiperiod models | Exactness can hinge on support and geometry; streamlined formulation must not hide restrictive assumptions |
| Wu–Li–Mao Generalization/Regularization | Projection-based generalization + exact regularization | Separate projected-set equivalence from original-set equality; separate dimension-free exponent from dimension-dependent constants |
| Zhang–Sun Multistage Wasserstein DR-MCO | Stagewise Wasserstein DRO + finite-sample guarantee + DDP | Distinguish within-stage iid, cross-stage sample independence, process misspecification, and exact-policy versus finite-iteration guarantees |
| Sutter–Van Parys–Kuhn Pareto Dominance | Dependent-process data + LDP-derived parametric DRO + statistical optimality | Distinguish LDP from finite-sample guarantees, process-law ambiguity from marginal metrics, and compressed-class optimality from no-loss sufficiency |

Read the corresponding file under `cases/` when a new project resembles one of these patterns.
