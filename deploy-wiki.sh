#!/bin/bash
# Helper script to deploy the wiki to GitHub Pages

set -e

echo "🔧 Setting up docs directory..."
mkdir -p docs_mkdocs
ln -sf "../Lecture Notes" "docs_mkdocs/Lecture Notes" 2>/dev/null || true
ln -sf ../Terminology "docs_mkdocs/Terminology" 2>/dev/null || true
ln -sf "../Tools and Commands" "docs_mkdocs/Tools and Commands" 2>/dev/null || true
ln -sf ../resources "docs_mkdocs/resources" 2>/dev/null || true
ln -sf ../Templates "docs_mkdocs/Templates" 2>/dev/null || true
ln -sf ../zAttachments "docs_mkdocs/zAttachments" 2>/dev/null || true
ln -sf ../README.md "docs_mkdocs/README.md" 2>/dev/null || true

echo "✅ Docs directory ready"
echo ""
echo "🏗️  Building site..."
mkdocs build

echo ""
echo "✅ Build successful!"
echo ""
echo "📦 Deploying to GitHub Pages..."
mkdocs gh-deploy --force

echo ""
echo "🎉 Deployment complete!"
echo "Your wiki will be available at:"
echo "https://fuadporoshtica.github.io/T-401-ICYB-CySec-Knowledge-Base/"
