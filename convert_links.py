#!/usr/bin/env python3
"""
Convert Obsidian wikilinks to standard markdown links for MkDocs compatibility.
Also fixes image paths and URL-encoded characters in file paths.
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote

def find_markdown_file(base_path, target_name):
    """Find a markdown file by name (case-insensitive search)."""
    # Remove .md extension if present
    target_name = target_name.replace('.md', '')
    
    # Search for the file
    for root, dirs, files in os.walk(base_path):
        # Skip .git and other hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'site']
        
        for file in files:
            if file.endswith('.md'):
                file_without_ext = file.replace('.md', '')
                if file_without_ext.lower() == target_name.lower():
                    full_path = os.path.join(root, file)
                    return os.path.relpath(full_path, base_path)
    
    return None

def calculate_relative_path(from_file, to_file):
    """Calculate relative path from one file to another."""
    from_dir = os.path.dirname(from_file)
    
    # Calculate relative path
    if from_dir:
        rel_path = os.path.relpath(to_file, from_dir)
    else:
        rel_path = to_file
    
    return rel_path

def convert_wikilink_to_markdown(match, current_file, base_path):
    """Convert a single wikilink to markdown format."""
    full_match = match.group(0)
    link_text = match.group(1)
    
    # Handle links with custom display text: [[Page|Display Text]]
    if '|' in link_text:
        target, display = link_text.split('|', 1)
        target = target.strip()
        display = display.strip()
    else:
        target = link_text.strip()
        display = target
    
    # Find the target file
    target_path = find_markdown_file(base_path, target)
    
    if target_path:
        # Calculate relative path from current file to target
        rel_path = calculate_relative_path(current_file, target_path)
        return f"[{display}]({rel_path})"
    else:
        # If file not found, keep the display text but remove the link
        print(f"  Warning: Could not find target '{target}' from {current_file}")
        return display

def fix_image_paths(content, current_file):
    """Fix image paths to be relative."""
    # Pattern: ![alt](path) or ![[path]]
    def replace_image(match):
        full_match = match.group(0)
        
        if full_match.startswith('![['):
            # Obsidian image format: ![[image.png]]
            image_name = match.group(1)
            # Convert to markdown format with relative path
            rel_path = calculate_relative_path(current_file, f"zAttachments/{image_name}")
            return f"![{image_name}]({rel_path})"
        else:
            # Standard markdown image: ![alt](path)
            alt = match.group(1)
            path = match.group(2)
            
            # If path starts with ../ or zAttachments/, it's likely correct
            if path.startswith('../') or path.startswith('zAttachments/'):
                # Decode URL-encoded characters
                decoded_path = unquote(path)
                return f"![{alt}]({decoded_path})"
            
            return full_match
    
    # Replace Obsidian-style image embeds: ![[image.png]]
    content = re.sub(r'!\[\[(.*?)\]\]', replace_image, content)
    
    # Fix URL-encoded paths in standard markdown images
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_image, content)
    
    return content

def fix_relative_links(content, current_file):
    """Fix relative links that use ../../ style paths."""
    def replace_link(match):
        text = match.group(1)
        path = match.group(2)
        
        # Decode URL-encoded characters in the path
        decoded_path = unquote(path)
        
        # Check if it's an anchor link or external link
        if decoded_path.startswith('#') or decoded_path.startswith('http'):
            return f"[{text}]({decoded_path})"
        
        # If it's a relative path, verify it exists
        if decoded_path.startswith('../') or '/' in decoded_path:
            return f"[{text}]({decoded_path})"
        
        return f"[{text}]({decoded_path})"
    
    # Fix standard markdown links with URL encoding
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
    
    return content

def process_markdown_file(file_path, base_path):
    """Process a single markdown file."""
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        relative_file_path = os.path.relpath(file_path, base_path)
        
        # Convert wikilinks: [[Page]] or [[Page|Display Text]]
        content = re.sub(
            r'\[\[([^\]]+)\]\]',
            lambda m: convert_wikilink_to_markdown(m, relative_file_path, base_path),
            content
        )
        
        # Fix image paths
        content = fix_image_paths(content, relative_file_path)
        
        # Fix relative links with URL encoding
        content = fix_relative_links(content, relative_file_path)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Updated")
        else:
            print(f"  - No changes needed")
            
    except Exception as e:
        print(f"  ✗ Error: {e}")

def main():
    """Main function to process all markdown files."""
    base_path = Path(__file__).parent
    print(f"Base path: {base_path}\n")
    
    # Find all markdown files
    markdown_files = []
    for root, dirs, files in os.walk(base_path):
        # Skip .git directory and site directory
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'site']
        
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    
    print(f"Found {len(markdown_files)} markdown files\n")
    
    # Process each file
    for md_file in sorted(markdown_files):
        process_markdown_file(md_file, base_path)
    
    print(f"\n✓ Conversion complete!")
    print(f"Processed {len(markdown_files)} files")

if __name__ == "__main__":
    main()
