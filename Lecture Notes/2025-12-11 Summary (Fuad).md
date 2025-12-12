---
aliases: []
date created: Thursday, 11. December 2025, 09:12
date modified: Friday, 12. December 2025, 12:12
---

# 2025-12-11 Summary (Fuad)
## **1. The Attack Surface**

The attack surface represents the total sum of exposure in a system.

- **Definition:** It is the sum of all potential vulnerabilities where an attacker could try to subvert the system’s intended purpose 1.
    
- **Scope:** It extends beyond just software and hardware to include **people** and **organizational structures**. If a person with access is malicious or compromised, the technical defenses (like firewalls) may be bypassed.
    
- **Vectors (Entry Points):**
    
    - **Network Access:** Wired connections, Wi-Fi, Bluetooth, and cellular networks222.
        
    - **Physical Media:** USB drives, CD-ROMs, hard drives3.
        
    - **Inputs:** Email (attachments, links), SMS messages, downloaded files444444444.
        
    - **Supply Chain:** Third-party software distributions, BIOS, chips, and embedded systems5.
        
    - **Hidden Vectors:** Malware embedded in “legitimate” files like free games or personality tests6.

---

## **2. Defense in Depth**

Defense is conceptualized as **Risk Management** because defending against *everything* is impossible with limited resources7.

### **A. Risk Formula**

$$Risk = Threat \times Vulnerability \times Cost$$

- **Threat:** The adversary or event.
    
- **Vulnerability:** The weakness in the system.
    
- **Cost:** The impact or loss if the event occurs8.
    

### **B. Risk Strategies**

1. **Mitigate/Reduce:** Lower the likelihood or impact (e.g., applying security patches)9.
    
2. **Avoid:** Stop the risky activity entirely (e.g., deciding not to process credit card payments to avoid PCI-DSS risks)10.
    
3. **Accept:** Acknowledge the risk because the cost of fixing it is higher than the potential loss. This requires management sign-off11.
    
4. **Transfer:** Move the risk to a third party, such as purchasing **cyber insurance** or using a cloud provider (AWS/Azure) to handle infrastructure security12.
    

### **C. Secure Design Principles**

These principles guide the architecture of secure systems13:

1. **Least Privilege:** Every user and process should operate with the minimum permissions necessary to do their job14.
    
2. **Fail-Safe Defaults:** The default state should be “deny” or “secure.”
    
    - *Analogy:* An airplane engine is designed to keep running if a control wire breaks (fail-operational), but a **firewall** should default to blocking traffic if it crashes or encounters an unknown rule (fail-safe)15.
        
3. **Economy of Mechanism:** Keep systems simple. Complex systems have more code, which means more bugs and vulnerabilities16.
    
4. **Complete Mediation:** Every access request must be checked against permissions every time. Do not rely on cached checks (e.g., checking a user’s password once at login doesn’t mean they are still authorized 10 minutes later)17.
    
5. **Open Design:** Security should not rely on secrecy (Security by Obscurity). The architecture and algorithms should be open to review (Kerckhoffs’s principle). Only the keys/passwords should be secret18.
    
6. **Psychological Acceptability:** Security controls must be usable. If a measure is too intrusive (e.g., excessively complex password rules), users will bypass it (e.g., writing passwords on sticky notes), making the system *less* secure19.
    

### **D. The Layered Approach**

Security requires multiple layers so that if one fails, others provide backup20.

1. **Physical:** Cameras, locks, guards, fences21.
    
2. **Technical:**
    
    - **Perimeter:** Firewalls, VPNs, DMZ22.
        
    - **Host/Endpoint:** Antivirus, EDR (Endpoint Detection and Response)23.
        
    - **Application:** Input validation, secure coding practices24.
        
    - **Data:** Encryption (at rest and in transit), Hashing, Backups25.
        
3. **Administrative:** Policies, user training, MFA (Multi-Factor Authentication), Patch management 26.

---

## **3. Computer Networks**

### **Models & Structure**

- **OSI vs. TCP/IP:** We generally use the 4-layer TCP/IP model (Link, Internet, Transport, Application) which maps to the 7-layer OSI model 27.
    
- **Packet Switching:** Data isn’t sent as a continuous stream but broken into **packets**. These packets can take different routes through the network and are reassembled by the receiver 28.
    

