# Roque History

## Seed Context
- User: Romulus Crisan
- Project: Hugo blog and publishing platform
- Focus: promotion, personal branding, and audience growth

## Learnings
- Initial team formed on 2026-03-29T18:30:11Z.
- **Current role mismatch**: About page reflects Trados/SDL (2019) as primary identity; doesn't surface Microsoft/identity focus. Major credibility gap for principal-level positioning.
- **Content orphaning**: 30+ technical posts (2011–2019) are undiscovered; no thematic organization or SEO clustering; homepage shows only 5 recent posts.
- **Audience capture gap**: No email signup, newsletter infrastructure, or subscriber path; relies entirely on organic discovery.
- **LinkedIn-to-site disconnect**: LinkedIn profile shows active hiring/thought leadership in identity/security; personal site has zero speaking/talks page or current-role positioning.
- **Metadata debt**: Homepage tagline generic; site description doesn't signal principal-level identity expertise; OG tags don't differentiate from 2019 status.
- **Key files**:
  - `/content/about.md` — requires major role/experience reordering
  - `/hugo.toml` — site-wide metadata
  - `/layouts/` — theme overrides (navbar, homepage hero, footer)
  - `/content/posts/` — 30+ blog posts, mostly pre-2020

## Session: Social Preview Metadata Audit (2026-03-29T20:22:00Z)
**Work:** Completed comprehensive audit of OpenGraph, Twitter Card, and social preview positioning across site.

**Findings:**
- **Theme infrastructure is complete**: Hugo blog-awesome theme includes full OG/Twitter templates + article schema
- **Critical gap 1 (Generic site description)**: Default "I blog, create software and am a engineering leader" masks principal-level positioning; every page without custom description falls back to this
- **Critical gap 2 (Missing per-post descriptions)**: Only 1 of 43 posts has custom description field; 40+ posts share generic fallback on LinkedIn/Slack preview
- **Critical gap 3 (No social images)**: Zero og:image/twitter:image tags on pages; theme supports it but no global ogimage in hugo.toml and posts lack image field
- **Critical gap 4 (Weak about page)**: About page inherits generic description instead of executive-grade positioning summary

**Recommended Phasing:**
- **Phase 1 (30 min):** Update hugo.toml: site description → principal positioning + add ogimage param + add About description frontmatter
- **Phase 2 (1–2 hrs):** Populate top 10 posts with post-description-overrides.json using recruiter-signal-framing + executive-credibility patterns (120–160 char summaries)
- **Phase 3 (optional):** Create branded 1200x630px OG image + populate featured_image on posts

**Decision Filed:** `.squad/decisions/inbox/roque-preview-copy.md` with implementation checklist, examples, and success metrics.

**Key Insight:** Social preview metadata is a *credibility multiplier* for principal-level positioning. Generic defaults neutralize the site's ability to signal authority when shared. Phase 1 is low-risk, high-payoff leverage point.

## Session: Growth & Outreach Review (2026-03-29T18:41:53Z)
**Work:** Completed personal brand repositioning audit with multi-phase roadmap.

**Recommended Direction:**
- **Phase 1:** Reposition About page as leadership trajectory (lead with Microsoft identity authority)
- **Phase 2:** Add Speaking/Talks page to surface domain authority and conference engagement
- **Phase 3:** Create Writing landing page with thematic organization (identity, architecture, leadership)
- **Phase 4:** Add email signup infrastructure for audience retention and recurring contact

**Why It Matters:**
- Current site positioning emphasizes Trados/SDL developer tooling (2011–2019) vs. current principal-level role
- Reposition signals principal-level identity/auth domain expertise for: hiring teams, industry peers, thought leaders, conference organizers
- Aligns personal site with active LinkedIn hiring/thought leadership profile

**Decision Filed:** `.squad/decisions.md` with multi-phase repositioning strategy.
**Status:** Awaiting user prioritization of About page + Writing page in editorial sprint.
