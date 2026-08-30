# Binding Notation Conventions

Use these conventions by default in every new RO/DRO derivation and manuscript section.

We denote by $[S]=\{1,2,\ldots,S\}$ the set of positive indices up to~$S$. We use boldface glyphs, such as $\bm{x}\in\mathbb{R}^D$ and $\bm{A}\in\mathbb{R}^{M\times N}$ to denote vectors (column, by default) and matrices, and we denote by $x_i$ the $i$-th element of vector~$\bm{x}$ and by ${a}_{ij}$ the $(i,j)$-th entry of matrix~$\bm{A}$. Special vectors and matrix of the appropriate dimension include $\bm{0}$, $\bm{e}$, $\bm{e}_i$, and $\bm{I}$, which correspond to (respectively) the vector of all zeros, the vector of all ones, the $i$-th standard basis, and the identity matrix.

We use $\tilde{\bm{v}} \sim \mathbb{P} \in \mathcal{M}(\mathcal{V})$ to denote an $N$-dimensional random variable~$\tilde{\bm{v}}$ governed by a probability distribution~$\mathbb{P}$, where $\mathcal{M}(\mathcal{V})$ represents the set of all probability distributions in a set $\mathcal{V} \subseteq \mathbb{R}^N$. The term $\mathbb{P}[\tilde{\bm{v}}\in\mathcal{V}]$ represents the probability of~$\tilde{\bm{v}}$ lying in the set~$\mathcal{V}$ evaluated on the probability distribution~$\mathbb{P}$. We use $\mathbb{E}_{\mathbb{P}}[\cdot]$ to signify the expectation with respect to $\mathbb{P}$.

## Derived conventions

Use the following derived conventions unless an existing manuscript requires otherwise.

- True but unknown distribution: $\mathbb{P}^\star$.
- Empirical distribution from $S$ observations: $\widehat{\mathbb{P}}_S$.
- Generic ambiguity set: $\mathcal{P}$; data-dependent ambiguity set: $\widehat{\mathcal{P}}_S$.
- Generic uncertainty set: $\mathcal{U}$ or a context-specific calligraphic set.
- Decision set: $\mathcal{X}$.
- Support of an uncertain/random vector: use a distinct calligraphic set such as $\mathcal{V}$, $\mathcal{Z}$, or $\Xi$; do not reuse the ambiguity-set symbol.
- Realization of $\tilde{\bm v}$: $\bm v$; sample $s$: $\widehat{\bm v}_s$ when it is an observed historical realization.
- Estimated deterministic parameter: hat, e.g. $\widehat{\bm\theta}$.
- True deterministic parameter: star, e.g. $\bm\theta^\star$.
- Stage index: normally $t$; sample index: normally $s$; component index: normally $i,j$.

## DRO baseline form

A standard minimization-form DRO model should normally read

$$
\inf_{\bm{x}\in\mathcal X}\;\sup_{\mathbb P\in\widehat{\mathcal P}_S}
\mathbb E_{\mathbb P}[\ell(\bm{x},\tilde{\bm v})].
$$

For reward maximization, use the corresponding max–inf form and keep the sign convention consistent throughout the paper.

## Prohibited drift

Unless the user explicitly requests it, do not switch equivalent objects among

- `\mathbf{x}`, `\boldsymbol{x}`, and `\bm{x}`;
- $P_0(\mathcal V)$, $\mathcal P(\mathcal V)$, and $\mathcal M(\mathcal V)$ for the space of probability laws;
- $\mathcal P$ as both a probability-measure space and an ambiguity set;
- tilde and non-tilde notation for the same random object.

## Auditor notation check

Before finalizing a theorem or proof, verify:

1. every bold symbol has a consistent dimension/type;
2. deterministic and random quantities are visually distinct;
3. empirical, estimated, and true quantities are distinguishable;
4. sample/stage/component indices do not collide;
5. probability and expectation subscripts identify the intended distribution;
6. all sets have one semantic role each.
