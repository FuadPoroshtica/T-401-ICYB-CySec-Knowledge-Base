---
aliases: []
date created: Tuesday, 25. November 2025, 22:11
date modified: Monday, 8. December 2025, 19:12
---

# Paravirtualization

**Term**: Paravirtualization

**Definition**: A method where the guest OS is modified to be aware that it is virtualized and uses special “[hypercalls](Paravirtualization/Hypercall.md)” to talk directly to the [hypervisor](../Hypervisor.md).

**Context/Example**: A Linux kernel compiled with paravirtualization support can ask the [hypervisor](../Hypervisor.md) for services instead of pretending it’s on bare metal, reducing overhead.

**Related Concepts**: [Hypercall](Paravirtualization/Hypercall.md), [full virtualization](Full%20Virtualization.md), drivers

[Hypercall](Paravirtualization/Hypercall.md)
