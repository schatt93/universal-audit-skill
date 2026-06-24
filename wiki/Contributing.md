# Contributing

## Filing issues

Use the issue forms (Issues → New issue):

- **Audit finding** — a defect/risk/gap/inconsistency, with an S1–S5 severity and concrete evidence.
- **Stale standard / edition** — an out-of-date standard or date-stamped claim (Principle 1), with the correct edition + an authoritative source.
- **Bug or inconsistency** — broken cross-reference, schema mismatch, namespace gap, contradictory wording.
- **New module or enhancement** — propose a new audit domain/module or improve an existing one.

Findings without evidence are closed — cite the artifact location and, where relevant, an external source with its date.

## Pull requests

The PR template carries a maintenance checklist:

- [ ] Ran the audit skill on the change (added a new `audits/AUDIT-RUN-<NNN>` if material)
- [ ] Bumped the version + changelog in `universal-audit-skill-v*.md`
- [ ] Rebuilt `SKILL.md` and repackaged `universal-audit-skill.skill`
- [ ] Appended the run to `audits/AUDIT-INDEX.md`
- [ ] Standards cited were validated against current sources (Principle 1)
- [ ] `validate` CI is green

## CI — the `validate` workflow

`.github/workflows/validate.yml` runs `.github/scripts/validate_skill.py` on every push/PR to `main`. It performs dependency-free structural checks:

- title version == metadata version;
- Stages A–E, Passes B1–B4, Principles 1–8 defined;
- internal `§N` cross-references resolve (external statutes excluded);
- module namespace integrity (single `A–Z`, two-letter `AA–AQ` skipping `AI`, no duplicates);
- packaged `SKILL.md` frontmatter present and description ≤ 1024 chars;
- `AUDIT-INDEX.md` well-formed (7 columns per row).

## Branch protection

`.github/ruleset-main.json` protects `main` — requires a PR, requires the `validate` check to pass, and blocks force-push/deletion. Rulesets are free on **public** repos; private repos need GitHub Pro/Team. Apply with:

```bash
gh api -X POST repos/schatt93/universal-audit-skill/rulesets --input .github/ruleset-main.json
```

## Development layout (`skill-dev/`)

- `trigger-evals.json` — the trigger eval set (should / should-not-trigger queries).
- `TRIGGER-TEST-*.md` — description trigger-test results.
- `universal-audit-skill-pkg/` — the unpacked skill (`SKILL.md` + `evals/`) used by the description optimizer.

To repackage the `.skill` after editing the master file, prepend the YAML frontmatter to the master `.md` to form `SKILL.md`, then zip the skill folder (the skill-creator's `package_skill.py` does this and validates it).
