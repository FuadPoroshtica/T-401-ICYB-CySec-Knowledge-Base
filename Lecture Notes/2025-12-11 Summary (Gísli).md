---
aliases: []
date created: Thursday, 11. December 2025, 09:12
date modified: Thursday, 11. December 2025, 10:12
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
- [Complete mediation](<../Terminology/Complete mediation.md>):
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

- It’s organized into layers in [OSI Model](<../Terminology/Networks/OSI Model/OSI Model.md>) and [TCP IP Model](<../Terminology/Networks/TCP IP Model/TCP IP Model.md>). We don’t have to memorize the layer numbers.
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
- Layer 2([LAN](<../Terminology/Networks/LAN.md>)): [MAC](<../Terminology/Networks/MAC.md>) address table / switching table

### [Physical Layer](../Terminology/Networks/OSI Model/1-Physical Layer.md)

For the cyber security final exam, we should know roughly what the purpose is of these layers, and have some idea of how this can be attacked.

## Link layer

Node-to-node delivery on the same network/medium.

- Ethernet
- WiFi

## [Network Layer](../Terminology/Networks/OSI Model/3-Network Layer.md)

Delivery of packets to devices anywhere in the network.

This requires:

- Addressing ([IP](<../Terminology/Networks/TCP IP Model/IP.md>) addresses)
    - Routing (finding the path)
- Forwarding (moving the packet from one link to another)

## [Transport Layer](../Terminology/Networks/OSI Model/4-Transport Layer.md)

Application multiplexing (ports). Essentially, it makes sure that data gets to the right application on the device.

Security context:

- Open ports are potential attack vectors.
    - An open port is like an open door into your house. The definition of an open port is that there is an application listening on that port.
    - We can find/scan for open ports using tools like `nmap`.
- <abbr title="Transmission Control Protocol">TCP</abbr> SYN flooding attack:
    - The attacker sends a lot of TCP SYN packets to a target server, but never completes the handshake. This leaves the server with a lot of half-open connections, consuming resources and potentially leading to a denial of service (DoS).
    - Mitigation strategies include SYN cookies, increasing backlog queue size, and reducing the SYN-RECEIVED timer.

## [Application Layer](../Terminology/Networks/OSI Model/7-Application Layer.md)

Responsible for providing network services directly to end-users and applications.

Various protocols operate at this layer, including:

- [HTTP](<../Terminology/Networks/Transfer Protocols/HTTP.md>) and [HTTPS](<../Terminology/Networks/Transfer Protocols/HTTPS.md>) (we should be aware of the difference between them)
    - These are the protocols used for web browsing.
- [TLS](<../Terminology/Networks/TLS.md>) for CIA (Confidentiality, Integrity, Availability) [TLS](<../Terminology/Networks/TLS.md>)
    - Provides encryption and secure communication over a network.
- <abbr title="Secure Shell">SSH</abbr> (vs Telnet)
    - Secure Shell (<abbr title="Secure Shell">SSH</abbr>) is a protocol for secure remote login and other secure network services over an insecure network. It encrypts the session, making it secure against eavesdropping, connection hijacking, and other attacks.
    - Telnet, on the other hand, transmits data in plaintext, making it vulnerable to interception and attacks.
- [DNS](<../Terminology/Networks/DNS.md>) (Domain Name System)
    - Translates human-readable domain names (like `www.example.com`) into IP addresses that computers use to identify each other on the network.
- [DHCP](<../Terminology/Networks/DHCP.md>) (Dynamic Host Configuration Protocol)
    - Automatically assigns IP addresses and other network configuration parameters to devices on a network, allowing them to communicate effectively.
- Email: [SMTP](<../Terminology/Networks/Transfer Protocols/SMTP.md>), <abbr title="Internet Message Access Protocol">IMAP</abbr>, <abbr title="Post Office Protocol Version 3">POP3</abbr>
    - [SMTP (Simple Mail Transfer Protocol)](../Terminology/Networks/Transfer Protocols/SMTP.md) is used for sending emails.
	- <abbr title="Internet Message Access Protocol">IMAP</abbr> (Internet Message Access Protocol) and <abbr title="Post Office Protocol Version 3">POP3</abbr> (Post Office Protocol version 3) are used for retrieving emails from a mail server.
	- <abbr title="Post Office Protocol Version 3">POP3</abbr> downloads the email to the local device and usually deletes it from the server, while <abbr title="Internet Message Access Protocol">IMAP</abbr> allows users to view and manage their emails directly on the server, keeping them synchronized across multiple devices.
