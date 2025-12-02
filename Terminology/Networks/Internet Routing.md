---
aliases: []
date created: Tuesday, 2. December 2025, 19:12
date modified: Tuesday, 2. December 2025, 19:12
---

# Internet Routing
How do packets actually get to their destination across multiple networks?
**IGP**: Interior Gateway Protocol (within an [Autonomous System (AS)](AS.md)).
**EGP**: Exterior Gateway Protocol (between autonomous systems).
**BGP**: Border Gateway Protocol (the main EGP used on the Internet).
**AS**: Autonomous System, a collection of [IP](TCP%20IP%20Model/IP.md) networks and [routers](Network%20hardware/Router.md) under the control of a single organization that presents a common routing policy to the Internet.

Routing is done on the basis of these autonomous systems (ASes). Each AS is assigned a unique AS number (ASN).
The BGP is used to exchange routing information between ASes, allowing [routers](Network%20hardware/Router.md) to determine the best path for data packets to reach their destination across the Internet.
Routers maintain a routing table that contains information about the paths to different network destinations. When a packet arrives at a router, the router examines the destination IP address and consults its routing table to determine the next hop for the packet. The packet is then forwarded to the next router along the path to its destination.

Interior Gateway Protocols (IGPs) are used within an AS to manage routing. Examples of IGPs include OSPF (Open Shortest Path First) and EIGRP (Enhanced Interior Gateway Routing Protocol).

## Routing Mechanics: Populating vs. Using the Routing Table
1. **Creating the table**
	1. **The goal**: build a map of the network. To know roughly where everything is. And each router needs to sort of learn this.
	2. **Input**: Updates from neighboring or statically configured routes.
	3. **Process**: Algorithms (e.g., Dijkstra’s, Bellman-Ford) to compute shortest paths.
		1. Dijkstra’s algorithm can’t be used in BGP because it requires complete knowledge of the distance between *all* the nodes, which is not feasible in the decentralized and dynamic environment of the Internet. BGP operates on a path-vector protocol, where each router shares information about the paths it knows to reach different networks, rather than requiring a complete map of the entire network.
		2. So they don’t use Dijkstra’s algorithm. They use Bellman-Ford, which is more suitable for distributed systems where each node only has knowledge of its immediate neighbors.
	4. **Result**: A forwarding table with next-hop information for each destination network.
	5. Inspect/modify with `route` / `Get-NetRoute` commands.
2. **Using the table**
	1. **The goal**: Move the packets *fast*.
	2. **Input**: An incoming packet’s destination IP address.
	3. **Process**: Lookup in the forwarding table to find the next hop (longest prefix match).
	4. **Result**: The packet is moved to the outbound interface towards the next hop. (Or dropped if no route is found.)

Some tools to see this on your machine:
- `traceroute` / `tracert`: Show the path packets take to a destination.
- `ping`: Test reachability of a host on an IP network.

The [Data Link Layer](../Terminology/Networks/OSI%20Model/2-Data%20Link%20Layer.md) uses [MAC](../Terminology/Networks/MAC.md) addresses to deliver frames within the same network.
“Frames” in this context means data packets at the link layer of the [OSI Model](../Terminology/Networks/OSI%20Model/OSI%20Model.md). So the ethernet frame is the data packet used in Ethernet networks at the link layer. Other frames include Wi-Fi frames, which are used in wireless networks.
The [MAC](../Terminology/Networks/MAC.md) address (Media Access Control address) is a unique identifier assigned to network interfaces for communications at the [Data Link Layer](../Terminology/Networks/OSI%20Model/2-Data%20Link%20Layer.md) of a network segment.
The [Network Layer](../Terminology/Networks/OSI%20Model/3-Network%20Layer.md) uses IP addresses to route packets between different networks.
