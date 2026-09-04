# Case: Kannan–Bayraksan–Luedtke Residuals-Based DRO

**Source:** Rohit Kannan, Güzin Bayraksan, James R. Luedtke, *Residuals-based Distributionally Robust Optimization with Covariate Information*.

## Research pattern

The target is a conditional stochastic program

$$
\inf_{\bm z\in\mathcal Z}\;\mathbb E[c(\bm z,\tilde{\bm Y})\mid \tilde{\bm X}=\bm x],
$$

under a regression representation $\tilde{\bm Y}=f^\star(\tilde{\bm X})+\tilde{\bm\varepsilon}$. A regression estimator $\widehat f_S$ and its empirical residuals generate scenarios for a new covariate realization $\bm x$. The DRO ambiguity set is centered at the resulting empirical residual-based distribution.

The key statistical decomposition separates two errors:

1. **prediction/regression error** from replacing $f^\star$ by $\widehat f_S$ at the new covariate and at the training covariates; and
2. **residual-distribution error** from approximating the conditional distribution by the empirical distribution of the true residual scenarios.

The Wasserstein triangle inequality connects these layers before the robust certificate is invoked.

## Finite-sample architecture

For the paper's Wasserstein ER-DRO construction, the baseline theoretical radius is

$$
\zeta_S(\alpha,\bm x)
=
\kappa^{(1)}_{p,S}(\alpha,\bm x)
+
\kappa^{(2)}_{p,S}(\alpha),
$$

where $\kappa^{(1)}$ controls regression estimation and $\kappa^{(2)}$ controls empirical Wasserstein error for the true residual scenarios. The two probability bounds are combined to obtain conditional-distribution containment and hence the finite-sample certificate

$$
\Pr\!
\left[
 g(\widehat{\bm z}^{\rm DRO}_S(\bm x);\bm x)
 \le
 \widehat v^{\rm DRO}_S(\bm x)
\right]
\ge 1-\alpha
$$

for almost every covariate realization under the paper's assumptions.

The paper also records the sharper Gao/Blanchet route: when the corresponding loss-level finite-sample theory applies, the residual-distribution contribution can be taken on the $S^{-1/2}$ scale, and the radius is combined as

$$
\zeta_S(\alpha,\bm x)
=
\max\!
\left\{
\kappa^{(1)}_{p,S}(\alpha,\bm x),
\bar\kappa^{(2)}_{p,S}(\alpha)
\right\},
\qquad
\bar\kappa^{(2)}_{p,S}(\alpha)=O(S^{-1/2}).
$$

With a parametric regression rate on the same scale, this yields the conventional $S^{-1/2}$ convergence rate for the resulting estimator.

## Researcher lessons

- Estimated residuals are data-dependent objects. Track the regression fit, residual construction, empirical center, and final optimizer in the randomness map.
- Keep response/residual dimension and covariate dimension distinct. The empirical Wasserstein term is governed by the response/residual geometry; the regression term is governed by the prediction method and covariate complexity.
- Decompose the radius according to the proof: regression estimation plus residual-distribution containment in the baseline route, or the theorem-specific combination used by a direct loss-level route.
- State whether the theorem is conditional on a realized covariate, pointwise for almost every covariate, or uniform over covariates.
- Radius selection by cross-validation is a separate statistical object from the radius used in a finite-sample theorem.

## Stress test

For any prediction-plus-DRO model, introduce an oracle empirical distribution built from $f^\star$ and true residuals. Bound the distance or performance gap between the estimated and oracle constructions, then separately control the oracle-to-population statistical error. Only after these two layers are composed should the robust certificate be transferred to the data-selected decision.
