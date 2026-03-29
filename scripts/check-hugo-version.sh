#!/usr/bin/env bash
set -euo pipefail

expected_version="${1:?expected Hugo version is required}"

if ! command -v hugo >/dev/null 2>&1; then
  echo "hugo is required (expected ${expected_version})." >&2
  exit 1
fi

current_version="$(
  hugo version \
    | sed -nE 's/.*hugo v([0-9]+\.[0-9]+\.[0-9]+).*/\1/p'
)"

if [[ -z "${current_version}" ]]; then
  echo "Unable to determine installed Hugo version." >&2
  exit 1
fi

if [[ "${current_version}" != "${expected_version}" ]]; then
  echo "Hugo ${expected_version} is required; found ${current_version}." >&2
  echo "Install the pinned version locally before running make targets." >&2
  exit 1
fi

if [[ "$(hugo version)" != *"+extended"* ]]; then
  echo "Hugo ${expected_version} extended is required for this repo." >&2
  exit 1
fi
