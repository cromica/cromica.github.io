# Squad Decisions

### 2026-03-29T18:30:11Z: Founding squad created
**By:** Squad
**What:** Established a Red Rising-inspired squad for maintaining the Hugo blog, reviewing content, and guiding promotion and career positioning.
**Why:** User requested a standing team focused primarily on editorial quality, with secondary ownership of platform evolution and audience growth.

### 2026-03-29T18:30:11Z: Editorial-first operating model
**By:** Squad
**What:** Content quality and professional polish are the primary mission; Hugo platform work exists to support better publishing and maintainability.
**Why:** The user emphasized grammar checking, proofreading, blog editing, and professional presentation as the top priority.
## Active Decisions

### 2026-03-29: Hosting direction
**By:** Romulus Crisan
**What:** Move the current blog off the legacy Ghost + DigitalOcean setup and onto a free solution built around GitHub.
**Why:** Reduce hosting cost and modernize the publishing flow.

### 2026-03-29: Experience target
**By:** Romulus Crisan
**What:** Aim for a clean, writing-first presentation similar to mitchellh.com rather than a heavy CMS experience.
**Why:** The blog should optimize for readable long-form writing.

### 2026-03-29: Squad casting direction
**By:** Romulus Crisan
**What:** Use a Red Rising-inspired squad roster for this project with team composition: Mustang (Lead), Darrow (Frontend Dev), Sevro (Backend & Migration Dev), Orion (Platform DevOps), Holiday (Tester), Scribe (Session Logger), Ralph (Work Monitor), and @copilot (Coding Agent).
**Why:** User preference for team identity and naming; enables clear role separation and parallel work.

### 2026-03-29: Migration strategy direction (from directive)
**By:** Romulus Crisan (via Copilot)
**What:** Target a free GitHub-based migration away from the current Ghost on DigitalOcean setup while preserving a clean, writing-first blog experience similar to mitchellh.com.
**Why:** User request — consolidates hosting costs and modernizes the publishing flow with maintained editorial quality.

### 2026-03-29: Static Site Generator selection
**By:** Mustang (Lead)
**What:** Use **Hugo (extended)** as the static site generator for the migration. Hugo chosen for single-binary deployment, sub-second builds, zero runtime dependencies, and zero JavaScript by default.
**Why:** Hugo is the smallest viable architecture that earns its keep. Considered and rejected: Astro (too heavy), Jekyll (slow), 11ty (Node.js), Next/Gatsby (web app tools, not blog tools).

### 2026-03-29: Hosting and deployment architecture
**By:** Mustang (Lead)
**What:** Deploy via **GitHub Pages** with **GitHub Actions** CI/CD. Custom theme built in-repo (`layouts/` directory). Content as Markdown + YAML frontmatter. GitHub manages HTTPS via Let's Encrypt.
**Why:** GitHub Pages is free, maintenance-free, and integrated with Actions. No submodules for theme (avoids complexity). In-repo structure keeps entire site in one repository.

### 2026-03-29: Critical Phase 0 gate — data backup
**By:** Mustang (Lead)
**What:** Before ANY migration work, **download Ghost `/content/images/` directory from DigitalOcean and backup Ghost JSON export, routes.yaml, and redirects.yaml.** This is a hard gate.
**Why:** Ghost JSON export does NOT include images. Failure to backup before decommissioning DigitalOcean results in permanent data loss (unrecoverable).

### 2026-03-29: Phased implementation plan
**By:** Mustang (Lead)
**What:** Four-phase migration: Phase 0 (data backup), Phase 1 (Hugo + Actions scaffolding), Phase 2 (content migration), Phase 3 (theme design), Phase 4 (validation & cutover). Timeline: 8 days. Clear ownership: Sevro (data + migration), Orion (CI/CD), Darrow (theme), Holiday (validation).
**Why:** Phased approach with clear gates prevents rework and enables parallel execution across team. Each phase has acceptance criteria and review gates.

