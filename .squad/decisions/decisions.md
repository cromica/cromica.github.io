# Decisions

## 2026-03-29: SSH Recovery — Remote Install (Phase 0 blocker resolution)
**By:** Mustang (Lead)
**Status:** RESOLVED
**Summary:** SSH auth blocker during Phase 0 asset capture was resolved by Romulus executing manual SCP commands from DigitalOcean. Remote system required password-based authentication due to key-pair misconfiguration. Resolved by re-issuing SCP commands with password prompt.

---

## 2026-03-29: Repository Strategy — blog-migration (Staging) vs. cromica.github.io (Live)
**Date:** 2026-03-29T16:10:00Z
**By:** Mustang (Lead)
**Status:** DECISION

### Problem
Should the new Hugo blog be scaffolded in the current `blog-migration` repository (private staging) and later migrated to `cromica.github.io` (public user-site), or should scaffolding happen directly in `cromica.github.io`?

### Context
- `blog-migration` (private): Contains Phase 0 Ghost backups, migration scripts, squad infrastructure. Migration-data/phase0/raw/ is gitignored and holds sensitive data (full database dump, config with credentials, subscriber/content data).
- `cromica.github.io` (public): GitHub Pages user-site repository. Currently Jekyll + Travis CI. Will be the final live blog destination.
- Phase 0 is complete; Phase 1 scaffolding (Orion) is unblocked and ready to start.

### Decision
**Adopt a two-repository strategy:**

1. **blog-migration remains the private staging & tooling repository:**
   - Phase 0 backups and gitignored raw artifacts stay here.
   - Migration scripts, content transformation logic, and Markdown output live here.
   - Sevro performs Ghost → Markdown transformation here in Phase 2.
   - Holiday validates content and routing here.

2. **cromica.github.io becomes the live site repository:**
   - Hugo scaffolding (config.yaml/hugo.toml, theme, layouts/, assets/) goes here.
   - GitHub Actions CI/CD deployment workflow goes here.
   - Final published content (posts/, static/) goes here after validation.
   - This is the public-facing, production repository.

3. **Handoff workflow:**
   - Sevro transforms Ghost → Markdown + YAML in blog-migration/content/posts/.
   - Holiday validates content, links, images, and SEO integrity using blog-migration.
   - Orion scaffolds Hugo + Actions in cromica.github.io (parallel with content work).
   - When Phase 2/3 is complete, Holiday syncs validated content to cromica.github.io/content/posts/.
   - Holiday verifies live deployment to cromica.github.io.

### Rationale
1. **Security:** Backups (database dumps, config files, full subscriber/content data) must not be exposed in a public repository. Keeping them in private blog-migration ensures no accidental leaks.
2. **Simplicity:** Scaffolding Hugo directly in the live target repo (cromica.github.io) avoids an extra merge/migration step that could introduce branch conflicts or content loss. Cleaner cut-over.
3. **Clear Separation:** Staging repo owns data, transformation, and validation logic. Live repo owns production deployment and public content. This mirrors standard CI/CD practice.
4. **Orion's Workflow:** Orion scaffolds once (in cromica.github.io) and does not need to port or replicate scaffolding from blog-migration.
5. **Project Intent:** "Deploy this blog as cromica.github.io" — the target is explicit. Direct scaffolding there accelerates the path to production.

### Guardrails for Orion (Phase 1 Scaffolding)
1. **Repository Target:** Scaffold Hugo + Actions in `cromica.github.io`, NOT in blog-migration.
2. **Content Placeholder:** Hugo config should expect content to live at `/content/posts/` and `/static/images/`. These will be populated in Phase 2/3.
3. **CI/CD Workflow:** GitHub Actions should deploy from `main` branch (or `hugo-source` branch if maintaining a build-source separation) to GitHub Pages.
4. **Theme Isolation:** Keep theme in `layouts/` (in-repo, not submodule) to maintain single-repository simplicity.
5. **DNS & Custom Domain:** Actions workflow should ensure GitHub Pages is configured for the custom domain (if applicable). Orion confirms this with Holiday before cutover.
6. **Branch Strategy:** Establish a clear strategy: either a single `main` branch (content + source together) or a split (e.g., `hugo-source` for source, Pages publishes from `/docs` or separate `gh-pages` branch). Document this in the Phase 1 scaffold.
7. **Secrets Management:** If Actions needs DigitalOcean or other external secrets during Phase 2 (for asset sync), use GitHub Actions secrets, not repo environment variables.
8. **No Backups in cromica.github.io:** Ensure migration-data/ and Phase 0 raw artifacts are NEVER committed to cromica.github.io. Keep them only in blog-migration.

