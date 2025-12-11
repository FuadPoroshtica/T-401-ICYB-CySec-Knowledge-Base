#!/bin/bash
set -e

echo "📦 Packaging wiki content..."
cd /home/fuad/Documents/T-401-ICYB-CySec-Knowledge-Base
tar czf /tmp/wiki-content.tar.gz --exclude='site' --exclude='docs_mkdocs' --exclude='.git' .

echo "📤 Uploading to Proxmox..."
scp /tmp/wiki-content.tar.gz root@192.168.148.254:/tmp/

echo "📥 Extracting in container..."
ssh root@192.168.148.254 "pct push 116 /tmp/wiki-content.tar.gz /tmp/wiki-update.tar.gz"
ssh root@192.168.148.254 "pct exec 116 -- bash -c 'cd /var/www/wiki && tar xzf /tmp/wiki-update.tar.gz && rm /tmp/wiki-update.tar.gz'"

echo "🏗️  Rebuilding wiki..."
ssh root@192.168.148.254 "pct exec 116 -- /usr/local/bin/update-wiki.sh"

echo ""
echo "✅ Wiki updated successfully!"
echo "🌐 Visit: http://192.168.148.134"
