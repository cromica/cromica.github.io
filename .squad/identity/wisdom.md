---
last_updated: 2026-03-29T11:26:36.525Z
---

# Team Wisdom

Reusable patterns and heuristics learned through work. NOT transcripts — each entry is a distilled, actionable insight.

## Patterns

<!-- Append entries below. Format: **Pattern:** description. **Context:** when it applies. -->

**Pattern:** Hard gates at data boundaries prevent unrecoverable loss. **Context:** When migrating away from external systems (Ghost on DigitalOcean), use a hard Phase 0 gate to backup all source data (JSON, images, configs) BEFORE proceeding with implementation. This is critical for legacy system migrations where data doesn't fully export (e.g., Ghost JSON omits images).

**Pattern:** Routes/redirects may be stored in reverse proxy config (nginx) or app-level YAML depending on Ghost version and deployment model. When separate YAML files are absent, check: (1) nginx site configs for rewrite rules, (2) Ghost JSON settings table for embedded routing. Both are legitimate evidence sources. This pattern is industry-standard for Ghost v1.x on nginx.

**Context:** When validating URL preservation during CMS migration, be explicit about where routing rules are stored before declaring a blocker. Ghost v1.25.5 uses nginx reverse proxy for URL mapping; v2.0+ may default to internal routes.yaml. Both are equivalent if captured in the backup.