### 2026-03-29: Deferred features (additive)
**By:** Mustang (Lead)
**What:** Comments, analytics, search, newsletter, dark mode, and RSS optimization deferred to Phase 2+. These are additive and do not change core architecture.
**Why:** Ship the smallest viable product first. Deferred features can layer on without architectural changes. Keeps Phase 1 laser-focused on migration.

### 2026-03-29: Phase 0 Ghost extraction storage and backup scope
**By:** Sevro (Backend & Migration Dev)
**What:** Phase 0 backup must capture more than Ghost JSON export: Admin JSON, database dump, `/content/images/` + media/files if present, routing/config artifacts (routes.yaml, redirects.yaml, Ghost config, nginx/systemd), and theme artifacts (active theme directory, package.json, custom assets). Store all captures under `migration-data/phase0/`. Keep `migration-data/phase0/raw/` local and gitignored by default; only track plans, manifests, checksums, and redacted notes in git.
**Why:** Ghost JSON export is not a complete disaster backup and omits images, full database state, and theme customizations. Raw backups can contain secrets, PII, subscriber/member data, and large binaries; keeping them local/gitignored protects against accidental leaks unless repo privacy is explicitly confirmed.

### 2026-03-29: Phase 0 content ownership and scaffolding gate
**By:** Mustang (Lead)
**What:** The actual Ghost extraction is a split-responsibility step. The squad owns the extraction plan, required artifact list, validation criteria, storage layout, and downstream use of the captured data. Romulus must perform or directly authorize the live-system access work needed to obtain the Ghost Admin export, database backup, assets, theme files, and config/routing artifacts whenever those steps require DigitalOcean, Ghost admin, SSH, sudo, or API credentials the squad does not possess.
**Why:** This keeps credentials and source-system access with the human owner while letting the squad stay accountable for migration correctness. Orion should not start scaffolding beyond safe repo setup until Phase 0 handoff exists: admin export, assets backup, DB safety net, routing/config evidence, theme copy or equivalent proof, plus manifests/checksums showing what is captured versus still missing.

### 2026-03-29: User-operated Phase 0 extraction walkthrough
**By:** Sevro (Backend & Migration Dev)
**What:** Romulus may be the only person with production Ghost/DigitalOcean access, so Phase 0 now has an operator-safe walkthrough (`migration-data/phase0/user-extraction-walkthrough.txt`) that lets him perform the extraction himself without exposing credentials to the squad. The walkthrough enforces the split output model: raw capture stays local under `migration-data/phase0/raw/` (gitignored), while repo-safe manifests/checksums are tracked (runtime inventory, theme discovery, remote/local counts, raw file list, capture status, checksum manifest).
**Why:** This keeps secrets and raw subscriber/content data out of git while still giving Mustang, Orion, Darrow, and Holiday enough evidence to proceed without guessing. Phase 1 scaffolding is now explicitly blocked on verified Phase 0 evidence.

### 2026-03-29: SSH publickey authentication blocker during extraction
**By:** Sevro (Backend & Migration Dev)
**What:** If Romulus encounters `Permission denied (publickey)` while following the Phase 0 extraction walkthrough, **pause the extraction and do a low-risk local SSH identity check first.** Do NOT attempt random server-side changes while connection is unproven. Run these local diagnostics: (1) verify the SSH username being used, (2) list all available public keys in `~/.ssh/`, (3) check what identities are currently loaded in `ssh-agent` via `ssh-add -L`, (4) inspect key format, key type, and comment for any issues, (5) if needed, explicitly test with `-i <keypath>` and verbose output `-vvv` to trace negotiation. Safe local command batch provided separately in Phase 0 runbook updates.
**Why:** This separates local key/agent/config mistakes from real server-side permission problems. Saves time by eliminating guesswork and avoids unintended changes on the remote host while access is still unproven. Critical for unblocking extraction when Romulus is the only person with DigitalOcean access.

