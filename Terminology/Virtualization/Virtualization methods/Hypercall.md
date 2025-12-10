---
aliases: []
date created: Tuesday, 25. November 2025, 22:11
date modified: Monday, 8. December 2025, 19:12
---

# Hypercall

**Term**: Hypercall

**Definition**: Special calls from a [paravirtualized](../Paravirtualization.md) guest OS to the [hypervisor](../Hypervisor.md), similar to how system calls go from user space to the kernel.

**Context/Example**: Instead of executing a privileged CPU instruction directly, a paravirtualized guest issues a hypercall so the hypervisor can perform the operation safely.

**Related Concepts**: [Containers](../Container.md), namespaces, cgroups, microservices, Kubernetes.
