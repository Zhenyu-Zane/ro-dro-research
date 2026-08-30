# Multistage Randomness and Sampling Map

## Process model

| Stage | Population object | Depends on history? | Model assumes stagewise independence? |
|---|---|---:|---:|
| $t=2$ |  |  |  |
| $\vdots$ |  |  |  |
| $t=T$ |  |  |  |

## Training-data architecture

| Stage | Training sample | Within-stage law | Shares paths/data with other stages? | Cross-stage independent? | Empirical object |
|---|---|---|---:|---:|---|
| $t=2$ |  |  |  |  |  |
| $\vdots$ |  |  |  |  |  |
| $t=T$ |  |  |  |  |  |

## Good events

$$
\mathcal E_t=\{\mathbb P_t^\star\in\widehat{\mathcal P}_{t,S_t}\},
\qquad
\mathcal E=\bigcap_{t=2}^T\mathcal E_t.
$$

For the joint probability, mark the justified route: independence/product, union bound/Bonferroni, martingale/mixing/Markov concentration, direct joint-process concentration, or other.

## Policy object

- exact optimal policy / arbitrary feasible policy / approximate policy: __________
- nonanticipativity information set: __________
- evaluation law: product marginals / true joint process / conditional kernels: __________

## Error layers

| Layer | Present? | Bound/certificate |
|---|---:|---|
| statistical |  |  |
| modeling/process mismatch |  |  |
| optimization |  |  |
| oracle |  |  |
| Monte Carlo evaluation |  |  |
