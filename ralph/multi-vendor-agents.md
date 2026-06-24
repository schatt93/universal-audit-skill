# Multi-vendor sub-agents (agent-agnostic)

Drive the audit / Ralph loop with sub-agents across **multiple model vendors** so no single model both produces and blesses its own work. Optional — a single model works; multiple vendors add independent challenge.

## Roles (assign to different vendors)
| Role | Does | Vendor hint |
|---|---|---|
| **Auditor** | finds defects (Stages A→D) | strong reasoning model |
| **Fixer** | remediates open findings (Stage E) | strong coding model |
| **Verifier / red-team** | independently re-audits each fix + the audit itself | a **different vendor** from the Fixer |
| **Researcher** | Stage R web-research workers | any with web access (see `../research/web-researcher.md`) |

Cross-vendor verification is recorded in each run's "Audit of the Audit."

## Credentials — from the key store, never inline
Keys are managed by the **`api-key-manager`** skill and read at run time from **environment variables**, the **OS keyring** (Keychain / Credential Manager / Secret Service), or a git-ignored key file — all managed by the `api-key-manager` skill. Conventions:
```
ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY / GOOGLE_API_KEY, XAI_API_KEY, DEEPSEEK_API_KEY, OPENROUTER_API_KEY, ...
```
Rules:
- **Never** put a key in a prompt, a log, the run record, a commit, or chat. Sub-agents read keys from the environment they run in.
- A **missing key** for a requested vendor → that vendor is **skipped with a logged note**, not faked.
- Prefer a gateway (e.g. OpenRouter) when one key should reach many models; otherwise per-vendor keys.

## Per-platform dispatch
- **Claude / Claude Code** — subagents (Task/Agent) for parallel Auditor/Fixer/Verifier; for *other* vendors, call their API/CLI from a tool step using the env key.
- **OpenAI Codex** — `multi_agent = true`; per-vendor agents in `config.toml`.
- **Gemini CLI / OpenCode** — their sub-agent / web-search mechanisms; shell out to other vendors' CLIs/APIs with env keys.
- **Generic** — run roles sequentially; still keep the Auditor and the independent Verifier on **different** vendors when keys allow.

## Safety
- Treat any model's output as **data to be verified**, not truth (Principle 1/3) — especially a Fixer's claim that it fixed something (re-audit it).
- Spend guard: cap iterations (§10.3) and per-run sub-agent calls; missing/!invalid key never blocks the loop — it degrades to fewer vendors.