### Next Steps
1. Orion begins Phase 1 scaffolding in cromica.github.io immediately.
2. Sevro begins Phase 2 content transformation in blog-migration (parallel).
3. Holiday validates both streams in Phase 3 (content + deployment).
4. Holiday performs final cutover and live verification in Phase 4.

---

## 2026-03-29: GitHub Pages User-Site Deployment Path (Orion — Phase 1)
**By:** Orion
**Status:** DECISION

### Decision
- Keep `blog-migration` as the Hugo source repository and deploy generated `public/` output into `cromica/cromica.github.io` branch `master`.
- Treat `cromica/cromica.github.io` branch `source` as legacy Jekyll-era source history, not the new source of truth.

### Rationale
A GitHub Pages user site can only publish from its own repository, so the lowest-maintenance split is: source here (blog-migration), published artifacts there (cromica/cromica.github.io master). This preserves the existing user-site repo, keeps deployment reversible, and avoids copying Hugo source into the artifact repo.

---

## 2026-03-29: Phase 1 Base URL and Permalink Defaults (Orion — Phase 1)
**By:** Orion
**Status:** DECISION

### Decision
- Phase 1 scaffolding targets `https://cromica.github.io/` as the production base URL.
- Sets Hugo post permalinks to `/:slug/`.

### Rationale
The target repo's custom-domain `CNAME` was intentionally removed and the captured legacy redirect evidence points toward flat slug destinations (for example `/why-a-blog`). This keeps the initial cutover cheap and reversible; a custom domain can be reintroduced as a separate cutover step once content and redirects are validated.

---

## 2026-03-29: User Directive — GitHub Blog Setup
**Timestamp:** 2026-03-29T15:01:03Z
**By:** Romulus Crisan (via Copilot)
**Status:** CAPTURED

### What
Set up the GitHub blog under repo https://github.com/cromica/cromica.github.io while Orion starts Phase 1 scaffolding.

### Why
User request — captured for team memory.

---

## 2026-03-29: Phase 1 Scaffold Review — Release-Safety Rejection
**Date:** 2026-03-29  
**By:** Holiday (Tester & Release Lead)  
**Status:** DECISION

### Verdict

Rejected the current Phase 1 scaffold for release readiness. Root cause: the GitHub Actions workflow auto-deployed every push to `main` directly into the live user-site repo's `master` branch without a promotion gate. Evidence shows scaffold output already replaced the published site with placeholder content before content migration was complete. Hugo build was not deterministic: CI installs an unpinned Ubuntu `hugo` package while local builds run a different version line.

### Recommendation

Keep the Hugo repo structure and cross-repo publish model, but require a safer promotion gate and deterministic Hugo pinning before approval. Mustang should revise the rejected artifact instead of Orion proceeding with Phase 1.

---

## 2026-03-29: Phase 1 Scaffold Revision — Manual Promotion & Pinned Hugo
**Date:** 2026-03-29  
**By:** Mustang (Lead)  
**Status:** DECISION

### What

Keep the two-repository Hugo → `cromica/cromica.github.io` deployment model, but remove automatic publish-on-push behavior. `main` now builds only; live publication requires an explicit manual workflow dispatch with `promote_to_pages=true` from `main`. Pin Hugo to `0.159.1` via a checked-in `.hugo-version`, and make both CI and local make targets enforce that exact extended release.

### Why

