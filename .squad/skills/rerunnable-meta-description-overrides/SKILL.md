---
name: "rerunnable-meta-description-overrides"
description: "Keep per-page SEO descriptions durable when migrated content is regenerated from source exports"
domain: "frontend"
confidence: "high"
source: "earned"
---

## Context

Use this when a migration script can be rerun and imported posts or pages are missing usable meta descriptions. Template-level fallbacks keep the site valid, but they flatten every article into the same generic snippet and will fail content QA.

## Patterns

- Store curated description overrides in a repo-tracked data file instead of hand-editing generated Markdown.
- Make the migration script read overrides first, then imported SEO fields, then a generated summary as the last safety net.
- Normalize whitespace before writing descriptions so front matter stays clean and diffs stay readable.
- Add a post-generation coverage check that proves every migrated page now has a `description`.
- Keep section-list descriptions (`content/posts/_index.md`, etc.) explicit too, so archive pages do not inherit the site-wide fallback.

## Examples

- `migration-data/phase2/post-description-overrides.json` as the editable source of truth for article summaries.
- `scripts/migrate_ghost_to_hugo.py` loading curated overrides and falling back to `custom_excerpt`, `meta_description`, or a trimmed body summary.
- `make migrate && make build` followed by a coverage script that reports zero missing post descriptions.

## Anti-Patterns

- Hand-editing generated Markdown and expecting those fixes to survive the next migration run.
- Relying only on the site description in the `<head>` partial for imported posts.
- Leaving metadata quality checks to manual spot checks instead of validating coverage with a script.
