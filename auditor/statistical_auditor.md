# Statistical Auditor

Audit from the probability space upward, not from the final inequality backward.

## 1. Randomness map

Verify every random object and its governing law.

Questions:

- Is the training sample iid?
- Are covariates conditioned on or random?
- Is the selected decision data-dependent?
- Are residuals computed with estimated parameters?
- Is a future observation independent of the training sample?
- Is the outer probability over data, future outcomes, or both?

## 2. Event semantics

Translate the theorem into a named event $\mathcal E_S$.

If the event is ambiguous in words, the theorem is not ready.

## 3. Pointwise versus uniform

A statement valid for each fixed $\bm x$ need not hold for the optimizer $\widehat{\bm x}_S$ selected from the same data.

Require a uniform event, independent validation data, stability argument, or another valid mechanism.

### Uniformity provenance

Record *why* the result is uniform. Typical mechanisms include:

- a single ambiguity-set/distribution-containment event whose deterministic implication holds for every decision;
- an exact projection/induced-set identity that transfers one common good event to every decision;
- a covering-number, VC/Rademacher, metric-entropy, or other empirical-process argument;
- algorithmic stability;
- sample splitting or independent validation.

Do not add a union bound over decisions when a single structural containment event is already uniform. Conversely, do not call a fixed-decision concentration result uniform merely because the same formula can be written for each decision.

## 4. Concentration theorem match

Check:

- independence/dependence class;
- identical distribution;
- boundedness/tails;
- dimensionality;
- metric order;
- moment requirements;
- support;
- whether constants are explicit/known.

## 5. Data reuse

If data are used to estimate parameters, construct residuals, choose hyperparameters, and evaluate guarantees, verify whether the theorem allows that reuse.

## 6. Conditional guarantees

When conditioning on observed contexts/covariates, distinguish a conditional statement from an unconditional one. Do not integrate or decondition without a valid argument.

## 7. Multiple events

If the proof needs parameter containment and distributional containment, check how confidence levels combine. Use a union bound only when appropriate and state the resulting level.

## 8. Finite-sample status

Reject “finite-sample” if the proof relies on an asymptotic approximation without a non-asymptotic error bound.

## 9. Rate anatomy and curse-of-dimensionality claims

Use `templates/rate_anatomy.md` for any nontrivial rate claim. Separate:

- the exponent of $S$ (or $N$);
- logarithmic factors;
- dimension in the exponent;
- dimension in multiplicative/additive constants;
- confidence dependence;
- moment/tail constants;
- hypothesis/decision-class complexity;
- metric/order parameters.

A dimension-independent sample-size exponent does **not** imply dimension-independent finite-sample constants or sample complexity. If a paper says “dimension-free” or “free from the curse of dimensionality,” identify exactly which sense is proved.

## 10. Guarantee strength

State exactly whether the theorem certifies:

- the robust objective;
- the selected decision's true objective;
- feasibility probability;
- optimality gap;
- ambiguity-set coverage.

Do not upgrade one into another.

## 11. Radius/certificate computability

For every data-dependent radius, threshold, or confidence set, list the quantities needed to evaluate it. If any required input is an unknown true moment, tail parameter, mixing coefficient, density bound, true covariance feature, or true estimation error, classify the theorem as a theoretical guarantee unless a valid computable bound is supplied.

Do not criticize a correct theorem merely for containing an unknown primitive if the authors only claim a theoretical guarantee. Veto only an overstatement such as “fully data-driven/computable certificate” when the required quantity is not operationally available.

## 12. Multistage sampling architecture

If a theorem contains stagewise ambiguity sets, a dynamic policy, or a joint trajectory, also run `multistage_statistical_auditor.md`. Do not infer cross-stage independence from within-stage iid sampling. If the proof multiplies stagewise event probabilities, identify the exact training-data law that makes those events independent.

## 13. Statistical–computational composition

If the certified decision/policy is produced by an approximate, finite-iteration, randomized, or inexact-oracle optimization method, also run `statistical_computational_composition_auditor.md`. State separately which theorem controls statistical error and which theorem controls optimization/policy error.

## 14. Theorem regime versus evaluation regime

Check whether the theorem evaluates a product of stagewise marginals, a true dependent joint process, or conditional transition laws. Numerical tests under a different process class are misspecification experiments unless a separate theorem transfers the guarantee.

## 15. Deviation-regime classification

For any asymptotic tail/rate statement, also run `deviation_regime_auditor.md`. Record whether the theorem is non-asymptotic, LDP, MDP, CLT/local asymptotic, or consistency/LLN. Never convert an LDP exponent into a finite-sample confidence level without an explicit finite-$S$ remainder theorem.

## 16. Dependent process law

For Markov, autoregressive, mixing, martingale, or trajectory data, also run `process_law_auditor.md` and fill `../templates/process_randomness_map.md`. Distinguish path laws, process parameters, stationary marginals/doublets, transition kernels, and statistics.

## 17. Sufficiency and compression

If a statistic/residual/feature representation replaces the raw training data and a theorem claims statistical optimality or no information loss, run `sufficiency_compression_auditor.md`. State the class over which the result is optimal.