`cromica/cromica.github.io` is the live surface, so scaffold output must not auto-promote during Phase 1. A checked-in Hugo version is the smallest durable way to keep local and CI builds deterministic without inventing extra infrastructure.

---

## 2026-03-29: Phase 1 Final Release-Safety Revision — Deploy Helper Version Enforcement
**Date:** 2026-03-29  
**By:** Sevro (Backend & Migration Dev)  
**Status:** DECISION

### What

The live publish helper must enforce the same pinned `.hugo-version` as CI and local `make` targets. `scripts/deploy-user-site.sh` now resolves the repo root, reads `.hugo-version`, and runs `scripts/check-hugo-version.sh` before it builds or attempts any push to `cromica/cromica.github.io`.

### Why

Manual deploy helpers are still release paths. If they shell out to whatever local `hugo` happens to be installed, the scaffold is not actually deterministic and a reviewed CI build can diverge from what gets published live. The version gate must fire before token use and before any live artifact generation.

---

## 2026-03-29: Phase 2 Migration Path — Ghost Export to Hugo Content
**Date:** 2026-03-29  
**By:** Sevro (Backend & Migration Dev)  
**Status:** DECISION

### Decision

Use a **rerunnable checked-in migration pipeline** centered on `scripts/migrate_ghost_to_hugo.py`.

- Source of truth for content transformation: `migration-data/phase0/raw/ghost-admin.json`
- Source of truth for legacy redirects: `migration-data/phase0/raw/nginx-sites.tar.gz`
- Source of truth for migrated assets: `migration-data/phase0/raw/ghost-content-images.tar.gz`
- Output model:
  - Hugo Markdown content in `content/posts/*.md`
  - Root pages in `content/about.md` and `content/contact.md`
  - Tracked static assets in `static/images/`
  - Migration audit outputs in `migration-data/phase2/reports/`

### Why

The Phase 0 Ghost export uses Mobiledoc `card-markdown` for every post, which means we can preserve authored markdown/HTML directly instead of attempting lossy HTML-to-Markdown reconstruction. Parsing nginx rewrite rules into Hugo `aliases` preserves the legacy URL trail without introducing runtime redirect infrastructure.

### Constraints

- Reruns require the local Phase 0 raw bundle to still exist under `migration-data/phase0/raw/`.
- CI does **not** depend on raw artifacts because generated Markdown and extracted images are checked into the repo.
- If future manual edits are made to migrated posts, treat migration output as the editable source of truth or preserve edits elsewhere before rerunning.
- `static/blog/index.html` intentionally carries the old `/blog/` root redirect because Hugo aliases handle page URLs but not directory-level catchall.

---

## 2026-03-29: Phase 3 Theme Decision — Writing-First Two-Column Layout
**Date:** 2026-03-29  
**By:** Darrow (Theme & UX)  
**Status:** DECISION

### Decision

The Phase 3 Hugo theme should use a writing-first two-column layout with a compact left rail for site identity/navigation and a restrained content column for everything else. Templates should consume migration-friendly front matter fields (`description`, `custom_excerpt`, `tags`, `categories`, `feature_image`/`image`) so Phase 2 can drop content in without reworking the theme.

### Why

This keeps the experience close to the mitchellh.com inspiration without importing app-like complexity. It also lets Sevro's migrated content land cleanly using metadata Ghost already exposes.

### Files Touched

- `hugo.toml`
- `layouts/_default/*`
- `layouts/partials/*`
- `static/css/site.css`
- `content/*`
- `archetypes/default.md`

---

## 2026-03-29: Token Setup Decision — PAGES_DEPLOY_TOKEN
**Date:** 2026-03-29  
**Owner:** Orion (Platform DevOps)  
**Status:** DECISION

### Decision

A Personal Access Token (PAT) named `PAGES_DEPLOY_TOKEN` must be created by the repo owner (Romulus) and stored as a GitHub Actions secret in the `cromica/blog-migration` source repository.

### Configuration

