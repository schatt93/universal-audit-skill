# Universal Audit, Verification & Test — Master Skill

A reusable, **artifact-agnostic audit / verification / red-team framework**, packaged as an installable Claude skill. Point it at almost any work product — code, applications, APIs, specs, architecture/design docs, data pipelines, ML/AI/LLM systems, infrastructure/IaC, financial and investment-research reports, market analyses, spreadsheets, and media/document files — and it classifies the artifact, runs only the relevant verification domains against *currently validated* industry standards, and produces a numbered, evidence-based audit record with severity-rated findings and a traceable remediation plan.

Written in the spirit of **IEEE 1028** and the auditing principles of **ISO 19011:2018**: adversarial toward the *artifact* (not the author), evidence-or-it-didn't-happen, and zero facts asserted from stale memory.

## Start here

- **[[Installation and Usage]]** — install the skill or run it as a prompt.
- **[[Methodology]]** — principles, stages, passes, and the severity model.
- **[[Module Reference]]** — the 42 domain modules and how they're selected.
- **[[Output and Schema]]** — what an audit run produces.
- **[[Maintenance and Audit Trail]]** — how the framework audits and versions itself.
- **[[Contributing]]** — issues, PRs, CI, and the update workflow.
- **[[FAQ]]** — common questions.

## At a glance

| | |
|---|---|
| **Modules** | 42 — system & quality (A–W), file/asset (X–AE), specialized professional (AF–AQ) |
| **Passes** | B1 Correctness · B2 Completeness · B3 Consistency · B4 Red-team |
| **Severity** | S1 Critical · S2 High · S3 Medium · S4 Low · S5 Info |
| **Depth** | Lightweight · Standard · **Deep** (default) |
| **Assurance** | Reasonable · Limited |
| **Outputs** | `audits/AUDIT-RUN-<NNN>-<date>.md` + append-only `audits/AUDIT-INDEX.md` |

## What makes it different

- **Dual-mode passes** — each universal check runs *constructively* ("is it right?") **and** *adversarially* ("prove it wrong"); a claim that survives a real attempt to break it is far better evidenced.
- **Runtime standards validation (Principle 1)** — editions, regulations, and defaults are treated as hypotheses and re-checked against authoritative sources, with the source + date recorded.
- **Traceability** — every finding (`Fn`) links to the fix (`Rn`) that resolves it, and back.
- **Portable** — runs on Claude, OpenAI Codex / AGENTS.md, Cursor, Gemini, and GitHub Copilot; a low-context **Lite** edition serves local / small-context models. See [[Platforms and Portability]].
- **Ground-truth reconciliation (Principle 9)** — validates the artifact's own assumptions and baseline against the actual system, catching stale plans before they regress working code.
- **Ralph loop & multi-vendor (§10)** — iterate audit→fix→re-audit to a clean, evidenced pass; drive it with sub-agents across model vendors (keys via the **api-key-manager** skill).
- **Self-auditing** — the framework is regularly run on itself; the trail is in [`audits/`](https://github.com/schatt93/universal-audit-skill/tree/main/audits).
