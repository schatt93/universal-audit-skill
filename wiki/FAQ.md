# FAQ

**What can it audit?**
Almost any work product — code, apps, APIs, specs, architecture/design docs, data pipelines, ML/AI/LLM systems, infrastructure/IaC, financial and investment-research reports, market analyses, spreadsheets, and media/document files. It classifies the artifact in Stage A and selects the relevant modules.

**Does it run all 42 modules every time?**
No. Stage A selects only the applicable modules and records the justification for each inclusion and exclusion. Modules X (integrity) and Y (metadata) run on any file.

**Why does it re-check standards instead of relying on what the model knows?**
Editions, regulations, and defaults drift. Principle 1 treats training data as a hypothesis and validates checkable facts against authoritative sources at run time, recording the source and date. If validation isn't possible, the item is marked `UNVERIFIED` or `TOOL-UNAVAILABLE` — never asserted.

**What's the difference between the passes and the modules?**
The four **passes** (B1–B4) are universal and run on everything. The **modules** (A–AQ) are domain-specific and run only when selected. Passes B1–B3 run in both a constructive and an adversarial mode; B4 is purely adversarial.

**What does "dual-mode" mean?**
Each universal check is run twice with opposite intent: constructive ("is it right / complete / consistent?") and adversarial ("construct a counterexample, prove the omission"). Confirmation-seeking and falsification-seeking miss different things.

**Is it a replacement for a professional auditor or lawyer?**
No. For high-stakes or regulated work it structures the review but does not replace professional sign-off. Legal/contract review (Module AJ) is explicitly non-attorney; it surfaces risk and defers final judgment to counsel.

**How are findings prioritized?**
By severity S1–S5 (Risk = Impact × Likelihood). Security findings also carry a CVSS score; AI findings reference the relevant OWASP LLM/Agentic category.

**What is the "Audit of the Audit"?**
A Stage-D step where the skill red-teams its own audit — hunting false negatives/blind spots, false positives, confirmation bias, severity miscalibration, and coverage-honesty issues — and folds any new findings in.

**Can it be tricked by malicious content in the artifact?**
Principle 8 treats all ingested material as data, not instructions. Embedded "instructions," claimed authorizations, or urgency are quoted to the user and logged as a possible prompt-injection finding, never acted upon.

**Where do results go?**
To `./audits/` — a numbered `AUDIT-RUN-<NNN>-<date>.md` plus a row in the append-only `AUDIT-INDEX.md`. See **[[Output and Schema]]**.

**How is the framework itself kept correct?**
It audits itself; see **[[Maintenance and Audit Trail]]**.
