# Example Audit Skeleton

## Claim

A data-driven Wasserstein DRO solution $\widehat{\bm x}_S$ satisfies a high-probability out-of-sample bound.

## Researcher route

1. Build $\widehat{\mathbb P}_S$.
2. Choose a Wasserstein ball $\widehat{\mathcal P}_S$.
3. Show $\mathbb P^\star\in\widehat{\mathcal P}_S$ with high probability.
4. On that event,
   $$
   \mathbb E_{\mathbb P^\star}[\ell(\widehat{\bm x}_S,\tilde{\bm v})]
   \le
   \sup_{\mathbb P\in\widehat{\mathcal P}_S}
   \mathbb E_{\mathbb P}[\ell(\widehat{\bm x}_S,\tilde{\bm v})].
   $$

## Auditor checks

- Is the concentration theorem valid for the sample law?
- Is the loss integrable over every distribution in the ball?
- Is the radius stated in the same Wasserstein convention as the theorem?
- Are all constants known?
- Does the containment event protect every decision, including the data-dependent optimizer? If yes, no separate uniform-over-$x$ concentration is needed for this deterministic implication.

## Verdict language

Only after those checks: PASS / PASS WITH CONDITIONS / NOT ESTABLISHED / FAIL.
