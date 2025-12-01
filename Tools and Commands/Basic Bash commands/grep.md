---
aliases: []
date created: Tuesday, 25. November 2025, 17:11
date modified: Monday, 1. December 2025, 21:12
---

# grep

**Tool/Command Name**: grep

**Purpose**: Find patterns in files using [`regex`](Regular%20Expression%20(e%20g%20regex).md)es.

**Basic Syntax/Usage Example**:

- Search for a pattern within a file:  `grep "<search pattern>" <path/to/file>`
    - Can also search in multiple files: `grep "<search pattern>" <path/to/file1> <path/to/file2>`
- Search for an exact string (disables regexes): `grep --fixed-strings "<search string>" <path/to/file>`
- Search for a pattern in all files recursively in a directory: `grep --recursive "<search pattern>" <path/to/directory>`
    - Search for a pattern in all files recursively in *the current directory*: `grep --recursive "<search pattern>" .`
- Print $n$ lines of Context *around* match: `grep --context <number of lines> "<search pattern>" <path/to/file>`
    - Print $n$ lines of Context *before* match: `grep --before-context <number of lines> "<search pattern>" <path/to/file>`
    - Print $n$ lines of Context *after* match: `grep --after-context <number of lines> "<search pattern>" <path/to/file>`

    ****

**Operating System(s)**: Linux, macOS, (Windows equivalent is `Select-String`).

**Link to Documentation/Homepage**: [https://www.gnu.org/software/grep/manual/grep.html](https://www.gnu.org/software/grep/manual/grep.html)
