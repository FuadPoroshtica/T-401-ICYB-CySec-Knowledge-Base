---
aliases: [Open Systems Interconnection]
date created: Tuesday, 2. December 2025, 19:12
date modified: Tuesday, 2. December 2025, 20:12
---

# OSI Model

The most common model is the OSI (Open Systems Interconnection) model, which has seven layers:

1. **[Physical Layer](../Terminology/Networks/OSI%20Model/1-Physical%20Layer.md) (Layer 1):** Deals with the physical connection between devices, including cables, [Switches](../Network%20hardware/Switch.md), and other hardware.
2. **[Data Link Layer](../Terminology/Networks/OSI%20Model/2-Data%20Link%20Layer.md) (Layer 2):** Responsible for node-to-node (a node here is a device or a point of connection in a network) data transfer and error detection/correction. (E.g., Ethernet, [MAC](../MAC.md) addresses.)
3. **[Network Layer](../Terminology/Networks/OSI%20Model/3-Network%20Layer.md) (Layer 3):** Manages data routing and forwarding between different networks. (E.g., [IP](../TCP%20IP%20Model/IP.md) addresses, [routers](../Network%20hardware/Router.md).) Basically, connections that are *more* than one hop away.
4. **[Transport Layer](../Terminology/Networks/OSI%20Model/4-Transport%20Layer.md) (Layer 4):** Ensures reliable data transfer between end devices. (E.g., [TCP](../TCP%20IP%20Model/TCP.md), [UDP](../UDP.md).). It essentially manages end-to-end communication. Ensuring that data is delivered error-free, in sequence, and with no losses or duplications.
5. **[Session Layer](../Terminology/Networks/OSI%20Model/5-Session%20Layer.md) (Layer 5):** Manages sessions or connections between applications. Establishes, maintains, and terminates connections. (E.g., APIs, sockets.)
6. **[Presentation Layer](../Terminology/Networks/OSI%20Model/6-Presentation%20Layer.md) (Layer 6):** Translates data formats between the application and the network. Handles data encryption, compression, and translation. (E.g., SSL/TLS, data encoding.)
7. **[Application Layer](../Terminology/Networks/OSI%20Model/7-Application%20Layer.md) (Layer 7):** Provides network services directly to end-user applications. (E.g., [HTTP](../Transfer%20Protocols/HTTP.md), [FTP](../Transfer%20Protocols/FTP.md), [SMTP](../Transfer%20Protocols/SMTP.md).). Services like web browsing, email, file transfer, etc.
