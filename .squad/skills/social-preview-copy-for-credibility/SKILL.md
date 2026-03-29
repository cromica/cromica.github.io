---
name: "social-preview-copy-for-credibility"
description: "Craft short-form social preview summaries that signal authority and credibility when posts are shared on LinkedIn, Slack, X (Twitter), and other social platforms."
domain: "marketing"
confidence: "high"
source: "earned"
---

## Context

When a post, page, or profile is shared on LinkedIn, Slack, or X, the platform extracts the `description` or `og:description` meta tag to show a preview. For principal-level professionals, generic descriptions ("I blog, create software and am an engineering leader") undermine authority. Custom social preview copy is a high-leverage credibility multiplier—especially for outreach to recruiters, peers, and thought leaders.

## Pattern

Social preview copy differs from website copy: it must **compress authority signals into 120–160 characters** while maintaining authentic voice.

### Three Rules

1. **Lead with specificity, not generality**
   - ❌ "I write about technology and leadership"
   - ✅ "Principal engineer building identity platforms at scale—50M+ users, federation architecture, team systems"

2. **Include quantified signal** (recruiter-signal-framing)
   - ❌ "Leadership and engineering expertise"
   - ✅ "Led multi-year platform modernization (9 teams, 50M+ users); building federation infrastructure for enterprise identity"
   - Why: Magnitude + context = credibility

3. **Mirror page purpose / audience intent**
   - For About page: executive-grade positioning (scale + current leverage)
   - For tech posts: specific insight or domain authority
   - For career/leadership posts: outcomes or philosophy grounded in action

### Character Budget

- **LinkedIn preview width:** 120–160 characters (title + description)
- **X/Twitter card:** ~200 characters total (title + description)
- **Slack unfurl:** Description + title + image (description visible in expanded mode)

Keep descriptions under 160 characters to ensure full visibility without truncation on most platforms.

## Examples

### About Page (Principal Positioning)
- ❌ Generic: "I blog, create software and am an engineering leader"
- ✅ Specific: "Principal Engineering Manager at Microsoft. Leading identity federation platforms, 50M+ user scale. Multi-year modernization, team systems, thought leadership."
- Why: Signals current role, domain, scale, and forward motion

### Tech Post (Domain Authority)
- Post: "How to upgrade your plugin to Trados Studio 2017"
- ❌ Fallback: "I blog, create software..."
- ✅ Post-specific: "Practical guide to upgrading Trados plugins—leveraging new APIs, maintaining backward compatibility, managing dependencies."
- Why: Reader immediately sees post solves their problem

### Leadership/Career Post (Outcome-Grounded)
- Post: "Code by the book"
- ❌ Fallback: "I blog, create software..."
- ✅ Post-specific: "The technical books that shaped my approach to clean code, architecture, and building high-performing teams."
- Why: Signals philosophy grounded in learning + systems thinking

### Platform Post (Insight-Driven)
- Post: "Why I choose GitHub Pages"
- ❌ Fallback: Generic site description
- ✅ Post-specific: "GitHub Pages: static hosting, markdown-first editing, free deployment, and complete control—why I migrated from traditional hosting."
- Why: Immediately positions value prop for sharing

## Components

### Site Description (Homepage + Fallback)
- **Purpose:** Default for all pages without custom description
- **Audience:** First-time visitors + undefined page contexts
- **Signal:** Principal-level role + domain + scale
- **Length:** ~120 chars
- **Template:** "[Role] at [Company] in [Domain]. [Current Initiative], [Scale Signal]. [One Leverage Signal]."
- **Example:** "Principal Engineering Manager at Microsoft in identity & security. Building federation platforms, 50M+ user scale. Multi-year modernization expertise."

### About Page Description
- **Purpose:** Executive positioning for recruiters/thought leaders discovering profile
- **Audience:** Career evaluation, speaking opportunities, collaboration
- **Signal:** Achievement + trajectory + current leverage
- **Length:** ~150 chars
- **Pattern:** Lead achievement → current initiative → forward motion

### Post Description (Individual Posts)
- **Purpose:** Drive clicks from social shares + search results
- **Audience:** Readers on LinkedIn/X/Slack + organic search
- **Signal:** Post-specific insight + domain relevance
- **Length:** ~120–140 chars (short enough to display fully on most platforms)
- **Pattern:** Specific outcome or insight (not generic role/bio)

## Anti-Patterns

❌ **Superlatives without specifics**
- "Amazing article on leadership" (every post says this)
- ✓ "How I scaled team velocity 3x through testing infrastructure"

❌ **Generic role restatement**
- "Writing about engineering leadership" (fallback behavior; wastes credibility)
- ✓ "Building high-performing teams: playbook from 50M+ user platform migrations"

❌ **Keyword stuffing for SEO**
- "identity security platform federation authentication" (sounds like spam)
- ✓ "Principal engineering lead building identity federation platforms at scale"

❌ **Modesty that undersells**
- "Thoughts on engineering" (sounds junior, not principal-level)
- ✓ "Architecture decisions from principal-level roles: federation, scale, team systems"

❌ **Mismatch between role and content**
- Tech post description: "I'm a principal engineer" (reader knows that; doesn't signal what post teaches)
- ✓ "Practical guide to [specific problem]: patterns from [scale context]"

## Implementation

### Storage
- **Site description:** `hugo.toml` params → applies to all pages by default
- **Per-page descriptions:** Frontmatter field (`description = "..."`) → overrides site default
- **Optional catalog:** `migration-data/phase2/post-description-overrides.json` for durable, rerunnable source of truth

### Verification
1. **`make build`** → Render site
2. **Grep public/ for og:description tags** → Confirm every page has a description (none should fallback to empty)
3. **Sample LinkedIn preview** → Share a URL, verify preview shows custom description, not generic fallback
4. **Check character count** → Descriptions under 160 chars stay visible on most platforms

## Applied Pattern

From credibility-audit sessions (2026-03-29):
- Current fallback description on 40+ posts masks post-specific value
- Site-level description undersells principal positioning when shared by executives
- Adding 10–15 custom post descriptions + one site description update = immediate credibility boost on social shares

## References

- `.squad/skills/recruiter-signal-framing/SKILL.md` — Scale/concurrency/leverage signal patterns
- `.squad/skills/executive-credibility-narratives/SKILL.md` — Achievement-anchored structure
- `.squad/skills/rerunnable-meta-description-overrides/SKILL.md` — Metadata durability patterns
- Theme template: `themes/hugo-blog-awesome/layouts/partials/meta/standard.html` (lines 12–26 define description fallback logic)

## Validation Checklist

Before considering social preview copy complete:

- [ ] Site description signals principal-level role + domain + current scale?
- [ ] About page description has achievement + trajectory + forward leverage?
- [ ] Top 10 posts have post-specific descriptions (not generic fallback)?
- [ ] All descriptions under 160 characters (preview visibility)?
- [ ] No superlatives; all signals backed by specifics?
- [ ] Voice matches author tone (authentic, not marketing-speak)?
- [ ] Recruiter/LinkedIn audience would immediately understand scope + value?
