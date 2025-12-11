---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Monday, 8. December 2025, 19:12
---

# Privileged Kernel mode

**Definition**: Privileged [Kernel](<./Kernel.md>) Mode is a special operating mode of the CPU that allows the [Operating System](Operating System.md) [Kernel](<./Kernel.md>) to execute critical and sensitive instructions that are restricted from regular user applications. In this mode, the kernel has full access to all hardware resources and can perform low-level operations necessary for managing the system.

**Context/Example**: When a user application needs to perform an operation that requires direct hardware access, such as reading from a disk or managing memory, it makes a system call to the operating system. The CPU switches from user mode to privileged kernel mode to allow the kernel to safely execute the requested operation before returning control back to the user application.

**Related Concepts**: Restricted Kernel Mode
