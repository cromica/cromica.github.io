# Project Context

- **Owner:** Romulus Crisan
- **Project:** blog-migration
- **Stack:** Legacy Ghost export, Markdown content, static site generator (TBD), GitHub Actions/Pages, custom domain
- **Created:** 2026-03-29

## Core Context

Platform and deployment owner for the blog migration squad.

## Learnings

- Phase 1 source-of-truth now lives in this repository as a minimal Hugo site; the publish target remains `cromica/cromica.github.io` branch `master`, while that repo's `source` branch is legacy Jekyll history.
- Key scaffold files: `hugo.toml`, `.github/workflows/hugo-user-site.yml`, `scripts/deploy-user-site.sh`, `layouts/_default/`, `content/`, and `static/.nojekyll`.
- Phase 1 defaults use `https://cromica.github.io/` and flat post permalinks (`/:slug/`) until custom-domain cutover and redirect verification are ready.
- The hosting target must be free and GitHub-centered.
- Deployment choices should support a personal blog, custom domain, and low maintenance overhead.
- Platform recommendations should leave room for a clean writing-first presentation.
- Local preview is expected to run against pinned `Hugo v0.159.1 extended`, enforced by `.hugo-version`, `Makefile`, and `scripts/check-hugo-version.sh`.
- Reliable local preview command path is `hugo server -D --bind 127.0.0.1 --baseURL http://127.0.0.1:1313/`; verify with an HTTP 200 on `http://127.0.0.1:1313/` before handing it back.
- Key local-preview files: `.hugo-version`, `Makefile`, `hugo.toml`, and `scripts/check-hugo-version.sh`.

## Phase 1 Scaffolding Gate (2026-03-29 15:35:09Z)

- **Status:** UNBLOCKED (as of 2026-03-29T14:52:10Z via Holiday re-review)
- **Phase 0 Closure:** All 6 critical artifacts verified with checksums. Routes/redirects evidence captured in nginx-sites.tar.gz (35+ rewrite rules) and Ghost JSON settings. No data-loss risk.
- **Holiday Final Verdict:** ✓ CLOSED — **Orion can start Phase 1 immediately. No blockers remain.**
- **Parallel work:** Darrow can begin theme customization; Holiday validates test case design
- **Next:** Orion proceeds with Hugo + GitHub Actions scaffolding. Phase 0 admin proof (manifests) can continue in parallel.

## Phase 1 Scaffolding Complete (2026-03-29 15:01:03Z)

- **Hugo scaffold:** Minimal site created in blog-migration with hugo.toml, make workflow (serve/build/clean), layouts/_default/ structure, content/ and static/ placeholders.
- **GitHub Actions pipeline:** .github/workflows/hugo-user-site.yml created for CI/CD build + deploy to cromica/cromica.github.io master branch.
- **Deploy script:** scripts/deploy-user-site.sh ready for local-to-remote artifact sync.
- **Validation:** ✓ Local Hugo build runs without errors, generates public/ correctly.
- **Repository strategy:** Aligned to Mustang's two-repository decision: blog-migration owns source and transformation; cromica/cromica.github.io owns final artifacts and deployment.
- **Defaults:** Base URL https://cromica.github.io/, flat permalinks /:slug/, theme in layouts/ (no submodule), GitHub Pages publishing from main.
- **Deferred:** GitHub Actions secrets wiring (token setup) for next manual step. Custom domain reintroduced after content validation.
- **Orchestration log created:** `.squad/orchestration-log/20260329-150103-orion.md`


## Token Setup & Deployment Strategy (2026-03-29 15:XX:XXZ)

- **PAGES_DEPLOY_TOKEN:** Personal Access Token (PAT) created for cross-repo GitHub Actions push to cromica/cromica.github.io.
- **Token scope:** `public_repo` + `repo:status` (minimum privileges for public-repo write).
- **Storage:** Secret stored in blog-migration repo settings (Settings → Secrets and variables → Actions).
- **Expiration:** 90 days (rotatable; rotate before expiry to maintain deployment continuity).
- **Deployment pattern:** Token passed to deploy script via `DEPLOY_TOKEN` environment variable; never logged or exposed in workflow output.
- **Next gate:** Deploy script (`scripts/deploy-user-site.sh`) must be tested end-to-end to confirm token is used correctly.

## GitHub Actions Verification Checklist Created (2026-03-29 15:XX:XXZ)

- **Document:** `.squad/decisions/inbox/orion-actions-verify.md` — comprehensive human checklist for workflow verification.
- **Coverage:** Secret storage and consumption (safe, no exposure), manual triggering, job monitoring, target repo verification, safe debugging, artifact verification, token rotation, and quick reference CLI commands.
- **Design principle:** All verification steps assume zero exposure of token value; uses commit history and GitHub UI to confirm deployment without inspecting secrets.
- **Scope:** Covers `hugo-user-site.yml` workflow building blog-migration and deploying to cromica/cromica.github.io master branch.
- **Safety:** Each debugging scenario includes common errors and fixes without requiring token value access.

## Local Preview Restart — Bearblog Version (2026-03-29 T16:59:40Z)

**Orion restarted local Hugo preview on the Bearblog version for immediate inspection.**

- **Assignment:** Restart local preview on Bear Blog version for immediate inspection.
- **Work completed:**
  - ✅ Stopped previous preview instance (if running)
  - ✅ Started `hugo server -D --bind 127.0.0.1 --baseURL http://127.0.0.1:1313/`
  - ✅ Verified server listening on `127.0.0.1:1313`
  - ✅ Confirmed HTTP 200 response from preview endpoint
  - ✅ Rendered content reflects Bearblog theme with thin overrides
  - ✅ Local preview synchronized with latest build output
  
- **Validation results:**
  - Hugo version: 0.159.1 extended (pinned) ✅
  - Bind address: 127.0.0.1:1313 ✅
  - HTTP status: 200 OK ✅
  - Base URL: http://127.0.0.1:1313/ ✅
  - Content: Reflects Bearblog switch with correct theme ✅
  
- **Decision:** Use repo-pinned Hugo binary (0.159.1 extended) and run local preview on loopback. Verify handoff by confirming HTTP 200 before announcement.
- **Rationale:** Keeps local preview aligned with version pin, avoids localhost conflicts on shared machines, HTTP verification catches silent failures.
  
- **Handoff status:** ✅ **PREVIEW READY**
  
- **Orchestration log:** `.squad/orchestration-log/2026-03-29T16-59-40Z-orion.md`
- **Decisions merged:** Orion local preview contract to `.squad/decisions.md`
- **Scribe:** Team history updated.
