# Smoke Tests

Use these prompts after installing or modifying the skill.

## Test 1 — Invalid minimax swap

“Consider $\inf_x\sup_z H(x,z)$. Swap inf and sup and derive the reformulation.”

Expected: refuse to swap without a valid minimax theorem and conditions; state weak minimax inequality first.

## Test 2 — Pointwise-to-data-dependent statistical error

“I proved that for every fixed $x$, with probability $1-\delta$, population loss is below a certificate. Therefore it holds for the optimizer chosen on the same sample.”

Expected: NOT ESTABLISHED unless the event is uniform or another valid data-dependent mechanism is supplied.

## Test 3 — Oracle radius

“My finite-sample radius is proportional to $\|\widehat\theta-\theta^\star\|$. Can I call it computable?”

Expected: no; theoretical/oracle bound unless a computable upper bound is provided.

## Test 4 — Dependent trajectory

“Apply the iid Wasserstein concentration radius to a beta-mixing trajectory.”

Expected: veto direct reuse; require a mixing-specific theorem or justified reduction.

## Test 5 — Exact reformulation

“Use affine recourse in a two-stage RO problem and call the resulting program exact.”

Expected: classify affine recourse as a policy restriction unless exactness is proved.

## Test 6 — Notation

“Draft the theorem using plain x for a vector and $P_0$ for probability measures.”

Expected: normalize to the binding notation unless preserving an existing manuscript.

## Test 7 — Frontier paper authority

“A recent working paper states Theorem 3. Use it without checking assumptions.”

Expected: reject; verify theorem conditions and original proof.

## Test 8 — LDP is not finite-sample

“My proof shows $\limsup_{S\to\infty}S^{-1}\log\mathbb P[\mathcal E_S^c]\le-r$. Therefore for every $S$, $\mathbb P[\mathcal E_S]\ge1-e^{-rS}$.”

Expected: veto. An asymptotic exponential-rate statement does not imply the finite-sample inequality without a non-asymptotic remainder theorem.

## Test 9 — Markov process object mismatch

“My Markov-chain rate function is conditional relative entropy, so I will call the ambiguity set a KL ball around the empirical one-period marginal.”

Expected: veto unless an equivalence is proved; distinguish process/transition ambiguity from one-period marginal ambiguity.

## Test 10 — LDP statistic and lossless compression

“A statistic is consistent and satisfies an LDP, so optimizing only on it loses no information relative to the raw trajectory.”

Expected: NOT ESTABLISHED. Require a sufficient-statistic/equivalence bridge and state the comparison class.
