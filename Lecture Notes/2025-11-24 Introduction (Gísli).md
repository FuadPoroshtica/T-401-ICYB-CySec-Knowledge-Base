---
aliases: []
date created: Tuesday, 25. November 2025, 16:11
date modified: Thursday, 4. December 2025, 11:12
---

# 2025-11-24 Introduction (Gísli)
(24.11.2025 W1 Monday 09:00)

## Course overview

### Course contents:

- Linux + Windows CLI tools.
- [OS](Operating%20System.md) basics ([access control](../Terminology/Defense & Control/Access Control)).
- Networking basics.
- [Virtualization](../Terminology/Virtualization/Virtualization).
    - Some of the labs we’ll be doing will be on virtual machines and stuff.
- Web security.
- Common tools for security testing.
- Principles of defense.
- Guest lectures on various topics: [phishing](../Terminology/Attacks/Phishing), information warfare, binary exploitation, maybe more topics.
They’ll be teaching us like shell scripts and stuff.
Computer architecture.

### Course material:

- Specific reading will be provided with the lectures.
- You should expect to spend several hours a week reading.
- Group assignment (CySec Knowledge Base) should be used to organize material and notes.
    - “Up to 12 students per group”??
    - Take notes during assignments and stuff.
    - We’re supposed to be doing this as a group.

### How to use AI in the course:

- Crucially, the content must be your original thought. Do **not** let it write stuff for you. You have to, of course, learn this stuff; don’t make it do things for you.
    - Ask it to provide sources, and it, of course, hallucinates a lot.
- The typical. Use it as a helper, an assistant, a search engine, etc.
- Use it to correct information, a helper with learning

### Equipment:

- Some labs will run directly on your laptop, and others on VMs.
- Linux, macOS & Windows are ok, this is actually encouraged in a group project.
- Back up your laptop! (in case something goes wrong.)

### Program:

- **09:00-12:00**: Lecture, reading, note-taking, quiz.
    - Quiz won’t be too big.
    - There’ll be two rooms for doing stuff. In there, there’ll be TAs to help with stuff. (*Also for labs?*)
- **12:40-16:00**: Lab assignment.
- Friday 12. December: exam.

### Grade Assessment:

- 30% quizzes (*worth ~2% each, people do it individually*)
- 30% lab assignments (*worth ~2% each, people do it in groups of 3-4 students*)
- 10% cysec knowledge base (*people do it in groups of up to 12 students*)
- 30% final exam (*people do it individually*)

### Communication:

- Piazza and Discord
- Piazza (private posts) for individual issues and grade issues.
- Email only if really necessary.

### ⚠️Hazard warning

- We will be playing with fire.
- Do not try techniques covered here on computers you do not control or do not have permission to test (*duh*).
- Obtain permission from the instructor if you are in any doubt whatsoever.
- Always get permission in writing.
- Be careful with any code or instructions you find online.

## Main lecture

### The problem: [attack surface](../Terminology/Attack Surface)

- Definition: “The sum of all potential vulnerabilities in a system where an attacker could try to subvert the intended purpose of the system and organization or person who is using it.”
    - E.g., they could obtain physical access, access via a public network, or access to online backups of your computer.
    - Basically, *any way* you get data into your system is an attack surface.
- Examples:
    - Email.
    - Network points of access.
    - USB, CD-ROM.
    - Downloaded [virus](../Terminology/Attacks/Malware/Virus)es and [malware](../Terminology/Attacks/Malware/Malware).
    - SMS messages.
    - Software distributions, external software, BIOS, chips,...
    - **Any form of input or control over the software or machine**.

### What are the real risks?

- Assume:
    - Secure machine, all [port](../Terminology/Systems & Plaforms/Port)s closed.
    - Local [firewall](../Terminology/Defense & Control/Firewall) enabled.
    - all software updates applied
- There are still risks:
    - Inadvertent virus introduction (email, USB, evil website, [Trojan](../Terminology/Attacks/Malware/Trojan) software)
    - Unpatched software versions
    - Zero-day exploit in an [OS](Operating%20System.md) or a network application.
        - An exploit in the software that can be used to gain access to the system, but there is no fix for it yet.
    - Web browser malware.
    - Hardware [backdoor](../Terminology/Attacks/Backdoor) (Intel Management System)
    - IT security failure.

### History of attacks

- **1971**: ARPANET: Creeper
    - First virus on the internet (which was just the ARPANET at this point).
    - It didn’t actually do anything harmful, just displayed a message. It was kind of just a warning.
- **1986**: North Korea trains the first “cyber-warriors”.
- **1988**: The Morris [worm](../Terminology/Attacks/Malware/Worm) brings down 6,000+ internet computers.
- **1994**: $10 million was stolen from Citibank by Russian hackers.
- **1999**: Windows 98: ‘Melissa email worm’ brings down all email globally.
- **2007**: Aurora generator test: 30 lines of code physically destroyed power generators.
- **2015**: Ukrainian power grid shutdown for 1-6 hours