- File sharing/file transfer: [FTP](<../Terminology/Networks/Transfer Protocols/FTP.md>), <abbr title="SSH File Transfer Protocol">SFTP</abbr>, <abbr title="Server Message Block">SMB</abbr>
	- [FTP](<../Terminology/Networks/Transfer Protocols/FTP.md>) (File Transfer Protocol) is used for transferring files between a client and server on a network. It is not secure as it transmits data in plaintext.
	- SFTP (<abbr title="Secure Shell">SSH</abbr> File Transfer Protocol) is a secure version of [FTP](<../Terminology/Networks/Transfer Protocols/FTP.md>) that uses <abbr title="Secure Shell">SSH</abbr> to encrypt the data transfer.
	- <abbr title="Server Message Block">SMB</abbr> (Server Message Block) is a network file sharing protocol that allows applications and users to read and write to files and request services from server programs in a computer network. It is commonly used in Windows environments.

## Network Security
- [Firewall](<../Terminology/Defense & Control/Firewall.md>) (packet filter)
    - What the [Firewall](<../Terminology/Defense & Control/Firewall.md>) actually does is that it filters packets based on rules.
    - The definition of a [Firewall](<../Terminology/Defense & Control/Firewall.md>) is: “A network security device that monitors and filters incoming and outgoing network traffic based on an organization’s previously established security policies.”
    - It can block or allow traffic based on IP addresses, ports, protocols, etc.
- <abbr title="Virtual Private Network">VPN</abbr> (Virtual Private Network)
	- A <abbr title="Virtual Private Network">VPN</abbr> creates a secure, encrypted connection over a less secure network, such as the internet. It allows users to send and receive data as if their devices were directly connected to a private network.
	- It provides confidentiality and integrity for data in transit.

# Operating System
## What is an [OS](<../Terminology/Systems & Plaforms/Operating System.md>)?
- Know the difference between the [Kernel](<../Terminology/Systems & Plaforms/Kernel.md>) and user space.
- Core functionality
    - Abstracton from raw hardware interfaces. E.g., instead of having to know how to talk to a hard drive, you can just use file system calls.
    - Arbitration / Resource management for multiple processes/users. Essentially deciding who gets to use what resources when.
    - Process management / scheduling. Running multiple processes at the same time on the same CPU core.
    - File systems. Managing how data is stored and retrieved on storage devices.
    - Protection (kernel vs. user space, user A vs. user B, process X vs process Y). Making sure that processes and users can’t interfere with each other in unauthorized ways.
- **Trusted Computing Base (TCB)**
    - The <abbr title="Trusted Computing Base">TCB</abbr> is the set of all hardware, software, and controls that are **critical to a system’s security**.
	  - It includes the OS kernel, security mechanisms, and any other components that enforce security policies.
    - The <abbr title="Trusted Computing Base">TCB</abbr> is responsible for maintaining the confidentiality, integrity, and availability of the system.
    - The smaller the <abbr title="Trusted Computing Base">TCB</abbr>, the easier it is to analyze and secure.
- Logging (for intrustion detection and forensics)
    - The OS should log security-relevant events, such as login attempts, file access, and system changes. These logs can be used for intrusion detection and forensic analysis in case of a security incident.

## OS Security

Issues:

- Memory Safety: [Buffer Overflows](../Terminology/Attacks/Buffer Overflow.md).
    - A [Buffer Overflow](../Terminology/Attacks/Buffer Overflow.md) occurs when a program writes more data to a buffer (a contiguous block of memory) than it can hold. This can overwrite adjacent memory, leading to unpredictable behavior, crashes, or security vulnerabilities.
    - Attackers can exploit [Buffer Overflows](../Terminology/Attacks/Buffer Overflow.md) to inject malicious code into a program’s memory space, allowing them to take control of the program or system.
    - Common mitigation techniques include bounds checking, stack canaries, and using safer programming languages.
- [Race conditions](../Terminology/Attacks/Race condition.md) (in [Access Control](../Terminology/Defense & Control/Access Control.md)), e.g., <abbr title="Time of Check to Time of Use">TOCTOU</abbr>
    - Race conditions occur when the behavior of a program depends on the timing or sequence of uncontrollable events, such as the order in which threads are scheduled. This can lead to unexpected behavior and security vulnerabilities.
    - TOCTOU (Time of Check to Time of Use) is a specific type of race condition where a resource is checked for a certain condition (e.g., access permissions) and then used later, but the condition may have changed in the meantime.
    - Attackers can exploit <abbr title="Time of Check to Time of Use">TOCTOU</abbr> vulnerabilities to gain unauthorized access to resources.
