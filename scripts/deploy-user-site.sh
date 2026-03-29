#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if [[ ! -f "$repo_root/.hugo-version" ]]; then
  echo "Pinned Hugo version file is missing: $repo_root/.hugo-version" >&2
  exit 1
fi

expected_hugo_version="$(tr -d '[:space:]' < "$repo_root/.hugo-version")"
"$repo_root/scripts/check-hugo-version.sh" "$expected_hugo_version"

TARGET_PAGES_REPO="${TARGET_PAGES_REPO:-${GITHUB_REPOSITORY:-cromica/cromica.github.io}}"
TARGET_PAGES_BRANCH="${TARGET_PAGES_BRANCH:-master}"
HUGO_BASEURL="${HUGO_BASEURL:-https://romuluscrisan.com/}"
DEPLOY_SHA="${GITHUB_SHA:-$(git rev-parse --short HEAD)}"

if [[ -z "${GH_TOKEN:-}" ]]; then
  if command -v gh >/dev/null 2>&1; then
    GH_TOKEN="$(gh auth token)"
    export GH_TOKEN
  else
    echo "Set GH_TOKEN or authenticate with gh before deploying." >&2
    exit 1
  fi
fi

workdir="$(mktemp -d)"
cleanup() {
  rm -rf "$workdir"
}
trap cleanup EXIT

hugo --gc --minify --baseURL "$HUGO_BASEURL"

git clone --quiet --branch "$TARGET_PAGES_BRANCH" "https://x-access-token:${GH_TOKEN}@github.com/${TARGET_PAGES_REPO}.git" "$workdir/target"
rsync -a --delete --exclude '.git/' public/ "$workdir/target/"

cd "$workdir/target"
touch .nojekyll
git add -A

if git diff --cached --quiet; then
  echo "No deployment changes detected."
  exit 0
fi

git config user.name "${GIT_AUTHOR_NAME:-github-actions[bot]}"
git config user.email "${GIT_AUTHOR_EMAIL:-41898282+github-actions[bot]@users.noreply.github.com}"
git commit -m "Deploy Hugo site from ${DEPLOY_SHA}"
git push origin "HEAD:${TARGET_PAGES_BRANCH}"
