---
aliases: []
date created: Monday, 1. December 2025, 20:12
date modified: Monday, 1. December 2025, 22:12
---

# OSINT & Networks 2025-12-01

(2025-12-01 W2 Monday 09:00)
He says that the knowledge base is there for a quick lookup on stuff. Again, he talks about not just copying the slides.
This course should roughly take 150-180 hours, so 50 hours/week, so roughly 10 hours/work day
Next week we’ll talk about networking stuff, virtual networking stuff.

The lab today will run until Thursday, and we’ll do 2 labs inbetween as well. It’ll take us a while to complete.

# Open Source Intelligence (OSINT)

Open Source Intelligence (OSINT) is the practice of gathering information from publicly available sources to be used in an intelligence context.

It is the practice of collecting, analyzing, and making decisions on information that is **publicly available** and **legally accessible**.

OSINT vs Classified Intelligence:

- Does **not** involve hacking, spying, or stealing restricted data.
- Relies entirely on data found in the public domain.
- “The information is out there; the skill lies in aggregating and analyzing it.”

It’s not the same as open source software. It’s just that it is publicly accessible, isn’t declassified.

It can be gotten from:

- The internet
    - Google Search
    - Social media
    - Discussion boards
    - Domain registration (Whois data)
- Government & public records
- Grey literature
    - Technical reports, etc that aren’t published *for* everyone, like they’re intended for only a specific subset of people, but are publicly available for everyone.
- Mass media

It can be used for red teams and blue teams. These teams are both working for the same organization, but are simulating both sides. Red team is attack, blue team is defense.

All of this can also be used in fields such as law, business intelligence, and journalism.

But it can also be used by the “dark side”, e.g. for:

- Target profiling
- Social engineering
- Doxxing (doc dropping)

## Tools and Techniques

(We’ll be doing this in the exercise today)
“Google Dorks”. Using commands to filter results for specific data types. E.g. `site:linkedin.com "project manager"`, etc.
Also DuckDuckGo.

