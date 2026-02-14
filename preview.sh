#!/usr/bin/env bash
# F.O.R.G.E Workshop Preview
# Generates the site with draft techniques visible, then serves locally.
set -euo pipefail

cd "$(dirname "$0")"

echo "=== F.O.R.G.E Workshop Preview ==="
echo ""

echo "[1/3] Generating framework data..."
python3 data/generate_framework.py
echo ""

echo "[2/3] Validating framework..."
python3 data/validate_framework.py
echo ""

echo "[3/3] Building site (preview mode)..."
FORGE_MODE=preview python3 generator/build.py
echo ""

echo "=== Starting local server ==="
echo "Open: http://localhost:8000"
echo "Press Ctrl+C to stop."
echo ""
python3 -m http.server 8000 --directory output