| Aspect | Value |
|--------|-------|
| **Token Name** | `PAGES_DEPLOY_TOKEN` |
| **Scope** | `public_repo`, `repo:status` |
| **Expiration** | 90 days (rotatable) |
| **Storage** | GitHub Actions secret in `cromica/blog-migration` |
| **Deployment Target** | `cromica/cromica.github.io` (public repo) |
| **Minimum Privileges** | Write to public repos only; no private repo, admin, or workflow access |

### Rationale

- **Minimum-privilege design:** Token scopes are limited to public repository access, reducing blast radius if exposed.
- **Rotatable:** 90-day expiration forces periodic security review and token rotation.
- **Cross-repo capability:** Allows workflows in `blog-migration` to authenticate pushes to the separate `cromica.github.io` deployment target.
- **No secrets in code:** Token is environment-injected, never committed; workflow logs mask the token value.

### Implementation

1. Romulus generates PAT in GitHub → Developer Settings → Personal Access Tokens
2. Copies token and stores as `PAGES_DEPLOY_TOKEN` secret in `cromica/blog-migration` settings
3. Deploy script (`scripts/deploy-user-site.sh`) receives token via `DEPLOY_TOKEN` environment variable
4. GitHub Actions workflow passes secret safely: `${{ secrets.PAGES_DEPLOY_TOKEN }}`

### Verification

- Workflow runs without missing-secret errors
- Logs show deploy script execution but mask the token value
- Successful push to `cromica/cromica.github.io` master branch

### Next Steps

- Deploy script end-to-end test (local and CI)
- Token rotation scheduling (before 90-day expiration)

---

## 2026-03-29: GitHub Actions Workflow Verification Checklist
**Author:** Orion (Platform DevOps)  
**Date:** 2026-03-29  
**Status:** REFERENCE

### Executive Summary

Concrete, human-safe checklist for verifying the GitHub Actions workflow that builds Hugo and deploys to `cromica/cromica.github.io` **master** branch. Assumes `PAGES_DEPLOY_TOKEN` secret is already configured in blog-migration repo settings. No token exposure. Safe debugging for deploy failures.

### Workflow Overview

- **Trigger:** PR, push to main, or manual dispatch
- **Build:** Hugo builds in `ubuntu-latest`
- **Deploy:** After main branch push (not during PR), script pushes public/ artifacts to `cromica/cromica.github.io` **master**
- **Auth:** GitHub Token (PAT) stored as `PAGES_DEPLOY_TOKEN` secret; never logged
- **Deploy script:** `scripts/deploy-user-site.sh` orchestrates git clone, rsync, commit, push

### Verification Steps Summary

1. **Verify Secret is Stored** — `gh secret list --repo cromica/blog-migration | grep PAGES_DEPLOY_TOKEN`
2. **Manually Trigger** — `gh workflow run hugo-user-site.yml --repo cromica/blog-migration`
3. **Monitor Run** — Watch for checkmarks (passing) or red X (failing)
4. **Confirm Secret Consumption** — Check for "Deploy Hugo site from" commits in target repo
5. **Verify Target** — Confirm `TARGET_PAGES_REPO: cromica/cromica.github.io` and `TARGET_PAGES_BRANCH: master`
6. **Debug Failures** — Build issues: check Hugo syntax; Deploy issues: verify token scope/expiry
7. **Verify Output** — Check target repo contains HTML artifacts, not source files
8. **Live Test** — Visit `https://cromica.github.io/` — homepage loads, posts visible, no 404s
9. **Token Rotation** — 90-day expiry; rotate before expiration

### Quick Reference

```bash
gh workflow run hugo-user-site.yml --repo cromica/blog-migration
gh secret list --repo cromica/blog-migration | grep PAGES_DEPLOY_TOKEN
gh api repos/cromica/cromica.github.io/commits --query '.[0].commit.message'
open https://cromica.github.io/
```

For full step-by-step details, see `.squad/decisions/inbox/orion-actions-verify.md` (archived).

---

## 2026-03-29: Theme Refresh Direction (Darrow — Phase 3)
**By:** Darrow  
**Status:** DECISION

