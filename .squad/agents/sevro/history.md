# Project Context

- **Owner:** Romulus Crisan
- **Project:** blog-migration
- **Stack:** Legacy Ghost export, Markdown content, static site generator (TBD), GitHub Actions/Pages, custom domain
- **Created:** 2026-03-29

## Core Context

Migration and backend implementation owner for the blog migration squad.

## Learnings

- Romulus may need an operator-safe, step-by-step Ghost extraction walkthrough because production access may stay with him rather than the squad.
- User-facing extraction guide lives at `migration-data/phase0/user-extraction-walkthrough.txt` and defines the exact Phase 0 handoff bundle.
- Team should treat Phase 1 scaffolding as blocked on a verified user-run Phase 0 capture bundle: raw data stays local/gitignored, manifests and checksums come back in-repo.
- Source content currently lives in an old Ghost deployment on DigitalOcean.
- Migration work needs to preserve posts, metadata, assets, and any necessary redirects.
- The final publishing workflow should stay GitHub-native and low-cost.
- Phase 0 backup scope must include Ghost Admin JSON, a database dump, `/content/images/`, routing/config files, and theme artifacts; JSON export alone is not enough.
- Store Phase 0 captures under `migration-data/phase0/`, with raw backups kept local/gitignored and manifests/checksums tracked separately.
- Key handoff artifacts after Phase 0: `migration-data/phase0/manifests/runtime-inventory.txt`, `migration-data/phase0/manifests/theme-discovery.txt`, `migration-data/phase0/manifests/remote-counts.txt`, and `migration-data/phase0/checksums/phase0-sha256.txt`.
- Live extraction guidance for Romulus should start in repo root `/Users/romulus.crisan/blog-migration`, create the local Phase 0 workspace first, then move into runtime inventory, admin export, config capture, assets, themes, DB, and verification.
- The safest operator walkthrough format is blunt and sequential: terminal location, short preflight checklist, exact first commands, expected outputs after each step, and explicit stop conditions when install path, DB engine, permissions, or asset storage do not match expectations.
- When Romulus hits `Permission denied (publickey)` during live extraction, treat it as a local SSH auth blocker first: inspect available public keys, agent state, and the exact SSH user before touching server-side migration steps.
- If `ssh-add -L` says `The agent has no identities` and verbose SSH ends with `No more authentication methods to try`, the strongest default diagnosis is "no usable private key is loaded or being offered from this machine," not a migration-script issue.
- The local macOS account name shown in terminal output (for example `romulus.crisan`) does not by itself prove the remote SSH username is wrong; confirm the actual `ssh user@host` target separately before blaming a short username like `romi`.

## Core Context (Summarized from Phase 0 work)

**Phase 0 — Data Extraction Complete:**
- Ghost Admin JSON extracted (668 KB, 43 posts, full schema)
- Routes/redirects captured via nginx-sites.tar.gz (3.3 KB, 35+ rewrite rules)
- Images extracted from Ghost content (36 MB, 65 images)
- Database dump and config secured (663 KB DB, 611 B config)
- All artifacts verified with checksums; raw data local/gitignored, manifests tracked
- SSH recovery completed via DigitalOcean console and fresh keypair injection
- Operator-safe handoff model established: Romulus executes extraction, squad validates manifests

**Phase 1 — Release-Safety Scaffold Hardening (Complete):**
- Manual promotion gate implemented: deploy only on workflow_dispatch with promote_to_pages=true
- Hugo pinned to 0.159.1 via .hugo-version, enforced in CI and local make targets
- Deploy helper (scripts/deploy-user-site.sh) now enforces version gate before any live publish work
- All build-producing paths now deterministic (CI, local make, deploy script)
- Phase 1 scaffold release-ready

**Phase 2 — Content Migration (Complete):**
- Rerunnable migration pipeline: scripts/migrate_ghost_to_hugo.py
- 41 posts + pages migrated to Hugo Markdown in content/posts/
- 65 images normalized to static/images/, Ghost references cleaned
- 33 aliases parsed from nginx config for URL preservation
- Ghost Mobiledoc card-markdown preserved directly (no lossy HTML conversion)
- Root pages (about.md, contact.md) created
- Migration audit reports tracked in migration-data/phase2/reports/

## SSH Key Recovery (2026-03-29)

