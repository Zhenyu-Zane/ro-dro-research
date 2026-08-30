# AGENTS.md

This repository is an Agent Skill, not an ordinary software project.

For any task involving robust optimization (RO), distributionally robust optimization (DRO), robust satisficing, ambiguity/uncertainty sets, exact reformulations, duality/minimax, statistical guarantees, multistage uncertainty, or OR/MS-style theory review:

1. Read `SKILL.md` first.
2. Follow its progressive-disclosure rule; do not load every file by default.
3. Treat `CORE_PRINCIPLES.md` and `auditor/VETO_POLICY.md` as non-negotiable.
4. Use the task workflow and auditor modules named by `SKILL.md`.
5. Never silently repair an invalid theorem or upgrade an approximation into an exact reformulation.

When editing the skill itself, keep `SKILL.md` provider-neutral and preserve relative paths. OpenAI-specific UI metadata belongs in `agents/openai.yaml` only.
