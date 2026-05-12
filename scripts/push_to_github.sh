#!/usr/bin/env bash
# push_to_github.sh — commit today's (or a specified day's) solutions and push.
#
# Usage:
#   ./push_to_github.sh                 # today
#   ./push_to_github.sh 2026-05-12      # a specific day
#
# Assumes:
#   - this folder is inside a git working tree connected to a GitHub remote
#   - `git push` works non-interactively (SSH key or stored credential)

set -euo pipefail

DAY="${1:-$(date +%F)}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ ! -d ".git" ]]; then
    # Find the closest parent that is a git repo.
    if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
        echo "ERROR: $ROOT is not inside a git repository." >&2
        echo "       Initialize a repo (or move this folder into your clone) before pushing." >&2
        exit 1
    fi
fi

# 1. Make sure today's pick has been generated. If it has, this is a no-op
#    because questions.json was already mutated and the solutions/DAY dir exists.
if [[ ! -d "solutions/$DAY" ]]; then
    python3 scripts/daily_pick.py "$DAY"
fi

# 2. Stage everything under solutions/DAY plus the rotated questions.json.
git add "solutions/$DAY" questions.json

# Nothing to commit on rest days? Exit quietly.
if git diff --cached --quiet; then
    echo "Nothing to commit for $DAY (probably a rest day)."
    exit 0
fi

# 3. Make a single commit. To get multiple green squares on the same day,
#    loop and commit each solution file separately instead.
COUNT=$(ls -1 "solutions/$DAY"/*.py 2>/dev/null | wc -l | tr -d ' ')
git commit -m "daily: $DAY — solved $COUNT problem(s)"
git push

echo "Pushed $COUNT problem(s) for $DAY."
