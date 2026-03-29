---
name: "static-site-finish-gate"
description: "How to decide whether a migrated static site is truly ready to hand back as finished"
domain: "testing"
confidence: "high"
source: "earned"
tools:
  - name: "bash"
    description: "Run the site build and scripted HTML checks"
    when: "When verifying launch readiness after a migration"
  - name: "rg"
    description: "Find stale migration copy and metadata gaps quickly"
    when: "When looking for unfinished-state text or missing front matter patterns"
---

## Context
Use this when a migrated Hugo or static site appears functionally complete and needs a final go/no-go decision. The dangerous failures at this stage are often not broken builds; they are quiet launch defects that only show up in production behavior, SEO metadata, or user-visible copy.

## Patterns
- Run a real build first, then validate the generated `public/` output rather than trusting source intent.
- Treat internal link integrity, asset existence, and redirect output as baseline checks, not proof of readiness.
- Distinguish real content pages from Hugo alias pages during metadata sweeps. Alias outputs are intentionally tiny redirect documents and will not carry full page SEO tags; only flag them if the redirect target itself is wrong or missing.
- Verify the live-publish path itself is gated. If a deploy helper can still push to production directly without an explicit promotion flag or guard, the migration is not safely finished.
- Search for stale phase-language across config, homepage copy, and empty-state templates. A site that tells readers “migration,” “Phase 2,” or “cutover remain” is not done, even if the code works.
- Check section `_index.md` content as part of the finish gate. Hugo list pages can still ship “imported archive” or “final theme later” language even after templates are cleaned up.
- Check rendered metadata, not just front matter. If posts without descriptions fall back to a generic site description, that is a launch blocker for a content migration.
- Spot-check utility pages such as About and Contact in rendered HTML, not just posts. Imported markdown that mixes headings with raw HTML links can survive the build but still emit malformed markup in `public/`, especially once output is minified to one line.

## Examples
- In this repo, `make build` succeeded and alias/link checks passed, but `scripts/deploy-user-site.sh` still exposed a direct publish path outside the workflow gate.
- `hugo.toml`, `content/_index.md`, `layouts/index.html`, and `layouts/_default/list.html` still contained migration-in-progress copy after the content import landed.
- `layouts/partials/head.html` rendered generic site-level descriptions on 40 post pages because the migrated post front matter in `content/posts/*.md` lacked `description`.
- `content/contact.md` built successfully, yet `/contact/` still rendered malformed nested mailto markup because imported inline HTML inside a heading was not caught by link existence scans.
- In this repo's Bearblog switch, `public/blog/2014/02/23/why-a-blog.html` and similar alias outputs were acceptable as minimal refresh redirects because their canonical and redirect targets resolved to valid live pages.

## Anti-Patterns
- Declaring victory because the site builds and the links resolve.
- Assuming a workflow gate is enough while a local helper can still publish live output directly.
- Letting fallback metadata hide missing per-post summaries across migrated content.
- Shipping placeholder or phase-language copy to production after the migration is supposed to be complete.
- Counting Hugo alias redirect pages as SEO failures just because they omit the full `<meta name="description">` set.
- Trusting repo-wide link crawls alone to catch malformed imported HTML on key utility pages.