- Command Injection
    - Command injection is a security vulnerability that occurs when an attacker is able to execute arbitrary commands on a host [Operating System](<../Terminology/Systems & Plaforms/Operating System.md>) via a vulnerable application. This typically happens when user input is not properly sanitized and is passed directly to a system shell or command interpreter.
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
- <abbr title="Set User ID">SUID</abbr> on Unix
    - The <abbr title="Set User ID">SUID</abbr> (Set User ID) is a special type of file permission in Unix and Linux operating systems that allows a user to execute a file with the permissions of the file owner, rather than the permissions of the user who is executing the file.
    - This is commonly used for executable files that require elevated privileges to perform certain tasks, such as changing passwords or accessing system resources.
    - While <abbr title="Set User ID">SUID</abbr> can be useful, it also poses security risks if not managed properly, as it can potentially allow unauthorized users to gain elevated privileges.

# Virtualization
## Types

What types we need to know for the exam:

- Different types:
	- [Hypervisor](<../Terminology/Virtualization/Hypervisor.md>) / [Virtual Machine](../Terminology/Virtualization/Virtual Machine (VM).md)
	- [Container](<../Terminology/Virtualization/Virtualization methods/Container.md>) (e.g., Docker)
	- [Emulation](<../Terminology/Virtualization/Virtualization methods/Emulation.md>)
- ... offer different
	- Isolation from each other,
	- Separation from the host,
	- Performance / cost.
- Main security issues:
	- VM/Container escape.
    	- When an attacker manages to break out of a virtual machine or container and gain access to the host system or other virtual machines/containers running on the same host.
	- Attacks on other containers/images on the same host (e.g., [Side-Channel Attacks](../Terminology/Virtualization/Side-Channel Attack.md))

# [Binary Exploitation](../Terminology/Binary Exploitation/Binary Exploitation.md)
## Buffer Overflow

We should understand what is a [Buffer Overflow](../Terminology/Attacks/Buffer Overflow.md), and how it can be exploited. Writing in memory outside the designated buffer for the input.

It can be used to overwrite the return address of a function, so that when the function returns, it jumps to attacker-controlled code. So we can call functions that normally we wouldn’t be able to call, or use parameters that we normally wouldn’t be able to use.

Part of the difficulty for attackers however is that attackers have to know the exact memory addresses of the code they want to jump to.

### Mitigation techniques

Executing code via buffer overflow is made more difficult by modern mitigations such as ASLR (Address Space Layout Randomization), which randomizes the memory addresses of key data areas of a process, making it harder for attackers to predict where their malicious code will be located.

Stack Canaries are another mitigation technique, which involves placing a small, known value (the canary) before the return address on the stack. If a buffer overflow occurs and overwrites the return address, it will also overwrite the canary. Before returning from the function, the program checks if the canary value has changed; if it has, the program knows that a buffer overflow has occurred and can take appropriate action (such as terminating the program) to prevent exploitation.

# Web Security
## Attack Surface

Server-Side:

- Visible Inputs (Forms, File Uploads)
- Hidden Inputs (<abbr title="Uniform Resource Locator/Universal Resource Locator">URL</abbr> Parameters, HTTP Headers, Cookies)
- <abbr title="Application Programming Interface">API</abbr> endpoints
- Supply Chain
    - The supply chain refers to all the libraries, frameworks, and third-party services that a web application depends on. Vulnerabilities in any of these components can introduce security risks to the application.
Client-Side:
- HTML, CSS, ... → DOM (Document Object Model)
    - The <abbr title="Document Object Model">DOM</abbr> represents the structure of a web page and can be manipulated by scripts, which can introduce security risks such as [Cross-Site Scripting (XSS)](<../Terminology/Attacks/XSS.md>) if not properly handled.
    - Understanding the <abbr title="Document Object Model">DOM</abbr> is crucial for identifying potential vulnerabilities in web applications.
- Client-Side Storage (Cookies, Access Tokens, ...)
    - Client-side storage mechanisms can be exploited if sensitive data is not properly protected, leading to risks such as session hijacking or unauthorized access.
- (Third-Party) Scripts
    - Third-party scripts can introduce vulnerabilities if they are compromised or malicious, potentially leading to attacks such as data theft or unauthorized actions on behalf of the user.

## Key Vulnerabilities
- [SQL Injection / SQLi](../Terminology/Web Security/SQL Injection (SQLi).md)
    - [SQL Injection (SQLi)](../Terminology/Web Security/SQL Injection (SQLi).md) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It occurs when user input is improperly sanitized and is directly included in <abbr title="Structured Query Language">SQL</abbr> queries. This can allow attackers to view, modify, or delete data in the database, as well as execute administrative operations.
    - *Mitigation*: Common mitigation techniques include using prepared statements and parameterized queries, input validation, and employing least privilege principles for database access.
