# Universal Audit, Verification & Test — Master Skill

A reusable, **artifact-agnostic audit / verification / red-team framework**, packaged as an installable Claude skill. Point it at almost any work product — source code, applications, APIs, specs, architecture and design docs, data pipelines, ML/AI/LLM systems, infrastructure/IaC, financial and investment-research reports, market analyses, spreadsheets, and media or document files — and it classifies the artifact, runs only the relevant verification domains against *currently validated* industry standards, and produces a numbered, evidence-based audit record with severity-rated findings and a traceable remediation plan.

It is written in the spirit of **IEEE 1028 (Software Reviews and Audits)** and the auditing principles of **ISO 19011:2018**: adversarial toward the *artifact* (not the author), evidence-or-it-didn't-happen, and zero facts asserted from stale memory.

---

## What it is

- **42 domain modules** across three groups: system & quality (`A`–`W`), file-format & asset (`X`–`AE`), and specialized professional domains (`AF`–`AQ`, including Financial/SOX, Medical-Device, Smart-Contract, Model-Risk, and Investment-Research & Market-Analysis).
- **Dual-mode universal passes** — every check runs in a *constructive* ("is it right?") and an *adversarial* ("prove it wrong") mode (Pass B1–B3), plus a cross-cutting red-team pass (B4).
- **Severity taxonomy** S1–S5 with orthogonal `Status` and `Tags`, and full **finding ↔ fix traceability**.
- **Runtime standards validation** — editions, regulations, and framework defaults are treated as hypotheses and re-checked against authoritative sources during the run.
- **Self-auditing** — the framework is regularly run on itself; the trail lives in [`audits/`](audits/).

## Repository layout

```
universal-audit-skill-v7.4.md   # the skill source (human-readable master prompt)
universal-audit-skill.skill     # installable package (SKILL.md + eval set)
audits/                         # audit outputs: AUDIT-INDEX.md + AUDIT-RUN-* records
skill-dev/                      # build & triggering artifacts
  ├─ trigger-evals.json         #   trigger eval set (should / should-not-trigger queries)
  ├─ TRIGGER-TEST-*.md          #   description trigger-test results
  └─ universal-audit-skill-pkg/ #   unpacked skill (for the description optimizer)
```

## How to use

**As an installed skill (Cowork / Claude Code).** Install `universal-audit-skill.skill` (use the *Save skill* button in Cowork, or your client's skill-install flow). It then triggers automatically when you ask to audit, verify, review, QA, fact-check, stress-test, red-team, or find defects/gaps/inconsistencies in something — even if you never say the word "audit." Audit outputs are written to `./audits/`.

**As a prompt.** Paste `universal-audit-skill-v7.4.md` into a fresh agent session that has (1) file read/write and (2) web search + page fetch. Fill the `<<…>>` placeholders (scope, artifact type(s), domain/regulatory context, audit depth, **audit output location**, objectives, materiality, assurance level) and run top-to-bottom. The agent selects which modules apply — it does not run all of them blindly.

**Pick a depth.** `Lightweight | Standard | Deep` (default **Deep**); assurance is `Reasonable | Limited`.

**Outputs.** Each run writes `audits/AUDIT-RUN-<NNN>-<YYYY-MM-DD>.md` (header · manifest · findings · consolidation · *audit of the audit* · remediation plan · open questions · verification ledger) and appends one row to `audits/AUDIT-INDEX.md`. The audit directory is created if absent and is configurable in §2.

## How it is maintained

The skill is maintained **by auditing itself** — the discipline it preaches, it practices.

- **Self-audit trail.** Every substantive change is driven by a recorded run in [`audits/`](audits/): e.g. `AUDIT-RUN-006` (internal consistency), `AUDIT-RUN-007` (financial-category coverage gap → new Module AQ), `AUDIT-RUN-008` (knowledge/instruction correctness + standards staleness). Findings carry IDs (`Fn`), fixes carry IDs (`Rn`), and `AUDIT-INDEX.md` is an append-only log of every run.
- **Runtime standards validation (Principle 1).** Named standards and editions are re-validated against authoritative sources and corrected when stale — e.g. `AUDIT-RUN-008` confirmed OWASP Top 10:2025, PCAOB AS 2201 (eff. 2026-12-15), and the EU AI Act Art. 50 date, and fixed an incorrect `ISO 19011` edition and superseded model-risk citations (SR 26-2).
- **Versioned & changelogged.** The master file carries a version, supersede note, and changelog; each substantive change bumps the version and repackages `universal-audit-skill.skill`.
- **Trigger tuning.** The skill's `description` (the field that decides when Claude invokes it) is evaluated against `skill-dev/trigger-evals.json` and tuned (see `skill-dev/TRIGGER-TEST-*.md`); the skill-creator's optimizer can refine it further in an authenticated environment.

### Update workflow

1. Run the skill on itself (or your target) → a new `audits/AUDIT-RUN-<NNN>`.
2. Apply remediations; bump the version + changelog in the master `.md`.
3. Rebuild `SKILL.md` and repackage `universal-audit-skill.skill`.
4. Append the run to `audits/AUDIT-INDEX.md`.

## Authors & credits

- **Architect & lead author** — **Shubhajit Chatterjee** ([@schatt93](https://github.com/schatt93))
- **Coding & research partner** — **Claude** (Anthropic)

This framework was architected and authored by **Shubhajit Chatterjee**, with **Claude** as an AI **coding & research partner** — co-drafting the modules, running the self-audits in [`audits/`](audits/), validating standards against current sources (Principle 1), and packaging the skill. Commits are co-attributed with `Co-authored-by: Claude`.

## License

Released under the **MIT License**, © 2026 Shubhajit Chatterjee ([@schatt93](https://github.com/schatt93)) — see [LICENSE](LICENSE).
