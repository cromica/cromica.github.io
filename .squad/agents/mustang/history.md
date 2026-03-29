# Mustang History

## Seed Context
- User: Romulus Crisan
- Project: Hugo blog and publishing platform
- Focus: editorial quality first, platform evolution second, brand and career impact always considered

## Learnings
- Initial team formed on 2026-03-29T18:30:11Z.
# Project Context

- **Owner:** Romulus Crisan
- **Project:** blog-migration
- **Stack:** Legacy Ghost export, Markdown content, static site generator (TBD), GitHub Actions/Pages, custom domain
- **Created:** 2026-03-29

## Core Context

Lead for the blog migration squad.

## Learnings

- The site is moving off an old Ghost deployment on DigitalOcean.
- The new target is a free solution centered on GitHub.
- The desired feel is clean and writing-first, similar to mitchellh.com.
- **Architecture decision (2026-03-29):** Hugo (extended) + GitHub Pages + GitHub Actions. Custom theme in-repo (not submodule). Content as Markdown + YAML frontmatter.
- **Why Hugo:** Single binary, zero npm dependencies, sub-second builds, zero JS by default. Smallest viable architecture. Beats Astro (too heavy), Jekyll (too slow), 11ty (still Node), Next/Gatsby (web app tools, not blog tools).
- **Critical risk:** Ghost JSON export does NOT include images. Must download `/content/images/` from DigitalOcean BEFORE decommissioning. This is a hard Phase 0 gate.
- **Ghost → Hugo migration:** Requires HTML-to-Markdown conversion (Turndown). Expect artifacts around code blocks, embeds, and Ghost cards. Budget manual cleanup time.
- **Slug preservation** is mandatory for SEO continuity.
- **Deferred features:** Comments, analytics, search, newsletter, dark mode. All additive — don't change the core architecture.
- **Theme lives in `layouts/`** — no git submodule. Extract only if reuse is needed later.
- **Repo structure:** `content/posts/`, `static/images/`, `layouts/`, `assets/css/`, `.github/workflows/deploy.yml`, `scripts/migrate-ghost.js`.
- **Squad routing:** Sevro owns data export + migration script. Orion owns CI/CD + DNS. Darrow owns Hugo theme. Holiday owns validation. @copilot can do boilerplate once stack is approved.
- **Decision file:** `.squad/decisions/inbox/mustang-migration-architecture.md`
- **Content ownership decision (2026-03-29):** Romulus owns any live Ghost/DigitalOcean extraction steps requiring credentials or privileged access; Sevro owns the capture plan, validation rules, manifests, and interpretation of the resulting artifacts. Orion's scaffolding should wait for the Phase 0 handoff package, not just verbal confirmation.
- **Go/no-go gate:** Before scaffolding depends on real content, require Phase 0 evidence in `migration-data/phase0/` including admin export, asset backup, DB safety net, routing/config artifacts, theme capture, and redacted manifests/checksums describing completeness and gaps.

### Repository Strategy (2026-03-29T16:10:00Z)

- **Phase 0 complete:** All Ghost backups secured in `migration-data/phase0/raw/` (gitignored): ghost-admin.json (668 KB), ghost-content-images.tar.gz (37.7 MB), ghost-themes.tar.gz, ghost-db.sql, nginx-sites.tar.gz, config.production.json.
- **Target repo exists:** cromica/cromica.github.io is a public GitHub Pages user-site repo. Currently Jekyll + Travis CI. Will be final destination.
- **Decision:** Two-repository strategy adopted.
  - **blog-migration (private):** Staging & tooling. Holds Phase 0 backups, migration scripts, content transformation logic (Ghost → Markdown). Sevro works here in Phase 2. Holiday validates here.
  - **cromica.github.io (public):** Live site. Receives Hugo scaffolding (Orion, Phase 1), theme, Actions workflow, and validated content (Holiday, Phase 4).
- **Why this strategy:** (1) Security: backups never exposed in public repo. (2) Simplicity: no extra merge step or rework for Orion. (3) Clarity: staging owns transformation; live owns production. (4) Intent: "Deploy this blog as cromica.github.io" — direct scaffolding accelerates path to production.
- **Guardrails for Orion:** Scaffold Hugo + Actions directly in cromica.github.io, not blog-migration. Content placeholders at `/content/posts/` and `/static/images/`. Use single `main` branch (or document split strategy if using build-source separation). Keep theme in `layouts/`, not submodule. Verify GitHub Pages is enabled and configured. Never commit Phase 0 backups or migration-data/ to cromica.github.io.
- **Handoff workflow:** Sevro transforms Ghost → Markdown in blog-migration. Holiday validates. Orion scaffolds Hugo + Actions in cromica.github.io (parallel). Holiday syncs validated content to cromica.github.io/content/posts/ when Phase 2/3 complete. Holiday verifies live deployment.

