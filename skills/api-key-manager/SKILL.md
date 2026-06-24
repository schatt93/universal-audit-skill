---
name: api-key-manager
description: Create, read, update, and delete model-vendor API keys for multi-model / multi-vendor agent work (e.g. the Universal Audit Ralph loop). Use whenever the user wants to add, set, store, list, rotate, or remove an API key for Anthropic, OpenAI, Gemini, xAI, DeepSeek, OpenRouter, or any model vendor, or to set up keys for multi-vendor sub-agents. Keys are kept in a git-ignored store (env file, mode 600) or environment variables — never in the repo, prompts, logs, or chat.
---

# API Key Manager

CRUD for the API keys that drive multi-vendor sub-agents. **Security-first:** keys live in a **git-ignored** env file (`~/.config/universal-audit/keys.env`, mode `600`) or in environment variables — never in the repo, a prompt, a log, a commit, or chat.

## Commands (`scripts/keyman.py`, Python 3, stdlib only)
- **Create / Update:** `python scripts/keyman.py add OPENAI_API_KEY --from-env TMP` (reads the value from env var `TMP`) — or omit `--from-env` to be prompted **hidden** via stdin. Avoid `--value` (it leaks to shell history).
- **Read (list):** `python scripts/keyman.py list` → names + **masked** values (`****last4`).
- **Read (one):** `python scripts/keyman.py get OPENAI_API_KEY` (masked; `--reveal` prints it, with a warning).
- **Delete:** `python scripts/keyman.py remove OPENAI_API_KEY`.
- **Path:** `python scripts/keyman.py path`.
- **Load into a shell** (no values printed): `eval "$(python scripts/keyman.py source-cmd)"` — then sub-agents read the keys from the environment.

## Provide a key safely (best → worst)
1. **An environment variable the agent already has** — nothing to store.
2. **This store, via stdin or `--from-env`** — persisted `600` + git-ignored.
3. **Pasting the raw key in chat — discouraged** (it lands in transcripts); if unavoidable, add it then **rotate** it.

## Conventions
Standard names so tools find them: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY` / `GOOGLE_API_KEY`, `XAI_API_KEY`, `DEEPSEEK_API_KEY`, `OPENROUTER_API_KEY`.

## Guarantees
- Store is `chmod 600`, its directory `700`, and **outside the repo** by default; the repo `.gitignore` also blocks `keys.env` / `*.env`.
- Values are never printed except `get --reveal`; `list` / `get` mask to the last 4 chars.
- Values are read from env / hidden stdin, **never from argv**.
- The Universal Audit **Ralph loop** (`ralph/multi-vendor-agents.md`) reads these keys from the environment to dispatch per-vendor sub-agents; a missing key simply skips that vendor.
