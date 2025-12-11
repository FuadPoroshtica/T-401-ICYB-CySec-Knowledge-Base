---
aliases: []
date created: Monday, 8. December 2025, 17:12
date modified: Monday, 8. December 2025, 19:12
---

# FurtherStudies
Day 1 - Intro
1-How the [Virus](../Terminology/Attacks/Malware/Virus.md) / attack worked
2What was the impact
3Which weakness was used

Creeper 1971:
1. Creeper was a [Worm](../Terminology/Attacks/Malware/Worm.md) — a type of malwere that replicates itself and spreads to other systems. In this case, its targets were Digital Equipment Corporation (DEC) computers which were linked to ARPANET.
2. connected teletype computer screens displayed the phrase: “I’m the creeper, catch me if you can!”
3. Unprotected [FTP](../Terminology/Networks/Transfer Protocols/FTP.md) access, Lack of security measures, open network architecture, no concept of [Malware](../Terminology/Attacks/Malware/Malware.md) protection. Its creator had simply wanted to create an experimental, self-duplicating program to illustrate that it was possible.
(https://www.exabeam.com/blog/infosec-trends/creeper-the-worlds-first-computer-virus/)

Morris Worm (1988):
(A worm unlike a virus can replicate and spread on its own, without human intervention.)
1. The Morris Worm automatically spread across the Internet by exploiting vulnerabilities in UNIX operating systems. Once inside a machine, it copied itself repeatedly due to a flaw in its design, overloading systems.
2. Around 6000 computers which was roughly 10% of the internet at the time, became unusable as the worm slowed or crashed systems.”Some institutions scrapped and replaced their systems, while others went offline for up to a week.  “The worm did not damage or destroy files, but it still packed a punch,” says an FBI case study of the event.
3. A hole in the debug mode of the Unix sendmail program, a [Buffer Overflow](../Terminology/Attacks/Buffer Overflow.md) or overrun hole in the finger network service, the transitive trust enabled by people setting up network logins with no password requirements via remote execution and exploited weak passwords
https://alumni.cornell.edu/cornellians/morris-worm/
https://en.wikipedia.org/wiki/Morris_worm

Vladimir Levin stealing 10 million USD from Citibank in 1994
Melissa Email Worm (1999)
Operation Olympic Games (2009)

Ukrainian Power Grid Shutdown (23rd December 2015)
1. The attackers initially gained access through [Phishing](../Terminology/Attacks/Phishing.md) email with a malicious attachments containing the malware, giving them a [Backdoor](../Terminology/Attacks/Backdoor.md) into the utility’s IT network. Over months they, compromised credentials and escalated privileges, ultimately reaching the control (SCADA) network that manages the grid operations. On December 23, they took control of operator workstations, opened circuit breakers at around 30, taking them all offline and causing the power outage. They disabled backup power and remote‑control functions, they also deployed KillDisk to erase utility systems and launched a telephone denial‑of‑service attack against customer call‑centers to hinder outage reporting.
2. The power outage effected around 225,000 Ukrainian customers, the first publicly acknowledged blackout caused by a cyberattack. Although electricity was restored within hours, the event demonstrated that a cyberattack could disrupt critical infrastructure beyond data theft, marking a historic warning for global grid operators.
3. The attackers exploited human network weaknesses (spear‑phishing to install malware), insufficient network segregation (allowing lateral movement from IT to SCADA systems), weak credential security, and lack of robust defense mechanisms preventing remote takeover of control‑system workstations and breaker controls.

WannaCry Ransomware Attack (2017)
(WannaCry is an example of crypto [Ransomware](../Terminology/Attacks/Malware/Ransomware.md), a type of malware used to extort money. Ransomware does this by either encrypting valuable files(crypto ransomware), so you are unable to read them, or by locking you out of your computer(locker ransomware), so you are not able to use it.)
1. The attack infected PCs and spread automatically between connected machines by itself without requiring user intervention or social engineering. It encrypted the user’s files and displayed a ransom note demanding payment in Bitcoin.
2. WannaCry had a major impact on organizations across the world, infecting over 230,000 computers and causing billions of dollars worth of damages. It had a particularly devastating effect on healthcare organizations
3. It uses the EternalBlue exploit to spread between connected systems that where not patched against the [Vulnerability](../Terminology/Vulnerability.md).
https://www.fortinet.com/resources/cyberglossary/wannacry-ransomware-attack
(**EternalBlue**, a [Zero-Day Vulnerability](../Terminology/Zero-Day Vulnerability.md) in devices that use an old version of SMB. It exploits a vulnerability in the Microsoft implementation of the Server Message Block (SMB) Protocol. This dupes a Windows machine that has not been patched against the vulnerability into allowing illegitimate data packets into the legitimate network. These data packets can contain malware such as a [Trojan](../Terminology/Attacks/Malware/Trojan.md), ransomware or similar dangerous program.)

Day 2- [Virtualization](../Terminology/Virtualization/Virtualization.md)

1. Under what specific scenarios would you have to choose VMs over [containers](../Terminology/Virtualization/Virtualization methods/Container.md) for security reasons, and vice-versa?
VM are better if security is the priority since each VM operates as a fully isolated computer with its own [OS](Operating System.md) and applications, so if one VM is compromised, it’s difficult for the attack to spread to other VMs or the host machine. But [containers](../Terminology/Virtualization/Virtualization methods/Container.md) share the host operating system kernel, so a vulnerability in the kernel can potentially affect all [containers](../Terminology/Virtualization/Virtualization methods/Container.md). So VMs are better suited for workloads that handle sensitive data or require strict security and compliance. [Containers](../Terminology/Virtualization/Virtualization methods/Container.md) might be chosen when performance is the priority as [containers](../Terminology/Virtualization/Virtualization methods/Container.md) are faster, lighter, and more resource efficient, the fast startup time of [containers](../Terminology/Virtualization/Virtualization methods/Container.md) directly contributes to scalability, making them ideal for microservices architectures.
https://monovm.com/blog/vm-vs-containers/

2. Research historical examples of [VM Escape](../Terminology/Virtualization/VM Escape.md) vulnerabilities (e.g., specific [CVEs](../Terminology/Vulnerability standards/CVE.md) for VMware, VirtualBox, KVM, or Docker). What were the root causes?
(VM escape is the process of a program breaking out of the VM on which it is running and interacting with the host operating system.)
  - CVE-2025-22224 is a Time-of-Check Time-of-Use (TOCTOU-is a class of software bugs caused by a [Race condition](../Terminology/Attacks/Race condition.md) involving the checking of the state of a part of a system (such as a security credential) and the use of the results of that check.) vulnerability in VMware ESXi and Workstation, rated critical with a CVSS score of 9.3. It stems from a heap overflow in the Virtual Machine Communication Interface (VMCI), enabling an out-of-bounds write. An attacker with local admin privileges on a VM can exploit this to execute code as the VMX process on the host.
  https://clovinsecurity.wixsite.com/clovin-security/post/ultimate-guide-to-cve-2025-22224-vmware-esxi-zero-day-vulnerability-exposed-clovin-security

2. [Side-Channel Attacks](../Terminology/Virtualization/Side-Channel Attack.md):
	1. What is a [Side-Channel Attack](../Terminology/Virtualization/Side-Channel Attack.md) (in the context of virtualization)?- An exploit that uses indirect data such as timing, power consumption, or electromagnetic emissions to extract sensitive information 
	2. Why is this especially problematic for cloud environments?- Even routine maintenance can introduce risks. During updates, temporary configuration changes might briefly expose resources, creating exploitation windows for vigilant attackers monitoring cloud environments.
	3. Find recent examples of such attacks and discuss their impact. 
	4. What mitigation strategies exist to counter these types of attacks?
3. What are the risks associated with using untrusted or vulnerable [container](../Terminology/Virtualization/Virtualization methods/Container.md) [images](../Terminology/Virtualization/Virtualization Hardening & Operations/Image.md) from public repositories?

Day 6 - Networks [Networks](../Terminology/Networks)
1. Find examples of vulnerabilities and attacks using Bluetooth:
	1. **PerfektBlue (2024-2025):** This recent vulnerability chain affects millions of vehicles through OpenSynergy's BlueSDK, enabling remote code execution over Bluetooth Classic with minimal user interaction.  Attackers within Bluetooth range can compromise infotainment systems to access GPS location, microphones, and contact lists. 
    2. **KNOB Attack (Key Negotiation of Bluetooth):** This exploit forces devices to agree on encryption keys with significantly reduced entropy during the pairing process, making brute-force attacks feasible. The vulnerability exists because the key negotiation itself isn't encrypted.
   3. **BLUFFS Attack (CVE-2023-24023):** Six attacks that break forward and future secrecy guarantees in Bluetooth, allowing adversaries-in-the-middle to compromise one session key and reuse it across multiple sessions. This affects Bluetooth Core Specification 4.2 to 5.4.
3. Why Bluetooth is a terrible protocol?
   1. **Complex Protocol Stack:** Bluetooth stacks handle large volumes of untrusted data through multi-layer protocols like L2CAP, RFCOMM, and AVRCP, largely implemented in C, combining memory safety risks with complex state handling.
   2. **Legacy Issues:** Legacy bugs often persist in modern systems for years, and many vulnerabilities are logic-based and difficult to detect using traditional testing methods.
   3. **Default Insecure Configurations:** Many devices ship with Bluetooth in discoverable mode or use weak default PINs, and developers often use insecure examples from SDKs without implementing proper security features.
   4. **Default Insecure Configurations:** Many devices ship with Bluetooth in discoverable mode or use weak default PINs, and developers often use insecure examples from SDKs without implementing proper security features.
5. What is the best protection against Bluetooth attacks? **Primary Defense:** The simplest and most effective way to block attacks is to turn off Bluetooth whenever you don't need it.
   **Additional Protections:**
   1. **Disable Discovery Mode:** Ensure devices are set to non-discoverable mode when not actively pairing.
   2. **Keep Firmware Updated:** Regular updates patch known vulnerabilities.
   3. **Use Strong Authentication:** Avoid default PINs like "0000" or "1234"
   4. **Reject Unknown Connections:** Never accept pairing requests from unrecognized devices
   5. **Avoid Public Pairing:** Don't pair devices in public spaces where attackers may be scanning
   6. **Use Encryption:** Enable Bluetooth encryption when available
   7. **Remove Old Pairings:** Delete unused or untrusted device pairings
   8. **For Organizations:** Implement Mobile Device Management (MDM) policies to control Bluetooth settings
7. What individuals and organizations can do prevent or defend against attacks that use Rogue Access Points?
   **What Are Rogue Access Points?** Unauthorized wireless access points installed on a secure network without administrator authorization. Evil twins are a specific type where hackers create fake Wi-Fi that mimics legitimate networks.
   **Individual Defenses:**
   1. **Use a VPN** - Your strongest defense. Even if you connect to a rogue AP, VPN encryption prevents hackers from reading your traffic.
   2. **Verify Networks** - Check that the SSID matches what the venue provides and look for duplicate network names. Ask staff when uncertain.
   3. **Disable Auto-Connect** - Regularly clear saved Wi-Fi networks so your device doesn't automatically connect to evil twins using familiar names.
   4. **Use HTTPS** - Stick to websites with the padlock icon, which encrypt communication.
   5. **Enable Multi-Factor Authentication** - Requires extra verification beyond passwords, protecting accounts even if credentials are stolen.
   6. **Avoid Sensitive Activities on Public Wi-Fi** - Use mobile data for banking or wait until you're on a trusted network.
   **Organization Defenses**
   1. **Deploy WIDS/WIPS** - Systems that scan Wi-Fi frequencies to detect unauthorized access points and can automatically block connections to them.
   2. **Network Segmentation** - Divide networks into VLANs so a breach in one segment doesn't grant access to everything
   3. **Strong Authentication** - Use WPA2/WPA3-Enterprise with 802.1X and RADIUS for secure authentication.
   4. **Regular Audits** - Regularly scan for unauthorized access points through automated and manual checks.
   5. **Physical Security** - Limit physical access to network hardware to prevent direct connection of rogue devices.
   6. **Employee Education** - Train staff on risks of unauthorized devices and enforce strict policies about personal routers.
   7. **Zero Trust Architecture** - Treat all users and devices as untrusted until authenticated and authorized.

Day 9 - AI Security [AI Security](../Terminology/Artifical_Intelligence/Defensive_Strategies)
1. The 2024 Hong Kong Deepfake Scam.
   - _What happened?_ In early February 2024, Hong Kong police reported a case where **deepfake techology** was employed to execute a multimillion-dollar **fraud**. The scammers orchestrated a video conference call, using deepfakes to impersonate the chief financial offier and other staff members of the mutlinational firm **Arup**, convincing a finance worker to transfer approximately 25 million dollars to five Hong Kong bank accounts.
   - _In general how can cases like these be prevented?_ These cases can be prevented be implementing **stronger verification methods** beyond visual confirmation, sucha as multi-factor authentication or independent confirmation of requests, as well as **training for employees** on recognizing deepfake technology and understanding the tactics used in such scams can help employees remain vigilant.
   - _What are security risks that come with the existence (and easy creation) of Deepfakes for:_
	 - _Individuals?_ Enabling impersonations of people and gain unauthorized access to sensitive information. Additionally, they can lead to reputational damage and privacy violations by creating misleading or harmful content that appears real.
     - _Organizations?_  Enabling impersonation executives, which can lead to unauthorized access to sensitive information and financial fraud. They can also damage an organization's reputation and undermine trust, making it essential for companies to implement detection technologies and response plans.
     - _Society as a whole?_ Enabling misinformation, identity theft, and manipulation of public opinion, particularly during elections or crises. Their realistic nature can undermine trust in genuine media, making it difficult for individuals to discern truth from falsehoods, which can lead to broader societal consequences.
     - Keywords: **Identity theft, fraud, undermining of democracy, misinformation**.   

Day 11 - Defense [Defense](../Terminology/Defense&Control)
1. What replaces the Firewall as a primary enforcement point in Zero Point?
   Instead of relying on a traditional perimeter firewall/VPN, Google uses **context-aware access proxies** and a **centralized Access Control Engine** that authenticate and authorize every request based on user identity and device trust, not network location.
2. How does a system decide if a device is trusted?
   Trust is determined dynamically using a Trust Inferer that evaluates multiple device and user attributes such as:
   - Device state (patch level, antivirus, encryption, certificates)
   - Whether the device is managed/registered
   - User identity and role
   - Contextual signals (location, time, behavior)
  Based on these, a trust level or tier is assigned, which dictates what resources the device can access. 
3. What are advantages and disadvantages of this approach regarding security?
   **Advantages:**
   - No trusted network perimeter — all access is verified per request, reducing implicit trust.
   - Granular, context-aware access control — decisions based on identity & device posture, not IP or location.
   - Least-privilege enforcement — devices/users get only what they need.
   - Improved protection against lateral movement — attackers can’t exploit broad network access.
   **Disadvantages:**
   - Complexity & cost — implementing continuous verification and trust inference requires major architectural changes.
   - Operational overhead — needs continuous monitoring of devices and identities.
   - Dependency on backend systems — if access proxies or identity services fail, user access and productivity are impacted.
   - Policy management difficulty — creating and maintaining fine-grained rules takes effort.
4. Quick summary of how Google replaced VPN and traditional firewalls
   **Traditional model:** If you’re on the corporate network (inside firewall + VPN), you’re trusted and get broad access. Google’s Zero Trust (BeyondCorp):
   - No special trusted network — whether you’re on-site or remote, all access is treated as coming from an untrusted network.
   - Authentication & authorization happen on every request through an access proxy using device identity + user credentials + context.
   - Firewall/VPN are not primary defense points — enforcement is done by access proxies and policy engines that verify trust continuously. 
