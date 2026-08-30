# Auditor Veto Policy

The Auditor is independent of the Researcher and has final authority over mathematical claim strength.

## Verdicts

### PASS

Use only when the argument establishes the stated result under the stated assumptions.

### PASS WITH EXPLICIT CONDITIONS

Use when the result is valid after adding identifiable conditions. The final theorem must visibly include those conditions.

### NOT ESTABLISHED

Use when the proof has a real gap but no explicit contradiction has been demonstrated.

Examples:

- strong-duality condition not verified;
- fixed-decision concentration used for a data-dependent optimizer without uniformity;
- measurable-selection issue ignored;
- attainment assumed but only a supremum is established.

### FAIL

Use when a specific error or counterexample is identified.

Examples:

- inequality direction is wrong;
- minimax swap fails;
- reverse implication of “equivalence” is false;
- iid theorem applied to data known to be dependent without a valid reduction;
- claimed certificate depends on an unavailable true quantity while being advertised as computable.

## Veto effect

`NOT ESTABLISHED` and `FAIL` prohibit language such as:

- theorem proved;
- exact reformulation;
- finite-sample certificate established;
- asymptotic optimality established.

The Researcher may propose a repair, but the repaired claim must be audited anew.

## No compromise verdicts

Do not use “probably correct,” “seems valid,” or “minor gap” for a central theorem. State exactly what is established.
