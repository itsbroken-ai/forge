#!/usr/bin/env bash
# F.O.R.G.E Workshop Preview
# Builds the site from data/framework.json (preview mode shows drafts), then serves locally.
# Source of truth is data/framework.json — edit it directly. (Matches deploy.sh.)
set -euo pipefail

cd "$(dirname "$0")"

echo "=== F.O.R.G.E Workshop Preview ==="
echo ""

echo "[1/2] Validating framework..."
python3 data/validate_framework.py
echo ""

echo "[2/2] Building site (preview mode)..."
FORGE_MODE=preview python3 generator/build.py
echo ""

echo "=== Starting local server ==="
echo "Open: http://localhost:8000"
echo "Press Ctrl+C to stop."
echo ""
python3 -m http.server 8000 --directory output
