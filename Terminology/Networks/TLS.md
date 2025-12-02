---
aliases: [Transport Layer Security]
date created: Tuesday, 2. December 2025, 20:12
date modified: Tuesday, 2. December 2025, 20:12
---

# TLS
**TLS (Transport Layer Security)** is a cryptographic protocol designed to provide secure communication over a computer network. TLS is widely used to secure data transmitted over the internet, including web browsing, email, instant messaging, and voice over IP (VoIP).
TLS operates on the [Transport Layer](OSI%20Model/4-Transport%20Layer.md) of the [OSI Model](OSI%20Model/OSI%20Model.md) and is the successor to the earlier Secure Sockets Layer (SSL) protocol.
TLS provides several key security features, including:
- **Encryption:** TLS encrypts data transmitted between a client and server, ensuring that sensitive information remains confidential and protected from eavesdropping.
- **Integrity:** TLS uses message authentication codes (MACs) to ensure that data has not been tampered with during transmission.
- **Authentication:** TLS supports the use of digital certificates to authenticate the identity of the server (and optionally the client), helping to prevent man-in-the-middle attacks.
TLS is commonly used in conjunction with other protocols, such as [HTTPS](Transfer%20Protocols/HTTPS.md) for secure web browsing, [FTPS](../Transfer%20Protocols/FTP.md) for secure file transfers, and [SMTP](Transfer%20Protocols/SMTP.md) for secure email communication.
Overall, TLS is a critical component of modern internet security, providing a secure foundation for online communication and data exchange.

## TLS Handshake
The goal: safely agree on a shared secret key over an insecure wire.
- Asymmetric cryptography (public key) cryptography to exchange a symmetric session key.
	- Used only during setup.
	- Slow, high overhead.
	- Used for Diffie-Hellman key exchange or RSA encryption of the session key.
- Symmetric cryptography (Session key)
	- Used for the actual data transfer.
	- Fast, low overhead.
	- Used for encrypting the data exchanged during the session (e.g., AES).
	- The session key is derived from the key exchange process during the handshake.
- Steps:
  1. Client Hello: Client sends supported TLS versions, cipher suites, and a random nonce.
  2. Server Hello: Server responds with chosen TLS version, cipher suite, its digital certificate, and a random nonce.
  3. Key Exchange: Client and server perform a key exchange (e.g., Diffie-Hellman) to derive a shared session key.
  4. Finished: Both parties send a Finished message encrypted with the session key to confirm that the handshake was successful.
  5. Secure Communication: Subsequent data is encrypted using the agreed-upon session key.
