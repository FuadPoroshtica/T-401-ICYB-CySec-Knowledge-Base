---
aliases: [Network Address Translation]
date created: Tuesday, 2. December 2025, 19:12
date modified: Tuesday, 2. December 2025, 19:12
---

# NAT
- A technique used to map multiple private [IP](TCP%20IP%20Model/IP.md) addresses to a single public [IP](TCP%20IP%20Model/IP.md) address (or a few addresses) before sending packets to another network (e.g., the Internet).
- Allows multiple devices on a local network to share a single public IP address.
- Helps conserve the limited number of available IPv4 addresses.
- Provides a layer of security by hiding internal IP addresses from the external network.
- Commonly used in home and office networks with [routers](Network%20hardware/Router.md) that perform NAT.

## NAT: Usability vs. Security Impact
**Pros**:
- The “natural firewall” effect: Devices behind a NAT are not directly reachable from the outside, which can enhance security.
- Topology hiding: The internal network structure is hidden from external entities.
- IPv4 Conservation: NAT helps mitigate the shortage of IPv4 addresses by allowing multiple devices to share a single public IP address. This is part of the reason why IPv4 is still widely used despite the exhaustion of available addresses, and why the switch to IPv6 has been slow.
**Cons**:
- Breaks end-to-end connectivity: Some applications and protocols that rely on direct peer-to-peer connections may not work properly behind a NAT.
	- Peer-to-peer applications are when you connect directly to another user’s device, rather than going through a central server. Examples include file-sharing applications, VoIP services, and sometimes online gaming.
	- Examples of workarounds are things like STUN (Session Traversal Utilities for NAT) and TURN (Traversal Using Relays around NAT), which help establish connections between devices behind NATs.
- Loss of attribution: It can be difficult to trace the origin of traffic, which can complicate logging and monitoring.

> [!warning] NAT is *not* a security feature.
> NAT stops unsolicited incoming connections from the outside, but it does not provide encryption or protect against attacks from the inside.

The connections initiated from inside the NAT to the outside are tracked in a NAT table.
When a packet comes back from the outside, the NAT device looks up the destination port in the NAT table to determine which internal device should receive the packet.
But this means that unsolicited incoming connections from the outside to devices behind the NAT are generally not possible, unless specific port forwarding rules are set up on the NAT device.

In the NAT translation table, we have a mapping of internal IP addresses and ports to the external IP address and ports. There’s the WAN (Wide Area Network) side, which is the public IP address assigned to the NAT device (like a router), and the LAN (Local Area Network) side, which consists of the private IP addresses and ports of the devices behind the NAT.

When a device inside the NAT initiates a connection to an external server, the NAT device records this mapping in its translation table. For example, if an internal device with IP address
