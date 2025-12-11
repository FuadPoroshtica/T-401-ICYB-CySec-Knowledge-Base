---
aliases: []
date created: Thursday, 11. December 2025, 09:12
date modified: Thursday, 11. December 2025, 09:12
---

# 2025-12-11 Introduction to Cyber Security Course Summary (Gísli)
- He’s currently going over the material in a different order, an order that “makes more sense”.

## Defense in Depth
- Least privilege:
	- Only give users the bare minimum privileges that they need
- Fail-safe defaults:
	- TODO
- Economy of Mechanism:
	- TODO
- Complete mediation:
	- ...always check access for every access, something
- Open design:
	- The opposite of security by obscurity. It shouldn’t depend on security by obscurity. The system should be easy to understand so that it is easy to analyze what is going on for forensics.
- Psychological acceptability:
	- Your security principles need to be accepted by the user, or else the user will circumvent it.
	- E.g. if you have super super complicated passwords, then the users might just write it down on a sticky note and basically make it completely useless.

### The layered approach

Every part of the system needs to be secure, there shouldn’t be just one super secure layer.

If one layer fails, the next one should catch it.

## Computer Networks

He’s not expecting us to know everything about computer networks, but we should understand the basics.

We should know:

- It’s organized into layers in [OSI Model](../Terminology/Networks/OSI%20Model/OSI%20Model.md) and [TCP IP Model](../Terminology/Networks/TCP%20IP%20Model/TCP%20IP%20Model.md). We don’t have to memorize the layer numbers.
- Data is split up into packets.
- The packets don’t just make one hop, they hop again and again between places.
	- Just like packages you get in the mail! They transfer between transport hubs!
- The packets are re-assembled on the other side.

### Identity & Addressing
*Problem: how do we identify a device among billions?*
todo

### Finding the path
*Problem: How does a packet know which wire leads to the destination?*
It uses routing tables.
- Layer 2(LAN): MAC address table / switching table

### [Physical Layer](../Terminology/Networks/OSI%20Model/1-Physical%20Layer.md)

For the cyber security final exam, we should know roughly what the purpose is of these layers, and have some idea of how this can be attacked.

## Link layer

Node-to-node delivery on the same network/medium.

- Ethernet
- WiFi

## [Network Layer](../Terminology/Networks/OSI%20Model/3-Network%20Layer.md)

Delivery of packets to devices anywhere in the network.

This requires:

- Addressing (IP addresses)
    - Routing (finding the path)
- Forwarding (moving the packet from one link to another)

## [Transport Layer](../Terminology/Networks/OSI%20Model/4-Transport%20Layer.md)

Application multiplexing (ports). Essentially, it makes sure that data gets to the right application on the device.

Security context:

- Open ports are potential attack vectors.
  - An open port is like an open door into your house. The definition of an open port is that there is an application listening on that port.
  - We can find/scan for open ports using tools like `nmap`.
- TCP SYN flooding attack:
  - The attacker sends a lot of TCP SYN packets to a target server, but never completes the handshake. This leaves the server with a lot of half-open connections, consuming resources and potentially leading to a denial of service (DoS).
  - Mitigation strategies include SYN cookies, increasing backlog queue size, and reducing the SYN-RECEIVED timer.

## [Application Layer](../Terminology/Networks/OSI%20Model/7-Application%20Layer.md)

Responsible for providing network services directly to end-users and applications.

Various protocols operate at this layer, including:

- [HTTP](../Terminology/Networks/Transfer%20Protocols/HTTP.md) and [HTTPS](../Terminology/Networks/Transfer%20Protocols/HTTPS.md) (we should be aware of the difference between them)
  - These are the protocols used for web browsing.
- [TLS (Transport Layer Security)](../Terminology/Networks/TLS.md) for CIA (Confidentiality, Integrity, Availability)
  - Provides encryption and secure communication over a network.
- SSH (vs Telnet)
  - Secure Shell (SSH) is a protocol for secure remote login and other secure network services over an insecure network. It encrypts the session, making it secure against eavesdropping, connection hijacking, and other attacks.
  - Telnet, on the other hand, transmits data in plaintext, making it vulnerable to interception and attacks.
- [DNS](../Terminology/Networks/DNS.md) (Domain Name System)
  - Translates human-readable domain names (like `www.example.com`) into IP addresses that computers use to identify each other on the network.
- [DHCP](../Terminology/Networks/DHCP.md) (Dynamic Host Configuration Protocol)
  - Automatically assigns IP addresses and other network configuration parameters to devices on a network, allowing them to communicate effectively.
- Email: [SMTP](../Terminology/Networks/Transfer%20Protocols/SMTP.md), IMAP, POP3
    - [SMTP (Simple Mail Transfer Protocol)](../Terminology/Networks/Transfer%20Protocols/SMTP.md) is used for sending emails.
	- IMAP (Internet Message Access Protocol) and POP3 (Post Office Protocol version 3) are used for retrieving emails from a mail server.
	- POP3 downloads the email to the local device and usually deletes it from the server, while IMAP allows users to view and manage their emails directly on the server, keeping them synchronized across multiple devices.
- File sharing/file transfer: [FTP](../Terminology/Networks/Transfer%20Protocols/FTP.md), SFTP, SMB
	- [FTP](../Terminology/Networks/Transfer%20Protocols/FTP.md) (File Transfer Protocol) is used for transferring files between a client and server on a network. It is not secure as it transmits data in plaintext.
	- SFTP (SSH File Transfer Protocol) is a secure version of FTP that uses SSH to encrypt the data transfer.
	- SMB (Server Message Block) is a network file sharing protocol that allows applications and users to read and write to files and request services from server programs in a computer network. It is commonly used in Windows environments.

