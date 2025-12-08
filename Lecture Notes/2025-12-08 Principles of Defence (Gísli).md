---
aliases: []
date created: Monday, 8. December 2025, 08:12
date modified: Monday, 8. December 2025, 09:12
---

- This week, up to Wednesday, will be the same as the last weeks.
- Thursday will be a summary lecture. No lab on Thursday. So we have time to prep the knowledge base and stuff.
- They’ll publish a small version of the exam, a practice exam, beforehand.
- The exam will be on Friday afternoon, at roughly 13:00.
- The lab today will be a bonus lab.

# 2025-12-08 Principles of Defence (Gísli)
Today we’ll be talking about *defense*, not just attacks like we’ve been doing so far.

# Economics of Defense
- One of the problems of defense is that cyber warfare is asymmetric. The attacker only needs to find *one flaw*, but the defender needs to fix all of them.
- **The goal:** The CIA triad:
	- **Confidentiality:** Information is not disclosed to unauthorized parties.
    - **Integrity:** Information is not altered or destroyed in an unauthorized
      manner.
    - **Availability:** Information is accessible and usable upon demand by an authorized entity.

## Security vs usability:
- The *most secure* computer is unplugged, buried in concrete, and guarded by sharks.
- *Problem*: it is useless, completely unusable.
- The easiest way to make something secure is to make it completely unusable.

Security measures must be **psychologically acceptable**. If security is too hard, users will bypass it.
- *Example:* You can make your users have a super complicated password that’s really hard to crack, like `æjalsASDJFOASDIF439II)/)(#d`, but instead of memorizing it the user will probably just write it on a sticky note.
 
We do not *eliminate* risk, we *manage* it.
$\text{Risk} = \text{Threat} \times \text{Vulnerability} \times \text{Cost}$.
- **Threat:** Who wants to attack us? *What* is the threat?
- **Vulnerability:** How easy is it to attack us? How *vulnerable* are we?
- **Cost:** What is the cost of the attack? What do we lose?
- (Threat × Vulnerability = is the likelihood of an attack happening.)
With countermeasures, we can address the vulnerability part. But we can also reduce the cost (impact), like having backups and having a plan for how we respond.

Mitigation is not the only option when facing a risk:
- **Mitigate/reduce:** Reduce likelihood or impact to an acceptable level.
- **Avoid:** Discontinue the activity that generates the risk. (E.g., we will not store credit card info, so we avoid the risk of leaking it.)
- **Accept:** The cost of the fix > impact of the risk. (E.g., small website that gets few visitors, so we accept the risk of DDoS.)
- **Transfer:** Move risk to a third party (e.g., insurance).

## Cost-benefit analysis
Do a cost-benefit analysis when deciding on countermeasures.

> [!example]
> You do not buy a $5,000 titanium lock to secure a $50 bike.

Defense cost must not exceed the value of what is being protected.
**Defense in-depth:** Multiple layers of defense, so if one fails, others are still there.

# Design Principles & Defense in-depth

## Core design principles
The most important ones from Saltzer & Schroeder are:
- **Least privilege:** Give each user/process the minimum privileges needed to perform its function.
  - E.g., a web server process should not run as root.
  - Why? Because if the process is compromised, the attacker only gets limited access.
- **Fail-safe defaults:** Default to no access, unless explicitly granted.
  - E.g., file permissions in Unix are by default restrictive.
  - Why? Because it’s easier to grant access than to revoke it.
  - Also, you’ll notice better when people don’t have *enough* access, because they’ll complain immediately. But no one complains when they have *too much* access.
- **Economy of mechanism:** Keep the design as simple and small as possible. Complexity hides vulnerabilities.
  - E.g., a simple protocol is easier to analyze for security flaws.
- **Complete mediation:** Every access to every resource must be checked for authorization.
  - E.g., a filesystem must check permissions on every file access.
  - Why? Because if some accesses are not checked, they can be exploited.
- **Open design:** The security of a system should not depend on the secrecy of its design or implementation.
  - E.g., open-source software can be reviewed by many experts.
  - Why? Because security through obscurity is not reliable.
  - **Avoid:** Security by obscurity.

# Defense in-depth
## The Layered Approach (The Onion)
The idea is that this is a layered approach.
No single control is infallible. If one layer fails, others are still there and catch the threat.
1. **Physical controls:** Locks, guards, cameras.
2. **Technical controls:** Firewalls, encryption, access control.
	- **Perimeter/Network defenses:** Firewalls, IDS/IPS, DMZ, VPN, Intrusion Detection Systems.
	- **Host/Endpoint defenses:** Antivirus, Monitoring
	- **Application defenses:** Input validation, secure coding practices.
	- **Data defenses:** Encryption, backups, hashing
