#!/usr/bin/env python3
"""CI validation for the Universal Audit Skill repo.

Structural, dependency-free checks on the master skill file, the packaged
SKILL.md frontmatter, and the audit index. Exits non-zero on any failure so
the `validate` workflow gates merges. Run from the repo root.
"""
import re
import sys
import glob
import pathlib

errors = []
checks = 0


def ok(name):
    global checks
    checks += 1
    print(f"PASS  {name}")


def bad(name, detail=""):
    global checks
    checks += 1
    errors.append(name)
    print(f"FAIL  {name}  {detail}".rstrip())


# --- locate the master skill file (highest version) ---
def ver_key(p):
    m = re.search(r"-v(\d+)\.(\d+)\.md$", p)
    return tuple(int(x) for x in m.groups()) if m else (0, 0)


masters = sorted(glob.glob("universal-audit-skill-v*.md"), key=ver_key)
if not masters:
    print("FAIL  master skill file present  (no universal-audit-skill-v*.md)")
    sys.exit(1)
master = masters[-1]
ok(f"master skill file: {master}")
t = pathlib.Path(master).read_text(encoding="utf-8")

# --- 1) title version == metadata version ---
mt = re.search(r"#\s+.*\(v(\d+\.\d+)\)", t)
mm = re.search(r"Version\s+(\d+\.\d+)", t)
if mt and mm and mt.group(1) == mm.group(1):
    ok(f"title/metadata version match (v{mt.group(1)})")
else:
    bad("title/metadata version match",
        f"title={mt.group(1) if mt else None} meta={mm.group(1) if mm else None}")

# --- 2) stages / passes / principles defined ---
if set(re.findall(r"^###\s+Stage\s+([A-E])", t, re.M)) == set("ABCDE"):
    ok("Stages A-E defined")
else:
    bad("Stages A-E defined")

if set(re.findall(r"\*\*Pass\s+B(\d)", t)) == {"1", "2", "3", "4"}:
    ok("Passes B1-B4 defined")
else:
    bad("Passes B1-B4 defined")

try:
    sec1 = t.split("## 1.")[1].split("## 2.")[0]
    principles = sorted({int(x) for x in re.findall(r"^(\d+)\.\s+\*\*", sec1, re.M)})
    if principles == list(range(1, 9)):
        ok("Principles 1-8 defined")
    else:
        bad("Principles 1-8 defined", str(principles))
except Exception as e:  # noqa: BLE001
    bad("Principles section parses", str(e))

# --- 3) internal section cross-refs resolve (exclude external statute numbers) ---
secs = {int(m) for m in re.findall(r"^##\s+(\d+)\.", t, re.M)}
EXTERNAL = {11, 242, 302, 404}  # 21 CFR 11/242, SOX 302/404 keep their own symbols
bad_refs = sorted({int(s) for s in re.findall(r"§\s*(\d+)", t)} - secs - EXTERNAL)
if not bad_refs:
    ok("internal section cross-refs resolve")
else:
    bad("internal section cross-refs resolve", f"unresolved {bad_refs}")

# --- 4) module namespace integrity ---
defined = [m for m in re.findall(r"\*\*([A-Z]{1,2})\.\s", t)
           if m not in {"S1", "S2", "S3", "S4", "S5"}]
singles = sorted(d for d in defined if len(d) == 1)
doubles = [d for d in defined if len(d) == 2]

expected_singles = [chr(ord("A") + i) for i in range(len(singles))]
if singles == expected_singles:
    ok(f"single-letter modules contiguous A-{singles[-1] if singles else '?'}")
else:
    bad("single-letter modules contiguous", str(singles))


def gen_doubles(n):
    out, i = [], 0
    while len(out) < n:
        s = "A" + chr(ord("A") + i)
        i += 1
        if s == "AI":  # intentionally skipped (collides with Module K = AI/ML)
            continue
        out.append(s)
    return out


if doubles == gen_doubles(len(doubles)):
    ok(f"two-letter modules contiguous AA-{doubles[-1] if doubles else '?'} (AI skipped)")
else:
    bad("two-letter modules contiguous (AI skipped)", str(doubles))

if len(set(defined)) == len(defined):
    ok(f"no duplicate module codes ({len(defined)} modules)")
else:
    bad("no duplicate module codes")

# --- 5) packaged SKILL.md frontmatter ---
skill_md = pathlib.Path("skill-dev/universal-audit-skill-pkg/SKILL.md")
if skill_md.exists():
    s = skill_md.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", s, re.S)
    if fm:
        body = fm.group(1)
        name = re.search(r"^name:\s*(\S+)", body, re.M)
        if name:
            ok(f"SKILL.md frontmatter name: {name.group(1)}")
        else:
            bad("SKILL.md frontmatter has name")
        parts = re.split(r"description:\s*>?-?\s*", body, maxsplit=1)
        dlen = len(" ".join(parts[1].split())) if len(parts) > 1 else 0
        if 0 < dlen <= 1024:
            ok(f"SKILL.md description length {dlen} <= 1024")
        else:
            bad("SKILL.md description length <= 1024", str(dlen))
    else:
        bad("SKILL.md frontmatter present")
else:
    bad("packaged SKILL.md present", str(skill_md))

# --- 6) audit index well-formed ---
idx = pathlib.Path("audits/AUDIT-INDEX.md")
if idx.exists():
    rows = [l for l in idx.read_text(encoding="utf-8").splitlines()
            if l.strip().startswith("|")]
    data = [r for r in rows if not set(r.replace("|", "").strip()) <= set("-: ")]
    if len(data) >= 2:
        ok(f"AUDIT-INDEX has {len(data) - 1} run row(s)")
    else:
        bad("AUDIT-INDEX has a header + run rows")
    bad_cols = [i for i, r in enumerate(data)
                if len(r.strip().strip("|").split("|")) != 7]
    if not bad_cols:
        ok("AUDIT-INDEX rows have 7 columns")
    else:
        bad("AUDIT-INDEX rows have 7 columns", f"row index {bad_cols}")
else:
    bad("AUDIT-INDEX present", str(idx))

print(f"\n{checks} checks, {len(errors)} failure(s)")
sys.exit(1 if errors else 0)
