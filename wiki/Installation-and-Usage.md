# Installation and Usage

## Option A — install for your agentic platform

| Platform | Entry point |
|---|---|
| **Claude / Claude Code** | `universal-audit-skill.skill` (install as a skill) |
| **OpenAI Codex** + any AGENTS.md tool | `AGENTS.md` at the project root |
| **Cursor** | `adapters/cursor/universal-audit.mdc` → `.cursor/rules/` |
| **Gemini CLI** | `adapters/gemini/` (`GEMINI.md` + a `/audit` command) |
| **GitHub Copilot** | `adapters/github-copilot/copilot-instructions.md` → `.github/` |
| **Local / small-context models** | `universal-audit-skill-lite.md` (Lightweight depth, chunked) |

See [[Platforms and Portability]] and `adapters/README.md`. For **Claude** specifically:

1. Download `universal-audit-skill.skill` from the repository.
2. Install it: in **Cowork**, use the *Save skill* button when the file is presented; in **Claude Code**, use your skill-install flow.
3. It then triggers automatically when you ask to **audit, verify, review, QA, fact-check, stress-test, red-team**, or **find defects / gaps / inconsistencies** in something — even if you never say the word "audit."

Audit outputs are written to a dedicated **`./audits/`** directory (created if absent).

## Option B — run as a prompt

Paste `universal-audit-skill-v10.1.md` (or `universal-audit-skill-lite.md` on small-context / local models) into a fresh agent session that has:

1. **file read/write**, and
2. **web search + page fetch** (needed for Principle 1 runtime validation).

If either capability is missing, the skill stops and says so rather than guessing.

## Inputs you fill (the `<<…>>` placeholders, §2)

| Input | Meaning |
|---|---|
| In scope / Out of scope | Paths, repos, files to audit (or exclude) |
| Artifact type(s) | e.g. "web app + API + specs", or "infer and confirm" |
| Domain / regulatory context | e.g. fintech (SEBI/DPDP), healthcare (HIPAA), EU (GDPR/AI Act) |
| Policies / standards to enforce | Internal style guide, target compliance regime |
| **Audit output location** | Folder for the record + index; default `./audits/` |
| Audit objectives | What the audit must achieve (distinct from scope) |
| Materiality threshold | What magnitude of issue counts as a finding |
| Sampling approach | What was fully examined vs. sampled |
| **Depth** | `Lightweight \| Standard \| Deep` — default **Deep** |
| **Assurance** | `Reasonable \| Limited` |

## Depth tiers

- **Lightweight** — universal passes + selected modules at checklist depth; adversarial techniques named/recommended; validate only safety-critical facts. For small/low-risk work.
- **Standard** — passes in both modes at full depth; modules fully checked; cheap adversarial tests executed; validate all time-sensitive facts.
- **Deep (default)** — everything in Standard *plus* active execution of adversarial tests (fuzzing, property-based, fault injection), exhaustive method coverage, and validation of **every** checkable fact. For production / regulated systems.

> If a run would exceed ~30 external lookups or the artifact is very large, the skill **chunks** the work (auditing in sections, each with its own coverage proof) rather than silently truncating.

See **[[Output and Schema]]** for what a run produces, and **[[Methodology]]** for how it runs.
