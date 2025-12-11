---
aliases: [Open Systems Interconnection]
date created: Tuesday, 2. December 2025, 19:12
date modified: Monday, 8. December 2025, 18:12
---

# OSI Model

The most common model is the OSI (Open Systems Interconnection) model, which has seven layers:

1. **[Physical Layer](1-Physical Layer.md) (Layer 1):** Deals with the physical connection between devices, including cables, [Switches](../Network hardware/Switch.md), and other hardware.
2. **[Data Link Layer](2-Data Link Layer.md) (Layer 2):** Responsible for node-to-node (a node here is a device or a point of connection in a network) data transfer and error detection/correction. (E.g., Ethernet, [MAC](<../MAC.md>) addresses.)
3. **[Network Layer](3-Network Layer.md) (Layer 3):** Manages data routing and forwarding between different networks. (E.g., [IP](../TCP IP Model/IP.md) addresses, [routers](../Network hardware/Router.md).) Basically, connections that are *more* than one hop away.
4. **[Transport Layer](4-Transport Layer.md) (Layer 4):** Ensures reliable data transfer between end devices. (E.g., [TCP](../TCP IP Model/TCP.md), [UDP](<../UDP.md>).). It essentially manages end-to-end communication. Ensuring that data is delivered error-free, in sequence, and with no losses or duplications.
5. **[Session Layer](5-Session Layer.md) (Layer 5):** Manages sessions or connections between applications. Establishes, maintains, and terminates connections. (E.g., APIs, sockets.)
6. **[Presentation Layer](6-Presentation Layer.md) (Layer 6):** Translates data formats between the application and the network. Handles data encryption, compression, and translation. (E.g., SSL/[TLS](<../TLS.md>), data encoding.)
7. **[Application Layer](7-Application Layer.md) (Layer 7):** Provides network services directly to end-user applications. (E.g., [HTTP](../Transfer Protocols/HTTP.md), [FTP](../Transfer Protocols/FTP.md), [SMTP](../Transfer Protocols/SMTP.md).). Services like web browsing, email, file transfer, etc.
