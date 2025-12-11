#!/bin/bash
# Workaround for MkDocs not supporting root as docs_dir
# We'll use a symlink approach

# Remove existing docs if it's our symlink
if [ -L "docs_mkdocs" ]; then
    rm docs_mkdocs
fi

# Create symlinks for all content directories
mkdir -p docs_mkdocs
ln -sf "../Lecture Notes" "docs_mkdocs/Lecture Notes"
ln -sf ../Terminology "docs_mkdocs/Terminology"
ln -sf "../Tools and Commands" "docs_mkdocs/Tools and Commands"
ln -sf ../resources "docs_mkdocs/resources"
ln -sf ../Templates "docs_mkdocs/Templates"
ln -sf ../zAttachments "docs_mkdocs/zAttachments"
ln -sf ../README.md "docs_mkdocs/README.md"

echo "Created docs_mkdocs directory with symlinks"
