# Statistical Rate Anatomy

Use this template whenever a theorem or paper claims a convergence rate, dimension-free behavior, curse-of-dimensionality avoidance, minimax optimality, or sample-complexity improvement.

| Component | Expression / dependence | Observable or known? | Audit note |
|---|---|---|---|
| sample-size exponent |  |  |  |
| logarithmic factors |  |  |  |
| dimension in exponent |  |  |  |
| dimension in constants |  |  |  |
| confidence parameter |  |  |  |
| moment/tail constants |  |  |  |
| hypothesis/decision-class complexity |  |  |  |
| metric/order parameter |  |  |  |
| other nuisance quantities |  |  |  |

## Required conclusions

State separately the asymptotic sample exponent; dimension dependence in constants; whether sample complexity is dimension-independent; whether the radius/certificate is computable from observed data; and whether “curse-free” refers only to the exponent or the full finite-sample bound.

Never infer dimension-free sample complexity merely because the exponent does not contain dimension.
