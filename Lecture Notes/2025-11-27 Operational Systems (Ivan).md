---
aliases: []
date created: Thursday, 27. November 2025, 09:11
date modified: Monday, 1. December 2025, 21:12
---

# 2025-11-27 Operational Systems (Ivan)

Ivan
- Manages hardware, processes, users, resources
- Kernel is a bridge between hardware and application
- Kernel has 2 modes - Privileged mode and Restricted mode
- Solves problems of differences in hardware, making API constant
- `printf()` is a sys call
- Kernel mode switching is resource expensive!
- Time multiplexing - Scheduling different processes on the CPU over time
- Space multiplexing - Dividing RAM and Disk space among processes and users
- Isolation used for not starving between processes
- Program vs process - static exe on disk vs a program is executed instructions in RAM
- Context switching - halts a process and switches to the other one, PCB
- OS does memory management, and does protection against fragmentation
- Seqfault - happens when OS tries to access a point in a memory that is not available in mapping in TLB
- TLB - Cache that holds the translation table
- Hardware MMU part of a processor that does the translation dig to vir and other way around.