3. **Administrative controls:** Policies, training, incident response plans.
	- **People:** Training, awareness programs, MFA (Multi-Factor Authentication), password policies.
	- **Technology:** Patch management, risk assessments, audits.
	- **Operations:** Principle of least privilege, change management, incident response.
*Scenario:* If a laptop is stolen (physical security fail), the hard drive encryption (data layer) protects the information.

## Classifying Controls
By type:
- **Physical:** Locks, guards, cameras.
- **Technical:** Firewalls, encryption, access control.
- **Administrative:** Policies, training, incident response plans.

By function:
- **Preventive:** Stop attacks before they happen (e.g., firewalls, access control).
- **Detective:** Identify and log attacks (e.g., IDS, monitoring).
- **Corrective:** Respond to and recover from attacks (e.g., backups, incident response).

# Standards, Frameworks, Checklists
Doing all of this is hard, so there are standards and frameworks and checklists to help you do the right thing.
- Checklists fossilize (don’t evolve with threats) procedures
	- Set expected procedure and outcomes
	- Can/should be audited
	- Reviewed when mistakes happen and improved
	- Think of them as a synchronization point
- Allow training and practice
	- Critical when dealing with “real-time” situations.
	- When the incident is started you need to react quickly.
- Widely adopted by critical industries, like aviation, healthcare, finance.

## Key frameworks & standards
Don’t reinvent the wheel. Use existing frameworks and standards.

- Management & process (organizational):
    - **ISO/IEC 27000 series:** international standard for Information Security Management Systems (ISMS). Focus on governance, risk management, and controls.
    - **NIST CSF (Cybersecurity Framework):** voluntary framework for managing cybersecurity risks. Focus on identifying, protecting, detecting, responding, and recovering.
- Technical implementation (Developer/Ops):
  - **CIS (Center for Internet Security) controls:** prioritized set of actions to protect against cyber threats. Focus on technical controls and best practices.
  - **OWASP Top 10:** list of the most critical web application security risks. Focus on web application security.

## EU Regulations
Apply in Iceland because of EEA membership.
- **GDPR (General Data Protection Regulation):** Protects personal data and privacy of EU citizens. Requires organizations to implement appropriate security measures.
- **NIS2 Directive (Network and Information Systems Directive):** Enhances cybersecurity across the EU.
- **Cyber Resilience Act (CRA):** Was just put it in the EU this year. Critical for developers: mandatory security requirements for products with digital elements (Software/IoT) placed on the EU market. It’s not in effect in Iceland *right now*, but will be very soon.
- **Digital operational resilience act (DORA):** Focuses on ICT risk management for financial entities.

## Other compliance standards
- PCI-DSS
- HIPAA
- SOC 2

# Incident Response & Recovery
In case shit still hit the fan, how do we react?
Assume you have no time when this happens.
Assume you will be (or already are) breached:
- **Incident Response Plan (IRP):** The “Fire Drill”. Who do you call? What do you turn off?
	- During the Akira attack here at HR, they tried to contact everyone they needed to, and tried to go on Microsoft Teams, but they couldn’t because it was down. So they had to go on Facebook to find everyone. This shouldn’t happen.
- **Chain of Custody:** Preserving evidence for legal action. Don’t just reboot the server!
	- Logging and forensics is important.

## Recovery: RPO and RTO
**RPO (Recovery Point Objective)**
- How much data can we afford to lose?
- Determined by backup frequency. Backing up all the data once an hour, once a day, etc.

**RTO (Recovery Time Objective)**
- How long can the system be down?
- Determined by redundancy and failover speed.

## Resilience: The 3-2-1 Backup Rule
Ransomware targets backups first. Don’t keep a backup just on your computer.

> [!info] The 3-2-1 rule.
> - **3** copies of data.
> - **2** Different media types (e.g., disk + tape/cloud)
> - **1** Copy offline (physically separated)

**Immutable backups:** Backups that cannot be altered or deleted, even by an administrator, for a set period.

# CTFs and Bug Bounties
A CTF (Capture The Flag) is a security competition where participants solve challenges to find “flags” (secret strings) hidden in the challenges.
A bug bounty program is a program where organizations pay security researchers to find and report vulnerabilities in their systems.
