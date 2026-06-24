# Output and Schema

## Where outputs go

All audit artifacts are written to a dedicated **audit directory** — default **`./audits/`** (configurable in §2, created if absent), kept out of the audited project's root and source tree.

- **Audit record:** `audits/AUDIT-RUN-<NNN>-<YYYY-MM-DD>.md`
- **Append-only index:** `audits/AUDIT-INDEX.md` — one row per run.

Run numbers increment from the highest existing run in the audit directory.

## Audit record structure (in order)

1. **Header** — run number, date, agent, scope, artifact type(s), **objectives**, **materiality**, **sampling**, **assurance level**, **depth**, modules selected + exclusion rationale, standards enforced (with validated editions/dates), tool-availability status.
2. **Manifest** — every in-scope artifact (path, title, type, version, owner).
3. **Findings** — every finding as a record, grouped by stage/module, sorted by severity.
4. **Consolidation summary** — counts by severity/category; root-cause clusters; false-positive notes; coverage proof.
5. **Audit of the Audit** — the Stage-D adversarial self-review and any findings it surfaced.
6. **Remediation plan** — fix records with `Fix ID`s.
7. **Open questions & decisions required** — consolidated for the user.
8. **Verification ledger** — sources + dates for validated facts; all `TOOL-UNAVAILABLE` / `UNVERIFIED` items for re-run.

## Finding record fields

`Finding ID (Fn)` · `Stage/Module` · `Location (file + section/line)` · `Description` · `Evidence (quote/reference + external source & date)` · `Category` · `Severity (S1–S5)` · `Impact` · `Likelihood` · `CVSS (security)` · `OWASP-LLM/Agentic ref (AI)` · `Status` · `Tags` · `Resolved by (→ Fix ID Rn)`

## Remediation record fields

`Fix ID (Rn)` · `Resolves (Fn…)` · `Description` · `Basis (cited current standard + date)` · `Effort` · `Dependencies/sequencing` · `Risk introduced` · `Validation/acceptance criteria` · `Priority` · `DECISION-REQUIRED? (+ question)`

## Index row

`Run | Date | Scope | Depth | Modules run | Findings (S1/S2/S3/S4/S5) | Status`

## Exit criteria & edge cases

A run is complete only when all stages executed, applicable modules ran at the chosen depth, each pass B1–B3 ran in both modes, the "Audit of the Audit" was performed, every finding is evidenced and classified, traceability links are intact, the false-positive pass is done, coverage is proven, time-sensitive facts are validated with recorded sources, and an **overall conclusion is stated against the objectives at the declared assurance level**.

- **Zero findings** → stated explicitly with the coverage proof ("clean at this depth" is a result).
- **Unreadable/unsupported artifact** → flagged, with the reason, and guidance requested.
- **Pending verification** → run is "complete-with-pending-verification"; the exact items to re-run are listed.
