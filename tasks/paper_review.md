# Task: Reviewer-Style Full Paper Audit

## Pass 1 — Model semantics

Check whether the model matches the operational process and information timing.

## Pass 2 — Assumption ledger

Extract every assumption and mark explicit/implicit, where used, plausibility, removability, and whether it is stronger than needed.

## Pass 3 — Theorem graph

Create a dependency graph and verify no circular reasoning.

## Pass 4 — Reformulations

Run `tasks/reformulate.md` on every major exactness claim.

## Pass 5 — Statistical results

Run `tasks/finite_sample.md` and/or `tasks/asymptotics.md` on every guarantee. For multistage results, map within-stage sampling, cross-stage dependence, full-path dependence, and evaluation law.

## Pass 6 — Algorithms

Check whether algorithms solve the exact model, approximation, or relaxation and verify bound directions. If a theorem concerns the exact optimizer, check finite-iteration inheritance with `auditor/statistical_computational_composition_auditor.md`.

## Pass 7 — Experiments

Check whether experiments test the mechanism and use nearest conceptual baselines. Compare theorem DGP/process assumptions with training/evaluation processes.

## Pass 8 — Novelty

Run `tasks/novelty.md` with a current literature search when available.

## Severity labels

- **Fatal** — invalidates a main theorem/model/conclusion.
- **Major** — central claim not established or missing necessary experiment.
- **Moderate** — repairable technical gap materially changing exposition/assumptions.
- **Minor** — non-substantive clarity or notation issue.

Run `auditor/internal_consistency_auditor.md` on central definitions/theorems. Do not inflate a uniquely recoverable typo into a theorem failure, but do not silently repair it.

## Statistical-regime and process-scope check

For non-iid/time-series/trajectory theorems, identify the path law and exact regime. Flag overstatement if LDP/MDP/CLT is described as finite-sample confidence. For statistical-optimality claims based on a summary statistic, state whether comparison is over all raw-data procedures or only statistic-based ones and verify any sufficiency bridge.
