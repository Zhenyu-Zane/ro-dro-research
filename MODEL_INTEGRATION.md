# Model Integration Notes

## Canonical entry point

All models should treat `SKILL.md` as the canonical instruction file. Do not maintain separate Claude/GPT copies of the mathematical instructions because they will drift.

## Progressive disclosure

The intended loading sequence is:

1. frontmatter `name` + `description` for trigger selection;
2. `SKILL.md` after trigger;
3. `CORE_PRINCIPLES.md` + the relevant `tasks/*.md` file;
4. only the `auditor/*.md`, `templates/*.md`, `references/*.md`, and `cases/*.md` files needed for the current claim.

This mirrors the Agent Skills design principle: metadata is cheap and always discoverable; detailed domain context is loaded only when needed.

## Claude-family agents

The skill uses the standard `SKILL.md` package shape used by Claude Agent Skills. `CLAUDE.md` exists only as a project-local pointer for Claude Code when this Git repository is opened directly rather than installed through a skills mechanism.

## OpenAI-family agents

The same provider-neutral `SKILL.md` is the substantive skill. `agents/openai.yaml` provides optional UI metadata for OpenAI/Codex skill surfaces. `AGENTS.md` is a project-local pointer for Codex-style repository agents.

## Other agents

Any agent that can read Markdown can invoke the skill manually by reading `SKILL.md` first and resolving its relative file references. The mathematical workflow does not depend on a vendor-specific API or tool.
