---
name: "user-operated-extraction"
description: "How to structure safe, user-run production data extraction when the squad does not hold access"
domain: "migration-safety"
confidence: "high"
source: "observed"
---

## Context

Use this when a migration depends on production data but the user, not the squad, holds the real access. The goal is to let the user perform a safe capture without exposing secrets, while still returning enough evidence for downstream engineering work.

## Patterns

### Split outputs into two buckets

- **Local-only raw capture:** exports, DB dumps, binary assets, theme copies, config bundles, logs.
- **Repo-safe handoff artifacts:** manifests, counts, checksums, redacted runtime inventory, and a short operator status note.

### Block implementation on verified capture

- Treat scaffolding or migration coding as blocked until the capture exists and is verified.
- Require concrete validation: file existence, JSON parse, remote/local counts, checksum manifest, and spot checks.

### Give commands with placeholders, not hidden assumptions

- Use explicit variables for host, SSH user, app path, and optional credentials.
- Provide a UI fallback when API credentials may not exist.
- Tell the operator exactly when to stop and ask for help instead of improvising.

### Structure live runbooks for immediate execution

- Start with the terminal location and the minimum safe preflight only.
- Make the first concrete commands create the local backup workspace before touching the remote host.
- Present steps in execution order, not architecture order.
- After each step, tell the operator what file, count, or command output should confirm success.
- Add hard stop conditions wherever the operator could otherwise guess: wrong app path, unknown DB engine, missing sudo/read access, external object storage, or count mismatches.

### Call out failure modes early

- Unknown install paths
- Unknown DB engine
- Missing sudo/DB access
- External object storage/CDN masking asset completeness
- Live-site edits causing export/DB drift

## Examples

- Good: “Keep `migration-data/phase0/raw/` local and gitignored; hand back `runtime-inventory.txt`, `remote-counts.txt`, `capture-status.txt`, and `phase0-sha256.txt`.”
- Good: “If you cannot identify whether Ghost uses MySQL or SQLite, stop and ask for help.”
- Bad: “Just export Ghost and copy the images.”

## Anti-Patterns

- Asking the user to paste secrets into tracked files
- Treating a Ghost JSON export as a complete backup
- Moving to scaffolding before counts/checksums/spot checks exist
- Writing a walkthrough that hides the exact expected handoff bundle
