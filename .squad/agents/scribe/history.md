# Scribe History

## Seed Context
- User: Romulus Crisan
- Project: Hugo blog and publishing platform
- Focus: preserve decisions, routing context, and team continuity

## Learnings
- Initial team formed on 2026-03-29T18:30:11Z.
# Project Context

- **Owner:** Romulus Crisan
- **Project:** blog-migration
- **Stack:** Legacy Ghost export, Markdown content, static site generator (TBD), GitHub Actions/Pages, custom domain
- **Created:** 2026-03-29

## Core Context

Agent Scribe initialized for the blog migration squad.

## Recent Updates

📌 Team roster defined for the blog migration project on 2026-03-29

## Learnings

- **User preference:** Red Rising-inspired squad identity, team naming convention enables clear role recognition and team cohesion.
- **Target outcome:** Free GitHub-based blog with a writing-first feel similar to mitchellh.com — emphasizes readable long-form content over CMS features.
- **Architecture:** Static site generator (choice TBD by Mustang) + GitHub Pages/Actions + custom domain; replaces legacy Ghost on DigitalOcean.
- **Team structure:** Clear role separation (Lead, Frontend Dev, Backend & Migration Dev, Platform DevOps, Tester) enables safe parallelization and prevents rework.
- **Decision flow:** Agents write to `.squad/decisions/inbox/{name}-{slug}.md`; Scribe merges into `.squad/decisions.md` after work blocks.
- **Critical path:** Mustang's architecture decision (SSG choice + content schema) unblocks Darrow, Sevro, and Orion for parallel implementation.
- **Governance:** Issue triage flows through Mustang; @copilot is capability-gated (🟢/🟡/🔴); Scribe logs after substantial work.
- **Key files:** `.squad/team.md` (roster), `.squad/routing.md` (work type → agent), `.squad/decisions.md` (active decisions), agent charters define collaboration patterns.
- **Architecture approved (2026-03-29):** Hugo (extended) + GitHub Pages + GitHub Actions. Custom theme in-repo. Content as Markdown + YAML. No submodules. Smallest viable: single binary, sub-second builds, zero runtime dependencies.
- **Critical risk:** Ghost JSON does NOT include images. Phase 0 hard gate: backup `/content/images/` BEFORE decommissioning DigitalOcean. This is owned by Sevro and is unrecoverable if missed.
- **Phased ownership:** Phase 0 (Sevro), Phase 1 (Orion + Darrow), Phase 2 (Sevro + Mustang review), Phase 3 (Darrow), Phase 4 (Holiday + Orion + Mustang). Parallel execution enabled by clear gates.
- **Phased ownership:** Phase 0 (Sevro), Phase 1 (Orion + Darrow), Phase 2 (Sevro + Mustang review), Phase 3 (Darrow), Phase 4 (Holiday + Orion + Mustang). Parallel execution enabled by clear gates.
- **Deferred features:** Comments, analytics, search, newsletter, dark mode—all additive, don't change core architecture. Ship MVP first, layer on later.
- **Decision documentation pattern:** Scribe creates session logs (human-readable narrative) + orchestration logs (structured coordination state). Both merged into squad narrative after work blocks.
- **Phase 0 backup scope:** Sevro defined comprehensive extraction protocol covering Ghost JSON, database dump, `/content/images/`, routing/config artifacts, theme artifacts, and runtime metadata. Raw backups kept local/gitignored by default to protect against accidental secrets/PII leaks in version control.
- **Handoff artifact pattern:** Each downstream agent receives explicit structured outputs they need (manifests, checksums, discoverable file locations) rather than raw backup dumps. Orion needs runtime-inventory + redacted config; Darrow needs theme-discovery + raw/themes/; Holiday needs completion report + checksums.
- **Extraction validation:** Phase 0 completeness proven via manifests (runtime-inventory, theme-discovery, file counts), checksums (SHA-256), spot checks (parse JSON, inspect images, read routes.yaml, check theme package.json), and remote vs local count comparison.
- **Ghost migration risks:** Ghost JSON export is incomplete (no images, no full DB state); images/theme customizations are highest-risk omissions. Hard gate on Phase 0 backup completion before DigitalOcean decommissioning—data loss if missed is unrecoverable.
- **Team-relevant decisions:** Store under `.squad/decisions/inbox/{agent}-{slug}.md`; Scribe merges after session completion. Example: sevro-phase0-extraction.md merged to decisions.md.
- **User-operated extraction pattern (2026-03-29):** When production access is held only by the user (Romulus owns Ghost/DigitalOcean), split the work: user performs live-system extraction steps (credentials, SSH, sudo), squad provides extraction plan and validation rules. User returns verified manifests/checksums; raw data stays local/gitignored. Reusable skill: `.squad/skills/user-operated-extraction/SKILL.md`.
- **Content ownership resolution (2026-03-29):** Credentials and source-system access stay with Romulus. Mustang and squad stay accountable for extraction correctness via validation manifests and checksums. Orion waits for Phase 0 handoff (admin export, assets, DB, config/routing artifacts, manifests) before starting Phase 1 scaffolding. Explicit gate prevents premature scaffolding against incomplete data.
- **Phase 0 → Phase 1 gate (2026-03-29):** Phase 1 scaffolding is now blocked on concrete Phase 0 evidence: `raw/admin/*.json` (valid), counts match, checksums exist, spot checks pass, and operator confirms extraction complete. Eliminates risk of building against incomplete or unverified source data.


## Session Notes

