---
aliases: []
date created: Monday, 8. December 2025, 17:12
date modified: Monday, 8. December 2025, 19:12
---

# FurtherStudies
Day 1intro
1-How the [Virus](../Terminology/Attacks/Malware/Virus.md) / attack worked
2What was the impact
3Which weakness was used

Creeper 1971:
1. Creeper was a [Worm](../Terminology/Attacks/Malware/Worm.md) — a type of malwere that replicates itself and spreads to other systems. In this case, its targets were Digital Equipment Corporation (DEC) computers which were linked to ARPANET.
2. connected teletype computer screens displayed the phrase: “I’m the creeper, catch me if you can!”
3. Unprotected [FTP](../Terminology/Networks/Transfer%20Protocols/FTP.md) access, Lack of security measures, open network architecture, no concept of [Malware](../Terminology/Attacks/Malware/Malware.md) protection. Its creator had simply wanted to create an experimental, self-duplicating program to illustrate that it was possible.
(https://www.exabeam.com/blog/infosec-trends/creeper-the-worlds-first-computer-virus/)

Morris Worm (1988):
(A worm unlike a virus can replicate and spread on its own, without human intervention.)
1. The Morris Worm automatically spread across the Internet by exploiting vulnerabilities in UNIX operating systems. Once inside a machine, it copied itself repeatedly due to a flaw in its design, overloading systems.
2. Around 6000 computers which was roughly 10% of the internet at the time, became unusable as the worm slowed or crashed systems.”Some institutions scrapped and replaced their systems, while others went offline for up to a week.  “The worm did not damage or destroy files, but it still packed a punch,” says an FBI case study of the event.
3. A hole in the debug mode of the Unix sendmail program, a [Buffer Overflow](../Terminology/Attacks/Buffer%20Overflow.md) or overrun hole in the finger network service, the transitive trust enabled by people setting up network logins with no password requirements via remote execution and exploited weak passwords
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
(**EternalBlue**, a [Zero-Day Vulnerability](../Terminology/Zero-Day%20Vulnerability.md) in devices that use an old version of SMB. It exploits a vulnerability in the Microsoft implementation of the Server Message Block (SMB) Protocol. This dupes a Windows machine that has not been patched against the vulnerability into allowing illegitimate data packets into the legitimate network. These data packets can contain malware such as a [Trojan](../Terminology/Attacks/Malware/Trojan.md), ransomware or similar dangerous program.)

Day 2- [Virtualization](../Terminology/Virtualization/Virtualization.md)

1. Under what specific scenarios would you have to choose VMs over [containers](../Terminology/Virtualization/Virtualization%20methods/Container.md) for security reasons, and vice-versa?
VM are better if security is the priority since each VM operates as a fully isolated computer with its own [OS](Operating%20System.md) and applications, so if one VM is compromised, it’s difficult for the attack to spread to other VMs or the host machine. But [containers](../Terminology/Virtualization/Virtualization%20methods/Container.md) share the host operating system kernel, so a vulnerability in the kernel can potentially affect all [containers](../Terminology/Virtualization/Virtualization%20methods/Container.md). So VMs are better suited for workloads that handle sensitive data or require strict security and compliance. [Containers](../Terminology/Virtualization/Virtualization%20methods/Container.md) might be chosen when performance is the priority as [containers](../Terminology/Virtualization/Virtualization%20methods/Container.md) are faster, lighter, and more resource efficient, the fast startup time of [containers](../Terminology/Virtualization/Virtualization%20methods/Container.md) directly contributes to scalability, making them ideal for microservices architectures.
https://monovm.com/blog/vm-vs-containers/

2. Research historical examples of [VM Escape](../Terminology/Virtualization/VM%20Escape.md) vulnerabilities (e.g., specific [CVEs](../Terminology/Vulnerability%20standards/CVE.md) for VMware, VirtualBox, KVM, or Docker). What were the root causes?
(VM escape is the process of a program breaking out of the VM on which it is running and interacting with the host operating system.)
  - CVE-2025-22224 is a Time-of-Check Time-of-Use (TOCTOU-is a class of software bugs caused by a [Race condition](../Terminology/Attacks/Race%20condition.md) involving the checking of the state of a part of a system (such as a security credential) and the use of the results of that check.) vulnerability in VMware ESXi and Workstation, rated critical with a CVSS score of 9.3. It stems from a heap overflow in the Virtual Machine Communication Interface (VMCI), enabling an out-of-bounds write. An attacker with local admin privileges on a VM can exploit this to execute code as the VMX process on the host.
  https://clovinsecurity.wixsite.com/clovin-security/post/ultimate-guide-to-cve-2025-22224-vmware-esxi-zero-day-vulnerability-exposed-clovin-security

2. [Side-Channel Attacks](../Terminology/Virtualization/Side-Channel%20Attack.md):
	1. What is a [Side-Channel Attack](../Terminology/Virtualization/Side-Channel%20Attack.md) (in the context of virtualization)?- An exploit that uses indirect data such as timing, power consumption, or electromagnetic emissions to extract sensitive information 
	2. Why is this especially problematic for cloud environments?- Even routine maintenance can introduce risks. During updates, temporary configuration changes might briefly expose resources, creating exploitation windows for vigilant attackers monitoring cloud environments.
	3. Find recent examples of such attacks and discuss their impact. 
	4. What mitigation strategies exist to counter these types of attacks?
3. What are the risks associated with using untrusted or vulnerable [container](../Terminology/Virtualization/Virtualization%20methods/Container.md) [images](../Terminology/Virtualization/Virtualization%20Hardening%20&%20Operations/Image.md) from public repositories?


