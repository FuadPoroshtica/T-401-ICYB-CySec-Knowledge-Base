---
aliases: []
date created: Tuesday, 25. November 2025, 22:11
date modified: Monday, 8. December 2025, 11:12
---

# Hypervisor
**Term**: Hypervisor (Virtual Machine Monitor, VMM)

**Definition**: The software layer that creates, runs, and manages [virtual machines](Virtual%20Machine%20(VM).md) while coordinating their access to the physical hardware.

**Context/Example**: VirtualBox, VMware ESXi, and KVM are hypervisors; they decide how much CPU, RAM, and disk each VM gets and enforce isolation.

**Related Concepts**: Type 1 / Type 2 hypervisor, [VM](Virtual%20Machine%20(VM).md), resource allocation, isolation.

---

## Types of Hypervisors

**Term**: Type 1 Hypervisor (Bare-Metal Hypervisor)

**Definition**: A hypervisor that runs *directly* on the physical hardware, with no “normal” host OS underneath.

**Context/Example**: VMware ESXi or Microsoft Hyper-V Server installed directly on a server; all [VMs](Virtual%20Machine%20(VM).md) run on top of this thin hypervisor layer.

**Related Concepts**: Type 2 hypervisor, [full virtualization](Virtualization%20methods/Full%20Virtualization.md), [multi-tenancy](Multi-Tenancy.md), cloud providers.

**Term**: Type 2 Hypervisor (Hosted Hypervisor)

**Definition**: A hypervisor that runs as a normal application on a host OS like Windows, macOS, or Linux.

**Context/Example**: VirtualBox or VMware Workstation installed in your desktop OS; the hypervisor is “just another program” the OS is running.

**Related Concepts**: Type 1 hypervisor, host OS, desktop virtualization.

---

## Hypervisor Vulnerability

**Term**: Hypervisor Vulnerability

**Definition**: A security flaw in the hypervisor that an attacker can exploit to impact multiple VMs or the host.

**Context/Example**: A bug in ESXi or KVM that lets a guest VM send specially crafted instructions and gain control over the hypervisor process.

**Related Concepts**: [VM escape](VM%20Escape.md), patch management, [CVE](Hypervisor.md), [attack surface](Hypervisor.md).
