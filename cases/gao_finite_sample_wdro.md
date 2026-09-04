# Case: Gao Finite-Sample Wasserstein DRO

**Source:** Rui Gao, *Finite-Sample Guarantees for Wasserstein Distributionally Robust Optimization: Breaking the Curse of Dimensionality*.

## Research pattern

The classical Wasserstein certificate first estimates the full data-generating distribution in Wasserstein distance. Gao instead targets the decision-relevant loss directly. For Wasserstein orders $p\in[1,2]$, the paper develops non-asymptotic uniform bounds in which an inverse-root-sample-size Wasserstein radius, up to logarithmic and complexity factors, can upper-bound true loss by Wasserstein robust loss plus a higher-order remainder.

The statistical mechanism has two layers:

1. a **variation-based concentration inequality** for a fixed loss, derived under a transportation-information inequality $T_p$ for the true distribution; and
2. a **uniformization step** over the loss class, using either covering numbers or localized Rademacher complexity indexed by loss variation.

Thus the proof target is a loss/performance event rather than the event that the entire true distribution lies in the empirical Wasserstein ball.

## Core proof architecture

For a loss $f$, define the Wasserstein regularizer

$$
R_{Q,p}(\rho;f)
:=
\sup_{P:W_p(P,Q)\le \rho}\mathbb E_P[f]
-
\mathbb E_Q[f].
$$

Under the paper's transportation-information and growth conditions, the fixed-loss concentration step controls empirical-to-population deviation through the inverse Wasserstein regularizer. The function-class step then yields a common high-probability event of the form

$$
\mathbb E_{\mathbb P^\star}[f_{\bm x}]
\le
\sup_{Q:W_p(Q,\widehat{\mathbb P}_S)\le \rho_S}
\mathbb E_Q[f_{\bm x}]
+r_S,
\qquad \forall \bm x\in\mathcal X,
$$

with $\rho_S$ having sample-size exponent $S^{-1/2}$ up to logarithmic/complexity factors and $r_S$ of higher order in the regimes established by the paper.

For $p=1$, the Wasserstein regularizer is controlled by the Lipschitz norm of the loss. For $p=2$, it is controlled to second order by an $L^2$ gradient norm when the loss has Lipschitz gradient. These variation terms are the quantities used to localize the function class.

## Researcher lessons

- Choose the statistical target before choosing the metric concentration theorem. Full-distribution Wasserstein containment and loss-level generalization are different proof routes.
- Interpret the $S^{-1/2}$ radius as a performance/generalization scaling; empirical Wasserstein convergence remains a separate distribution-estimation object.
- For uniform guarantees, record the exact complexity mechanism: finite union, covering number, or localized Rademacher complexity.
- When stating that a rate avoids the classical Wasserstein curse, report the sample-size exponent, logarithmic factors, transport/concentration constants, and loss-class complexity separately.
- Match $p=1$ arguments to Lipschitz variation and $p=2$ arguments to gradient variation and the corresponding transportation-information condition.

## Stress test

Given a proposed Wasserstein finite-sample theorem, attempt both routes separately: distribution containment and direct loss-level generalization. If the latter is used, reconstruct the fixed-loss concentration inequality, the uniformization argument, and the conversion from variation control to the robust-loss certificate for the same loss class.
