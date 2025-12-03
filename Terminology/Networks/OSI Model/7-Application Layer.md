---
aliases: [Application Layer]
date created: Tuesday, 2. December 2025, 10:12
date modified: Tuesday, 2. December 2025, 20:12
---

# 7-Application Layer
The **Application Layer** is the seventh and highest layer in the [OSI Model](OSI%20Model.md) of computer networking. It is responsible for providing network services directly to end-user applications. The Application Layer facilitates communication between software applications and the underlying network, enabling users to access network resources and serThe AppThe Application Layer encompasses a wide range of protocols and services, including [HTTP](../Transfer%20Protocols/HTTP.md) for web browsing, [FTP](../Transfer%20Protocols/FTP.md) for file transfers, [SMTP](../Transfer%20Protocols/SMTP.md) for email communication, and [DNS](DNS.md) for domain name resolution.

The Application Layer also handles various functions such as resource sharing, remote file access, and network management. It provides an interface for applications to interact with the network, allowing users to perform tasks such as sending emails, browsing the web, and transferring files.

The Application Layer works closely with the [Presentation Layer](6-Presentation%20Layer.md) to ensure that data is properly formatted and presented to the user.

## The Web: HTTP vs. HTTPS
**HTTP (Port 80)**:
- Request/response protocol. (GET, POST, PUT, DELETE, ...)
- Stateless (each request is independent), cleartext (no encryption).
- Risk: Everything is visible to anyone who can intercept the traffic (e.g., passwords, cookies, personal data).
- Vulnerabilities: Anyone on the network path (in the same Wi-Fi or [LAN](../LAN.md)) can eavesdrop (packet sniffing).

**HTTPS (Port 443)**:
- HTTP inside a TLS (Transport Layer Security) tunnel.
- Security: Encryption, integrity, authentication.
- Prevents listening in, but also Man-in-the-Middle attacks (if the attacker can’t get a valid certificate).
- Certificates: Issued by Certificate Authorities (CAs) to verify the identity of websites and enable secure connections.
