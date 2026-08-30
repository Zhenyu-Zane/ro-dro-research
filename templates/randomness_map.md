# Randomness Map

## Objects

| Object | Symbol | Random? | Governing law / conditioned on | Data-dependent? | Observed at decision time? |
|---|---|---:|---|---:|---:|
| Training data | $\mathcal D_S$ |  |  |  |  |
| Estimator |  |  | induced by $\mathcal D_S$ | yes | yes |
| Empirical/reference distribution | $\widehat{\mathbb P}_S$ |  | induced by $\mathcal D_S$ | yes | yes |
| Ambiguity/uncertainty set |  |  | induced by $\mathcal D_S$ | yes | yes |
| Decision | $\widehat{\bm x}_S$ |  | induced by $\mathcal D_S$ | yes | yes |
| Future outcome | $\tilde{\bm v}_{\rm new}$ |  | $\mathbb P^\star$ | no | no |

## Target event

$$
\mathcal E_S = \{\cdots\}.
$$

## Outer probability

State whether it is over training sample only, training plus future sample, conditional on context, or another process/trajectory.

## Good-event decomposition

$$
\mathcal E_S = \mathcal E_{1,S}\cap\cdots\cap\mathcal E_{K,S}.
$$

For each event state the theorem used to bound its probability.

## Multistage trigger

If there are multiple stages or full trajectories, also complete `templates/multistage_randomness_map.md`. Record whether stage-specific empirical measures are built from separate datasets or shared sample paths.
