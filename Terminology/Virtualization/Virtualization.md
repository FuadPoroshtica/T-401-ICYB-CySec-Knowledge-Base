---
aliases: []
date created: Wednesday, 26. November 2025, 18:11
date modified: Monday, 8. December 2025, 19:12
---

# Virtualization


[Host Machine / Host OS](Virtualization/Host%20Machine%20Host%20OS.md)

[Virtual Machine (VM)](Virtual%20Machine%20(VM).md)

[Hypervisor](Hypervisor.md)

[Virtualization methods](Virtualization/Virtualization%20methods.md)

[Virtualization Hardening & Operations](Virtualization/Virtualization%20Hardening%20&%20Operations.md)

---

**Term**: Virtualization

**Definition**: A set of technologies that make one physical computer behave like many separate “virtual” computers by abstracting hardware into software.

**Context/Example**: One powerful server can be split into several [Virtual Machines (VMs)](Virtual%20Machine%20(VM).md), each running its own OS (e.g., one Linux server, one Windows server) on the same physical box.

**Related Concepts**: [Virtual machine](Virtual%20Machine%20(VM).md), [hypervisor](Hypervisor.md), [containers](Virtualization%20methods/Container.md), cloud computing

## Security Challenges

[VM Escape](VM%20Escape.md)

[Multi-Tenancy](Multi-Tenancy.md)

[Side-Channel Attack](Side-Channel%20Attack.md)

## Mitigating Security Risks

Patch Management
Principle of Least Privilege → give users/programs only the minimum permission they need to do their job.
Disable unused [ports](../Systems%20&%20Plaforms/Port.md)
