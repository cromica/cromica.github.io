# Squad Team

> Migrate romuluscrisan.com from legacy Ghost on DigitalOcean to a free GitHub-hosted, writing-first blog.

## Coordinator

| Name | Role | Notes |
|------|------|-------|
| Squad | Coordinator | Routes work, enforces handoffs and reviewer gates. |

## Members

| Name | Role | Charter | Status |
|------|------|---------|--------|
| Mustang | Lead | `.squad/agents/mustang/charter.md` | ✅ Active |
| Darrow | Frontend Dev | `.squad/agents/darrow/charter.md` | ✅ Active |
| Sevro | Backend & Migration Dev | `.squad/agents/sevro/charter.md` | ✅ Active |
| Orion | Platform DevOps | `.squad/agents/orion/charter.md` | ✅ Active |
| Holiday | Tester | `.squad/agents/holiday/charter.md` | ✅ Active |
| Scribe | Session Logger | `.squad/agents/scribe/charter.md` | 📋 Silent |
| Ralph | Work Monitor | — | 🔄 Monitor |

## Coding Agent

<!-- copilot-auto-assign: false -->

| Name | Role | Charter | Status |
|------|------|---------|--------|
| @copilot | Coding Agent | — | 🤖 Coding Agent |

### Capabilities

**🟢 Good fit — auto-route when enabled:**
- Bug fixes with clear reproduction steps
- Test coverage and isolated refactors
- Documentation cleanups and small content tooling
- Boilerplate setup once the stack is chosen

**🟡 Needs review — route to @copilot but flag for squad member PR review:**
- Medium implementation work with clear acceptance criteria
- Migration helpers once content schema is locked
- CI/CD wiring that follows established repo patterns

**🔴 Not suitable — route to squad member instead:**
- Platform choice and architecture decisions
- Experience design and content model design
- Security-sensitive domain and DNS decisions
- Work requiring cross-agent migration planning

## Project Context

- **Owner:** Romulus Crisan
- **Stack:** Legacy Ghost export, Markdown content, static site generator (TBD), GitHub Actions/Pages, custom domain
- **Description:** Migrate romuluscrisan.com to a free GitHub-based personal blog with a clean, Mitchell Hashimoto-style reading experience.
- **Project:** cromica.github.io (`source` branch)
- **Active Repo:** `cromica/cromica.github.io`
- **Created:** 2026-03-29
