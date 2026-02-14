#!/usr/bin/env bash
# F.O.R.G.E Production Deploy
# Generates the site with drafts filtered out. Optionally pushes to Vercel.
set -euo pipefail

cd "$(dirname "$0")"

echo "=== F.O.R.G.E Production Deploy ==="
echo ""

echo "[1/3] Generating framework data..."
python3 data/generate_framework.py
echo ""

echo "[2/3] Validating framework..."
python3 data/validate_framework.py
echo ""

echo "[3/3] Building site (production mode)..."
python3 generator/build.py
echo ""

if [[ "${1:-}" == "--push" ]]; then
    echo "=== Deploying to Vercel ==="
    vercel --prod
else
    echo "=== Build complete ==="
    echo "Run './deploy.sh --push' to deploy to Vercel."
fi
