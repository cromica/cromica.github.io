# GitHub Actions Cross-Repo Deployment Verification

**Author:** Orion (Platform DevOps)  
**Pattern Type:** CI/CD verification checklist  
**Applies to:** GitHub Actions workflows that authenticate to external repositories using GitHub Tokens (PAT)  
**Cost Model:** Free (uses GitHub UI and CLI); no third-party services.  
**Maintenance Burden:** Low — verify checklist before each major deployment change or token rotation.

## Problem Statement

When deploying artifacts via GitHub Actions to an external repository (e.g., build output → GitHub Pages repo), teams need to verify:
1. The token is securely stored and not exposed in logs
2. The token is actually being used (consumed) by the workflow
3. Artifacts are being pushed to the intended target repo/branch
4. Failures can be debugged without exposing the token

Standard approaches often inspect logs directly (exposing secrets risk) or trust the process without verification. This pattern provides safe, verifiable steps.

## The Pattern

### Layer 1: Secret Storage Verification (No Token Exposure)
- Verify secret exists in repo settings via GitHub UI or `gh secret list`
- Confirm the secret name matches what the workflow expects
- Accept that GitHub intentionally hides the token value (this is correct behavior)

**Why:** Confirms baseline setup before testing deployment.

### Layer 2: Artifact Verification (Observable Output)
- Instead of inspecting logs, verify artifacts arrived in the target repository
- Check commit history in target repo for deploy commits with expected message format
- Example: `gh api repos/{owner}/{target-repo}/commits` to list recent deploys
- Example: Verify `public/` directory structure exists in target after workflow runs

**Why:** Artifact presence proves authentication + push succeeded without inspecting secrets.

### Layer 3: Safe Debugging (Failures Don't Require Token Access)
- Common failures: token expiry (401), wrong scope (403), target branch doesn't exist, wrong repo name
- Errors appear in workflow logs but only token-related info, not token value itself
- Fix escalation: rotate token, verify scope, check target repo exists — no token inspection needed

**Why:** Entire debugging workflow is safe; no logs are scrutinized that contain the token.

### Layer 4: Rotation Schedule + Monitoring
- Document token expiry date (GitHub shows it when created)
- Set calendar reminder to rotate before expiry (typically 90 days)
- Recognize early warning: workflow fails with `401 Unauthorized` on previously-working deployment
- Safe rotation: create new PAT, update secret, delete old token

**Why:** Prevents surprise production downtime from expired tokens.

## Implementation Checklist

### Setup (One-time)
- [ ] Create PAT in GitHub account settings (Developer settings → Personal access tokens → Tokens (classic))
- [ ] Select scopes: `public_repo` + `repo:status` (minimum for public-repo write)
- [ ] Note expiry date (default 90 days)
- [ ] Add secret to source repo: Settings → Secrets and variables → Actions → New repository secret
- [ ] Name the secret something memorable (e.g., `PAGES_DEPLOY_TOKEN`)
- [ ] Reference the secret name in workflow env or steps (e.g., `${{ secrets.PAGES_DEPLOY_TOKEN }}`)
- [ ] Deploy script consumes secret as environment variable (`$GH_TOKEN` or `$DEPLOY_TOKEN`)

### Verification (Before Each Major Deployment)
1. **Trigger workflow manually** (GitHub UI → Actions → workflow name → Run workflow)
2. **Monitor job steps** (look for green checkmarks on build/deploy steps)
3. **Check target repo commits** (not logs) for deploy commits with correct message format
4. **Verify artifacts** in target repo (e.g., `public/` folder, expected structure)
5. **Test live outcome** if applicable (visit deployed site, verify content)

### Debugging (If Deployment Fails)
1. **Inspect workflow logs** for error class (401, 403, git error, network error)
2. **Match error to common cause** (expiry, scope, branch doesn't exist, etc.)
3. **Fix and retry** (rotate token, update scope, create branch, etc.)
4. **Re-verify artifacts** in target repo to confirm fix

### Rotation (Before Token Expiry)
1. **Create new PAT** with same scopes
2. **Update secret** in source repo with new PAT value
3. **Test deployment** once to confirm new token works
4. **Delete old token** from GitHub account settings

## Common Failure Modes

| Error | Cause | Fix |
|-------|-------|-----|
| `401 Unauthorized` | Token expired or malformed | Rotate token; verify it's base64'd correctly |
| `403 Forbidden` | Token lacks required scope | Check token scopes in GitHub settings; rotate with correct scopes |
| `fatal: could not read Username` | Token not passed correctly to deploy script | Verify env var name matches deploy script (e.g., `GH_TOKEN` vs `DEPLOY_TOKEN`) |
| `fatal: unable to access 'https://...' Timeout` | Network/GitHub API issue or PAT not recognized | Retry deployment; if persistent, verify token is active (not revoked) |
| `error: src refspec main does not exist` | Target branch doesn't exist | Create target branch manually or update workflow to use existing branch |
| Deploy step skipped | Secret not found or named incorrectly | Verify secret exists and workflow uses exact name (case-sensitive) |

## Real Example: Blog Deployment

**Workflow:** `hugo-user-site.yml` in `cromica/blog-migration`  
**Target:** `cromica/cromica.github.io` on branch `master`  
**Secret:** `PAGES_DEPLOY_TOKEN` (PAT with `public_repo` + `repo:status`)  
**Deploy Script:** `scripts/deploy-user-site.sh` consumes `$GH_TOKEN`

**Verification Steps:**
1. Confirm secret `PAGES_DEPLOY_TOKEN` exists in `cromica/blog-migration` settings
2. Trigger workflow: `gh workflow run hugo-user-site.yml --repo cromica/blog-migration`
3. Wait for build-and-deploy job to complete (green checkmark expected on deploy step)
4. Check commits in target repo: `gh api repos/cromica/cromica.github.io/commits --query '.[0].commit.message'`
5. Look for message: `Deploy Hugo site from <sha>`
6. If found, workflow authenticated and pushed successfully ✓

## Operational Notes

- **Token Scope:** Always use minimum necessary (`public_repo` is usually enough for Pages deployment)
- **Log Scrubbing:** GitHub automatically redacts secret values in logs; you will NOT see the token value printed
- **Artifact-First Debugging:** Always check target repo first; logs are secondary
- **Automation:** Can write post-deploy test in workflow to verify artifacts exist (e.g., check that index.html exists in target)
- **Cost:** Free — uses GitHub's free Actions quota and API

## Reusable Commands

```bash
# Verify secret exists (name only, not value)
gh secret list --repo {source-repo} | grep {SECRET_NAME}

# List recent commits in target repo (proves deployment)
gh api repos/{owner}/{target-repo}/commits --query '.[0:5].{msg: commit.message, date: commit.author.date}'

# Trigger workflow
gh workflow run {workflow-file.yml} --repo {source-repo}

# Check workflow run status
gh run list --repo {source-repo} --workflow {workflow-file.yml} --limit 1

# Rotate secret (interactive)
gh secret set {SECRET_NAME} --repo {source-repo}
# Paste new token when prompted
```

## Related Decisions

- **Token Expiry:** 90 days; rotate before expiry to prevent deployment downtime
- **Scopes:** `public_repo` + `repo:status` for public-repo writes; adjust if deploying to private repo
- **Deploy Script Pattern:** Use environment variables for sensitive auth; never hardcode or log tokens
- **Target Repo Strategy:** Keep target repo separate from source (cleaner history, easier rollback)
