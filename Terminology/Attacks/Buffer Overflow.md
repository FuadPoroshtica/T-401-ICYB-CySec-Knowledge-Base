---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Wednesday, 10. December 2025, 21:12
---

# Buffer Overflow

**Term**: Buffer Overflow

**Definition**: A buffer overflow attack occurs when more data is written to a buffer than it can hold, which can lead to adjacent memory being overwritten. This can cause unexpected behavior, crashes, or vulnerabilities that attackers can exploit.

**Context/Example**: In programming languages like C or C++, if a program does not properly check the size of input data before copying it into a fixed-size buffer, an attacker can provide input that exceeds the buffer’s capacity. This can overwrite critical data structures, such as return addresses on the stack, allowing the attacker to execute arbitrary code.

**Related Concepts**: Buffers, memory leak, cleaning algorithms
