---
aliases: [Paravirtualisation]
date created: Tuesday, 25. November 2025, 22:11
date modified: Wednesday, 10. December 2025, 22:12
---

# Paravirtualization

**Term**: Paravirtualization

**Definition**: A method where the guest OS is modified to be aware that it is virtualized and uses special “[Hypercalls](Hypercall.md)” to talk directly to the [Hypervisor](../Hypervisor.md).

**Context/Example**: A Linux [Kernel](../../Systems & Plaforms/Kernel.md) compiled with paravirtualization support can ask the [Hypervisor](../Hypervisor.md) for services instead of pretending it’s on bare metal, reducing overhead.

**Related Concepts**: [Hypercall](Hypercall.md), [full virtualization](Full Virtualization.md), drivers