### Decision
Refresh the Hugo theme away from the earlier left-rail shell into a polished writing-first layout with:
- A compact top header for identity and navigation
- Soft surface panels for homepage modules, list pages, and articles
- A two-column homepage with recent writing plus lightweight reading-path/topic cards

### Why
The content already carries the site. The previous shell read as structurally correct but visually raw. Moving to a cleaner header and restrained panel system keeps the site lightweight while giving the writing stronger hierarchy and a more finished presentation.

### Files
- `layouts/_default/baseof.html`
- `layouts/index.html`
- `layouts/_default/list.html`
- `layouts/_default/single.html`
- `layouts/partials/{head,navigation,article-meta,entry-list}.html`
- `static/css/site.css`
- `hugo.toml`

---

## 2026-03-29: Launch Copy Must Read as Finished (Mustang — Phase 3 Review)
**By:** Mustang (Lead)  
**Status:** DECISION

### Decision
User-facing site copy should describe the blog as a live, finished publication rather than an in-progress migration. Clear migration-status language removal required from both templates and config (`hugo.toml`, `layouts/index.html`, `layouts/_default/list.html`) as well as section front matter that renders directly into list pages (`content/_index.md`, `content/posts/_index.md`).

### Why
A Hugo build can be functionally correct while still undermining launch readiness through copy that says "Phase 1," "migration," or "final theme." Readers judge the shipped experience, not the repo history, so finished-state review must cover rendered copy paths as well as build health.

---

## 2026-03-29: Theme Refresh Launch Review — Accepted with Polish Notes (Holiday — Phase 3 Approval)
**By:** Holiday (Tester)  
**Status:** DECISION

### Verdict
Launch review accepts the refreshed Hugo theme as ready to ship. Evidence: `make build` passed on pinned Hugo 0.159.1 and produced 119 pages / 66 aliases; rendered `public/` output showed zero broken internal file references, zero post pages falling back to generic site description, and preserved legacy aliases (e.g., `public/blog/2014/02/23/why-a-blog.html` → canonical URL).

### Non-Blocking Polish Notes
- `/contact/` renders malformed nested mailto markup (from imported content)
- Posts index meta description still uses phrase "migrated archive"

Neither issue materially undermines launch readiness.

---

## 2026-03-29: Theme Polish — Copy & Markup Fixes (Darrow — Post-Approval)
**By:** Darrow  
**Status:** DECISION

### Changes Applied
1. **Posts Index Copy** (`content/posts/_index.md`)
   - Before: "Browse the migrated archive of posts..."
   - After: "Browse posts..."
   - Rationale: Removed "migrated archive" language to present site as live, finished product

2. **Contact Page Markup** (`content/contact.md`)
   - Before: `### Email: <a href="mailto:cromica@gmail.com" target="_top">cromica@gmail.com</a>`
   - After: `### Email: cromica@gmail.com`
   - Rationale: Nested HTML anchor in Markdown header created malformed output; simplified to plain text

### Validation
Build completed successfully with `hugo --minify`:
- 119 pages generated
- 0 errors
- Total build time: 449ms

---

## 2026-03-29: Deploy-Script Reviewer Deadlock — RESOLVED (Holiday → Sevro Coordination)
**By:** Holiday (Tester & Release Lead)  
**Status:** DECISION

### Resolution
The Phase 1 deploy-script safety issue (requiring `.hugo-version` enforcement in `scripts/deploy-user-site.sh` before any build/push) has been **completed by Sevro**. No agent reassignment needed.

### Evidence
- `scripts/deploy-user-site.sh` now reads `.hugo-version`, calls `scripts/check-hugo-version.sh`, validates Hugo version before token use or artifact generation
- Uncommitted changes in working directory confirm version enforcement in place

### Outcome
- Deploy-script blocker is **RESOLVED**
- Phase 4 acceptance criteria now focus on two remaining user-visible blockers: (1) migration-state copy in `hugo.toml`, `content/_index.md`, `layouts/`, and (2) missing per-post `description` front matter on 40+ post pages
- Proceed with Phase 2/3/4 validation work without agent deadlock
