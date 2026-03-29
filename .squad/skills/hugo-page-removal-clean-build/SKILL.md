---
name: "hugo-page-removal-clean-build"
description: "Remove standalone Hugo pages without leaving stale navigation or orphaned rendered output behind"
domain: "frontend"
confidence: "high"
source: "earned"
tools:
  - name: "bash"
    description: "Run the existing Hugo build and verify stale output is gone from public/"
    when: "After removing a page or section from site content/config"
---

## Context
Use this when a Hugo site needs to retire a standalone page such as Contact, About, or another root-level utility page. The risky failure mode is not just a lingering nav link; deleted pages can remain in `public/` after a normal build if the destination directory is not cleaned.

## Patterns
- Delete the source content file from `content/` so Hugo stops rendering the page.
- Remove any corresponding `menu.main` entry from `hugo.toml` when the active theme reads navigation from Hugo menus.
- Set `cleanDestinationDir = true` in `hugo.toml` so a standard build removes orphaned rendered files from `public/`.
- Validate with the repo’s existing build command, then explicitly check that `public/<slug>/index.html` no longer exists.

## Examples
- In this repo, removing `content/contact.md` was not enough on its own because `public/contact/index.html` survived the first rebuild.
- Adding `cleanDestinationDir = true` to `hugo.toml` let the next `make build` remove the stale `/contact/` output without any extra cleanup step.
- `themes/hugo-blog-awesome/layouts/partials/header.html` renders navigation from `.Site.Menus.main`, so removing the `Contact` menu item from `hugo.toml` fully removed the header link.

## Anti-Patterns
- Deleting a page file but leaving its menu entry in config.
- Trusting a successful Hugo build as proof that removed pages disappeared from `public/`.
- Hardcoding cleanup into a one-off shell command instead of fixing the repo-level Hugo config.