- When local key search fails during Phase 0 extraction, the operator needs out-of-band (DigitalOcean console) access to inject a fresh public key server-side.
- Safe recovery path: (1) generate fresh ed25519 keypair on macOS with `ssh-keygen -t ed25519 -f ~/.ssh/id_blog_migration -N "" -C "..."`, (2) gain console access to droplet, (3) create `.ssh` directory with correct perms (700), (4) append public key to `~/.ssh/authorized_keys` with safe `cat >>` (not clobber), (5) verify permissions (600 on file, 700 on dir, correct owner), (6) test from macOS with explicit `-i` flag and `-vvv` if needed, (7) record host/user/key in `~/.ssh/config` for convenience.
- Key principle: append, never overwrite; verify permissions after each step; test from macOS before resuming remote work.
- If SSH user is unknown, use console to list `/home/` or run `getent passwd | grep '/home'` to discover likely usernames.

## Ghost Discovery Runbook (2026-03-29)

- Created operator-safe SSH discovery walkthrough in `migration-data/phase0/ssh-ghost-discovery-runbook.md`.
- Runbook provides exact command sequence to locate Ghost install, config, content, database type, theme, and Nginx config.
- Each step includes success criteria, what to record, and hard-stop conditions for ambiguous cases.
- Final step compiles a runtime inventory block for the operator to paste back to the squad.
- Follows user-operated-extraction skill: read-only commands, explicit placeholders, clear handoff format.
- Safe for non-technical operators; enforces verification before proceeding to raw capture steps.
- Assumes SSH access already working and operator is on Ubuntu/DigitalOcean.

## Phase 0 Capture Runbook — Discovery Interpretation (2026-03-29)

**Discovery Input:**
- Ghost home: `/var/www/romuluscrisan.com/ghost`
- Content path confirmed with 66 images (~37 MB)
- Config: `/var/www/romuluscrisan.com/ghost/config.production.json`
- DB client: MySQL
- Service: systemd-managed
- Server: DigitalOcean Droplet, Nginx reverse-proxy to `127.0.0.1:2368`

**Key Constraint:** Database password was exposed in discovery chat. Must rotate post-extraction.

**Runbook Structure:**
- Preflight verification (read-only)
- Ghost admin JSON export (UI-first, filesystem fallback)
- MySQL dump or SQLite copy
- Config snapshot (with redacted version for repo)
- Image + content tarballs (two separate archives for safety)
- Theme bundle
- Nginx routing proof
- Manifests and checksums (repo-safe handoff)
- Verification and download steps

**Handoff Artifacts:**
- `manifests/raw-file-list.txt`
- `manifests/remote-counts.txt`
- `manifests/capture-status.txt`
- `manifests/phase0-sha256.txt`
- Raw captures under `raw/` (local/gitignored): ghost-admin.json or ghost-db-dump.sql, ghost-content-images.tar.gz, ghost-content-data.tar.gz, ghost-themes.tar.gz, ghost-config.json, nginx-site-config.txt

**Next Step:** Romulus executes the runbook; squad receives verified manifests and checksums before Phase 1 scaffolding.

## Phase 0 Validation Checkpoint (2026-03-29 T+N)

- User pasted Phase 0 raw-file-list.txt and phase0-sha256.txt showing 5 completed artifacts totaling ~37.7 MB
- **Verdict:** Capture is 71% complete (5 of 7 expected artifacts)
- **Missing:** Ghost Admin JSON export (master content record) and routes/redirects evidence
- **Risk:** Without Admin JSON, downstream content migration cannot map posts, tags, metadata, and publishing state. Without routes/redirects, URL preservation is incomplete.
- **Next action:** Romulus must capture Ghost Admin JSON via Ghost UI or filesystem fallback, plus routes.yaml/redirects.yaml before Phase 1 scaffolding proceeds
- Provided exact SCP download commands, manifest creation patterns, and checksum verification steps
- Emphasized that config.production.json must stay local-only and redacted inventory should replace it in tracked files
- Flagged nginx-sites.tar.gz as suspiciously small (4.0K); will require post-download inspection
- Recorded verification summary format for Romulus to paste back after Phase 0 completion

## Phase 0 Checkpoint Handoff Gate (2026-03-29 15:35:09Z)

- **Scribe recorded orchestration log and session checkpoint** documenting Phase 0 status as 71% complete with explicit blockers on Ghost Admin JSON export and routes/redirects
- **Merged decision to .squad/decisions.md:** Phase 0 checkpoint decision now in permanent record; Decision captured: Romulus must complete Ghost Admin JSON and routes/redirects captures using SCP downloads and checksum verification before Phase 1 scaffolding (Orion) proceeds
- **Phase 1 remains explicitly blocked** until Phase 0 evidence is complete
- **Parallel work paths:** Darrow can begin theme customization; Holiday can review validation plan
- **Risk recorded:** Ghost Admin JSON export is canonical content structure source; raw DB dump insufficient; routes/redirects omission = incomplete URL preservation
- **Operator-safe model:** Raw captures stay local/gitignored; repo tracks only manifests, checksums, and redacted notes

