---
name: "hugo-social-preview-metadata"
description: "Emit consistent Open Graph and Twitter metadata for Hugo pages with durable summary and image fallbacks"
domain: "frontend"
confidence: "high"
source: "earned"
---

## Context

Use this when a Hugo site renders weak social previews because descriptions only come from sparse front matter or because multiple template layers emit conflicting Open Graph / Twitter tags.

## Patterns

- Put the social metadata contract behind root-level partial overrides so the active site, not the vendored theme, controls preview behavior.
- Resolve descriptions in a clear order: explicit `description`, page description/summary, cleaned body excerpt, then site description.
- Reuse page image fields already present in content (`featured_image`, `feature_image`, `image`) before falling back to a site-wide social image.
- When the fallback image lives in `assets/`, process it through Hugo into a 1200x630 image so home and older posts still share with a proper card shape.
- Override the theme head partial if necessary to remove duplicate internal Open Graph / Twitter template calls; one metadata source is safer than two competing ones.
- Keep section landing pages (`content/_index.md`, `content/posts/_index.md`) explicitly described so they do not inherit a weak global fallback.

## Examples

- Metadata helper: `layouts/partials/meta/resolved.html`
- Standard tags: `layouts/partials/meta/standard.html`
- Article tags + JSON-LD: `layouts/partials/meta/post.html`
- Head override to suppress duplicate social tags: `layouts/partials/head.html`
- Configured fallback art: `hugo.toml` with `params.socialImage = 'avatar.jpg'`

## Anti-Patterns

- Letting the theme partials and Hugo internal templates both emit Open Graph / Twitter tags with different values.
- Depending on site-wide description text for migrated posts that have no front matter summary.
- Using a portrait avatar directly as the final fallback URL when Hugo can generate a card-sized derivative from the same asset.
