# Cryptography

Cryptography is the practice and study of techniques for secure communication in the presence of adversarial behavior.

## Fundamental Concepts

### Symmetric Encryption
Uses the same key for both encryption and decryption.

**Common Algorithms:**
- AES (Advanced Encryption Standard)
- DES/3DES
- ChaCha20

**Use Cases:**
- Bulk data encryption
- Secure file storage
- VPN tunnels

### Asymmetric Encryption
Uses a pair of keys: a public key for encryption and a private key for decryption.

**Common Algorithms:**
- RSA
- ECC (Elliptic Curve Cryptography)
- Diffie-Hellman

**Use Cases:**
- Secure key exchange
- Digital signatures
- TLS/SSL certificates

### Hash Functions
One-way functions that produce a fixed-size output from variable-size input.

**Common Hash Functions:**
- SHA-256, SHA-3
- BLAKE2
- Argon2 (for passwords)

**Properties:**
- Deterministic
- Pre-image resistant
- Collision resistant

### Digital Signatures
Provide authenticity, integrity, and non-repudiation.

**Process:**
1. Hash the message
2. Encrypt the hash with private key
3. Recipient verifies with public key

## Key Management

### Best Practices
1. Generate keys using cryptographically secure random number generators
2. Store keys securely (HSMs, key vaults)
3. Implement key rotation policies
4. Use appropriate key lengths
5. Destroy keys securely when no longer needed

### Public Key Infrastructure (PKI)
A framework for managing digital certificates and public-key encryption:
- Certificate Authorities (CAs)
- Registration Authorities (RAs)
- Certificate Revocation Lists (CRLs)
- OCSP (Online Certificate Status Protocol)