## Phase 0 COMPLETION VALIDATION (2026-03-29 Post-Checkpoint)

**Status: PHASE 0 NOW COMPLETE — UNBLOCKS PHASE 1**

- **Ghost Admin JSON export:** Present locally (668 KB, ghost-admin.json). Valid JSON, Ghost v1.25.5, contains 43 posts, all schema tables (posts, tags, users, settings, subscribers, posts_tags, posts_authors). Canonical content source verified.
- **Routes/Redirects evidence:** Not as separate YAML files, but **equivalent evidence captured** in two forms:
  1. Nginx config bundle (nginx-sites.tar.gz, 3.3 KB) contains rewrite rules showing old Jekyll → Ghost URL mapping
  2. Ghost JSON export `settings` table embeds routing configuration
  - Verdict: Acceptable for Ghost v1.25.5 deployment model (routing managed via Nginx proxy + DB settings, not separate YAML)
- **All artifacts verified:** 8 total files (37.7 MB): ghost-admin.json, images (36 MB), themes (92 KB), DB dump (663 KB), config (611 B), nginx archive (3.3 KB), checksums, plus config.production.json (local-only). All sizes reasonable, checksums validated.
- **nginx-sites.tar.gz size validation:** 3.3 KB is correct for Nginx text configs on minimal DigitalOcean Debian install; archive integrity verified (contains 10 expected files). Not a data loss issue.
- **No outstanding blockers:** All Phase 0 required artifacts now present and verified. Written decision to `.squad/decisions/inbox/sevro-phase0-validation.md` recommending Phase 1 (Orion) unblocked.
- **Key insight:** Routes/redirects in Ghost deployments may not be YAML-based standalone files; always check Nginx config and Ghost settings DB before assuming missing YAML = missing routing logic.
- **Operator-safe handoff confirmed:** Raw captures local (.gitignored), manifests/checksums tracked, no credentials/secrets in repo, evidence chain complete.

## Phase 0 Final Closure (2026-03-29 T14:52:10Z — Holiday Re-Review)

- **Ghost Admin JSON export:** Present, verified (668 KB, 43 posts, full schema). Canonical content source confirmed.
- **Routes/redirects evidence:** Complete via nginx-sites.tar.gz (3.3 KB, 35+ rewrite rules) + Ghost JSON settings table. No separate YAML files needed for Ghost v1.25.5 nginx deployment (industry-standard).
- **All 6 critical artifacts verified with checksums:** ghost-admin.json, ghost-content-images.tar.gz (36 MB), ghost-themes.tar.gz (92 KB), ghost-db.sql (663 KB), config.production.json (611 B), nginx-sites.tar.gz (3.3 KB).
- **Data integrity:** All checksums pass, all files non-zero, JSON valid.
- **Verdict:** ✓ CLOSED — Data-safe, no loss risk, no URL preservation gaps.
- **Recommendation:** Orion can start Phase 1 immediately. All blockers cleared.
- Orchestration log: `/Users/romulus.crisan/blog-migration/.squad/orchestration-log/2026-03-29T14-52-10Z-holiday.md`

- **Phase 1 release-safety revision (2026-03-29):** `scripts/deploy-user-site.sh` now resolves the repo root, reads `.hugo-version`, and runs `scripts/check-hugo-version.sh` before any live build/push work. That closes the last drift hole where a manual deploy helper could bypass the pinned Hugo used by CI and `make`.
- **Deployment-critical files:** `.hugo-version`, `scripts/check-hugo-version.sh`, `scripts/deploy-user-site.sh`, `.github/workflows/hugo-user-site.yml`, and `README.md`.
- **Validation pattern:** For release-sensitive scaffolds, prove both the happy path and the guardrail: run `make build` with the pinned binary, then simulate a wrong `hugo` earlier in `PATH` and verify the live deploy script aborts before touching token/publish logic.

