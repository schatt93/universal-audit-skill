# Audit Index

Append-only log of audit runs. Newest at top. *(Prior history cleared at user request on 2026-06-21; numbering restarted.)*

| Run | Date | Scope | Depth | Modules run | Findings (S1/S2/S3/S4/S5) | Status |
|-----|------|-------|-------|-------------|---------------------------|--------|
| 008 | 2026-06-23 | `universal-audit-skill-v7.2.md` (consistency + knowledge + instruction + staleness) | Deep (Reasonable for consistency; Limited for staleness) | Pass B1 currency-validation (13 standards web-checked) · Pass B3 cross-ref/namespace/schema · O Documentation | 0 / 0 / 1 / 2 / 1 (4 + info) | Complete — clean structure; 1 factual error (ISO 19011), 2 staleness; R07–R11 **applied in v7.3** |
| 007 | 2026-06-23 | `universal-audit-skill-v7.1.md` (financial-category coverage gap — investment research / market analysis) | Deep method, Limited assurance (single-domain completeness) | Pass B2 vs. AF/AM/AK + generic J/K/O/Q · external standards benchmark (FINRA/SEC/EU-MAR/SEBI/IOSCO/CFA/GIPS) | 0 / 1 / 0 / 0 / 0 (1 coverage gap) | Complete — resolved by new Module AQ in **v7.2** (also carries R01–R05) |
| 006 | 2026-06-23 | `universal-audit-skill-v7.1.md` (internal-consistency audit) | Standard (Reasonable; internal consistency only) | Pass B3 · programmatic cross-ref/schema/namespace integrity pass | 0 / 0 / 3 / 1 / 1 (5 total) | Complete — R01–R05 **applied in v7.2** |
| 005 | 2026-06-21 | `universal-audit-prompt-v7.md` (confirmatory full-document audit) | Deep (Reasonable assurance, internal integrity) | Universal B1–B4 · O Documentation · programmatic cross-ref/schema integrity pass | 0 / 0 / 0 / 0 / 2 (2 Info; **PASSES**) | Complete — v7 confirmed clean; 2 Info items polished in **v7.1** |
| 004 | 2026-06-21 | `universal-audit-prompt-v6.md` (extended 7-domain completeness benchmark) | Deep (Limited assurance) | Pass B2 vs. legal · medical-device · ESG · smart-contract · model-risk · safety-critical · cyber-ops/forensics (+ long-tail named) | 7×S2 + 2×S3 (9 domain gaps) | Complete — incorporated in v7 (Group 3) |
| 003 | 2026-06-21 | `universal-audit-prompt-v6.md` (targeted 3-domain completeness benchmark) | Deep (Limited assurance) | Pass B2 vs. financial/SOX · hardware/firmware · scientific/research data | 3 / 0 / 0 / 0 / 0 (3 domain gaps) | Complete — folds into Group 3 |
| 002 | 2026-06-21 | `universal-audit-prompt-v5.md` (self-audit + industry benchmark) | Deep | Universal B1–B4 · O Documentation · external practice benchmark (6 domains) | 0 / 1 / 8 / 1 / 1 (11 total) | Complete (all incorporated in v6) |
| 001 | 2026-06-21 | `universal-audit-prompt-v4.md` (self-audit) | Standard | Universal B1–B4 (constructive + adversarial) · O Documentation · cross-ref/schema check | 0 / 0 / 1 / 0 / 2 (3 total) | Complete (fixes applied in v4.1) |
