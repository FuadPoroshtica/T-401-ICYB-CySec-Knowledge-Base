---
aliases: [Internet Protocol]
date created: Tuesday, 2. December 2025, 19:12
date modified: Thursday, 11. December 2025, 09:12
---

# IP

The **Internet Protocol (IP)** is a fundamental protocol in the Internet Protocol Suite that is responsible for addressing and routing data packets across networks.

IP assigns unique numerical addresses, known as IP addresses, to devices on a network, allowing them to communicate with each other.

There are two main versions of IP in use today: IPv4 and IPv6. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses to accommodate the growing number of devices connected to the internet.

IP operates at the [Network Layer](../OSI%20Model/3-Network%20Layer.md) (Layer 3) of the [OSI Model](../OSI%20Model/OSI%20Model.md), which is responsible for packet forwarding, including routing through intermediate [routers](../Network%20hardware/Router.md).

IP works in conjunction with other protocols, such as [TCP (Transmission Control Protocol)](TCP.md) and [UDP (User Datagram Protocol)](../UDP.md), to facilitate reliable and efficient data transmission over networks.

IP is a connectionless protocol, meaning that it does not establish a dedicated end-to-end connection before transmitting data. Instead, data packets are sent independently and may take different paths to reach their destination.

IP addresses are typically represented in a dotted-decimal format for IPv4 (e.g., `192.168.1.1`) and in hexadecimal colon-separated format for IPv6 (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).

IP plays a crucial role in the functioning of the internet and other computer networks, enabling devices to locate and communicate with each other across diverse and interconnected networks.

## IPv4 Reserved Addresses
- Some addresses are reserved for special purposes.
- Examples:
	- Localhost: 127.0.0.1 (actually the entire 127/8 range)
	- Local private networks: 10/8, 172.16/12, 192.168/16, ...
	- Multicast: 224. - 239. (Most significant 4 bits are 1110)
	- Limited (local) broadcast: 255.255.255.255/32
	- Complete list: [https://en.wikipedia.org/wiki/Reserved_IP_addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses)
These are not routable on the public Internet.

There aren’t enough IPv4 addresses for all devices connected to the Internet.

IPv4 only allows for about 4.3 billion (4.3 x 10^9) unique addresses.

## Subnet addressing - Subnet mask

Subnetworks (subnets) are a logical divison of an IP network.

198.0.1.130/24 means that the first 24 bits are the network ID, and the last 8 bits are the host ID. 198.0.1/24 and 198.0.1.130/24 are the same network, because they have the same first 24 bits.

In more detail, the slash notation here (/24) is called CIDR (Classless Inter-Domain Routing) notation. It means that the first 24 bits of the IP address are used for the network portion, and the remaining bits (in this case, 8 bits) are used for the host portion. This allows for flexible allocation of IP addresses and efficient routing.

Subnet mask: A 32-bit number that masks an IP address and divides the IP address into network and host portions.

IPv4 address: 32 bits (32b) (4 bytes (4B)).

<font color="#ff0000">172</font>.<font color="#00b050">16</font>.<font color="#00b0f0">254</font>.<font color="#7030a0">1</font> = <font color="#ff0000">10101100</font>.<font color="#00b050">00010000</font>.<font color="#00b0f0">11111110</font>.<font color="#7030a0">00000001</font> ← 4 blocks of 8 bits each (1 byte), so 4 bytes.

Each byte is represented as a decimal number (0-255).

Notionally, high end bits are network identifier, low end bits are host identifier. So for 198.0.1.130:

- Network ID: 198.0.1
- Host ID: 130

## The IPv4 Datagram

![](../../../zAttachments/Pasted%20image%2020251202091743.png)
