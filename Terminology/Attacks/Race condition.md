---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Monday, 1. December 2025, 21:12
---

# Race condition
**Term**: Race condition

**Definition**: When multiple threats or processes are trying to access the shared data in the same time, this is not good! This causes you not to know what will go to hell, addr leaks, memory corruption, security vulnerabilities.

**Context/Example**: 3 Threads accessing the same picture in the same time, 1st thread is looking at the picture, 2nd one changes it and 3th one deletes it… This causes chaos

**Related Concepts**: Memory, threads, cpu