- [Insecure Direct Object References (IDOR)](../Terminology/Insecure Direct Object References (IDOR).md)
    - [Insecure Direct Object References (IDOR)](../Terminology/Insecure Direct Object References (IDOR).md) is a web security vulnerability that occurs when an application exposes a reference to an internal implementation object, such as a file, database record, or <abbr title="Uniform Resource Locator/Universal Resource Locator">URL</abbr>, without proper [Access Control](../Terminology/Defense & Control/Access Control.md). This allows attackers to manipulate these references to gain unauthorized access to data or functionality.
    - *Example*: An application that uses sequential numeric IDs in <abbr title="Uniform Resource Locator/Universal Resource Locator">URL</abbr>s (e.g., `/user/123`) without verifying the user’s authorization to access that resource.
    - *Mitigation*: Mitigation strategies include implementing proper [Access Controls](../Terminology/Defense & Control/Access Control.md), validating user input, and using indirect references
- [Broken Authentication](../Terminology/Web Security/Broken Authentication.md) (passwords, session ids, tokens)
    - [Broken Authentication](../Terminology/Web Security/Broken Authentication.md) refers to vulnerabilities in the authentication mechanisms of a web application that allow attackers to compromise user accounts or gain unauthorized access. This can occur due to weak password policies, session management flaws, or inadequate protection of authentication credentials.
    - *Mitigation*: Mitigation techniques include implementing strong password policies, using multi-factor authentication, securely managing sessions, and regularly reviewing authentication mechanisms for vulnerabilities.
- [Cross-Site Scripting (XSS)](<../Terminology/Attacks/XSS.md>)
⇒ [OWASP](<../Terminology/Web Security/OWASP.md>) Top-Ten
The main problem with “Vibe Coding” is that it encourages developers to write code quickly without actually understanding it or considering security implications.

# AI
## Attack Surfaces
- Input Surface
  - User Prompts. Malicious users can craft prompts to manipulate the AI into generating harmful or unintended outputs.
  - Uploaded Documents. If the AI processes uploaded documents, attackers can embed malicious content to exploit vulnerabilities in the AI system.
  - Web Search results. If the AI uses web search results to inform its responses, attackers can manipulate search results to influence the AI’s output.
  - *Attack Vectors*: [Prompt Injection](../Terminology/Artifical Intelligence/Prompt Injection.md), Jailbreaking.
- Model Surface
  - Weights & Embeddings. Attackers can manipulate the model’s weights or embeddings to alter its behavior.
  - The neural network file. If attackers gain access to the model file, they can modify it to introduce vulnerabilities or change its functionality.
  - *Attack Vectors*: Extraction of (private) training data, [Backdoors](<../Terminology/Attacks/Backdoor.md>).
- Agency Surface
  - Plugins, <abbr title="Application Programming Interface">API</abbr> calls, Code Execution. If the AI has access to external plugins, <abbr title="Application Programming Interface">API</abbr>s, or can execute code, attackers can exploit these capabilities to perform malicious actions.
  - *Attack Vectors*: Confused deputies (tricking the model into doing something it has the ability to do, but shouldn’t)

## AI-Enabled Cybercrime

GenAI lowers the barrier of entry for attackers.

- Polymorphic Malware
  - Using LLMs to generate unique variants of malware that can evade traditional signature-based detection methods.
- Social Engineering at Scale:
  - Phishing: Generating convincing phishing emails or messages tailored to specific targets.
  - Deepfakes: Creating realistic fake audio or video content to impersonate individuals for fraudulent
- Vulnerability Discovery
  - Using AI to analyze software code and identify potential vulnerabilities more efficiently than traditional methods.

# Societal Aspects
## What is OSINT?

Should know what this is.

## What is OPSEC (Operational Security)?

We should know: Why is this important? Why should you know this even if you don’t do anything illegal?

## Phishing Website Detection

We should know:

- What are they?
- Why is it difficult to detect them?
- Basic techniques for detecting them.
- Why are they created and how?
- Attackers can’t put too many resources in, which makes it easier to detect them.
- *Mitigation:*
    - **User education.** We need to educate users to recognize phishing attempts and be cautious when clicking on links or providing sensitive information.
    - **Email filtering.** Implementing robust email filtering systems can help identify and block phishing emails before they reach users.
    - **Browser security features.** Modern browsers often include features that can help detect and warn users about potential phishing websites.
    - **<b><abbr title="Uniform Resource Locator/Universal Resource Locator">URL</abbr></b> analysis tools.** Using tools that analyze <abbr title="Uniform Resource Locator/Universal Resource Locator">URL</abbr>s for suspicious patterns or characteristics can help identify phishing sites.

