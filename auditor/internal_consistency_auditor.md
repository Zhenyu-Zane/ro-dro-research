# Auditor: Internal Theorem/Definition Consistency

Use this module in theorem-level paper audits and whenever a proof relies on a chain of numbered definitions, assumptions, lemmas, propositions, or equations.

## 1. Cross-check local contracts

For every central result, compare:

- constraint directions and index ranges in the primal model;
- the corresponding perturbation/value-function definition;
- multiplier sign restrictions;
- theorem statement;
- proof substitutions;
- later corollaries that specialize the result.

A mismatch such as reversing equality and inequality index sets can invalidate a literal displayed definition even if the intended argument is recoverable.

## 2. Distinguish typo from substantive failure

Classify an inconsistency as:

- **typographical/local** — the intended statement is uniquely recoverable from surrounding definitions and the proof consistently uses the corrected version;
- **repairable technical** — a missing/reversed condition requires a nontrivial amendment but does not change the central theorem;
- **substantive** — alternative interpretations lead to different feasible sets, dual variables, probability events, or conclusions.

Do not inflate an obvious typo into a fatal theorem failure. Conversely, do not silently repair a displayed statement without reporting the repair.

## 3. Check index and object reuse

Audit:

- $t$ versus $s$ stage/sample indices;
- vector dimension versus sample size;
- equality versus inequality multiplier signs;
- empirical versus population distributions;
- original versus projected ambiguity sets;
- exact versus approximate policy objects.

## 4. Output

Report:

1. exact location/object of inconsistency;
2. why it conflicts with another statement;
3. most plausible intended correction;
4. whether any downstream theorem actually relies on the erroneous literal version;
5. severity: `local typo / moderate / major / fatal`.
