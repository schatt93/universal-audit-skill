---
name: api-key-manager
description: Create, read, update, and delete model-vendor API keys for multi-model / multi-vendor agent work (e.g. the Universal Audit Ralph loop). Use whenever the user wants to add, set, store, list, rotate, or remove an API key for Anthropic, OpenAI, Gemini, xAI, DeepSeek, OpenRouter, or any model vendor, or to set up keys for multi-vendor sub-agents. Keys are kept in the OS keyring (Keychain / Credential Manager / Secret Service) or a git-ignored env file — never in the repo, prompts, logs, or chat.
---

# API Key Manager

CRUD for the API keys that drive multi-vendor sub-agents. **Security-first** — keys live in the **OS keyring** or a **git-ignored** env file, never in the repo, a prompt, a log, a commit, or chat.

## Backends (most → least secure)
- **`keyring`** *(preferred)* — the **OS keyring**: macOS **Keychain**, Windows **Credential Manager**, Linux **Secret Service / KWallet** — via `pip install keyring`. Secrets are stored encrypted by the OS; only a non-secret **index of key names** (`~/.config/universal-audit/keyring-index.json`) is kept locally so `list` / `remove` can enumerate.
- **`file`** *(fallback)* — a git-ignored env file (`~/.config/universal-audit/keys.env`, mode `600`).
- **`auto`** *(default)* — keyring if a usable OS backend is present, else file.

Show the active backend: `python scripts/keyman.py backend`.

## Commands (`scripts/keyman.py`, Python 3; `keyring` only for the keyring backend)
- **Create / Update:** `keyman add OPENAI_API_KEY --from-env TMP` (reads from env var `TMP`) — or omit `--from-env` for a **hidden stdin** prompt. Avoid `--value` (shell-history leak).
- **Read (list):** `keyman list` → names + **masked** values (`****last4`).
- **Read (one):** `keyman get OPENAI_API_KEY` (masked; `--reveal` prints it, with a warning).
- **Delete:** `keyman remove OPENAI_API_KEY`.
- **Pick backend:** add `--backend keyring|file|auto` to any command.
- **Load into a shell** (so sub-agents can read the keys): keyring → `eval "$(python scripts/keyman.py export-env)"`; file → `eval "$(... source-cmd)"` (sources the 600 file without printing values). Either way the agent's visible output shows no secrets.

## Provide a key safely (best → worst)
1. **OS keyring** via `keyman add` (hidden prompt) — encrypted at rest by the OS.
2. **An env var the agent already has** — nothing to store.
3. **The git-ignored file store** — `600`, never committed.
4. **Pasting a raw key in chat — discouraged** (it lands in transcripts); if unavoidable, add it then **rotate**.

## Conventions
Standard names so tools find them: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY` / `GOOGLE_API_KEY`, `XAI_API_KEY`, `DEEPSEEK_API_KEY`, `OPENROUTER_API_KEY`.

## Guarantees
- Keyring secrets are held by the OS; the file store is `600`, its directory `700`, **outside the repo**; `.gitignore` also blocks `keys.env` / `*.env` / `*.key`.
- Values are read from env / hidden stdin, **never argv**; printed only via `get --reveal`; `list` / `get` mask to the last 4 chars.
- The Ralph loop (`../../ralph/multi-vendor-agents.md`) reads keys from the environment to dispatch per-vendor sub-agents; a missing key simply skips that vendor.
