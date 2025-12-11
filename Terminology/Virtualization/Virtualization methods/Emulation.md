---
aliases: []
date created: Tuesday, 25. November 2025, 22:11
date modified: Monday, 8. December 2025, 19:12
---

# Emulation
**Term**: Emulation

**Definition**: Simulating the *entire* hardware platform, often a different CPU architecture, by translating instructions so foreign binaries can run.

**Context/Example**: Using [QEMU](<../../../Tools and Commands/Setup & Config/Qemu.md>) to run an ARM Linux [image](<../Virtualization Hardening & Operations/Image.md>) on an x86 laptop; every ARM instruction is translated to x86, which is much slower but highly flexible.

**Related Concepts**: [Virtualization](<../Virtualization.md>) vs emulation, instruction translation, performance overhead.
