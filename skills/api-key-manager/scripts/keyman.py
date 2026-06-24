#!/usr/bin/env python3
"""api-key-manager — CRUD for model-vendor API keys used by the Ralph multi-vendor loop.

Keys live in a git-ignored env file (default ~/.config/universal-audit/keys.env, mode 600) or
in environment variables — never in the repo, prompts, logs, or chat. Values are read from an
env var or a hidden stdin prompt, never from argv (which leaks to ps / shell history).
"""
import argparse, os, sys, getpass, pathlib, re

DEFAULT = pathlib.Path(os.environ.get(
    "UNIVERSAL_AUDIT_KEYS",
    str(pathlib.Path.home() / ".config" / "universal-audit" / "keys.env")))


def load(p):
    d = {}
    if p.exists():
        for ln in p.read_text().splitlines():
            ln = ln.strip()
            if not ln or ln.startswith("#") or "=" not in ln:
                continue
            k, v = ln.split("=", 1)
            d[k.strip()] = v.strip()
    return d


def save(p, d):
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(p.parent, 0o700)
    except OSError:
        pass
    body = ("# api-key-manager store - DO NOT COMMIT (mode 600).\n"
            + "\n".join(f"{k}={v}" for k, v in sorted(d.items())) + "\n")
    p.write_text(body)
    try:
        os.chmod(p, 0o600)
    except OSError:
        pass


def mask(v):
    return ("*" * max(0, len(v) - 4) + v[-4:]) if v else "(empty)"


def main():
    ap = argparse.ArgumentParser(prog="keyman",
                                 description="CRUD for vendor API keys (git-ignored store).")
    ap.add_argument("--store", help=f"store path (default {DEFAULT})")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="create/update a key")
    a.add_argument("name")
    a.add_argument("--from-env", help="read the value from this env var")
    a.add_argument("--value", help="UNSAFE (leaks to shell history); prefer --from-env or stdin")
    sub.add_parser("list", help="list names + masked values")
    g = sub.add_parser("get", help="show one key (masked)")
    g.add_argument("name")
    g.add_argument("--reveal", action="store_true", help="print the full secret (warns)")
    rm = sub.add_parser("remove", help="delete a key")
    rm.add_argument("name")
    sub.add_parser("path", help="print the store path")
    sub.add_parser("source-cmd", help="print the shell cmd to load keys into env (no values shown)")
    args = ap.parse_args()
    p = pathlib.Path(args.store) if args.store else DEFAULT
    d = load(p)

    if args.cmd == "path":
        print(p); return
    if args.cmd == "source-cmd":
        print(f"set -a; . '{p}'; set +a   # loads keys into env without printing them"); return
    if args.cmd == "list":
        if not d:
            print(f"(no keys) store: {p}"); return
        mode = oct(p.stat().st_mode & 0o777) if p.exists() else "----"
        print(f"store: {p}  (mode {mode})")
        for k, v in sorted(d.items()):
            print(f"  {k} = {mask(v)}")
        return
    if args.cmd == "get":
        if args.name not in d:
            print(f"no such key: {args.name}", file=sys.stderr); sys.exit(1)
        if args.reveal:
            print("WARNING: revealing a secret to stdout.", file=sys.stderr)
            print(d[args.name])
        else:
            print(mask(d[args.name]))
        return
    if args.cmd == "remove":
        if d.pop(args.name, None) is None:
            print(f"no such key: {args.name}", file=sys.stderr); sys.exit(1)
        save(p, d); print(f"removed {args.name}"); return
    if args.cmd == "add":
        if not re.fullmatch(r"[A-Z0-9_]+", args.name):
            print("name must be UPPER_SNAKE, e.g. OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
        if args.from_env:
            val = os.environ.get(args.from_env)
            if not val:
                print(f"env var {args.from_env} is empty/unset", file=sys.stderr); sys.exit(1)
        elif args.value is not None:
            print("WARNING: --value can leak via shell history; prefer --from-env or stdin.", file=sys.stderr)
            val = args.value
        else:
            val = getpass.getpass(f"{args.name} value (hidden): ")
        if not val.strip():
            print("empty value", file=sys.stderr); sys.exit(1)
        d[args.name] = val.strip(); save(p, d)
        print(f"saved {args.name} = {mask(val.strip())}  -> {p}")
        return


if __name__ == "__main__":
    main()
