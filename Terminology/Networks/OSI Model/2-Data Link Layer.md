---
aliases: [Data Link Layer]
date created: Tuesday, 2. December 2025, 10:12
date modified: Thursday, 11. December 2025, 09:12
---

# Data Link Layer

The **Data Link Layer** is the second layer in the [OSI Model](OSI%20Model.md) of computer networking. It is responsible for establishing, maintaining, and terminating a reliable link between two directly connected nodes on a network.

The Data Link Layer handles error detection and correction, as well as flow control, to ensure that data is transmitted accurately and efficiently over the physical medium. It also manages the framing of data packets, adding headers and trailers to create frames that can be transmitted over the network.

The Data Link Layer is divided into two sublayers:

1. the [Media Access Control](../MAC.md) (MAC) layer, which controls access to the physical medium,
2. and the Logical Link Control (LLC) layer, which manages communication between devices on the same network.

The Data Link Layer works closely with the [Physical Layer](Physical%20Layer.md) to provide reliable data transfer over the physical medium.

## Link Layer Functions

Node-to-node data transfer on the same network

- **Framing**: Packaging bits into frames (data link layer PDU).
    - A frame typically includes a header (with source and destination MAC addresses), payload (the actual data), and a trailer (for error checking).
- **Error detection and correction**: Detecting and correcting errors that may occur during transmission (e.g., CRC - Cyclic Redundancy Check).
    - Error detection: Identifying errors in transmitted data using techniques like parity checks, checksums, and CRC.
- **Medium access control**: Determining how devices share the physical medium (e.g., CSMA/CD - Carrier Sense Multiple Access with Collision Detection for Ethernet).
    - Controlling access to the shared communication medium to avoid collisions and ensure fair usage among multiple devices.
- **Flow control**: Don’t send faster than the receiver can handle.
    - Techniques like sliding window protocols to manage the rate of data transmission between sender and receiver.
- Provide an interface to the [Network Layer](3-Network%20Layer.md) that is (somewhat) independent of the type of physical medium.
    - E.g., Ethernet, Wi-Fi, PPP (Point-to-Point Protocol).

## Link Layer Protocols

- **Ethernet (IEEE 802.3):**
    - The standard for wired [Local Area Networks (LANs)](../LAN.md) .
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