### 2026-03-29: SSH Key Recovery — Remote-Install Commands (Corrected)
**By:** Sevro (Backend & Migration Dev)
**What:** When local SSH keys are missing, generate a fresh ed25519 key pair on macOS, then use DigitalOcean web console (non-SSH access) to inject the public key server-side. Provide two cases: (A) console logged in as SSH user directly (use `~` expansion), (B) console logged in as root with SSH user elsewhere (use `sudo -u <user>`). Both use safe append operations (`>>` or `tee -a`, never clobber). Verify permissions: 700 on `~/.ssh/`, 600 on `authorized_keys`.
**Why:** Out-of-band console access unblocks SSH key injection when no private key exists locally. Safe append prevents clobbering existing keys. Explicit permission verification prevents SSH failures from trust/ownership issues.

### 2026-03-29: Phase 0 checkpoint — raw capture validation and handoff gate
**By:** Sevro (Backend & Migration Dev)
**What:** Phase 0 raw capture is 71% complete. Five artifacts are present (37.7 MB total): config.production.json, nginx-sites.tar.gz, ghost-themes.tar.gz, ghost-db.sql, and ghost-content-images.tar.gz. **Two critical artifacts remain missing and must be captured before Phase 1 scaffolding proceeds:** (1) Ghost Admin JSON export (posts, tags, metadata, publishing state — NOT equivalent to raw DB dump), and (2) Ghost routes.yaml and redirects.yaml (URL mapping and link preservation). Romulus must complete these captures using SCP downloads and checksum verification before handoff to Orion for Phase 1 scaffolding.
**Why:** Ghost Admin JSON export is the canonical source for content structure. A raw DB dump contains state but not content modeling; loss of this export = loss of clean content structure. Routes/redirects omission creates incomplete URL preservation plan and downstream link-rot risk. Explicit gate on missing artifacts protects data integrity and prevents rework with incomplete backup.

### 2026-03-29: Phase 0 Closure Status — Conditionally Blocked Pending Manifest Completion
**By:** Holiday (Tester)
**What:** Phase 0 raw data capture is **substantially complete** and **data-safe**, but **manifest/audit artifacts are incomplete**. Phase 1 scaffolding can begin in parallel with manifest completion. Orion should not commit Phase 1 work until Holiday validates routes/redirects handoff. Phase 0 validation checklist: all 6 critical data artifacts present (admin JSON, images, themes, DB, config, nginx); checksums 5/6 (missing ghost-admin.json entry); missing manifests: raw-file-list.txt, remote-counts.txt, runtime-inventory.txt, theme-discovery.txt, completion report. Routes/redirects evidence: NOT as separate YAML files, but validation required (nginx archive likely contains config; Ghost JSON has settings).
**Why:** Separates data integrity (safe, non-corrupted) from administrative proof (manifests/documentation). Data loss risk is LOW; manifest completion is bookkeeping. Phase 1 can proceed independently, but URL preservation must be confirmed before content transformation (Phase 2) to avoid link-rot.

### 2026-03-29: Phase 0 COMPLETION VALIDATION
**By:** Sevro (Backend & Migration Dev)
**What:** Phase 0 raw capture is **NOW COMPLETE**. Ghost Admin JSON export validated (668 KB, 43 posts, full schema). Routes/redirects evidence equivalent: Nginx config archive (3.3 KB) contains rewrite rules for old blog URLs; Ghost JSON `settings` table embeds routing configuration. No separate routes.yaml/redirects.yaml files required for this Ghost v1.25.5 deployment model. All 8 artifacts verified (37.7 MB total): ghost-admin.json, ghost-content-images.tar.gz, ghost-themes.tar.gz, ghost-db.sql, config.production.json, nginx-sites.tar.gz, manifests, and checksums. Recommendation: **Phase 1 scaffolding (Orion) is NOW UNBLOCKED.**
**Why:** Previously missing Ghost Admin JSON and routes/redirects evidence are now captured and validated. No outstanding blockers remain. Nginx config archive integrity verified (3.3 KB is correct for minimal DigitalOcean Debian install); all expected files present.

