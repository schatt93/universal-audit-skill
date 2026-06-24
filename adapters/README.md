# Adapters — deploy the auditor on any agentic platform

The audit methodology lives in **one** place: [`../universal-audit-skill-v9.0.md`](../universal-audit-skill-v9.0.md) (full) and [`../universal-audit-skill-lite.md`](../universal-audit-skill-lite.md) (low-context). These adapters are thin entry points that point your agent at it — copy the one(s) for your platform into your target project.

| Platform | Use this | Place it at | Notes |
|---|---|---|---|
| **OpenAI Codex** + any AGENTS.md tool | [`../AGENTS.md`](../AGENTS.md) | project root | Open standard — also read by Cursor, Gemini CLI, Copilot, Windsurf |
| **Claude / Claude Code** | `../universal-audit-skill.skill` (or its `SKILL.md`) | install as a skill | Triggers on audit / verify / review intents |
| **Cursor** | [`cursor/universal-audit.mdc`](cursor/universal-audit.mdc) | `.cursor/rules/` | `.mdc` with frontmatter; ask the agent to audit to invoke |
| **Gemini CLI** | [`gemini/GEMINI.md`](gemini/GEMINI.md) + [`gemini/commands/audit.toml`](gemini/commands/audit.toml) | project root + `.gemini/commands/` | adds an `/audit` slash command |
| **GitHub Copilot** | [`github-copilot/copilot-instructions.md`](github-copilot/copilot-instructions.md) | `.github/` | repo-wide instructions (VS Code, Visual Studio, JetBrains) |

Every adapter references the master file as the single source of truth, so there is exactly **one** methodology to maintain.

## Local / small-context models
Point the adapter at [`../universal-audit-skill-lite.md`](../universal-audit-skill-lite.md) instead of the full file, run at **Lightweight** depth, and audit **one module / section at a time**, persisting the findings ledger to `audits/` between chunks so context can be released. See the master's *"Low-context & local models"* note.

*Adapter formats validated 2026-06-24 against each platform's current documentation.*
**Currency (Stage R).** Before judging, run the deep-research loop — decompose the audit's knowledge needs, web-search and *verify* the current standards / advisories / CVEs / best practices, and cite them in a Research Brief; never judge a fast-moving artifact from memory. Engine: `research/research-workflow.md` + `research/web-researcher.md`.
