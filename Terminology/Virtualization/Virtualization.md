---
aliases: [Virtualisation]
date created: Wednesday, 26. November 2025, 18:11
date modified: Thursday, 11. December 2025, 09:12
---

# Virtualization

[Host Machine (Host OS)](Host Machine (Host OS).md)

[Virtual Machine (VM)](Virtual Machine (VM).md)

[Hypervisor](<./Hypervisor.md>)

[Virtualization methods](Virtualization methods/Virtualization methods.md)

[Virtualization Hardening & Operations](Virtualization Hardening & Operations/Virtualization Hardening & Operations.md)

---

**Term**: Virtualization

**Definition**: A set of technologies that make one physical computer behave like many separate “virtual” computers by abstracting hardware into software.

**Context/Example**: One powerful server can be split into several [Virtual Machines (VMs)](Virtual Machine (VM).md), each running its own [OS](<../Systems & Plaforms/Operating System.md>) (e.g., one Linux server, one Windows server) on the same physical box.

**Related Concepts**: [Virtual machine](Virtual Machine (VM).md), [hypervisor](<./Hypervisor.md>), [containers](<./Virtualization methods/Container.md>), cloud computing

## Security Challenges

[VM Escape](VM Escape.md)

[Multi-Tenancy](<./Multi-Tenancy.md>)

[Side-Channel Attack](Side-Channel Attack.md)

## Mitigating Security Risks

Patch Management

Principle of Least Privilege → give users/programs only the minimum permission they need to do their job.

Disable unused [ports](<../Systems & Plaforms/Port.md>)