- **2026-03-29 Squad Setup Session:** Merged copilot directive into decisions.md, created session log (`.squad/log/2026-03-29T12-20-squad-setup.md`), established orchestration framework. All agents initialized with proper charter context. Work ready for Mustang to lead architecture scoping.
- Cross-agent dependencies: Mustang → {Darrow, Sevro, Orion, Holiday}. Other agents can begin preparatory work in parallel while awaiting Mustang's direction.
- Casting state: Red Rising universe approved, 5 agents active (Mustang, Darrow, Sevro, Orion, Holiday) + 3 support (Scribe, Ralph, @copilot). Capacity: 12 agents within policy.
- **2026-03-29 Mustang Architecture Session:** Logged Mustang's migration architecture proposal. Created session log (`.squad/log/2026-03-29T13-30-mustang-architecture.md`) and orchestration log (`.squad/orchestration-log/2026-03-29T13-30-architecture.md`). Merged 7 architecture decisions into decisions.md. Squad ownership mapped across 4 phases with clear gates. Phase 0 (Sevro) now unblocked to begin data backup immediately.
- **2026-03-29 Sevro Phase 0 Extraction Session:** Logged Sevro's comprehensive Phase 0 Ghost extraction plan. Created session log (`.squad/log/2026-03-29T14-10-sevro-phase0-extraction.md`) and orchestration log (`.squad/orchestration-log/2026-03-29T14-10-sevro-phase0-extraction.md`). Merged Phase 0 backup scope decision into decisions.md. Documented handoff artifacts for Orion, Darrow, Holiday with explicit manifests and checksums. Phase 0 plan ready for execution once credentials provided.
- **2026-03-29 Content Ownership and Extraction Handoff Session:** Logged Mustang and Sevro's resolution of content ownership split (credentials stay with Romulus, squad owns extraction rules). Created session log (`.squad/log/2026-03-29T15-00-content-ownership-handoff.md`) and orchestration log (`.squad/orchestration-log/2026-03-29T15-00-content-ownership-handoff.md`). Merged two inbox decisions into decisions.md: Phase 0 content ownership gate and user-operated extraction walkthrough. Extracted reusable skill pattern for user-operated extraction (`.squad/skills/user-operated-extraction/SKILL.md`). Phase 1 scaffolding now has explicit verification gate: Phase 0 must return verified manifests/checksums before Orion begins work.
- **2026-03-29 SSH Publickey Auth Blocker Session:** Logged Sevro's diagnosis and safe local SSH troubleshooting runbook. Romulus hit `Permission denied (publickey)` during Phase 0 extraction, blocking all phases. Sevro provided 5-step diagnostic command batch (verify SSH target, list local keys, check ssh-agent state, inspect key metadata, verbose SSH test) for Romulus to execute locally without server access. Created session log (`.squad/log/2026-03-29T15-30-sevro-ssh-auth-blocker.md`) and orchestration log (`.squad/orchestration-log/2026-03-29T15-30-ssh-auth-blocker.md`). Merged SSH auth blocker decision into decisions.md. Extraction remains blocked pending Romulus's local key diagnosis feedback.
- **2026-03-29 Phase 0 Checkpoint Session (15:35:09Z):** Processed SPAWN MANIFEST from Sevro on Phase 0 raw capture validation. Romulus provided raw-file-list.txt and phase0-sha256.txt showing 5 artifacts (~37.7 MB) with checksums. Verdict: 71% complete; Ghost Admin JSON export and routes/redirects remain critical blockers. Created orchestration log (`.squad/orchestration-log/20260329-153509-sevro-phase0-checkpoint.md`) and session log (`.squad/log/20260329-153509-phase0-checkpoint.md`). Merged Phase 0 checkpoint decision to decisions.md. Updated Mustang/Orion/Sevro agent histories with explicit Phase 1 blocking status. Deleted merged inbox decision. Phase 1 remains blocked on verified Ghost Admin JSON + routes/redirects capture.
- **2026-03-29 Phase 0 Review and Validation Gate Session (14:47:18Z - SPAWN MANIFEST):** Parallel agent work: Sevro validated local Phase 0 capture completeness; Holiday reviewed Phase 0 gate and decided closure status. **Outcome:** Phase 0 data safe; Phase 1 unblocked pending 15-min admin proof work. Sevro: Ghost Admin JSON now present (668 KB, 43 posts); routes/redirects evidence captured (Nginx config + Ghost settings); all 8 artifacts verified (37.7 MB). Holiday: Data integrity ✓ SAFE; manifests ⚠ INCOMPLETE (5 admin files missing); closure CONDITIONALLY BLOCKED on manifest completion (estimated 15 min, no data re-capture). Created orchestration logs for both agents (`.squad/orchestration-log/2026-03-29T14-47-18Z-sevro.md`, `.squad/orchestration-log/2026-03-29T14-47-18Z-holiday.md`). Created session log (`.squad/log/2026-03-29T14-47-18Z-phase0-review.md`). **Scribe merged 13 decision inbox files into decisions.md** (consolidated Phase 0 validation, closure status, SSH key recovery, extraction guidance patterns, content ownership, etc.). Deleted all inbox files after merge (no overlaps/duplicates). Updated Sevro/Holiday agent histories with phase 0 outcomes. **Resolution:** Phase 1 scaffolding (Orion) NOW UNBLOCKED; Sevro/Holiday can complete admin proof (manifests) in parallel. Coordination state: Darrow can begin theme research, Holiday can begin validation plan design.