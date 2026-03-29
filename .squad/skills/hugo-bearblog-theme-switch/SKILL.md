---
name: "hugo-bearblog-theme-switch"
description: "Switch a Hugo site onto hugo-bearblog while preserving migrated content, metadata, and simple site-specific polish"
domain: "frontend"
confidence: "high"
source: "earned"
---

## Context

Use this when an existing Hugo blog should adopt `janraasch/hugo-bearblog` without throwing away migrated content structure, metadata fields, or GitHub Pages deployability.

## Patterns

- Vendor the upstream theme into `themes/hugo-bearblog/` so the site stays deployable without submodule setup.
- Set `theme = 'hugo-bearblog'` in `hugo.toml`, then keep only thin root-level overrides for the pages where content shape matters: home, list, single, terms, and a base template when page titles/SEO need custom rules.
- Put visual polish in `layouts/partials/custom_head.html` plus `static/css/custom.css`; let the upstream Bearblog stylesheet remain the base layer.
- Preserve migration metadata explicitly: support `seo_title`, `description`, `custom_excerpt`, and image fields `feature_image`, `featured_image`, `image` in the override templates.
- If the site needs a fallback social image, use a custom param like `params.socialImage` instead of `params.images` so you can control SEO tags without fighting Hugo's internal defaults.
- Keep archive URLs explicit. If the old site exposed `/blog/` but the Hugo section is `/posts/`, add a lightweight redirect in `static/blog/index.html`.

## Examples

- Config anchor: `hugo.toml`
- Theme vendor path: `themes/hugo-bearblog/`
- Thin overrides: `layouts/_default/{baseof,index,list,single,terms}.html`
- Theme-specific polish: `layouts/partials/{header,footer,custom_head,seo_tags}.html`
- CSS override layer: `static/css/custom.css`

## Anti-Patterns

- Leaving old in-repo layouts in place so they silently override Bearblog and make the theme switch fake.
- Forking the full Bearblog theme just to change spacing, typography, or header/footer copy.
- Depending on `params.images` for fallback social art when you also need custom per-page SEO rules.
- Deleting archive redirects during the theme switch and breaking legacy navigation paths.
