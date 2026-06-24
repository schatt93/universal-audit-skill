# Universal Audit, Verification & Test — Master Skill

A reusable, **artifact-agnostic audit / verification / red-team framework** that runs on **any agentic coding platform** — Claude, OpenAI Codex, Cursor, Gemini, GitHub Copilot, and any [AGENTS.md](https://agents.md)-aware tool — with a low-context **Lite** edition for local / small-context models. Point it at almost any work product — source code, applications, APIs, specs, architecture/design docs, data pipelines, ML/AI/LLM systems, infrastructure/IaC, financial and investment-research reports, market analyses, spreadsheets, and media/document files — and it classifies the artifact, runs only the relevant verification domains against *currently validated* industry standards, and produces a numbered, evidence-based audit record with severity-rated findings and a traceable remediation plan.

Written in the spirit of **IEEE 1028** and **ISO 19011:2018**: adversarial toward the *artifact* (not the author), evidence-or-it-didn't-happen, and zero facts asserted from stale memory — and it validates not only external facts but the artifact's own **stated assumptions against ground truth** (Principle 9).

---

## What it is

- **42 domain modules** across three groups: system & quality (`A`–`W`), file-format & asset (`X`–`AE`), and specialized professional domains (`AF`–`AQ`, including Financial/SOX, Medical-Device, Smart-Contract, Model-Risk, and Investment-Research & Market-Analysis).
- **Dual-mode universal passes** — every check runs in a *constructive* ("is it right?") and an *adversarial* ("prove it wrong") mode (Pass B1–B3), plus a cross-cutting red-team pass (B4).
- **9 operating principles** — including runtime validation of *external* facts (P1) and of the artifact's own preconditions / baseline against the *actual system* (**P9 — ground-truth reconciliation**, so stale plans and invalid assumptions are caught before they regress working code).
- **Severity taxonomy** S1–S5 with orthogonal `Status` and `Tags`, and full **finding ↔ fix traceability**.
- **Portable** — native adapters for Claude, OpenAI Codex / AGENTS.md, Cursor, Gemini, and GitHub Copilot; one methodology, one source of truth.
- **Deep-research currency engine (Stage R)** — before judging, it autonomously decomposes its knowledge needs, runs iterative web searches, verifies sources, and synthesizes a cited **Research Brief**, so it audits against *current* standards and advisories, not memory.
- **Ralph loop & multi-vendor (§10)** — optionally iterate audit→fix→re-audit to a clean, *evidenced* pass, with sub-agents across model vendors (Auditor / Fixer / independent cross-vendor Verifier) whose keys are managed by the **`api-key-manager`** skill.
- **Self-auditing** — the framework is regularly run on itself; the trail lives in [`audits/`](audits/).

## Platforms

| Platform | Entry point | Notes |
|---|---|---|
| **Claude / Claude Code** | [`universal-audit-skill.skill`](universal-audit-skill.skill) (install as a skill) | triggers on audit / verify / review intents |
| **OpenAI Codex** + any AGENTS.md tool | [`AGENTS.md`](AGENTS.md) | open standard — also Cursor, Gemini CLI, Copilot, Windsurf |
| **Cursor** | [`adapters/cursor/universal-audit.mdc`](adapters/cursor/universal-audit.mdc) → `.cursor/rules/` | `.mdc` rule |
| **Gemini CLI** | [`adapters/gemini/`](adapters/gemini/) — `GEMINI.md` + `/audit` command | TOML slash command |
| **GitHub Copilot** | [`adapters/github-copilot/copilot-instructions.md`](adapters/github-copilot/copilot-instructions.md) → `.github/` | VS Code / Visual Studio / JetBrains |
| **Local / small-context models** | [`universal-audit-skill-lite.md`](universal-audit-skill-lite.md) | index that defers to the full spec; Lightweight depth, chunked |

See [`adapters/README.md`](adapters/README.md) for the deployment matrix.

## Repository layout

```
universal-audit-skill-v10.1.md   # the skill source — full methodology (single source of truth)
universal-audit-skill-lite.md   # condensed core for local / small-context models (defers to the full file)
universal-audit-skill.skill     # installable Claude package (SKILL.md + eval set)
AGENTS.md                       # universal adapter (open standard: Codex, Cursor, Gemini, Copilot, Windsurf, ...)
adapters/                       # native entry points per platform (Cursor .mdc, Gemini, Copilot, Codex)
research/                       # deep-research currency engine (Stage R) + web-research sub-agent
ralph/                          # Ralph loop (iterate to a clean pass) + multi-vendor sub-agent specs
skills/api-key-manager/         # secure CRUD for multi-vendor API keys (OS keyring or git-ignored store)
audits/                         # audit outputs: AUDIT-INDEX.md + AUDIT-RUN-* records
skill-dev/                      # build & triggering artifacts (eval set, trigger tests, unpacked pkg)
wiki/                           # documentation (source for the GitHub Wiki)
```

## How to use

**Install / deploy for your platform** from the table above (or [`adapters/README.md`](adapters/README.md)). It then triggers when you ask to audit, verify, review, QA, fact-check, stress-test, red-team, or find defects / gaps / inconsistencies in something — even if you never say the word "audit." Audit outputs are written to `./audits/`.

**Run as a prompt** (any agent). Paste `universal-audit-skill-v10.1.md` — or `universal-audit-skill-lite.md` on small-context / local models — into a session with (1) file read/write and (2) web search + page fetch. Fill the `<<...>>` placeholders (scope, artifact type(s), domain/regulatory context, audit depth, **audit output location**, objectives, materiality, assurance level) and run top-to-bottom. The agent selects which modules apply — it does not run all of them blindly.

**Pick a depth.** `Lightweight | Standard | Deep` (default **Deep**); assurance is `Reasonable | Limited`.

**Outputs.** Each run writes `audits/AUDIT-RUN-<NNN>-<YYYY-MM-DD>.md` (header, manifest, findings, consolidation, *audit of the audit*, remediation plan, open questions, verification ledger) and appends one row to `audits/AUDIT-INDEX.md`. The audit directory is created if absent and is configurable in section 2.

## Multi-vendor keys (optional — for the Ralph loop, §10)

To drive the loop with sub-agents across model vendors, store each vendor's API key with the **`api-key-manager`** skill — in the **OS keyring** (preferred) or a git-ignored `600` file, never the repo, prompts, logs, or chat:

```bash
pip install keyring   # OS keyring backend: macOS Keychain / Windows Credential Manager / Linux Secret Service

KM=skills/api-key-manager/scripts/keyman.py
python $KM add OPENAI_API_KEY            # hidden prompt (or: --from-env VAR); also ANTHROPIC_API_KEY, GEMINI_API_KEY, ...
python $KM list                          # names + masked values
python $KM backend                       # show the active store (keyring | file)
eval "$(python $KM export-env)"          # load keys into this shell for the sub-agents (no values printed)
```

A missing key just skips that vendor. See [`skills/api-key-manager/SKILL.md`](skills/api-key-manager/SKILL.md).

## How it is maintained

The skill is maintained **by auditing itself** — the discipline it preaches, it practices.

- **Self-audit trail.** Every substantive change is driven by a recorded run in [`audits/`](audits/): e.g. `AUDIT-RUN-006` (internal consistency), `AUDIT-RUN-007` (financial-category coverage gap -> new Module AQ), `AUDIT-RUN-008` (knowledge/instruction correctness + standards staleness), `AUDIT-RUN-009` (multi-platform + low-context + Principle 9), `AUDIT-RUN-010` (fresh full self-audit), and `AUDIT-RUN-011`–`013` (deep-research engine → Ralph loop + multi-vendor → OS-keyring key store). Findings carry IDs (`Fn`), fixes carry IDs (`Rn`), and `AUDIT-INDEX.md` is an append-only log of every run.
- **Runtime standards validation (Principle 1).** Named standards and editions are re-validated against authoritative sources and corrected when stale.
- **Ground-truth reconciliation (Principle 9).** The skill verifies an artifact's stated preconditions and baseline against the *actual* system — added from live-test feedback where a stale plan's invalid baseline risked regressing working code.
- **Versioned & changelogged.** The master file carries a version, supersede note, and changelog; each substantive change bumps the version and repackages `universal-audit-skill.skill`. CI (`.github/workflows/validate.yml`) enforces structural integrity.
- **Trigger tuning.** The skill's `description` is evaluated against `skill-dev/trigger-evals.json` and tuned (see `skill-dev/TRIGGER-TEST-*.md`).

### Update workflow

1. Run the skill on itself (or your target) -> a new `audits/AUDIT-RUN-<NNN>`.
2. Apply remediations; bump the version + changelog in the master `.md`.
3. Rebuild `SKILL.md` and repackage `universal-audit-skill.skill`.
4. Append the run to `audits/AUDIT-INDEX.md`.

## Authors & credits

- **Architect & lead author** — **Shubhajit Chatterjee** ([@schatt93](https://github.com/schatt93))
- **Coding & research partner** — **Claude** (Anthropic)

This framework was architected and authored by **Shubhajit Chatterjee**, with **Claude** as an AI **coding & research partner** — co-drafting the modules, running the self-audits in [`audits/`](audits/), validating standards against current sources (Principle 1), and packaging the skill. Commits are co-attributed with `Co-authored-by: Claude`.

## License

Released under the **MIT License**, © 2026 Shubhajit Chatterjee ([@schatt93](https://github.com/schatt93)) — see [LICENSE](LICENSE).