## Information Warfare
- *Attack surface:* There has been a shift from broadcast media to social media.
- Actors can be state sponsors, mercenaries.
- *Tactics:* Astroturfing (fake grassroots movements), bots, trolls, troll armies, deepfakes.
- *Detection:* Anomalies such as “bot holidays” (sudden drops in activity because they all shift their attention to something else), all protesters suspiciously using the same posters (unrealistic).
- *Strategic goal:* Unlike Cyber Warfare, the goal is not to take down systems, but to influence populations. Information warfare hacks human psychology and perception rather than computer systems.
- *Defense:* Requires a combination of technology (detection algorithms), policy (regulation of social media platforms), and education (media literacy programs).

## Privacy
- Privacy vs. Security: They are related but not the same. Security is about protecting data from unauthorized access, while privacy is about controlling how personal data is collected, used, and shared. They can support each other, but they can also have conflicting interests.
- Why does it matter? Privacy is a fundamental human right and is essential for maintaining individual autonomy and freedom. In the digital age, where vast amounts of personal data are collected and processed, protecting privacy is crucial to prevent misuse, discrimination, and loss of trust.
- *Potential attacks:*
  - **Data breaches:** Unauthorized access to personal data can lead to identity theft, financial fraud, and other harms.
  - **Surveillance:** Excessive monitoring of individuals can infringe on privacy rights and lead to a chilling effect on free expression.
  - **Data mining and profiling:** Collecting and analyzing personal data can lead to invasive profiling and discrimination.
- *Mitigation strategies (techniques to protect privacy):*
  - **k-Anonymity:** A technique that removes or masks personally identifiable information from datasets, making it difficult to link data back to specific individuals. This helps protect privacy when sharing or analyzing data.
  - **Attribute-Based Credentials:** A method of authentication that allows users to prove certain attributes (e.g., age, membership) without revealing their full identity. This helps protect user privacy by minimizing the amount of personal information shared.
  - **Differential Privacy:** A technique that adds controlled noise to datasets or query results to protect individual privacy while still allowing for useful data analysis. This helps prevent the identification of individuals in aggregated data.
  - **Limiting Data Collection:** Collecting only the minimum amount of personal data necessary for a specific purpose helps reduce the risk of privacy breaches.

# Up Next
## Exam

Logistics:

- Friday 12.12.2025 13:00-15:00 (various rooms).
- Meet in front of M106, at least 15 minutes before it starts.
- We’ll use Digiexam, but also need access to Internet to access your Knowledge Base.
	- In case Digiexam fails (which has happened before), we should consider printing out the important parts of our Knowledge Base. He recommends 20 pages or so.
	- (Note to self: potentially consider the Zettelkasten method for this? It’s the original method for wikis, after all. Used before WWII)

## Types of Exam Questions
- He’s gonna post a practice exam today in Digiexam!
	- Lets us test it out.
	- Lets us test if we can actually access our knowledge base in Digiexam.

What will be on the exam? :

- All the hard questions, of course.
- Multiple-choice similar to Quizzes, some may be simple text input.
	- E.g., ”Which command line tool is often used to find which services are running on a server that you can not login to?” (`nmap` is the answer in this case)
- Questions about knowing how to use the tools you were supposed to use in the labs.
	- E.g., ”Write a shell command or sequence of commands that finds all lines containing your username in the files in `/var/log/`.”
- Questions about understanding different kinds of **vulnerabilities**, how they can be **exploited**, what effect an exploit could have and how to **mitigate** the problem.
	- E.g., “The Morris Worm (1988) used two kinds of vulnerabilities. Briefly explain what those vulnerabilities were, how it allowed the worm to execute code and how similar exploits can be prevented.”
	- (Note to self: write down all the “further reading” things he’s asked us to do after every lecture, and write info about all of those topics. I’ve been neglecting them too much…)
- Questions about technologies we discussed, what their purpose is, roughly how they work, what security issues arise due to them, and which ones they potentially help mitigate.
- Understanding [Defense in Depth](../Terminology/Defense & Control/Defense in Depth.md) and Design Principles for Secure Systems and how this ties into the other topics.

## Knowledge Base
- Hand in a link today.
- Fix formatting, and finish after the exam.
- Don’t forget the 1-2 page reflection document.

There won’t be a class with the TAs today.