## Phase 0 Checkpoint Status (2026-03-29 15:35:09Z)

- **Phase 0 is 71% complete:** Romulus provided Phase 0 raw-file-list.txt and phase0-sha256.txt showing 5 captured artifacts (~37.7 MB): config.production.json, nginx-sites.tar.gz, ghost-themes.tar.gz, ghost-db.sql, ghost-content-images.tar.gz
- **Critical blockers remain:** Ghost Admin JSON export (canonical content structure, posts/tags/metadata) and routes/redirects (Ghost routes.yaml + redirects.yaml for URL preservation) must still be captured before Phase 1 proceeds
- **Phase 1 explicitly blocked** until Ghost Admin JSON and routes/redirects are provided; Orion cannot begin scaffolding; Darrow can proceed with theme design work in parallel
- **Scribe recorded:** Orchestration checkpoint (`.squad/orchestration-log/20260329-153509-sevro-phase0-checkpoint.md`), session log (`.squad/log/20260329-153509-phase0-checkpoint.md`), merged inbox decision to decisions.md
- **Next action:** Romulus executes final Phase 0 steps using provided SCP commands and checksum verification; returns admin export + routes evidence for squad handoff

## Repository Strategy Decision & Phase 1 Kickoff (2026-03-29 15:01:03Z)

- **Decision made:** Two-repository strategy approved. blog-migration remains private staging/tooling for Phase 0 backups and content transformation. cromica.github.io becomes live site for Hugo scaffolding, Actions, and deployment.
- **Rationale:** Security (no backups in public repo), simplicity (direct scaffolding in target avoids extra merge), clarity (staging owns transformation; live owns production), speed (intent is explicit: "deploy as cromica.github.io").
- **Guardrails for Orion:** Scaffold Hugo + Actions directly in cromica.github.io, not blog-migration. Keep theme in layouts/, no backups in public repo. Parallel work enabled: Sevro and Darrow unblocked. Holiday standing by for Phase 2/3 validation.
- **Orchestration log created:** `.squad/orchestration-log/20260329-150103-mustang.md`

- **Phase 1 scaffold revision (2026-03-29):** The live publish path must have an explicit promotion gate. `.github/workflows/hugo-user-site.yml` now builds on PR/push but only deploys on manual dispatch from `main` with `promote_to_pages=true`.
- **Deterministic Hugo pattern:** Pin Hugo in `.hugo-version` and enforce it in both CI and local `make` targets through `scripts/check-hugo-version.sh`. Avoid distro package installs in CI for release-sensitive scaffolds.
- **Deployment-critical files:** `.github/workflows/hugo-user-site.yml`, `.hugo-version`, `Makefile`, `scripts/check-hugo-version.sh`, and `README.md`.
- **Launch-copy gate (2026-03-29):** Finished-state review must clear migration-status language from both shared config/template copy and section front matter. In this repo, `hugo.toml`, `content/_index.md`, `content/posts/_index.md`, `layouts/index.html`, and `layouts/_default/list.html` together control whether the public site reads as launched or still mid-migration.

## Phase 1 Scaffold Revision Submission (2026-03-29 T15:41:33Z)

**Mustang revised Phase 1 scaffold after Holiday's first rejection, implementing manual promotion gate and pinned Hugo.**

- **Changes made:**
  - Added explicit manual promotion gate in `.github/workflows/hugo-user-site.yml`: deploy runs only on `workflow_dispatch` from `main` with `promote_to_pages=true`.
  - Pinned Hugo to `0.159.1` via checked-in `.hugo-version`.
  - Updated CI and local `make` targets to enforce pinned Hugo version via `scripts/check-hugo-version.sh`.
- **Outcome:** Manual promotion gate is now real; Hugo pinning in CI/local paths is real. Deploy helper (`scripts/deploy-user-site.sh`) does not yet enforce `.hugo-version`; this becomes Sevro's final Phase 1 issue.
- Orchestration log: `/Users/romulus.crisan/blog-migration/.squad/orchestration-log/2026-03-29T15-41-33Z-mustang.md`
- Decision artifacts merged to `.squad/decisions/decisions.md`:
  - Mustang Phase 1 scaffold revision

**Next:** Sevro implements deploy helper version enforcement (Phase 1 final revision).
