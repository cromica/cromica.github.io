# Project Context

- **Owner:** Romulus Crisan
- **Project:** blog-migration
- **Stack:** Legacy Ghost export, Markdown content, static site generator (TBD), GitHub Actions/Pages, custom domain
- **Created:** 2026-03-29

## Core Context

Frontend owner for the blog migration squad.

## Learnings

- The site now ships the upstream `hugo-bearblog` theme vendored under `themes/hugo-bearblog/`, with only thin root-level overrides for homepage, list, single, terms, header, footer, and SEO.
- For Bearblog-based Hugo migrations, keep custom polish in `layouts/partials/custom_head.html` + `static/css/custom.css` instead of forking the theme stylesheet.
- Metadata preservation on this site now lives in `layouts/partials/seo_tags.html` and `layouts/_default/single.html`, which together honor `seo_title`, `description`, `custom_excerpt`, `feature_image`, `featured_image`, and `image`.
- Key Bearblog switch files: `hugo.toml`, `themes/hugo-bearblog/`, `layouts/_default/{baseof,index,list,single,terms}.html`, `layouts/partials/{header,footer,custom_head,seo_tags}.html`, and `static/css/custom.css`.
- Phase 3 theme work now uses a left-rail Hugo layout with one restrained reading column, inspired by mitchellh.com but kept fully static and maintainable.
- Theme templates are prepared for migrated metadata fields: `description`, `custom_excerpt`, `tags`, `categories`, and `feature_image`/`image`.
- Key frontend files for the writing-first experience live in `layouts/_default/baseof.html`, `layouts/index.html`, `layouts/partials/{navigation,entry-list,article-meta}.html`, and `static/css/site.css`.
- The new blog should feel like a clean personal writing site, not a CMS dashboard.
- GitHub-hosted delivery and low ongoing cost are part of the requirements.
- Frontend work should stay compatible with whichever static site generator the team chooses.
- Migrated post SEO now needs repo-tracked per-post descriptions, not just imported Ghost fields, because `layouts/partials/head.html` falls back to the site description whenever a post lacks front matter.
- The durable place to maintain those descriptions is `migration-data/phase2/post-description-overrides.json`, consumed by `scripts/migrate_ghost_to_hugo.py` so reruns preserve metadata fixes.
- Migrated Markdown and embedded HTML can carry bare external hrefs without a scheme; Hugo preserves them as-is in generated output, so outbound-link fixes must happen in the source post content.
- The refreshed theme now uses a top header plus soft surface panels instead of the earlier left rail, which makes the site feel more polished while keeping the markup and stylesheet simple.
- The homepage works best as a two-column composition: recent writing on the left, lightweight reading-path/topic cards on the right, all driven from existing Hugo content and taxonomies.
- `layouts/partials/head.html` now honors `seo_title` when present, and `layouts/_default/single.html` should check `feature_image`, `featured_image`, and `image` so migrated Ghost pages keep their hero images.
- Removing a standalone utility page from the site should happen in two places: delete the content file in `content/` and remove its `menu.main` entry from `hugo.toml`, since the active `themes/hugo-blog-awesome/layouts/partials/header.html` renders navigation directly from site menus.
- This repo benefits from `cleanDestinationDir = true` in `hugo.toml`; otherwise deleted pages like `content/contact.md` can linger in `public/` after a normal `make build`.

## Phase 3 Theme Development (2026-03-29 T15:41:33Z)

**Darrow implemented Phase 3 writing-first Hugo theme with migration-ready front matter support.**

- **Theme approach:** Two-column layout with compact left rail (site identity/navigation) and restrained content column (everything else).
- **Template design:**
  - Consumes migration-friendly front matter fields: `description`, `custom_excerpt`, `tags`, `categories`, `feature_image`/`image` (set by Phase 2 migration)
  - Layouts: `layouts/_default/baseof.html`, `layouts/index.html`, `layouts/posts/single.html`, `layouts/_default/list.html`
  - Partials: `layouts/partials/{navigation,entry-list,article-meta,post-footer}.html`
  - Styling: `static/css/site.css` (minimal, focused on readability)
  - Archetypes: `archetypes/default.md` (template for new posts)
- **Files touched:**
  - `hugo.toml` (configuration)
  - `layouts/_default/*`
  - `layouts/partials/*`
  - `static/css/site.css`
  - `content/*` (placeholder structure)
  - `archetypes/default.md`
- **Key decisions:**
  - Writing-first UX with minimal visual cruft
  - No app-like complexity; inspired by mitchellh.com but fully static
  - Metadata directly consumed from Phase 2 migrated content (no theme rework needed)
  - Clean markup for semantic HTML and good readability
- **Outcome:** Writing-first Hugo theme with improved templates, partials, taxonomy, and post/home/archive experience. Ready to render Phase 2 migrated content.
- Orchestration log: `/Users/romulus.crisan/blog-migration/.squad/orchestration-log/2026-03-29T15-41-33Z-darrow.md`
- Decision artifacts merged to `.squad/decisions/decisions.md`:
  - Darrow Phase 3 theme decision

