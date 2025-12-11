---
aliases: [Dynamic Host Configuration Protocol]
date created: Tuesday, 2. December 2025, 19:12
date modified: Thursday, 11. December 2025, 09:12
---

# DHCP

The **Dynamic Host Configuration Protocol (DHCP)** is a network management protocol used to automate the process of configuring devices on [IP](TCP IP Model/IP.md) networks.

DHCP allows devices to automatically receive [IP](TCP IP Model/IP.md) addresses and other network configuration parameters, such as subnet masks, default gateways, and [DNS](<./DNS.md>) server addresses, from a DHCP server.

This eliminates the need for manual configuration of network settings on each device, making it easier to manage large networks.

When a device connects to a network, it sends a DHCPDISCOVER message to locate a DHCP server.

The DHCP server responds with a DHCPOFFER message, which includes an available [IP](TCP IP Model/IP.md) address and other configuration parameters.

The device then sends a DHCPREQUEST message to request the offered [IP](TCP IP Model/IP.md) address, and the DHCP server responds with a DHCPACK message to confirm the assignment.

The assigned [IP](TCP IP Model/IP.md) address is typically leased for a specific period, after which the device must renew the lease to continue using the address.

DHCP operates using the [User Datagram Protocol (UDP)](<./UDP.md>) at the [Transport Layer](OSI Model/4-Transport Layer.md) (Layer 4) of the [OSI Model](OSI Model/OSI Model.md).

It uses [UDP](<./UDP.md>) [Port](../Systems & Plaforms/Port.md) 67 for DHCP server communication and [UDP](<./UDP.md>) [Port](../Systems & Plaforms/Port.md) 68 for DHCP client communication.

DHCP is widely used in both home and enterprise networks to simplify network administration and ensure efficient allocation of [IP](TCP IP Model/IP.md) addresses.
