# Deep-Research Currency Engine — workflow (agent-agnostic)

The reusable research loop that the audit's **Stage R** runs to gather and verify *current* knowledge before judging an artifact. Platform-neutral — works on any agent with web search + fetch, and uses parallel sub-agents where available (see [`web-researcher.md`](web-researcher.md)). Adapted, agent-agnostic, from structured deep-research agents (outline -> deep -> report), specialized for **audit evidence**.

## When to run
- Early, right after Stage A selects modules — to ground the whole run.
- On demand, whenever a pass or module reaches a checkable, time-sensitive fact (standard edition, regulation, security advisory, dependency CVE, best practice, benchmark).

## Phases

### 1. Decompose -> Research Outline
Derive research items from artifact type(s) + selected modules + domain/regulatory context + objectives. Each item has fields:

| field | meaning |
|---|---|
| `claim` | what must be confirmed (e.g. "current OWASP Top 10 edition") |
| `current_value` | the confirmed current value / edition |
| `source` | authoritative URL (primary > secondary) |
| `date_checked` | when verified |
| `changed` | what changed vs the artifact's assumption / prior edition |
| `applicability` | how it bears on this audit |

The outline is the **smallest** set that covers every time-sensitive fact the audit will rely on.

### 2. Checkpoint (optional, human-in-the-loop)
Show the outline; let the user add / trim items (per master §7). Proceed at Deep depth if unconfirmed, stating so.

### 3. Deep research (iterative, fan-out, parallel)
For each item: reformulate queries; fan out across multiple sources; fetch the authoritative source; capture the exact value + date. Dispatch **one web-research worker per item in parallel** where the platform supports it (see `web-researcher.md`); otherwise sequentially. Retry with reformulated queries (>=3) before tagging a failure.

### 4. Verify (adversarial)
For each source: authoritative? current? primary-over-secondary? does it actually support the claim? **Triangulate >=2 independent sources for high-impact items.** Seek disconfirming evidence. Flag tampered / outdated / cherry-picked sources. Tool failure -> `TOOL-UNAVAILABLE`; genuine absence -> `UNVERIFIED`.

### 5. Synthesize -> Research Brief
Write `audits/AUDIT-RUN-<NNN>-research.md`: each item with `current_value` + `source` + `date`, grouped by module, with an *as-of* timestamp and a short "what changed / what to re-check" note. This Brief + the Verification Ledger are the **only** basis for time-sensitive assertions in Stages C and E.

## Research Brief template
```
# Research Brief — AUDIT-RUN-<NNN> (as of <YYYY-MM-DD>)

## <Module / area>
- **<claim>** — current: <value/edition>; source: <URL> (checked <date>);
  changed: <...>; applies: <...>; tag: [verified | UNVERIFIED | TOOL-UNAVAILABLE]

## Open / pending verification
- <items that could not be confirmed — must be re-run when tools are restored>
```

## Depth
- **Lightweight** — research only safety/correctness-critical items.
- **Standard** — research all time-sensitive / high-impact items.
- **Deep** — research every checkable currency item; triangulate the high-impact ones.
