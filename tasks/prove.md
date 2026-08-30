# Task: Construct or Audit a Theorem/Proof

## 1. Freeze the theorem contract

Before proving anything, rewrite the theorem into assumptions, quantified objects, conclusion, scope/dependence of constants, and whether the conclusion is deterministic, probabilistic, or asymptotic. Do not change this contract during the proof without declaring a revised theorem.

## 2. Build the dependency graph

Use `templates/theorem_proof_packet.md` and run `auditor/internal_consistency_auditor.md` for theorem-level audits. List every lemma/proposition/external theorem required, detect circular dependencies, and cross-check constraint directions, index ranges, multiplier signs, and perturbed value-function definitions.

## 3. Prove local claims at their natural level

Do not bundle delicate steps into “it follows.” Isolate existence/attainment, convexity/concavity, continuity/semicontinuity, minimax interchange, duality, measurable selection, limit interchange, concentration, and uniform convergence.

## 4. Match theorem conditions

For every external theorem, create `source condition -> current object -> verified by assumption/lemma`. If one condition is unverified, the proof is incomplete.

## 5. Edge and boundary cases

Check zero radius, zero dual multiplier, empty/interiorless feasible set, singular covariance/normalization, unbounded support, nonattained infimum, ties/nonunique optimizer, sample size below dimension, and degenerate distributions.

## 6. Counterexample search

Ask what happens if each major assumption is removed. Use `auditor/counterexample_auditor.md`. Distinguish structural assumptions from proof conveniences.

## 7. Proof style

Prefer a short roadmap, named claims/steps, explicit use of assumptions, and a clean final implication. Avoid decorative notation and unnecessary lemmas.

## 8. Auditor verdict

A proof is not accepted until the Auditor labels it PASS or PASS WITH EXPLICIT CONDITIONS. Report local typographical inconsistencies separately from substantive mathematical failures; do not silently repair them.
