#!/usr/bin/env bash
# Build the production artifact exactly as CI does, then run the build validator.
#
#   scripts/build.sh                 # production artifact into ./public
#
# HUGO can point at a specific binary (CI pins 0.158.0; newer local versions print theme
# deprecation warnings that --panicOnWarning would turn into failures, so the flag is only
# added when the binary matches CI).
set -euo pipefail
cd "$(dirname "$0")/.."

HUGO_BIN="${HUGO:-hugo}"
CI_HUGO_VERSION="0.158.0"
BASE_URL="https://ryanorban.com/"
DEST="public"
CONFIG="hugo.toml"
VALIDATOR_ARGS=()

PANIC=()
if "$HUGO_BIN" version | grep -q "v${CI_HUGO_VERSION}"; then
  PANIC+=(--panicOnWarning)
else
  echo "note: $("$HUGO_BIN" version | head -1) != CI ${CI_HUGO_VERSION}; --panicOnWarning skipped" >&2
fi

HUGO_ENVIRONMENT=production TZ=America/Los_Angeles \
  "$HUGO_BIN" --cleanDestinationDir --minify "${PANIC[@]}" \
    --baseURL "$BASE_URL" --config "$CONFIG" --destination "$DEST"

python3 scripts/validate_site.py --public "$DEST" --url-manifest scripts/baselines/public-urls.txt "${VALIDATOR_ARGS[@]}"
