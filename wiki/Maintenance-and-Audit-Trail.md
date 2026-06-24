# Maintenance and Audit Trail

The framework is maintained **by auditing itself** — the discipline it preaches, it practices. Every substantive change is driven by a recorded run in [`audits/`](https://github.com/schatt93/universal-audit-skill/tree/main/audits).

## Self-audit history

| Run | Focus | Outcome |
|---|---|---|
| 001–005 | Early self-audits + industry benchmarking | Folded into v4–v7 |
| **006** | Internal consistency (Pass B3) | 5 findings (title version, module range, dual-mode scope, schema gap, naming) → **R01–R05**, applied in v7.2 |
| **007** | Financial-category coverage gap (Pass B2) | Found no home for investment-research/market-analysis content → **new Module AQ** (v7.2) |
| **008** | Consistency + knowledge + instruction + **staleness** | Validated 13 standards live; corrected `ISO 19011` edition, refreshed **SR 26-2** and **NIST 800-61 r3** → **R07–R11**, applied in v7.3 |
| **009** | Multi-platform + low-context + Principle 9 | Ground-truth gap from live feedback → **Principle 9**, the **Lite** edition, and platform adapters (Codex/AGENTS.md, Cursor, Gemini, Copilot); description trimmed → **v8.0** |
| **010** | Fresh full self-audit | Caught a systematic **date error** (records dated a day early) + doc-trail lag → corrected; v8.0 otherwise confirmed clean |

Findings carry IDs (`Fn`), fixes carry IDs (`Rn`), and `AUDIT-INDEX.md` is an append-only log of every run.

## How currency is kept (Principle 1)

Named standards and editions are re-validated against authoritative sources and corrected when stale. For example, AUDIT-RUN-008 confirmed OWASP Top 10:2025, PCAOB AS 2201 (effective 2026-12-15), and the EU AI Act Art. 50 date (2026-08-02), and corrected an invalid `ISO 19011:2026` reference to **ISO 19011:2018**.

## Versioning

The master file (`universal-audit-skill-v<major>.<minor>.md`) carries a version, a supersede note, and a changelog. Each substantive change bumps the version and repackages `universal-audit-skill.skill`. CI (see **[[Contributing]]**) enforces that the title version matches the metadata version.

## Update workflow

1. Run the skill on itself (or your target) → a new `audits/AUDIT-RUN-<NNN>`.
2. Apply remediations; bump the version + changelog in the master `.md`.
3. Rebuild `SKILL.md` and repackage `universal-audit-skill.skill`.
4. Append the run to `audits/AUDIT-INDEX.md`.

## Trigger tuning

The skill's `description` (the field that decides when Claude invokes it) is evaluated against `skill-dev/trigger-evals.json` and tuned (`skill-dev/TRIGGER-TEST-*.md`). The latest run scored the description **20/20** then refined it to add a personal-finance/bookkeeping carve-out (re-tested 8/8). The skill-creator's optimizer can refine it further in an authenticated environment.
