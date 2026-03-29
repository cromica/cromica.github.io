---
name: "github-pages-user-site-source-repo"
description: "How to keep Hugo source in one repo while publishing a GitHub Pages user site from another repo"
domain: "deployment"
confidence: "high"
source: "observed"
tools:
  - name: "github-mcp-server-list_branches"
    description: "Check legacy branch layout in the target Pages repo"
    when: "Before deciding which branch should receive built artifacts"
  - name: "github-mcp-server-get_file_contents"
    description: "Inspect whether the target repo is source-oriented or already stores built output"
    when: "When inheriting an old Jekyll or static-site repo"
---

## Context
Use this pattern when the source repository is not the GitHub Pages user-site repository, but the published site must still live in `username.github.io`.

## Patterns
- Keep the content/theme/build source in the working repository.
- Treat the `username.github.io` repo as a deployment artifact repository.
- Build locally or in CI, then push the generated site into the user-site repo's publish branch.
- If the target repo has a legacy source branch and a built-output branch, preserve the built-output branch for publishing and freeze the old source branch rather than mixing architectures.
- Default the initial base URL to the GitHub Pages hostname if the custom-domain state is uncertain or intentionally removed.
- Add an explicit promotion gate before wiring `push` on the source repo to the live publish branch. For migrations, use manual approval, a dedicated release branch, or a preview target until cutover is intentionally authorized.
- Pin the Hugo version used in CI (and prefer an explicit extended/non-extended choice) so "deterministic build" claims remain true across local and GitHub Actions runs.
- Use a checked-in version file such as `.hugo-version` as the single source of truth, then make both CI and local commands read from it. This avoids version drift between a package-manager install on one machine and an action-managed install in CI.
- Extend that same pinning rule to any manual deploy script that can build before pushing live artifacts; a deploy script that shells out to plain `hugo` reintroduces drift even if `make build` and CI are pinned.
- Make the deploy helper resolve the repository root and read `.hugo-version` itself before any auth, clone, or push logic. Release guards belong inside the live publish path, not only in README guidance or surrounding workflow steps.
- Make the promotion gate visible in the workflow interface itself (for example, `workflow_dispatch` + required boolean input), so approval is an intentional operator action rather than an implicit branch side effect.

## Examples
- `blog-migration` contains Hugo source and GitHub Actions.
- `cromica/cromica.github.io` receives generated files on branch `master`.
- Deployment uses a repo-scoped token in CI rather than relying on same-repo Pages actions, because user-site publishing cannot originate from another repository.

## Anti-Patterns
- Moving Hugo source into the user-site artifact repo just to satisfy Pages.
- Assuming the target repo default branch is the correct publish branch without checking its history.
- Reintroducing a `CNAME` during Phase 1 when domain cutover has not been explicitly validated.
- Auto-promoting scaffold or partial-migration output from `main` into `username.github.io` production on every push, because the user-site repo is the live surface, not a safe preview.
- Calling the build deterministic while CI pulls an unpinned distro `hugo` package that can drift from local development versions.
- Calling the build deterministic while a local deploy helper still runs plain `hugo` without checking the pinned version file first.
- Checking the pin only in earlier build steps while the actual live publish helper can still be launched directly from a shell with a different `hugo` on `PATH`.
- Relying on README instructions alone for release gating while the workflow still deploys automatically on `push`; if the workflow does not enforce the gate, the gate does not exist.
