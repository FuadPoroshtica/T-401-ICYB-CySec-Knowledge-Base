---
aliases: [User Datagram Protocol]
date created: Tuesday, 2. December 2025, 19:12
date modified: Monday, 8. December 2025, 18:12
---

# UDP
The **User Datagram Protocol (UDP)** is a communication protocol used across the Internet for time-sensitive transmissions such as video playback or [DNS](/DNS) lookups.
UDP is a connectionless protocol, meaning it does not establish a dedicated end-to-end connection before sending data.
This allows for faster data transmission but does not guarantee delivery, order, or error-checking.
UDP operates at the [Transport Layer](OSI%20Model/4-Transport%20Layer.md) (Layer 4) of the [OSI Model](OSI%20Model/OSI%20Model.md), alongside [TCP (Transmission Control Protocol)](TCP%20IP%20Model/TCP.md).
It is often used in applications where speed is more critical than reliability, such as online gaming, live streaming, and voice over IP (VoIP).

UDP packets, known as datagrams, contain source and destination [ports](../Systems%20&%20Plaforms/Port.md), length, and a checksum for error-checking.
Because of its low overhead, UDP is suitable for applications that require efficient transmission of small amounts of data without the need for acknowledgment or retransmission.

However, due to its lack of reliability features, UDP is not ideal for applications that require guaranteed delivery of data, such as file transfers or web browsing.
UDP is commonly used in conjunction with other protocols, such as the [Domain Name System (DNS)](DNS.md) and the [Dynamic Host Configuration Protocol (DHCP)](DHCP.md), to facilitate various network services.
