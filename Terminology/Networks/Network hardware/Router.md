---
aliases: [Network router, routers]
date created: Tuesday, 2. December 2025, 19:12
date modified: Monday, 8. December 2025, 18:12
---

# A Network Router
- Routers forward packets between (local) networks.
- (Unlike [Switches](Switch.md), routers operate at Layer 3 ([Network Layer](../OSI Model/3-Network Layer.md)) of the [OSI Model](../OSI Model/OSI Model.md).)
- The difference between a [Switch](Switch.md) and a router is that a [Switch](Switch.md) connects devices within the same network, while a router connects *different* networks together.

**Home router:**
A home router is actually much more than just a router. It typically combines multiple functions:
- [Switch](Switch.md).
- Wireless access point (for Wi-Fi).
- Router.
- NAT (Network Address Translation).
    - NAT is for sharing a *single* public [IP](../TCP IP Model/IP.md) address among *multiple* devices on a local network. What it does is that it translates the private [IP](../TCP IP Model/IP.md) addresses of devices on the local network to the public [IP](../TCP IP Model/IP.md) address when they access the internet, and vice versa for incoming traffic.
- [Firewall](../Terminology/Defense & Control/Firewall) (basic security features).

**Backbone routers:**
- These are high-capacity routers that form the core of the internet.
- They are things that ISPs use to connect to each other. Like they can be used for a whole country or region.
