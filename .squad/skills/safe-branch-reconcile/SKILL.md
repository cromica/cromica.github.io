---
name: "safe-branch-reconcile"
description: "Safely reconcile a dirty local branch with its remote counterpart while preserving local working-tree edits and append-only team state."
domain: "git"
confidence: "high"
source: "earned"
tools:
  - name: "git"
    description: "Fetch, stash, merge, restore, and validate local branch integration."
    when: "Use when local and remote both moved and the working tree must be preserved."
---

## Context
Use this pattern when a branch is both ahead of and behind its remote, and there are uncommitted local edits that must survive the integration. It is especially useful when append-only coordination files (histories, decisions, logs) are mixed with overlapping bootstrap or configuration files.

## Patterns
1. Create a safety ref before reconciliation (`git branch backup/...`).
2. Stash working-tree edits before integrating remote history.
3. Merge the remote branch locally when you need to preserve both histories.
4. For overlapping framework/bootstrap files, resolve conflicts in favor of the currently active local operating model if the user asked to preserve it.
5. Keep remote-only additions that are additive (templates, skills, scaffolding).
6. Commit the merge, then restore the stashed working tree and verify the preserved edits are back.
7. Validate the repo with `git status` plus the existing project build/test command.

## Examples
- `source` ahead/behind `origin/source` with local edits in `content/about.md` and `.squad/*.md`.
- Remote adds new `.squad/templates/` and `.squad/skills/` files while local work rewrites squad identity and appends new history entries.

## Anti-Patterns
- Pulling directly into a dirty working tree and hoping Git preserves everything automatically.
- Resolving append-only history/decision conflicts by deleting local entries.
- Discarding the local operating model in overlapping squad-definition files without checking which state is active for the current session.
