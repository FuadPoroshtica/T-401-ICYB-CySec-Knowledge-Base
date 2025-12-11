---
aliases: [Side-Channel Attacks, Side Channel Attack, Side Channel Attacks]
date created: Tuesday, 25. November 2025, 22:11
date modified: Wednesday, 10. December 2025, 22:12
---

# Side-Channel Attack

**Term**: Side-Channel Attack (in [virtualization](<./Virtualization.md>))

**Definition**: An attack that recovers secrets not by breaking a cryptographic hash *directly*, but by analyzing indirect signals like timing, cache use, or power consumption of a shared system. In [virtualization](<./Virtualization.md>), side-channel attacks often target shared resources between [VMs](<Virtual Machine (VM>).md) on the same host to extract sensitive data.

**Context/Example**: On a shared cloud host, a malicious [VM](<Virtual Machine (VM>).md) measures CPU cache timings to infer what another [VM](<Virtual Machine (VM>).md) is doing and extract cryptographic keys.

**Related Concepts**: [Multi-Tenancy](<./Multi-Tenancy.md>)
