---
name: "ghost-to-hugo-rerunnable-migration"
description: "Preserve Ghost content by replaying Mobiledoc markdown, asset rewrites, and nginx redirects into Hugo content"
domain: "migration"
confidence: "high"
source: "earned"
---

## Context

Use this when a legacy Ghost archive has already been captured and the job is to turn it into checked-in Hugo content without depending on Ghost at build time.

## Patterns

- Prefer Ghost `mobiledoc` over rendered `html` when the export uses `card-markdown`; that keeps author-written markdown/HTML closer to the original source and avoids lossy re-conversion.
- When fidelity is the goal, migrate only source-authored metadata (`custom_excerpt`, `meta_description`, etc.) and delete override catalogs that inject curated copy on rerun.
- Rewrite `/content/images/...` references into tracked Hugo static assets (for example `static/images/...`) so CI builds do not need access to the raw archive.
- Parse redirect evidence from captured nginx config and project those mappings into Hugo `aliases` for individual posts; use a tiny static redirect page only for directory-level catchalls like `/blog/`.
- Emit a checked-in migration report with counts, unresolved-link inventory, and generated file list so later QA has something concrete to diff.
- Make reruns cheap: deterministic output paths, overwrite generated files in place, and clean stale generated posts only when they carry an explicit migration marker.
- For Hugo section pages that did not exist in Ghost, keep generated scaffolding minimal and derived from raw site settings only; do not invent marketing copy that will drift from source.

## Examples

- `scripts/migrate_ghost_to_hugo.py` in this repo reads `migration-data/phase0/raw/ghost-admin.json`, `ghost-content-images.tar.gz`, and `nginx-sites.tar.gz`, then emits `content/posts/*.md`, `content/about.md`, `content/contact.md`, `static/images/`, and `migration-data/phase2/reports/`.
- The same pipeline rewrites old `romuluscrisan.com` links and `/content/images/...` paths so Hugo output no longer references the retired Ghost install.

## Anti-Patterns

- Rebuilding posts from Ghost `html` when `mobiledoc` is available; that is extra damage for no gain.
- Preserving hand-edited copy in generated Markdown after the migration source of truth changes; those edits will either drift silently or get clobbered on rerun.
- Leaving image references pointed at `/content/images/` or the old production domain.
- Treating redirect capture as optional; content migration without alias coverage is just link rot with nicer templates.
- Depending on local raw artifacts during CI builds instead of checking in the transformed content and extracted assets.
