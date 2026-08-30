# RO/DRO Research Skill

A research-grade **Agent Skill** for robust optimization (RO) and distributionally robust optimization (DRO), with a veto-powered mathematical Auditor.

**Current version: V1.3.1**

The skill is designed for research tasks where a plausible-looking derivation is not enough. It can propose formulations, reformulations, theorems, statistical guarantees, algorithms, experiments, and paper positioning, but claims of exactness or theorem validity are accepted only after an independent audit.

## What it is strongest at

- exact and safe RO/DRO reformulations;
- strong-duality and minimax verification;
- finite-sample and out-of-sample guarantees;
- Wasserstein, moment, and divergence-based ambiguity sets;
- robust satisficing and data-driven uncertainty sets;
- contextual, decision-dependent, adjustable, two-stage, and multistage models;
- dependent-process/statistical-regime audits;
- algorithm/statistics guarantee composition;
- OR/MS-style theorem and paper stress testing.

## Why this repository is model-portable

The repository follows the open **Agent Skills** pattern: a self-contained folder with a `SKILL.md` file containing YAML frontmatter (`name`, `description`) plus progressively disclosed instructions, references, scripts, and examples.

- `SKILL.md` is the canonical, provider-neutral entry point.
- `agents/openai.yaml` adds optional OpenAI/Codex UI metadata without changing the skill logic.
- `AGENTS.md` helps Codex/GPT-style coding agents discover the skill when the repository itself is opened as a workspace.
- `CLAUDE.md` gives Claude Code the same repository-local discovery hint.

No provider-specific wrapper duplicates the mathematical instructions; there is one source of truth: `SKILL.md`.

## Repository map

```text
ro-dro-research/
├── SKILL.md                    # canonical skill entry point
├── CORE_PRINCIPLES.md          # non-negotiable research rules
├── AGENTS.md                   # Codex/GPT workspace discovery hint
├── CLAUDE.md                   # Claude Code workspace discovery hint
├── agents/
│   └── openai.yaml             # optional OpenAI skill metadata
├── tasks/                      # task-specific workflows
├── auditor/                    # veto-powered audit modules
├── templates/                  # proof/reformulation/statistics ledgers
├── references/                 # compact technical maps and conventions
├── cases/                      # representative frontier/stress-test cases
├── examples/                   # smoke tests and audit examples
└── scripts/                    # deterministic diagnostic utilities
```

## Installation / use

### Agent Skills-compatible products

Install or import the **whole repository folder** as one skill. Keep the relative directory structure intact. The agent should discover the metadata in `SKILL.md`, load the full file only when the description matches the task, and then open task/auditor/reference files as needed.

### Claude / Claude Code

Claude supports Agent Skills as folders containing `SKILL.md`. Import the folder/ZIP through the skill mechanism available in your Claude surface, or place the folder in the skill location used by Claude Code. If you simply clone this repository as the active project, `CLAUDE.md` tells Claude Code to route RO/DRO work through `SKILL.md`.

### OpenAI / GPT / Codex

OpenAI products that support Agent Skills can use the same `SKILL.md` package. `agents/openai.yaml` provides optional display metadata for OpenAI skill surfaces. If the repository is opened directly as a Codex workspace rather than installed as a skill, `AGENTS.md` points Codex to the canonical skill entry point.

## Example prompts that should trigger the skill

- “Derive an exact finite-dimensional reformulation of this Wasserstein DRO model and audit every duality step.”
- “Check whether this finite-sample guarantee is actually valid when the training data are serially dependent.”
- “Formulate a two-stage robust model with decision-dependent information discovery and verify nonanticipativity.”
- “Review this theorem and tell me whether the claimed OR/MS contribution survives a proof-level audit.”
- “Construct a data-driven ambiguity set, derive its guarantee, and separate oracle constants from operational tuning parameters.”

## Core operating rule

> **Novelty may be speculative; mathematical correctness may not be.**

The Researcher may propose aggressive ideas. The Auditor may return only:

- `PASS`
- `PASS WITH EXPLICIT CONDITIONS`
- `NOT ESTABLISHED`
- `FAIL`

`NOT ESTABLISHED` and `FAIL` veto publication-style claims of exactness or theorem validity.

## Notation

The binding notation convention is in `references/notation_conventions.md`. In particular, vectors/matrices use `\bm{}` notation, random vectors carry a tilde, distributions use `\mathbb{P}`, and probability-measure spaces use `\mathcal{M}(\mathcal{V})` unless an existing manuscript must preserve its own notation.

## Validation

From the repository root:

```bash
python scripts/structure_check.py .
python scripts/notation_lint.py manuscript.tex
python scripts/claim_inventory.py manuscript.tex
```

The scripts are conservative diagnostics. They do not replace theorem-level auditing.

## Sources and copyright

The skill was developed from a canonical DRO monograph/survey and representative RO/DRO research papers, then hardened through external theorem-level stress tests. The original papers and books are **not redistributed** in this repository. `references/source_hierarchy.md`, `references/source_files.md`, and `cases/` document how they inform the skill.

## Version history

See `VERSION.md` and `STRESS_TEST_REPORT.md`.
