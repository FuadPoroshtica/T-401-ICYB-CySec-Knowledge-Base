---
aliases: [Address Resolution Protocol]
date created: Tuesday, 2. December 2025, 20:12
date modified: Tuesday, 2. December 2025, 20:12
---

# ARP
**ARP (Address Resolution Protocol)** is used to map [IP](TCP%20IP%20Model/IP.md) addresses to [MAC](MAC.md) addresses within a local network.
When a device wants to communicate with another device on the same network, it sends an ARP request to ask “Who has this IP address?” The device with that IP address responds with its MAC address.

If a computer doesn’t know the MAC address of a device it wants to communicate with, it sends out an ARP request as a broadcast to all devices on the local network. The device with the matching IP address responds with its MAC address.

In the lecture, the teacher went into the terminal and runs `arp -n` to see the ARP table on his system. It shows:
- Address (IP address)
- HWtype (hardware type, e.g., Ethernet)
- HWaddress (MAC address)
    - Essentially a mapping of IP addresses to MAC addresses that the system has learned.
- Flags
    - Indicate the status of the ARP entry (e.g., whether it’s complete, incomplete, permanent, or published).
- Mask
    - Subnet mask associated with the IP address.
- Iface (interface)
    - The network interface associated with the ARP entry (e.g., eth0, wlan0).

If you get several responses to an ARP request, you might be under an ARP [Spoofing](../Attacks/Spoofing.md) attack. Because normally only one device should respond with its MAC address.
