---
name: "project-conventions"
description: "Squad workflow and migration-safety conventions for this repository"
domain: "project-conventions"
confidence: "high"
source: "observed"
---

## Context

This repo is organized around squad coordination for a Ghost-to-GitHub blog migration. Work should respect squad decisions first, especially hard gates around data safety, and leave behind structured artifacts that other agents can use without reverse-engineering your session.

## Patterns

### Read squad context before acting

- Start with `.squad/decisions.md` for active direction.
- Read your agent history under `.squad/agents/<name>/history.md`.
- Read `.squad/identity/now.md` and `.squad/identity/wisdom.md` when present.
- If you make a team-relevant decision, write it to `.squad/decisions/inbox/<agent>-<slug>.md`.

### Error Handling

- Prefer explicit capture of failure modes over optimistic plans.
- For migration work, call out missing access, unknown install paths, version differences, and data-shape uncertainty instead of assuming the happy path.
- Treat Phase 0 backup completeness as a hard gate: if a source artifact is not captured, mark it explicitly as missing or blocked.

### Testing

- Validate with inventories, counts, checksums, and spot checks when code tests do not exist yet.
- Before declaring migration backup work complete, compare remote vs local counts and record checksum manifests.

### Code Style

- Favor blunt, operationally clear documentation over polished but vague prose.
- Use exact file paths and command patterns with placeholders when real credentials or hosts are not available.
- Keep raw sensitive data out of tracked files unless the team has explicitly approved it.

### File Structure

- `.squad/decisions.md` — active team decisions
- `.squad/decisions/inbox/` — proposed decisions for Scribe to merge
- `.squad/agents/<name>/history.md` — agent-specific persistent learnings
- `migration-data/phase0/` — Phase 0 capture planning, manifests, checksums, and local-only raw backup staging
- Keep raw migration captures under `migration-data/phase0/raw/` and treat them as local-only unless repo privacy is confirmed

## Examples

- Good: define `migration-data/phase0/manifests/runtime-inventory.txt` and `checksums/phase0-sha256.txt` as handoff outputs for other agents.
- Good: document both `redirects.yaml` and version-specific fallback paths when Ghost deployment details are unknown.
- Bad: saying "export Ghost and copy images" without recording counts, checksums, paths, or DB backup strategy.

## Anti-Patterns

- **Assuming Ghost JSON is the whole backup** — it is not; assets, DB state, and theme/config artifacts can be lost.
- **Committing raw backup data blindly** — risks leaking secrets, PII, and bulky binaries.
- **Skipping the squad paper trail** — if a decision matters to other agents, write the inbox note and update history.