### **Layers & Specific Vulnerabilities**

1. Physical Layer 29

- **Function:** Transmits raw bits (signals) over wire or air (encoding, signaling).
    
- **Attacks:**
    
    - **Wiretapping:** Copper wires emit electromagnetic waves that can be read without cutting the wire30.
        
    - **Jamming:** Flooding the radio frequency (DoS) to block Wi-Fi/Bluetooth31.
        
    - **Rogue Devices:** Plugging a Raspberry Pi or laptop directly into a wall port bypasses the firewall32.
        
    - *Rule:* Physical access usually trumps software security33.
        

2. Link Layer (Local Network) 34

- **Scope:** Node-to-node delivery on the *same* network (LAN).
    
- **Addressing:** Uses **MAC Addresses** (Physical, hardcoded on the Network Interface Card)35.
    
- **Protocols:** Ethernet (802.3) and Wi-Fi (802.11)36363636.
    
- **Function:** Switches use **MAC Address Tables** to direct traffic to the specific physical port where the device is connected37.
    
- **Attacks:**
    
    - **MAC Spoofing:** Pretending to be another device by faking the MAC address38.
        
    - **ARP Poisoning:** Corrupting the mapping between IP and MAC addresses to intercept traffic (Man-in-the-Middle)3939.
        
    - **Switch Overloading:** Flooding a switch so it fails “open” and acts like a hub, broadcasting traffic to everyone40.
        

3. Network Layer (Internet) 41

- **Scope:** Delivery across different networks (Global).
    
- **Addressing:** Uses **IP Addresses** (Logical, routable)42.
    
- **Function:** **Routers** use Routing Tables and protocols (like BGP) to determine the “next hop” to get a packet closer to its destination43434343.
    
- **Attacks:**
    
    - **IP Spoofing:** Faking the source IP address44.
        
    - **BGP Hijacking:** Announcing false routing paths to redirect global internet traffic45.
        

4. Transport Layer 46

- **Function:** Host-to-host communication and application multiplexing using **Ports**.
    
- **Protocols:**
    
    - **TCP:** Connection-oriented, reliable (handshake).
        
    - **UDP:** Connectionless, faster, unreliable.
        
- **Attacks:**
    
    - **SYN Flooding:** A DoS attack where the attacker sends many SYN (start connection) requests but never completes the handshake, exhausting server memory47.
        
    - **Open Ports:** Any open port is a potential entry point in the attack surface48.
        

5. Application Layer 49

- **Function:** Services for users (Web, Email, File Transfer).
    
- **Protocols:** HTTP/HTTPS, SSH, SMTP, DNS.
    
- **DNS (Domain Name System):** Maps human-readable names (e.g., `canvas.ru.is`) to IP addresses. Vulnerable to **DNS Cache Poisoning** (sending users to a fake IP for a real name)50505050.
    
- **TLS/SSL:** Provides **End-to-End Encryption**. It ensures:
    
    - **Confidentiality:** No one in the middle (ISP, Router) can read the data.
        
    - **Integrity:** Data hasn’t been modified in transit.
        
    - **Authentication:** Verifies the server is who it claims to be (via Certificates)51.
        

### **Network Defense**

- **Firewalls:** Filter packets based on rules (IP, Port). If traffic is encrypted (HTTPS), the firewall cannot see the payload unless it performs “Deep Packet Inspection” (acting as a proxy)52.
    
- **VPN (Virtual Private Network):** Tunnels traffic securely through an untrusted network53.

---

## **4. Operating Systems (OS)**

### **Core Concepts**

- **Kernel vs. User Space:** The **Kernel** is the trusted core with full hardware access. **User Space** is where applications run with restricted privileges. The OS mediates all access between the two54.
    
- **Functions:** Resource arbitration (CPU/RAM), Process scheduling, File systems, and **Logging** (critical for forensics) 55.
    
- **Trusted Computing Base (TCB):** The collection of all hardware, firmware, and software components that are critical to the system’s security. If the TCB is compromised, the system is compromised56.
    

### **OS Vulnerabilities**

1. **Memory Safety (Buffer Overflows):** Programs (especially in C/C++) writing data outside allocated memory bounds. Attackers use this to overwrite return addresses and hijack control flow to execute their own code (shellcode) 57575757.
    
