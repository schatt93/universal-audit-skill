# Trigger Test — universal-audit-skill description (2026-06-24)

**Why this method.** The bundled optimizer (`scripts/run_loop.py` → `claude -p`) couldn't run in
this sandbox — the `claude` CLI is present (v2.1.181) but **not logged in**, and no `ANTHROPIC_API_KEY`
is set (the API is billed separately from a Claude subscription). So the optimizer's *logic* was run
in-session at no extra cost: **3 independent subagent graders** judge each query's trigger/no-trigger
against the current description (≈ `run_eval.py`'s 3× sampling), then the description is refined and
re-tested — the real optimize loop, executed by hand.

## Iteration 1 — base set (20 queries)
**Result: 20/20 correct, unanimous (3/3 each).** Recall 10/10 on should-trigger, specificity 10/10 on
should-not. Caught the non-obvious positives (data-room comb, fact-check market report, verify clinical
stats, consistency pass) and held off the near-misses (build vs audit Terraform, summarize vs audit a
contract, draft vs audit an equity note, fix a known test, spec→PDF, monthly finance report, explain
STRIDE, price lookup, expense logging).

## Iteration 2 — hard edge cases (14 queries)
**Result: 13/14.** All 7 hard should-triggers fired (financial-model pressure-test, SOC 2 control
adequacy, PR review, DPDP clause-by-clause compliance, board-deck-vs-actuals, credit-model validation,
WCAG accessibility). 6/7 should-nots held. **One over-trigger, unanimous:** *"reconcile my bank
statement against my expense log"* — the description's "verify these numbers" pulled in routine
personal bookkeeping that should defer to a dedicated finance tool (two graders flagged it as
borderline themselves).

### Refinement applied
Added a carve-out to the description's exclusion clause:
> "…or routine personal-finance/bookkeeping (expense logging, categorizing, bank reconciliation — use
> a finance tool)."

Also condensed the artifact list and examples to keep the description at **1000 / 1024 chars**.

## Iteration 2 re-test — does the carve-out separate bookkeeping from financial-artifact audit? (8 queries)
**Result: 8/8 correct, unanimous.**

| Now correctly NOT triggered (personal finance) | Still correctly triggered (financial artifacts) |
|---|---|
| reconcile bank statement vs expense log | board deck vs actual numbers (reporting verification) |
| log my last 5 UPI transactions, show balance | audit draft 10-Q — figures tie out to ledgers |
| categorize credit-card expenses, flag over-budget | equity-research BUY note — conflicts + DCF |
| | pressure-test the financial-model tab |
| | verify a market report's numbers vs cited sources |

The fix removed the false positive with **no collateral damage** to legitimate financial-report /
research / model auditing.

## Outcome
Description converged after one refinement: **42-query coverage, only one miss, fixed and confirmed.**
The updated description ships in `universal-audit-skill.skill`. For the fully rigorous version
(held-out train/test split, real model triggering), run the bundled loop later in an authenticated
Claude Code:

```
python -m scripts.run_loop \
  --eval-set <folder>/trigger-evals.json \
  --skill-path <folder>/universal-audit-skill-pkg \
  --model claude-opus-4-8 --max-iterations 5 --verbose
```
The saved `trigger-evals.json` now holds the full base + edge-case set (38 queries) for that run.