He lists a bunch of tools. Tool to select tools: [OSINT Framework](https://osintframework.com/).

## OPSEC

When you actually do this as a professional, you should also be careful that *your* information isn’t available online.

> [!definition] Definition: OPSEC (Operational Security)
The process of protecting individual pieces of data that could be grouped together to give away critical information (like your identity or location).
>

There are multiple things that can be done, like using browser plugins to block trackers and such; blocking cookies or trackers, blocking JavaScript.
You shouldn’t be logged into your personal account in your browser if you don’t want to be found.
A VPN (Virtual Private Network) can also hide your traffic.

You should protect your hardware and software. Make sure your own system is safe. Like running it on a VM.
There are even OSs for this, like Tails OS. It’s an “amnesiac system”, it clears everything after you’re done.

You could hide your location with a VPN, Tor (The Onion Router) or by using a public Wi-Fi.

We want to counter “Browser fingerprinting” (screen resolution, installed fonts, battery level) to track unique devices even without cookies.
Countermeasures:

1. User agent [spoofing](../Terminology/Attacks/Spoofing). Basically lying to the website? Like “Hahha yeahhh I’m tootally using Chrome right now”. There are even extensions made for just this.
2. Script blockers, e.g., uBlock Origin, NoScript.
3. Dedicated research browser.

If you investigate a target on LinkedIn, LinkedIn will tell the target “John Smith viewed your profile”. To avoid this, analysts use Sock Puppets. Fake identities created for research purposes.
Anatomy of a sock puppet:

- Use a fake name.
- Use an AI-generated face. (E.g., [https://thispersondoesnotexist.com](https://thispersondoesnotexist.com/))
- And more...
Of course, we only use *legal* means.

Behavioral OPSEC (human factors).

- Avoid cross-contamination.
- Physical separation.
- Copy/paste discipline.

OSINT: The internet creates a massive amount of “noise”. OSINT is the process of filtering that noise to find the “signal”.

OPSEC in OSINT: Preemptively masks your trail to evade identification.

## Lab Today:

- Lab 6.
- Select a target (company, organization) in Iceland.
- Find everything you can about them **using legal means**.
- Plan an attack (**but don’t actually do it**), again only with **legal means**.

# Introduction to Computer Networks

(We’ll continue this lecture tomorrow).

## Structure and components

LAN (Local Area Network) is a network that connects computers within a limited area, like a home, school, or office building.
There are all kinds of technologies to connect things together, like Ethernet, Wi-Fi, Bluetooth, etc.
More details about a Local Area Network (LAN) in a home:
Typically, we have a home router that connects to the ISP (Internet Service Provider) via a modem.
The home router typically has a built-in switch to connect multiple wired devices, and also provides Wi-Fi for wireless devices.
(A switch is a device that connects multiple devices on a LAN and uses MAC (Media Access Control) addresses to forward data to the correct destination.)
And in reality, the internet itself is just a huge network of networks.

### A network hub:

- They are largely obsolete, replaced by network switches.
- Hubs are simple connection devices.
- They broadcast incoming data to all connected devices.
- (They operate at the physical layer (Layer 1) of the OSI model.)

A switch looks the same as a hub.

### A network switch:

- More intelligent than a hub.
- It knows which devices are connected to which ports.
- It forwards data only to the intended recipient device.
- Unmanaged switches are plug-and-play.
- Managed switches offer advanced features like VLANs (Virtual Local Networks), QoS (Quality-of-Service), and network monitoring. They can be controlled and customized via software.
- Handles a Local Area Network (LAN).
- (Operates at the data link layer (Layer 2) of the OSI model.)

### A router:

- Routers forward packets between (local) networks.
- (Unlike switches, routers operate at Layer 3 (Network Layer) of the OSI model.)
- The difference between a switch and a router is that a switch connects devices within the same network, while a router connects *different* networks together.

**Home router:**
A home router is actually much more than just a router. It typically combines multiple functions:

- Switch.
- Wireless access point (for Wi-Fi).
- Router.
- NAT (Network Address Translation).
    - NAT is for sharing a *single* public IP address among *multiple* devices on a local network. What it does is that it translates the private IP addresses of devices on the local network to the public IP address when they access the internet, and vice versa for incoming traffic.
- [Firewall](../Terminology/Defense & Control/Firewall) (basic security features).

**Backbone routers:**

- These are high-capacity routers that form the core of the internet.
- They are things that ISPs use to connect to each other. Like they can be used for a whole country or region.

### Structure of the internet:

- End devices (computers, smartphones, etc).
- Local Area Networks (LANs).
- ISPs (Internet Service Providers).

The endpoints connect to ISPs via various means (DSL, cable, fiber, cellular, satellite), which connect to AS (Autonomous Systems) that make up the internet backbone. AS are large networks or group of networks under a common administration, like an ISP or a large organization. AS can be connected together with IXPs (Internet Exchange Points), which are physical locations where different AS can exchange traffic with each other.
So, the order is sorta like:
End devices → LANs → ISPs → AS → IXPs → *other* AS → *other* ISPs → *other* LANs → *other* end devices.

## Layered architecture

The internet uses a layered architecture to manage the complexity of networking.
![[Pasted image 20251201102251.png|700]]

### OSI Model

The most common model is the OSI (Open Systems Interconnection) model, which has seven layers:

1. **Physical Layer (Layer 1):** Deals with the physical connection between devices, including cables, switches, and other hardware.
2. **Data Link Layer (Layer 2):** Responsible for node-to-node (a node here is a device or a point of connection in a network) data transfer and error detection/correction. (E.g., Ethernet, MAC addresses.)
3. **Network Layer (Layer 3):** Manages data routing and forwarding between different networks. (E.g., IP addresses, routers.) Basically, connections that are *more* than one hop away.
4. **Transport Layer (Layer 4):** Ensures reliable data transfer between end devices. (E.g., TCP, UDP.). It essentially manages end-to-end communication. Ensuring that data is delivered error-free, in sequence, and with no losses or duplications.
5. **Session Layer (Layer 5):** Manages sessions or connections between applications. Establishes, maintains, and terminates connections. (E.g., APIs, sockets.)
6. **Presentation Layer (Layer 6):** Translates data formats between the application and the network. Handles data encryption, compression, and translation. (E.g., SSL/TLS, data encoding.)
7. **Application Layer (Layer 7):** Provides network services directly to end-user applications. (E.g., HTTP, FTP, SMTP.). Services like web browsing, email, file transfer, etc.

### TCP/IP Model

The TCP/IP (Transmission Control Protocol/Internet Protocol) model is another widely used networking model, especially for the internet. It only uses these four layers:

1. Link Layer (combines OSI Layers 1 and 2)
2. Internet Layer (OSI Layer 3)
3. Transport Layer (OSI Layer 4)
4. Application Layer (combines OSI Layers 5, 6, and 7)

Great lies in networking: “An application only needs...”

### How is data sent over the internet? - Packet Switching

The internet uses a method called **packet switching** to send data. Instead of sending data as a continuous stream, it breaks the data into smaller packets. Each packet contains a portion of the data, along with metadata like source and destination addresses, sequence numbers, and error-checking information.
Steps:

1. Data is broken into smaller chunks called “packets”.
2. Packets are sent independently over the network.
3. Packets may take different routes to reach the destination.
4. At the destination, the receiver needs to reassemble the packets into the original data.

Packets may take any path through the network, reassembled by the receiver.

(**Lego analogy**: Each packet is like a Lego brick. You can send the bricks separately, and the receiver can put them together to build the original structure.)

Sometimes we have to consider *where* our packets are being sent. E.g., if you’re in Iceland and you’re sending data to a server in the US, your packets might go through multiple countries. This can have implications for privacy and security.

## Problems and their solutions

### 1. Identity and addresing

*Problem: How do we identify a device among billions?Solution: IP addresses (network layer) and MAC addresses (data link layer).*

- **LAN: MAC Addresses (physical addresses)**. (e.g. `00:1A:2B:3C:4D:5E` with IPv4 (Internet Protocol version 4))
    - Hardcoded into the Network Interface Card (NIC) of a device.
    - They are unique to each device.
- **Internet: IP Addresses (logical addresses)**. (e.g., `192.168.1.1`)
    - Routable accross the global internet (unless not).
    - Assigned by network administrators or ISPs.
    - Can be static (permanent) or dynamic (temporary).
- **Application layer: Domain Names (human-readable addresses)**. (e.g., `www.example.com`)
    - Translated to IP addresses using DNS (Domain Name System).

**Potential attacks:**

- **[Spoofing](../Terminology/Attacks/Spoofing)**: Faking the source address of a packet to impersonate another device. (MAC or IP address in packets.)
- Attacks on the mappings between different addresses: ARP (Address Resolution Protocol) poisoning (mapping between MAC and IP), DNS cache poisoning (mapping between domain names and IP addresses).

Between these addresses there exist mappings:

- MAC ↔ IP: ARP (Address Resolution Protocol)
    - Used to map a device’s MAC address to its IP address within a local network.
- Domain Name ↔ IP: DNS (Domain Name System)
    - Translates human-readable domain names to IP addresses.

### 2. Finding the path to the destination

*Problem: How does a packet know which wire leads to the destination?Solution: Routing (network layer).*

- **Layer 2 (LAN)**: MAC address table / Switching table in a switch.
    - The MAC address table maps MAC addresses to specific ports on the switch.
    - When a switch receives a packet, it looks up the destination MAC address in its table to determine which port to forward the packet to.
    - If the destination MAC address is not in the table, the switch broadcasts the packet to all ports except the one it was received on.
    - The switching table is built dynamically as the switch learns the MAC addresses of connected devices.
- **Layer 3 (Internet)**: Routers have routing tables.
    - Routing tables contain information about the paths to different networks, the next hop for each possible destination, and metrics to determine the best path.
    - Routing protocols (like OSPF (Open Shortest Path First), BGP (Border Gateway Protocol)) are used to exchange information between routers and update their routing tables.
    - When a router receives a packet, it looks up the destination IP address in its routing table to determine the best path to forward the packet.
    - Routers use routing protocols (like OSPF, BGP) to exchange information about network topology and update their routing tables.

**Potential attacks:**

- Attacks on the tables or devices themselves, e.g., routing table poisoning, MAC table overflow attacks.
- Attacks on the protocols that make the tables, e.g., OSPF attacks, BGP hijacking.

### 3. Application Multiplexing

*Problem: Which application on the destination device should receive the packet?Solution: Ports (transport layer).*

- Well known ports: 0-1023 (e.g., HTTP: 80, HTTPS: 443, FTP: 21, SSH: 22).
- Ephemeral ports: randomly assigned ports for temporary communication (1024-65535) for client apps (e.g., your browser tab).
- Sockets: IP Address + Port number = Unique connection identifier. (E.g., `192.168.1.1:80` for a web server.)

**Security context: [Attack surface](../Terminology/Attack Surface).**
Every open port is a potential entry point for attackers. Services listening on ports can have vulnerabilities that can be exploited.
Port scanning (e.g., `nmap`) is a technique used by attackers (and security professionals) to identify open ports on a target system. Tools like Nmap can be used for this purpose. It’s essentially a reconnaissance phase where attackers knock on the doors (ports) to see which ones are open. In many countries this is a criminal offense if done without permission.

### Communication language: What is a protocol?

- **Definition:** A protocol is a set of rules and conventions that govern how data is transmitted and received over a network.
- **Components of a protocol:**
    1. Syntax: Structure or format of the data. (e.g., headers, fields, structure, etc.)
    2. Semantics: Meaning of the data. (what the bits represent)
    3. Timing: When data should be sent and how fast.
    4. Expected behavior: How devices should respond to different situations.

**Security context: Protocol vs. Reality.**
Security vulnerabilities often arise when the implementation (code) assumes that the other party will follow the protocol correctly, but in reality, attackers may exploit weaknesses in the implementation or deviate from the protocol to gain unauthorized access or disrupt communication.

## Physical + (Data) Link Layer

(We’ll cover more layers tomorrow)

- Transmitting and receiving raw bit streams over a physical medium.
- Synchronization between the sender and receiver clocks.
- Encoding & Signaling: defining how bits are represented on the medium (e.g., electrical voltages, light pulses, radio waves).

**Security context: Physical security.**

- **Wiretapping**: Copper emits electromagnetic signals that can be intercepted.
- **Jamming**: Disrupting wireless signals to prevent communication. DoS against the physical medium.
- **Rogue devices**: Unauthorized devices connected to the network (e.g., rogue access points). Like plugging an attacker’s device directly into a wall port to circumvent the firewall.
- **Rule #1**: If an attacker can physically access your network, then software-based security measures can’t save it.

### Link Layer Functions

Node-to-node data transfer on the same network

- **Framing**: Packaging bits into frames (data link layer PDU).
    - A frame typically includes a header (with source and destination MAC addresses), payload (the actual data), and a trailer (for error checking).
- **Error detection and correction**: Detecting and correcting errors that may occur during transmission (e.g., CRC - Cyclic Redundancy Check).
    - Error detection: Identifying errors in transmitted data using techniques like parity checks, checksums, and CRC.
- **Medium access control**: Determining how devices share the physical medium (e.g., CSMA/CD - Carrier Sense Multiple Access with Collision Detection for Ethernet).
    - Controlling access to the shared communication medium to avoid collisions and ensure fair usage among multiple devices.
- **Flow control**: Don’t send faster than the receiver can handle.
    - Techniques like sliding window protocols to manage the rate of data transmission between sender and receiver.
- Provide an interface to the Network Layer that is (somewhat) independent of the type of physical medium.
    - E.g., Ethernet, Wi-Fi, PPP (Point-to-Point Protocol).

### Link Layer Protocols

- **Ethernet (IEEE 802.3):**
    - The standard for wired local area networks (LANs).
    - In practice often Point-to-Point connections (switch to end device), but technically supports a shared medium (the wire, the bus).
    - Mechanism: Random access with collision detection (CSMA/CD - Carrier Sense Multiple Access with Collision Detection).
- **Wi-Fi (IEEE 802.11):**
    - Uses a shared medium (radio waves). Every packet is broadcast to all devices within range.
    - Mechanism: Random access with collision avoidance (CSMA/CA).
- **Bluetooth (IEEE 802.15.1):**
    - Type: PAN (Personal Area Network).
    - Mechanism: Master/Slave topology using Frequency Hopping Spread Spectrum (FHSS) to avoid interference.
- **USB (Universal Serial Bus):**
    - Mechanism: Host-Controller architecture with polling.
    - Unlike Ethernet, devices speak only when the Host (computer) asks them to.

Currently he’s showing us Wireshark. Wireshark is a network protocol analyzer that captures and displays packets in real-time. It allows you to see the details of network traffic, including headers, payloads, and protocols used.
Basically, you can see all the packets being sent and received on your network interface.
We can see:

- The frame number.
- The ethernet frame details (source and destination MAC addresses, type).
- The IP packet details (source and destination IP addresses, protocol).
    - Inside it is a UDP (User Datagram Protocol) segment, and in it we see the source and destination ports, length, checksum.
- Domain Name System (DNS) query details.

It’s very nice to inspect the packets and what’s going on, network-wise, in your system.

He shows us the ARP (Address Resolution Protocol) packets. ARP is used to map IP addresses to MAC addresses within a local network.
When a device wants to communicate with another device on the same network, it sends an ARP request to ask “Who has this IP address?” The device with that IP address responds with its MAC address.

If a computer doesn’t know the MAC address of a device it wants to communicate with, it sends out an ARP request as a broadcast to all devices on the local network. The device with the matching IP address responds with its MAC address.

He goes into the terminal and runs `arp -n` to see the ARP table on his system. It shows:

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

If you get several responses to an ARP request, you might be under an ARP [spoofing](../Terminology/Attacks/Spoofing) attack. Because normally only one device should respond with its MAC address.

### Layer 2 Vulnerabilities: Wired Networks

ARP Poisoning → Man-in-the-Middle (MitM) Attack.

- Mechanism: Send fake ARP replies to associate the attacker’s MAC address with the IP address of another device (e.g., the gateway).
- Result: Traffic intended for the target device is sent to the attacker instead.
- Mitigation: Use static ARP entries, ARP spoofing detection tools, or switch to IPv6 (which uses NDP - Neighbor Discovery Protocol).

MAC flooding

- Mechanism: Send a large number of fake MAC addresses to the switch to overflow its MAC address table.
- Result: The switch enters “fail-open” mode and broadcasts all incoming traffic to all ports, allowing the attacker to capture sensitive data.
- Mitigation: Use port security features on switches to limit the number of MAC addresses per port.

### Bluetooth.

Nothing more to say. Bluetooth *is* a vulnerability. It’s a complex mess that has a lot of problems.

### Layer 2 Vulnerabilities: Wireless Networks

**Rogue Access Points (E.g., “wifi pinapple”)**

- **Mechanism**: Set up an unauthorized access point with the same SSID (network name) as a legitimate one.
- **Result**: Users unknowingly connect to the rogue AP, allowing the attacker to intercept and manipulate their traffic.
- **Mitigation**: Use strong authentication and encryption (e.g., WPA3), and educate users about verifying network names.

**Deauthenticaiton / Jamming (DoS)**

- **Mechanism**: Send deauthentication frames to disconnect users from a legitimate access point.
- **Goal**: Disrupt communication or force users to connect to a rogue AP.
- **Mitigation**: Use management frame protection (e.g., 802.11w).

### Layer 2 Vulnerabilities: Physical

**Physical Interface Trust (e.g., BadUSB)**

- **Mechanism**: An attacker plugs a malicious device (e.g., USB stick) into a trusted system.
- **Result**: The malicious device can exploit vulnerabilities in the system or network.
- **Mitigation**: Physical security measures (e.g., locked server rooms, port security).

## Further studies

- Find examples of vulnerabilities and attacks using Bluetooth and learn why Bluetooth is a terrible protocol.
- What is the best protection against Bluetooth attacks?
- How to prevent or defend against attacks that use Rogue Access Points? Distinguish between what individuals and what organizations can do

[Lab 6 (W2-G3)](OSINT%20&%20Networks%202025-12-01/Lab%206%20(W2-G3).md)