- Phase 2 migration path now lives in `scripts/migrate_ghost_to_hugo.py`; it reads `migration-data/phase0/raw/ghost-admin.json`, rewrites Ghost image paths and old-domain links, parses nginx redirects from `migration-data/phase0/raw/nginx-sites.tar.gz`, and emits Hugo content plus alias metadata.
- Generated Hugo content now lives in `content/posts/*.md` plus `content/about.md` and `content/contact.md`; the migration report is tracked in `migration-data/phase2/reports/content-migration-report.json` and `content-migration-summary.txt`.
- Ghost Mobiledoc in this export is uniformly `card-markdown`; preserving that markdown/HTML payload is safer than re-deriving content from rendered HTML, and Hugo's `unsafe = true` setting is required for those legacy embeds/snippets.
- Legacy `/content/images/...` references are now normalized to tracked site assets under `static/images/`; 65 images were extracted from `migration-data/phase0/raw/ghost-content-images.tar.gz` for build-safe CI output.
- Redirect preservation is split: per-post Hugo `aliases` cover 33 historical Ghost/Jekyll URLs parsed from nginx config, while `static/blog/index.html` handles the legacy `/blog/` root redirect.

## Phase 1 Final Release-Safety Revision (2026-03-29 T15:41:33Z)

**Sevro closed final scaffold drift issue, implementing deploy helper version enforcement for Phase 1 readiness.**

- **Changes made:**
  - `scripts/deploy-user-site.sh` now resolves repo root, reads `.hugo-version`, and runs `scripts/check-hugo-version.sh` before any build/push.
  - Version gate fires before token use and before any live artifact generation.
  - Manual deploy helpers are now release-safe (deterministic like CI).
- **Outcome:** Deploy helper now enforces pinned `.hugo-version` before live publish. Phase 1 scaffold is release-ready.
- Orchestration log: `/Users/romulus.crisan/blog-migration/.squad/orchestration-log/2026-03-29T15-41-33Z-sevro.md`
- Decision artifacts merged to `.squad/decisions/decisions.md`:
  - Sevro Phase 1 final release-safety revision

## Phase 2 Content Migration — Ghost → Hugo (2026-03-29 T15:41:33Z, background)

**Sevro implemented Phase 2 content migration pipeline, converting Ghost export to Hugo-ready Markdown.**

- **Approach:** Rerunnable checked-in migration pipeline centered on `scripts/migrate_ghost_to_hugo.py`
- **Inputs:**
  - `migration-data/phase0/raw/ghost-admin.json` (668 KB, 43 posts)
  - `migration-data/phase0/raw/nginx-sites.tar.gz` (3.3 KB, 35+ rewrite rules)
  - `migration-data/phase0/raw/ghost-content-images.tar.gz` (36 MB)
- **Outputs:**
  - Hugo Markdown in `content/posts/*.md` (41 posts + pages)
  - Root pages: `content/about.md`, `content/contact.md`
  - Static assets in `static/images/` (65 images, cleaned of Ghost references)
  - Audit reports in `migration-data/phase2/reports/`
- **Key decisions:**
  - Preserve Ghost Mobiledoc `card-markdown` directly instead of lossy HTML-to-Markdown reconstruction
  - Parse nginx rewrite rules into Hugo `aliases` for URL preservation (33 aliases)
  - Normalize legacy image paths to tracked site assets
  - Use `static/blog/index.html` for legacy `/blog/` root redirect
- **Outcome:** Imported 41 posts + pages, 65 images, 33 aliases, cleaned Ghost image references. Content ready for Phase 3 theme integration.
- Orchestration log: `/Users/romulus.crisan/blog-migration/.squad/orchestration-log/2026-03-29T15-41-33Z-sevro.md`
- Decision artifacts merged to `.squad/decisions/decisions.md`:
  - Sevro Phase 2 migration path

**Next:** Darrow Phase 3 theme development; Holiday validation of Phase 2/3 integration.

- User preference reset for Phase 2 content: raw Ghost fidelity beats curated copy. Keep Bearblog theme work, but remove post-description rewrites, home/section marketing copy, and manual outbound-link cleanup if it was not required for Hugo mechanics.
- `scripts/migrate_ghost_to_hugo.py` now treats `custom_excerpt` / `meta_description` as the only valid migrated descriptions; it no longer synthesizes summaries or consumes `migration-data/phase2/post-description-overrides.json`.
- Minimal section scaffolding is acceptable when no raw Ghost source exists: `content/_index.md` now reflects Ghost site title/description only, and `content/posts/_index.md` is title-only.
- Raw-source verification path for this repo: rerun `python3 scripts/migrate_ghost_to_hugo.py`, inspect diffs in `content/`, then validate with `make build`.
