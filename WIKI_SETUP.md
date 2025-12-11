# Wiki Setup Guide

This repository has been configured to work as a beautiful wiki using **MkDocs with Material theme**.

## 🌐 Viewing the Wiki

Once deployed, your wiki will be available at:
**https://fuadporoshtica.github.io/T-401-ICYB-CySec-Knowledge-Base/**

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- pip

### Installation
```bash
pip install mkdocs mkdocs-material
```

### Local Development

1. **Setup the docs directory** (required before running MkDocs):
   ```bash
   bash .mkdocs-workaround.sh
   ```
   Or manually create the symlinks if the script doesn't exist.

2. **Run the local server**:
   ```bash
   mkdocs serve
   ```
   Then open http://127.0.0.1:8000 in your browser.

3. **Build the static site**:
   ```bash
   mkdocs build
   ```
   The site will be generated in the `site/` directory.

## 📦 Deployment

### Automatic Deployment (GitHub Actions)
Every push to the `main` or `master` branch will automatically:
1. Build the MkDocs site
2. Deploy it to GitHub Pages

The workflow is defined in `.github/workflows/deploy-mkdocs.yml`.

### Manual Deployment
```bash
# Setup docs directory first
bash .mkdocs-workaround.sh

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## 📝 Content Structure

The wiki is organized as follows:
- **Lecture Notes**: Course lecture notes organized by date
- **Terminology**: Cybersecurity terms and definitions
- **Tools and Commands**: Security tools and command references
- **Resources**: Additional learning materials and references

## 🔗 Link Format

All Obsidian wikilinks (`Page`) have been converted to standard markdown links (`[Page](path/to/page.md)`).

If you add new content:
- Use standard markdown links: `[Text](path/to/file.md)`
- For images: `![Alt text](../zAttachments/image.png)`

## 🛠️ Troubleshooting

### "docs_dir" error when running mkdocs
Make sure you've run the setup script first:
```bash
bash .mkdocs-workaround.sh
```

### Links not working
- Check that paths are relative
- Ensure `.md` extension is included
- Verify the target file exists

### Images not displaying
- Images should be in `zAttachments/` directory
- Use relative paths from the current file
- Example: `![Image](../zAttachments/image.png)`

## 📚 MkDocs Configuration

The configuration is in `mkdocs.yml`. Key features enabled:
- **Material theme** with dark/light mode toggle
- **Search** with highlighting
- **Navigation** with tabs and sections
- **Code highlighting** with copy button
- **Table of contents** with auto-following

## 🔄 Converting New Obsidian Links

If you add new content with Obsidian wikilinks, you can run the conversion script:
```bash
python3 convert_links.py
```

This script:
- Converts `Page` to `[Page](path/to/page.md)`
- Fixes image paths
- Handles URL-encoded characters

## 📋 Files to Ignore

The following files are git-ignored:
- `site/` - Generated wiki site
- `docs_mkdocs/` - Symlinked docs directory
- `.mkdocs-workaround.sh` - Setup script
- `convert_links.py` - Link conversion script

---

For more information about MkDocs, visit: https://www.mkdocs.org/
For Material theme docs, visit: https://squidfunk.github.io/mkdocs-material/
