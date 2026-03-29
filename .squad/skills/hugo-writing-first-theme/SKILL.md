---
name: "hugo-writing-first-theme"
description: "A durable pattern for Hugo blogs that prioritize readable prose, obvious navigation, and migration-friendly metadata"
domain: "frontend"
confidence: "high"
source: "earned"
---

## Context

Use this when a Hugo blog needs a calm, personal-site presentation rather than a CMS-style homepage. It fits migrations especially well because the templates can honor imported summaries, tags, and feature images without adding JavaScript or build tooling.

## Patterns

- Use a simple two-column shell: a narrow left rail for identity/navigation and one restrained prose column for the content.
- If the content is strong but the presentation feels unfinished, swap the left rail for a compact top header and use subtle surface panels to create hierarchy without turning the site into a dashboard.
- Keep headings/navigation in sans-serif, body copy in serif, and lean on spacing plus hierarchy instead of decorative UI.
- Configure menus in `hugo.toml` instead of hardcoding links in templates.
- Support migration-friendly fields in templates: `description`, `custom_excerpt`, `tags`, `categories`, and `feature_image`/`image`.
- On single pages, also check `featured_image` so Ghost-era standalone pages keep their hero art after migration.
- Build reusable partials for navigation, post metadata, and entry lists so homepage, list pages, and single pages stay aligned.
- Add taxonomies early even if content is not imported yet; empty states are cheaper than theme rewrites.
- A good homepage split is: primary recent-writing column plus a narrow companion column for reading-path guidance and tag/topic navigation.

## Examples

- `layouts/_default/baseof.html` for the left-rail shell and footer.
- `layouts/partials/entry-list.html` for chronological archive rows with summaries and tags.
- `layouts/_default/single.html` for article presentation with optional feature image and metadata.
- `static/css/site.css` for a no-build, typography-first styling layer.
- `layouts/index.html` can stay lightweight while still feeling intentional by pairing a recent-post feature card with a secondary info column and small site stats.

## Anti-Patterns

- Recreating a marketing homepage with cards, panels, or dashboard chrome.
- Hardcoding nav links or post metadata rules that should come from Hugo config/front matter.
- Waiting until after migration to support tags/excerpts/images; that causes avoidable template churn.
- Adding JavaScript or CSS tooling when plain Hugo templates and one stylesheet are enough.
