---
aliases: []
date created: Tuesday, 25. November 2025, 22:11
date modified: Monday, 1. December 2025, 22:12
---

# Side-Channel Attack

**Term**: Side-Channel Attack (in [virtualization](/Virtualization))

**Definition**: An attack that recovers secrets not by breaking a cryptographic hash *directly*, but by analyzing indirect signals like timing, cache use, or power consumption of a shared system.

**Context/Example**: On a shared cloud host, a malicious [VM](Virtual%20Machine%20(VM).md) measures CPU cache timings to infer what another [VM](Virtual%20Machine%20(VM).md) is doing and extract cryptographic keys.

**Related Concepts**: [Multi-tenancy](Multi-Tenancy.md)
