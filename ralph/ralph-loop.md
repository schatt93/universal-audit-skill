# Ralph Loop — iterate the audit to a clean pass (agent-agnostic)

The "Ralph" pattern: run the audit, fix what it finds, re-audit, and repeat **until the work passes for real** — with hard guards so it never spins forever or fakes a pass. Master reference: §10.

## Loop
```
n = next run number
loop:
  run full audit (Stages A→R→E) -> audits/AUDIT-RUN-<n>-*.md (+ research brief)
  if exit_criteria_met(): declare PASS; stop
  if iteration >= MAX or no_new_resolutions(): escalate to human; stop   # never declare pass
  apply validated Stage-E fixes for open findings (DECISION-REQUIRED -> pause for human)
  n += 1   # fresh run, no carried state (Principle 2)
```
Each iteration is its own numbered run record, so the trail shows the convergence.

## Exit criteria ("100% pass") — ALL must hold
- [ ] No `Open` finding at/above the materiality threshold (default: zero S1–S3 open; S4/S5 resolved or explicitly accepted).
- [ ] Coverage proven vs the manifest + module selection (both pass modes for B1–B3; modules at the chosen depth).
- [ ] Stage-R currency fresh; no `UNVERIFIED` / `TOOL-UNAVAILABLE` left unaddressed.
- [ ] "Audit of the Audit" clean.
- [ ] Every applied fix independently re-verified (ideally by a different vendor — see `multi-vendor-agents.md`).

A pass is a positive, evidenced result — not "no new findings."

## Guards
- **MAX_ITERATIONS** (default 5, configurable). On reach: stop + escalate with remaining findings.
- **No-progress / oscillation:** if a pass resolves nothing new, stop + escalate.
- **No false pass:** failed / skipped / unverifiable steps are tagged `TOOL-UNAVAILABLE` or `UNVERIFIED`, never counted as resolved. Do not accept a task's failure as the result.
- **Human checkpoints:** `DECISION-REQUIRED`, risk-acceptance, and scope changes pause the loop.
- **Regression guard (Principle 9):** every re-audit verifies fixes against the actual system and did not break working code.

## Driving it
- An agent runs this loop directly (no extra tooling needed).
- For unattended runs, a thin driver can re-invoke the agent per iteration and stop on the PASS marker or MAX_ITERATIONS; keep the same guards.
