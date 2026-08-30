# Source Hierarchy and Evidence Policy

## Tier 0 — Mathematical primitives

Examples: convex analysis, measure theory, probability, optimal transport, concentration inequalities, minimax theorems, stochastic-process results.

Use the original theorem source when a proof depends critically on its hypotheses. A secondary survey may guide navigation but should not be the sole authority for a delicate qualification condition.

## Tier 1 — Canonical DRO backbone

The primary conceptual backbone is Daniel Kuhn, Soroosh Shafiee, and Wolfram Wiesemann, *Distributionally Robust Optimization* (2024, arXiv:2411.02549).

Its architecture organizes ambiguity sets, topology/attainment, duality, finite convex reformulations, regularization, numerical methods, and statistical guarantees. See `dro_canonical_map.md`.

## Tier 2 — Established seminal RO/DRO literature

Examples include classical robust optimization, moment DRO, distributionally robust convex optimization, Wasserstein DRO, and related statistical foundations.

When invoking a named reformulation or guarantee, verify the actual statement and conditions of the relevant paper/book.

## Tier 3 — Recent peer-reviewed research projects

Representative cases include robust satisficing, prediction-plus-robustification, and decision-dependent information discovery.

Use them to learn research design, modeling innovations, theorem architecture, and computational validation. Do not treat their theorem statements as primitive axioms.

## Tier 4 — Frontier working papers

Representative cases include data-driven uncertainty-set geometry, knowledge-guided Wasserstein DRO, contextual robust optimization, and streamlined robustness.

These are useful for identifying current directions but can contain errors or assumptions unsuitable for a new problem. Re-prove or re-check every critical step.

## Evidence labels in research output

When relevant, label support as:

- **Established theorem** — directly supported by a verified theorem under matched assumptions.
- **Derived here** — proved in the current work.
- **Research conjecture** — plausible but not established.
- **Empirical observation** — supported by experiments/data only.
- **Working-paper precedent** — appears in a frontier source but is not being treated as foundational authority.

## Novelty searches

Novelty is time-sensitive. When web/literature search is available, perform a fresh search before stating that no prior work exists. Search by mathematical primitive, not only by application keywords.
