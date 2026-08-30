# Auditor: Multistage Statistical Guarantees

Use this module whenever a finite-sample or statistical claim concerns a two-stage or multistage model, a dynamic policy, stagewise ambiguity sets, or trajectory data.

The central rule is:

> **Stagewise model independence, within-stage iid sampling, cross-stage independence of training sets, and iid sample paths are different assumptions. Never treat them as interchangeable.**

## 1. Identify the stochastic object being certified

Write explicitly whether the theorem concerns:

- a product distribution of stagewise marginals;
- a joint path distribution;
- conditional transition kernels;
- a Markov process;
- a mixing/trajectory process;
- independently sampled stage-specific datasets.

A guarantee for the product law $\mathbb P_2^\star\otimes\cdots\otimes\mathbb P_T^\star$ is not automatically a guarantee for a dependent joint law on full trajectories.

## 2. Build a sampling-architecture table

For each stage $t$, record:

| Item | Required description |
|---|---|
| Population object | marginal $\mathbb P_t^\star$, conditional kernel, or joint process |
| Training observations | $\{\tilde{\bm v}_{t,s}\}_{s\in[S_t]}$ or path coordinates |
| Within-stage dependence | iid / mixing / Markov / other |
| Cross-stage dependence | independent datasets / shared sample paths / other |
| Across-path dependence | iid paths / dependent trajectories |
| Empirical object | $\widehat{\mathbb P}_{t,S_t}$ or joint empirical law |

Do not proceed until this table is coherent with the model's information structure.

## 3. Audit joint good-event probabilities

Suppose the proof defines stagewise events $\mathcal E_t$ and needs

$$
\mathbb P\left[\bigcap_{t=2}^T \mathcal E_t\right].
$$

A product identity

$$
\mathbb P\left[\bigcap_{t=2}^T \mathcal E_t\right]
=\prod_{t=2}^T\mathbb P[\mathcal E_t]
$$

is valid only when the events are independent under the training-data law. Within-stage iid sampling alone does not imply this.

If cross-stage independence is unavailable, use a valid dependence-aware argument. A default safe option is Bonferroni/union bound:

$$
\mathbb P\left[\bigcap_{t=2}^T\mathcal E_t\right]
\ge 1-\sum_{t=2}^T\mathbb P[\mathcal E_t^c].
$$

Do not silently replace an unjustified product by a product-style confidence allocation.

## 4. Distinguish model independence from data independence

A dynamic programming recursion may assume stagewise-independent future uncertainty. That assumption concerns the **decision model**.

The statistical proof additionally needs a law for the **training data**. Examples:

- If complete sample paths are iid from a product law, cross-stage coordinate datasets are mutually independent.
- If complete sample paths are iid from a dependent joint law, each stage's marginal observations may be iid across paths, but the stage-specific empirical measures are generally dependent across stages.
- If each stage is sampled from a separate experiment, cross-stage independence may hold even without a trajectory interpretation.

The Auditor must state which case applies.

## 5. Check policy-level scope

Identify whether the result is for:

- the exact optimal policy;
- every feasible policy;
- an $\varepsilon$-optimal robust policy;
- a policy returned by a finite-iteration algorithm;
- a policy evaluated under the true joint process.

A theorem for the exact optimizer of the stagewise-independent robust model does not automatically certify an approximate policy or a policy evaluated under a dependent process.

## 6. Check dynamic measurability and nonanticipativity

For recursive expected-cost guarantees, verify:

- measurable policy selections exist where required;
- the policy depends only on information available at that stage;
- the evaluation law matches the conditioning structure used in the policy;
- all expectations are well defined.

## 7. Theorem-versus-experiment scope

Experiments may deliberately evaluate a stagewise-independent model on dependent trajectories. This can be a legitimate robustness experiment, but the theoretical guarantee does not transfer unless separately proved.

Label clearly:

- **theorem regime**;
- **model-misspecification experiment**;
- **empirical observation only**.

## 8. Verdict rules

- **PASS** — stochastic process, sampling architecture, joint event calculation, and policy object all match.
- **PASS WITH EXPLICIT CONDITIONS** — proof is valid once a missing but natural cross-stage or path-sampling condition is stated.
- **NOT ESTABLISHED** — stagewise concentration is valid but the joint-event or policy-level step is unsupported.
- **FAIL** — an explicit dependence structure contradicts a product/independence step or the claimed guarantee is for a different process than the one analyzed.
