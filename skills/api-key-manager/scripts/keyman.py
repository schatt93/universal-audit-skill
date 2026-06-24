#!/usr/bin/env python3
"""api-key-manager — CRUD for model-vendor API keys (OS keyring or git-ignored file).

Backends (most -> least secure):
  keyring : the OS keyring — macOS Keychain, Windows Credential Manager, Linux Secret Service /
            KWallet — via the `keyring` package (pip install keyring). Service name: "universal-audit".
  file    : a git-ignored env file (default ~/.config/universal-audit/keys.env, mode 600).
Default backend is "auto": keyring if a usable OS backend is present, else file.

Values are read from an env var or a hidden stdin prompt, never from argv (which leaks to ps /
shell history). Keys are never printed except `get --reveal`; list/get mask to the last 4 chars.
"""
import argparse, os, sys, json, getpass, pathlib, re

SERVICE = "universal-audit"
CFG = pathlib.Path(os.environ.get("UNIVERSAL_AUDIT_HOME", str(pathlib.Path.home()/".config"/"universal-audit")))
FILE_STORE = pathlib.Path(os.environ.get("UNIVERSAL_AUDIT_KEYS", str(CFG/"keys.env")))
KR_INDEX = CFG/"keyring-index.json"   # stores NAMES only (never secrets), so list/remove can enumerate


def _keyring():
    try:
        import keyring
        from keyring.backends.fail import Keyring as Fail
        return None if isinstance(keyring.get_keyring(), Fail) else keyring
    except Exception:
        return None


def resolve(name):
    if name == "file":
        return "file"
    if name == "keyring":
        if _keyring() is None:
            sys.exit("keyring backend unavailable — run `pip install keyring` and ensure an OS backend "
                     "(Keychain / Credential Manager / Secret Service).")
        return "keyring"
    return "keyring" if _keyring() is not None else "file"


def file_load():
    d = {}
    if FILE_STORE.exists():
        for ln in FILE_STORE.read_text().splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, v = ln.split("=", 1); d[k.strip()] = v.strip()
    return d


def file_save(d):
    FILE_STORE.parent.mkdir(parents=True, exist_ok=True)
    try: os.chmod(FILE_STORE.parent, 0o700)
    except OSError: pass
    FILE_STORE.write_text("# api-key-manager store - DO NOT COMMIT (mode 600).\n"
                          + "\n".join(f"{k}={v}" for k, v in sorted(d.items())) + "\n")
    try: os.chmod(FILE_STORE, 0o600)
    except OSError: pass


def kr_names():
    try: return sorted(set(json.loads(KR_INDEX.read_text()))) if KR_INDEX.exists() else []
    except Exception: return []


def kr_names_save(names):
    KR_INDEX.parent.mkdir(parents=True, exist_ok=True)
    try: os.chmod(KR_INDEX.parent, 0o700)
    except OSError: pass
    KR_INDEX.write_text(json.dumps(sorted(set(names))))


def mask(v): return ("*" * max(0, len(v) - 4) + v[-4:]) if v else "(empty)"


def get_val(b, n): return file_load().get(n) if b == "file" else _keyring().get_password(SERVICE, n)


def set_val(b, n, v):
    if b == "file":
        d = file_load(); d[n] = v; file_save(d)
    else:
        _keyring().set_password(SERVICE, n, v); kr_names_save(kr_names() + [n])


def del_val(b, n):
    if b == "file":
        d = file_load()
        if n not in d: return False
        del d[n]; file_save(d); return True
    kr = _keyring()
    if kr.get_password(SERVICE, n) is None and n not in kr_names(): return False
    try: kr.delete_password(SERVICE, n)
    except Exception: pass
    kr_names_save([x for x in kr_names() if x != n]); return True


def names(b): return sorted(file_load().keys()) if b == "file" else kr_names()


def main():
    ap = argparse.ArgumentParser(prog="keyman", description="CRUD for vendor API keys (OS keyring or git-ignored file).")
    ap.add_argument("--backend", choices=["auto", "keyring", "file"], default="auto")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("name"); a.add_argument("--from-env"); a.add_argument("--value")
    sub.add_parser("list")
    g = sub.add_parser("get"); g.add_argument("name"); g.add_argument("--reveal", action="store_true")
    rm = sub.add_parser("remove"); rm.add_argument("name")
    sub.add_parser("backend")
    sub.add_parser("export-env")
    sub.add_parser("source-cmd")
    args = ap.parse_args()
    b = resolve(args.backend)

    if args.cmd == "backend":
        print(b + ("  (OS keyring, service: " + SERVICE + ")" if b == "keyring" else f"  (file: {FILE_STORE})")); return
    if args.cmd == "source-cmd":
        if b != "file": sys.exit('source-cmd is for the file backend; for keyring use: eval "$(keyman export-env)"')
        print(f"set -a; . '{FILE_STORE}'; set +a"); return
    if args.cmd == "export-env":
        print('# usage: eval "$(keyman export-env)"  — loads keys into this shell (values not shown by the agent)', file=sys.stderr)
        for n in names(b):
            v = (get_val(b, n) or "").replace("'", "'\\''")
            print(f"export {n}='{v}'")
        return
    if args.cmd == "list":
        ns = names(b)
        if not ns: print(f"(no keys)  backend: {b}"); return
        print(f"backend: {b}" + ("  (OS keyring)" if b == "keyring" else f"  ({FILE_STORE})"))
        for n in ns: print(f"  {n} = {mask(get_val(b, n) or '')}")
        return
    if args.cmd == "get":
        v = get_val(b, args.name)
        if v is None: sys.exit(f"no such key: {args.name}")
        if args.reveal: print("WARNING: revealing a secret.", file=sys.stderr); print(v)
        else: print(mask(v))
        return
    if args.cmd == "remove":
        if not del_val(b, args.name): sys.exit(f"no such key: {args.name}")
        print(f"removed {args.name} from {b}"); return
    if args.cmd == "add":
        if not re.fullmatch(r"[A-Z0-9_]+", args.name): sys.exit("name must be UPPER_SNAKE, e.g. OPENAI_API_KEY")
        if args.from_env:
            v = os.environ.get(args.from_env)
            if not v: sys.exit(f"env var {args.from_env} is empty/unset")
        elif args.value is not None:
            print("WARNING: --value can leak via shell history; prefer --from-env or stdin.", file=sys.stderr); v = args.value
        else:
            v = getpass.getpass(f"{args.name} value (hidden): ")
        if not v.strip(): sys.exit("empty value")
        set_val(b, args.name, v.strip())
        print(f"saved {args.name} = {mask(v.strip())}  -> {b}" + ("" if b == "keyring" else f" ({FILE_STORE})"))
        return


if __name__ == "__main__":
    main()