Part of our research task today is looking at how they work, what weaknesses they used, etc.

### Cyber defence

Definition: “Acting in anticipation to oppose an attack through cyber and cognitive domains.”

The attacker wants to read, modify, inject, and control the system.
An old idea is to put a firewall between the attacker and all the data. But we can’t just do this anymore because we need to get information in and out of our system.
The most secure system is also unusable. We have to consider the users.

Computer security involves:

- Preventing and detecting unwanted access, use of computers, and theft of data
- preventing and detecting unauthorized modification
- Preventing and detecting unauthorized injection of data, computers, etc.
Every computer professional should be doing it this way anyway.

### Categories of computer security threats:

- **Unauthorized access**
- **Unauthorized modification**
- **Unauthorized disclosure**
- **Denial of authorized access**
- **Forgery**
- **[Repudiation](../Terminology/Repudiation)** - where the integrity of an asset can be disputed
- **[Spoofing](../Terminology/Attacks/Spoofing)** - masquerading as a legitimate entity.
- Still missing that don’t really fit well in these:
    - Information warfare?
    - Bribery/blackmail?
    - Deliberate incompetence?
    - Inducing system overload?

### Other forms of attack

- Denial-of-Service attack
- Modify information
- Physical destruction - Stuxnet
- Infrastructure attack
- [Ransomware](../Terminology/Attacks/Malware/Ransomware)
- Masquerade as a victim
- Add files - poison web cache
- [Corporate espionage](../Terminology/Attacks/Corporate Espionage)
- Information warfare

### Computer security evolution

- Prevent attacks (programming and design quality)
- Testing!
- Manufacturers: offer small sums of money to report bugs (bug bounties)
- Nation states: offer large sums of money to buy attacks for future use (zero-day bugs)
- And the consequence was...
    - ...market-based pricing providing a guide to relative security.

### Up next:

### Further reading (we have to read this):

- **1971**: ARPANET: Creeper
    - First [virus](../Terminology/Attacks/Malware/Virus) on the internet (the ARPANET at this point).
    - It didn’t actually do anything harmful, just displayed a message. It was kind of just a warning.
- **1988**: The Morris [worm](../Terminology/Attacks/Malware/Worm) brings down 6,000+ internet computers.
- **1994**: $10 million was stolen from Citibank by Russian hackers.
- **2009**: Operation Olympic Games
- **2017**: WannaCry ransomware attack

“Look into the following computer viruses and attacks and find out:

1. How the viruses/attacks worked,
2. which impact they had and
3. which weakness(es) they used”
The attacks:
- Creeper (1971)
    - **How it worked:** Copied itself between computers and printed
    - **Impact:** Displayed the message: “I’m the creeper, catch me if you can!” on infected systems. It was not malicious and did not cause harm to the systems. Could only have affect about 28 machines in total.
    - **Weaknesses used:** Exploited vulnerabilities in ARPANET’s TENEX operating system.
- Morris Worm (1988)
    - **How it worked:** Exploited vulnerabilities in the debug mode of Unix sendmail, a [buffer overflow](../Terminology/Attacks/Buffer Overflow) [vulnerability](../Terminology/Vulnerability) in the “finger” network service, and he transitive trust enabled by people setting up network [logins](https://en.wikipedia.org/wiki/Login) with no [password](https://en.wikipedia.org/wiki/Password) requirements via [remote execution](https://en.wikipedia.org/wiki/Berkeley_r-commands) (rexec) with [Remote Shell](https://en.wikipedia.org/wiki/Remote_Shell) (rsh), termed “rexec/rsh”, as well as weak passwords
    - **Impact:**
    - **Weaknesses used:**
- Vladimir Levin stole $10 million USD from Citibank (1994)
    - **How it worked:**
    - **Impact:**
    - **Weaknesses used:**
- Melissa Email Worm (1999)
    - **How it worked:**
    - **Impact:**
    - **Weaknesses used:**
- Operation Olympic Games (Stuxnet) (2009)
    - **How it worked:**
    - **Impact:**
    - **Weaknesses used:**
- Ukrainian Power Grid Shutdown (23rd December 2015)
    - **How it worked:**
    - **Impact:**
    - **Weaknesses used:**
- WannaCry Ransomware Attack (2017)
    - **How it worked:**
    - **Impact:**
    - **Weaknesses used:**

### Lab 1

- Check the security of your own system.
- Useful resources:
    - [https://nvd.nist.gov](https://nvd.nist.gov/) (US) National Vulnerability Database
    - [https://www.cve.org](https://www.cve.org/), [https://www.cvedetails.com](https://www.cvedetails.com/) Maintains a searchable database of [CVE](../Terminology/Vulnerability standards/CVE)s (Common Vulnerabilities and Exposures).
        - Sponsored by the US Dept. of Homeland Security.
        - Restricted to publicised vulnerabilities.
    - [https://www.exploit-db.com](https://www.exploit-db.com/) Public open source database of vulnerabilities

3-4 lab groups work together for the CySec Knowledge Base thing?
