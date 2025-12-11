---
aliases: [Transport Layer]
date created: Tuesday, 2. December 2025, 10:12
date modified: Thursday, 11. December 2025, 09:12
---

# 4-Transport Layer

The Transport Layer is the fourth layer in the [OSI Model](OSI%20Model.md) of computer networking.

It is responsible for providing reliable data transfer services between end systems, ensuring that data is delivered accurately and in the correct order.

The Transport Layer manages end-to-end communication, including error detection and correction, flow control, and congestion control.

It uses protocols such as the [Transmission Control Protocol (TCP)](../TCP%20IP%20Model/TCP.md) and the [User Datagram Protocol (UDP)](../UDP.md) to facilitate data transfer between applications running on different devices.

The Transport Layer works closely with the [Network Layer](3-Network%20Layer.md) to provide end-to-end data delivery across multiple networks.

## TCP vs. UDP
**UDP (User Datagram Protocol):**
- Connectionless protocol. Fire-and-forget. No handshake, no confirmation.
- Fast, low overhead, no guarantees.
- Use cases: Streaming, gaming, VoIP, [DNS](../DNS.md) queries. For when delivering *fast* is more important than delivering *reliably*.

**TCP (Transmission Control Protocol):**
- Connection-oriented protocol. **3-Way Handshake** (syn, syn-ack, ack) to establish a connection.
	- **SYN**: Client sends a SYN packet to the server to initiate a connection.
	- **SYN-ACK**: Server responds with a SYN-ACK packet to acknowledge the receipt of the SYN and to indicate its willingness to establish a connection.
	- **ACK**: Client sends an ACK packet back to the server to acknowledge the receipt of the SYN-ACK, completing the handshake.
- Guarnteed delivery, in-order delivery, flow control, congestion control.
- Use cases: Web browsing ([HTTP](../Transfer%20Protocols/HTTP.md)/[HTTPS](../Transfer%20Protocols/HTTPS.md)), email ([SMTP](../Transfer%20Protocols/SMTP.md), IMAP), file transfer ([FTP](../Transfer%20Protocols/FTP.md)). For when *reliable* delivery is more important than *fast* delivery.

**Possible attacks:**
- **TCP SYN Flood**: An attacker sends a large number of SYN requests to a target server, but never finishes the handshake by sending the final ACK. This leaves the server with many half-open connections, consuming resources and potentially leading to a denial of service (DoS) for legitimate users.