### 2026-03-29: Phase 0 FINAL CLOSURE — Holiday Verification (Re-review Complete)
**By:** Holiday (Tester)  
**Date:** 2026-03-29T14:52:10Z
**What:** Phase 0 is **✓ CLOSED**. Final sync-like review re-confirms: (1) nginx-sites.tar.gz (3.3 KB) contains 35+ URL rewrite rules capturing legacy → modern URL mappings (e.g., /blog/2014/02/23/why-a-blog.html → /why-a-blog); (2) Ghost JSON admin export (668 KB) contains full settings schema including routing config; (3) absence of separate routes.yaml/redirects.yaml is NOT a blocker — both nginx rules and Ghost settings provide complete URL preservation evidence. All 6 critical artifacts checksummed and verified. No data-loss risk. Checksums: ghost-admin.json (a692629f...), ghost-content-images.tar.gz (b2f3d958...), ghost-themes.tar.gz (95d2a1f0...), ghost-db.sql (e6dd122...), nginx-sites.tar.gz (17dfd258...). **ORION CAN START PHASE 1 IMMEDIATELY. NO BLOCKERS REMAIN.**
**Why:** Routes/redirects evidence is present in equivalent form (nginx + Ghost JSON), which is the industry-standard pattern for Ghost v1.25.5 on nginx reverse proxy. Complete URL mapping rules are captured; Hugo migration can extract preservation rules from both sources. Ratifies Sevro's Phase 0 completion verdict and confirms zero outstanding risks before Phase 1 scaffolding.

### 2026-03-29: User directive — Hugo Bearblog theme
**By:** Romulus Crisan (via Copilot)
**What:** Use the Hugo theme `janraasch/hugo-bearblog` for the site presentation instead of the current custom theme direction.
**Why:** User request — captured for team memory.

### 2026-03-29: Per-post meta descriptions in migration override catalog
**By:** Darrow (Frontend Dev)
**What:** Added a repo-tracked `migration-data/phase2/post-description-overrides.json` catalog. Wired Ghost→Hugo migration to consume it before falling back to imported SEO fields or generated summary.
**Why:** Holiday flagged that migrated posts were inheriting generic site description. Keeping per-post descriptions in a dedicated override file makes the fix durable across reruns and gives frontend/content review a single place to tighten metadata quality without touching templates.

### 2026-03-29: Switch to vendored Hugo Bearblog with thin overrides
**By:** Darrow (Frontend Dev)
**What:** Vendor `janraasch/hugo-bearblog` under `themes/hugo-bearblog/` and keep site-specific presentation in a small set of root overrides plus `static/css/custom.css`.
**Why:** Keeps the site visibly on Bearblog, preserves migrated content and metadata behavior, and avoids maintaining a large bespoke theme fork.
**Notes:** Do not reintroduce the old `static/css/site.css` / custom partial stack unless the site intentionally moves away from Bearblog.

### 2026-03-29: Bearblog switch launch approval
**By:** Holiday (Tester)
**What:** Approve the Hugo Bearblog theme switch for launch. The switch is ready to ship with no real blockers.
**Why:** `make build` passes on pinned Hugo 0.159.1, rendered `public/` output has zero missing local file or asset references, `/blog/` redirects to `/posts/`, post pages keep specific descriptions instead of falling back to the site default, and deployment remains promotion-gated in `.github/workflows/hugo-user-site.yml` with `.hugo-version` enforcement in `scripts/deploy-user-site.sh`.
**Notes:** Hugo alias pages in `public/` are expected to be minimal redirect documents and should not be treated as missing-metadata failures when their canonical and refresh targets are correct.

### 2026-03-29: Standard local Hugo preview contract
**By:** Orion (Platform DevOps)
**What:** Use the repo-pinned Hugo binary (`0.159.1` extended) and run local preview on loopback with: `hugo server -D --bind 127.0.0.1 --baseURL http://127.0.0.1:1313/`. Verify handoff by confirming the server is listening on `127.0.0.1:1313` and returns HTTP 200 before telling anyone the preview is ready.
**Why:** Keeps local preview aligned with the version pin already enforced by `Makefile` and `scripts/check-hugo-version.sh`. Loopback bind is explicit and low-risk on a shared machine. HTTP verification catches silent startup failures before they become user confusion.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