2. **Race Conditions (TOCTOU):** “Time-of-Check to Time-of-Use.” An attacker changes a file/resource *after* the security check but *before* the program uses it58.
    
3. **Command Injection:** Tricking the OS into executing shell commands via unsanitized input59.
    
4. **Privilege Escalation:** Exploiting a bug to promote a standard user to Administrator/Root60.
    
5. **Rootkits:** Malware that modifies the OS kernel or system binaries to **hide its own presence** (hiding processes, files, or network connections)61.

---

## **5. Web Security**

### **Attack Surface**

- **Server-Side:** Includes all inputs the server processes.
    
    - *Visible:* Forms, file uploads.
        
    - *Hidden:* HTTP Headers, Cookies, URL parameters, API endpoints 62.
        
- **Client-Side:** The environment is the user’s browser (DOM, HTML, JavaScript). The server cannot trust the client environment 63.
    

### **OWASP Top Vulnerabilities**

1. **SQL Injection (SQLi):** Inserting malicious SQL queries into input fields. If the application concatenates input directly into a database query, the attacker can read/modify the database64.
    
2. **Cross-Site Scripting (XSS):** Injecting malicious JavaScript into a trusted website. When other users view the page, the script executes in their browser (stealing cookies/sessions)65.
    
3. **Broken Authentication:** Flaws in session management (predictable session IDs) or credential handling allow account hijacking66.
    
4. **IDOR (Insecure Direct Object References):** Accessing data by simply changing an ID in the URL (e.g., changing `user_id=100` to `user_id=101` to see someone else’s profile) without proper authorization checks67.

---

## **6. AI & Security**

### **The AI Attack Surface**

1. **Input Surface:** Attacks via user prompts or uploaded data.
    
    - **Prompt Injection / Jailbreaking:** Crafting inputs to bypass the AI’s safety filters (e.g., “Do anything now” or roleplaying scenarios) 68.
        
2. **Model Surface:** Attacks on the AI model itself.
    
    - **Training Data Extraction:** Querying the model to reveal private data it memorized during training.
        
    - **Backdoors:** Poisoning the training data so the model behaves normally except for a specific “trigger” input 69.
        
3. **Agency Surface:** Attacks on the tools the AI controls.
    
    - **Confused Deputy:** Tricking the AI into using its tools (plugins, APIs) to perform malicious actions (e.g., “Delete all emails”) 70.
        

### **AI-Enabled Threats**

- **Polymorphic Malware:** Using LLMs to rewrite malicious code logic dynamically, changing the file signature to evade static antivirus detection71.
    
- **Social Engineering at Scale:** AI generates phishing emails with perfect grammar and context. Deepfakes enable realistic voice (vishing) and video fraud 72.
    
- **Vulnerability Discovery:** Attackers use AI to analyze open-source code and find 0-day exploits faster than defenders can patch them73.

---

## **7. Social Aspects**

- **OSINT (Open Source Intelligence):** The practice of gathering actionable intelligence from public sources (social media, public records, DNS records) 74.
    
- **OPSEC (Operational Security):** Protecting unclassified data that could be aggregated to reveal sensitive info (e.g., not posting photos of server room badges, hiding location/identity) 75.
    
- **Information Warfare:** Attacks on **human perception** rather than infrastructure.
    
    - **Astroturfing:** Using bots to create a fake consensus or illusion of public support.
        
    - **Bot Holidays:** Anomalies where hate speech/activity drops suddenly, revealing that the activity was automated 76.

---

## **8. Exam Preparation**

- **Logistics:** Friday, Dec 12, 13:00 - 15:00. Meet at **M106** 15 mins early77.
    
- **Format:** Digiexam (Internet access required for Knowledge Base).
    
- **Question Types:**
    
    - **Multiple Choice:** Similar to quizzes.
        
    - **CLI Practical:** You may be asked to write a specific command (e.g., “Write a command to find all lines containing your username in `/var/log/` using grep”) 78.
        
    - **Conceptual:** Explain vulnerabilities (e.g., “How did the Morris Worm work? What two vulnerabilities did it use?”).
        
    - **Defense:** Explain how *Defense in Depth* or *Least Privilege* applies to a specific scenario 79.
        
