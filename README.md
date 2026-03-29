# blog-migration

Phase 2 content migration is now wired into the Ghost-to-Hugo scaffold.

## What this repo does now

- Builds a minimal in-repo Hugo site.
- Converts the captured Ghost export into Hugo content and static assets with a rerunnable migration script.
- Validates builds in GitHub Actions on pull requests and automatically publishes pushes to `source`.
- Uses the GitHub Pages user-site repository `cromica/cromica.github.io` as both the canonical Hugo source (`source`) and the published branch (`master`).

## Local commands

```bash
make migrate
make build
make serve
```

`make migrate` expects the local Phase 0 raw capture bundle under `migration-data/phase0/raw/`. Generated Markdown, aliases, reports, and extracted site images are checked into the repo so CI builds do not depend on those raw artifacts.

## Pinned Hugo version

- The repo pins Hugo in `.hugo-version`.
- Local `make build` and `make serve` fail fast if your installed Hugo version does not match the pinned version.
- `scripts/deploy-user-site.sh` reads the same `.hugo-version` file before it builds live output, so manual deploys cannot publish with a drifted local Hugo binary.
- CI installs the same pinned extended Hugo release, so local and GitHub Actions builds stay aligned.

## Deployment model

`cromica/cromica.github.io` is now the source of truth for the site:

- `source` stores the Hugo source.
- `master` stores the built site that GitHub Pages serves.
- Every push to `source` builds with the pinned Hugo version and pushes the generated output to `master`.
- The configured production host is `https://romuluscrisan.com/`.