- Orchestration log: `/Users/romulus.crisan/blog-migration/.squad/orchestration-log/2026-03-29T15-41-33Z-darrow.md`
- Decision artifacts merged to `.squad/decisions/decisions.md`:
  - Darrow Phase 3 theme decision

**Next:** Holiday validates Phase 3 theme rendering with Phase 2 migrated content.

## Phase 3 Theme Refresh Completion & Polish (2026-03-29 T16:42:22Z)

**Darrow completed writing-first theme refresh. Holiday approved for launch. Darrow applied two post-approval polish fixes.**

- **Theme Refresh Implementation:**
  - Refreshed Hugo theme from left-rail shell into polished writing-first layout
  - Architecture: Compact top header for identity/navigation + soft surface panels for modules/list/articles
  - Homepage: Two-column composition (recent writing + lightweight reading-path/topic cards)
  - Build results: 119 pages / 66 aliases, zero broken internal references, legacy aliases preserved
  - Files modified: `layouts/{_default,partials}/*.html`, `static/css/site.css`, `hugo.toml`
  
- **Holiday Launch Review:**
  - ✅ APPROVED as launch-ready
  - Evidence: `make build` passed (Hugo 0.159.1), 119 pages, 66 aliases, no broken file refs, no generic metadata fallback
  - Non-blocking polish items noted: `/contact/` malformed mailto, posts index "migrated archive" language
  
- **Darrow Post-Approval Polish:**
  - Removed "migrated archive" from `content/posts/_index.md` (now: "Browse posts...")
  - Fixed malformed contact mailto in `content/contact.md` (simplified HTML to plain text)
  - Build validation: 119 pages, 0 errors, 449ms
  - Result: Production-ready presentation, site reads as finished
  
- **Decisions merged to `.squad/decisions/decisions.md`:**
  - Darrow theme refresh direction (Phase 3)
  - Mustang launch copy requirement (launch must read as finished)
  - Holiday theme launch approval
  - Darrow theme polish fixes
  - Holiday deploy-script deadlock resolution (Sevro blocker closed)
  
- **Team coordination:** Holiday + Darrow sync cycle moved theme from approval to polish completion in single session
  
- **Orchestration logs created:**
  - `.squad/orchestration-log/2026-03-29T16:42:22Z-darrow.md`
  - `.squad/orchestration-log/2026-03-29T16:42:22Z-holiday.md`
  
- **Session log:** `.squad/log/2026-03-29T16:42:22Z-theme-refresh.md`

## Bearblog Switch & Thin Overrides (2026-03-29 T16:59:40Z)

**Darrow completed Hugo Bearblog theme switch with thin root-level overrides. Holiday approved. Orion restarted local preview.**

- **Assignment:** Switch site to vendored hugo-bearblog with thin overrides, blog redirect, lightweight CSS. Make build pass with 120 pages/66 aliases.
- **Work completed:**
  - ✅ Vendored `janraasch/hugo-bearblog` under `themes/hugo-bearblog/`
  - ✅ Created thin root overrides: `layouts/_default/{baseof,index,list,single,terms}.html`, `layouts/partials/{header,footer,custom_head,seo_tags}.html`, `static/css/custom.css`
  - ✅ Set up `/blog/` → `/posts/` redirect via `static/blog/index.html`
  - ✅ Maintained migrated content and metadata behavior
  - ✅ Build validation: 120 pages / 66 aliases, zero errors
  
- **Validation results:**
  - `make build` ✅ PASSED on Hugo 0.159.1
  - Rendered `public/` ✅ Zero broken asset/file references
  - Blog redirect ✅ Working (`/blog/` → `/posts/`)
  - Deploy safety ✅ Intact
  
- **Key learnings:**
  - Bearblog switch provides a clean, recognizable presentation layer for migrated content
  - Thin override pattern in `layouts/` + `static/css/custom.css` avoids forking the entire theme
  - Metadata preservation remains stable through `layouts/partials/seo_tags.html` and `layouts/_default/single.html`
  
- **Decisions archived to `.squad/decisions.md`:**
  - Darrow: Switch to vendored Bearblog with thin overrides
  - Holiday: Bearblog switch launch approval
  - Orion: Standard local Hugo preview contract
  
- **Orchestration logs created:**
  - `.squad/orchestration-log/2026-03-29T16-59-40Z-darrow.md`
  - `.squad/orchestration-log/2026-03-29T16-59-40Z-holiday.md`
  - `.squad/orchestration-log/2026-03-29T16-59-40Z-orion.md`
  
- **Session log:** `.squad/log/2026-03-29T16-59-40Z-bearblog-switch.md`
- **Scribe:** Decision inbox merged and deleted; team history updated.