## Network Security
- [Firewall](../Terminology/Defense%20&%20Control/Firewall.md) (packet filter)
  - What the [Firewall](../Terminology/Defense%20&%20Control/Firewall.md) actually does is that it filters packets based on rules.
  - The definition of a [Firewall](../Terminology/Defense%20&%20Control/Firewall.md) is: “A network security device that monitors and filters incoming and outgoing network traffic based on an organization’s previously established security policies.”
  - It can block or allow traffic based on IP addresses, ports, protocols, etc.
- VPN (Virtual Private Network)
	- A VPN creates a secure, encrypted connection over a less secure network, such as the internet. It allows users to send and receive data as if their devices were directly connected to a private network.
	- It provides confidentiality and integrity for data in transit.

# Operating System
## What is an [OS](../Terminology/Systems%20&%20Plaforms/Operating%20System.md)?
- Know the difference between the [Kernel](../Terminology/Systems%20&%20Plaforms/Kernel.md) and user space.
- Core functionality
  - Abstracton from raw hardware interfaces. E.g., instead of having to know how to talk to a hard drive, you can just use file system calls.
  - Arbitration / Resource management for multiple processes/users. Essentially deciding who gets to use what resources when.
  - Process management / scheduling. Running multiple processes at the same time on the same CPU core.
  - File systems. Managing how data is stored and retrieved on storage devices.
  - Protection (kernel vs. user space, user A vs. user B, process X vs process Y). Making sure that processes and users can’t interfere with each other in unauthorized ways.
- Trusted computing base (TCB)
  - The TCB is the set of all hardware, software, and controls that are **critical to a system’s security**.
	  - It includes the OS kernel, security mechanisms, and any other components that enforce security policies.
  - The TCB is responsible for maintaining the confidentiality, integrity, and availability of the system.
  - The smaller the TCB, the easier it is to analyze and secure.
- Logging (for intrustion detection and forensics)
  - The OS should log security-relevant events, such as login attempts, file access, and system changes. These logs can be used for intrusion detection and forensic analysis in case of a security incident.

## OS Security

Issues:

- Memory Safety: Buffer Overflows.
  - A buffer overflow occurs when a program writes more data to a buffer (a contiguous block of memory) than it can hold. This can overwrite adjacent memory, leading to unpredictable behavior, crashes, or security vulnerabilities.
  - Attackers can exploit buffer overflows to inject malicious code into a program’s memory space, allowing them to take control of the program or system.
  - Common mitigation techniques include bounds checking, stack canaries, and using safer programming languages.
- Race Conditions (in access control), e.g., TOCTOU
  - Race conditions occur when the behavior of a program depends on the timing or sequence of uncontrollable events, such as the order in which threads are scheduled. This can lead to unexpected behavior and security vulnerabilities.
  - TOCTOU (Time of Check to Time of Use) is a specific type of race condition where a resource is checked for a certain condition (e.g., access permissions) and then used later, but the condition may have changed in the meantime.
  - Attackers can exploit TOCTOU vulnerabilities to gain unauthorized access to resources.
- Command Injection
  - Command injection is a security vulnerability that occurs when an attacker is able to execute arbitrary commands on a host operating system via a vulnerable application. This typically happens when user input is not properly sanitized and is passed directly to a system shell or command interpreter.
  - Attackers can exploit command injection vulnerabilities to gain unauthorized access, manipulate data, or compromise the system.
  - Mitigation strategies include input validation, using parameterized queries, and avoiding the use of system shells for executing commands.
- Privilege Escalation
  - Privilege escalation is a security vulnerability that allows an attacker to gain elevated access to resources that are normally protected from an application or user. This can occur through various means, such as exploiting software vulnerabilities, misconfigurations, or weaknesses in access control mechanisms.
  - There are two types of privilege escalation: vertical (gaining higher privileges, e.g., from user to admin) and horizontal (gaining access to resources of another user with the same privilege level).
  - Common mitigation techniques include regular patching, proper access control, and using the principle of least privilege.
- Rootkits
  - A rootkit is a type of malicious software designed to gain unauthorized root or administrative access to a computer system while hiding its presence. Rootkits can modify system files, processes, and configurations to evade detection by traditional security measures.
  - Attackers use rootkits to maintain persistent access to compromised systems, often for malicious purposes such as data theft, espionage, or launching further attacks.
  - Detection and removal of rootkits can be challenging, and mitigation strategies include using specialized rootkit detection tools, maintaining up-to-date security software, and regularly monitoring system integrity.
Important concepts:
- User (and process) permissions
- Root/Admin vs. User
- SUID on Unix
  - The SUID (Set User ID) is a special type of file permission in Unix and Linux operating systems that allows a user to execute a file with the permissions of the file owner, rather than the permissions of the user who is executing the file.
  - This is commonly used for executable files that require elevated privileges to perform certain tasks, such as changing passwords or accessing system resources.
  - While SUID can be useful, it also poses security risks if not managed properly, as it can potentially allow unauthorized users to gain elevated privileges.

# Virtualization
## Types

What types we need to know for the exam:

- Different types:
	- Hypervisor / Virtual Machine
	- Container (e.g., Docker)
	- Emulation
- ... offer different
	- Isolation from each other,
	- Separation from the host,
	- Performance / cost.
- Main security issues:
	- VM/Container escape.
    	- When an attacker manages to break out of a virtual machine or container and gain access to the host system or other virtual machines/containers running on the same host.
	- Attacks on other containers/images on the same host (e.g., side-channel attacks)

# Binary Exploitation

We should understand what is a buffer overflow, and how it can be exploited. Writing in memory outside the designated buffer for the input.

It can be used to overwrite the return address of a function, so that when the function returns, it jumps to attacker-controlled code. So we can call functions that normally we wouldn’t be able to call, or use parameters that we normally wouldn’t be able to use.
