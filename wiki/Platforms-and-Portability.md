# Platforms and Portability

The audit methodology is platform-neutral and lives in one source of truth — **`universal-audit-skill-v8.0.md`** (full) and **`universal-audit-skill-lite.md`** (low-context). Thin **adapters** point each platform's native mechanism at it, so there is exactly one methodology to maintain.

## Deployment matrix

| Platform | Use this | Place it at | Notes |
|---|---|---|---|
| **OpenAI Codex** + any AGENTS.md tool | `AGENTS.md` | project root | Open standard; also Cursor, Gemini CLI, Copilot, Windsurf |
| **Claude / Claude Code** | `universal-audit-skill.skill` (or its `SKILL.md`) | install as a skill | triggers on audit / verify / review intents |
| **Cursor** | `adapters/cursor/universal-audit.mdc` | `.cursor/rules/` | `.mdc` with frontmatter (`description`, `alwaysApply`) |
| **Gemini CLI** | `adapters/gemini/GEMINI.md` + `commands/audit.toml` | project root + `.gemini/commands/` | adds an `/audit` slash command |
| **GitHub Copilot** | `adapters/github-copilot/copilot-instructions.md` | `.github/` | VS Code / Visual Studio / JetBrains |

## AGENTS.md — the open standard

`AGENTS.md` is a simple, open format for guiding coding agents — adopted as an open standard (a Linux Foundation directed fund) and read by OpenAI Codex, Cursor, Gemini CLI, GitHub Copilot, Windsurf, and dozens of other tools. The repo ships one at its root; copy it into your target project. Keep it operational and under ~32 KiB (Codex's default `project_doc_max_bytes`).

## Local & low-context models

Use [`universal-audit-skill-lite.md`](https://github.com/schatt93/universal-audit-skill/blob/main/universal-audit-skill-lite.md) — an index + minimal operating core that **defers to the full spec for detail**. Run at **Lightweight** depth, audit **one module / section at a time**, and persist the findings ledger to `audits/` between chunks so context can be released. The Lite edition maps each task to the exact master section (§1 principles, §3 stage/pass, Stage C module, §4–§5 schema, Appendix standards) to pull on demand — so small models don't miss key instructions by relying on the summary alone.

*Adapter formats validated 2026-06-23 against each platform's current documentation.*
