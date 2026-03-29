---
name: "hugo-local-preview"
description: "How to start and verify a persistent local Hugo preview with the repo's pinned version"
domain: "deployment"
confidence: "high"
source: "observed"
tools:
  - name: "bash"
    description: "Check the pinned Hugo version, launch the server, and verify HTTP readiness"
    when: "When a user wants a local preview URL that keeps running"
---

## Context
Use this when a Hugo site in this repository needs to be previewed locally for a human to visit in a browser. The important failure modes are version drift, binding to the wrong interface, and declaring success before the server actually answers HTTP requests.

## Patterns
- Read `.hugo-version` and honor the repository pin before starting the preview.
- Run the repo's existing guard (`scripts/check-hugo-version.sh`) instead of trusting `hugo version` by eye.
- Bind preview to `127.0.0.1` unless there is a clear requirement for LAN access; it is safer on shared machines and still easy for the local user to open.
- Prefer `http://127.0.0.1:1313/` as the explicit local URL when port 1313 is free.
- After launch, verify both socket state (`lsof ... LISTEN`) and an actual HTTP response (`curl -I`) before handing back the URL.
- If startup fails, report the exact remediation from the version check first; in this repo that usually means installing Hugo `0.159.1 extended`.

## Examples
- Guard check: `./scripts/check-hugo-version.sh 0.159.1`
- Preview launch: `hugo server -D --bind 127.0.0.1 --baseURL http://127.0.0.1:1313/`
- Readiness proof: `curl -I http://127.0.0.1:1313/` returns `HTTP/1.1 200 OK`

## Anti-Patterns
- Starting `hugo server` without checking the pinned version first.
- Binding to `0.0.0.0` by default on a shared laptop.
- Reporting a preview URL based only on process start output without checking the port and HTTP response.
