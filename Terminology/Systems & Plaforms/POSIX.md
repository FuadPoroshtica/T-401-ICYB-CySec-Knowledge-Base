---
aliases: []
date created: Monday, 1. December 2025, 20:12
date modified: Thursday, 4. December 2025, 08:12
---

# POSIX

**Term**: POSIX

**Definition**:
Stands for “**P**ortable **O**perating **S**ystem **I**nterface” (the **X** stands for UNIX)
A family of standards that defines compatibility between different [Unix-like](Unix-Like.md) operating systems. If an API works on [Unix-like](Unix-Like.md) system A, then it should work on a [Unix-like](Unix-Like.md) system B.

POSIX Model of permission:

- Permissions apply to three rigid categories:
    1. User (Owner)
    2. Group
    3. Others (World)
- The Bits: Read (r), Write (w), Execute (x)
- Representation: Octal (e.g., 755) or symbolic (rwxr-xr-x).

**Example:** Linux and MacOS are POSIX compliant,

**Related Concepts**: [Unix-Like](Unix-Like.md), Linux, Permissions
