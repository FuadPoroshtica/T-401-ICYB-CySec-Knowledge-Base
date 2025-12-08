- On Thursday, there will be no lab.
  Friday afternoon will be the exam
- **In the economics of defense**, the defender must be right 100% of the time, but the attacker only once.
- Security is always a tradeoff because sharks always surround you.
  That’s why they made 443 known as HTTPS, a secure tunnel.
- Risk = Threat x vulnerability x Cost
  Threats: Who attacks?
  Vulnerability: where are we weak?
  Cost/impact: What do we lose?
  *(Threat x Vulnerability = Likelihood)*
- Mitigate/Reduce, Avoid, Accept, and Transfer
- The cost should exceed the asset's value.
- **Design Principles & Defense in Depth**: Don't run a web server as root.
- Fail-safe defaults, rules what is allowed, economy of mechanism  
- Complete mediation, open design. Avoid: Security by Obscurity.
- **Defense in depth**: Everything can fail, you should have a next one to defend 
- You want to protect a physical. You want to have firewall separation between the internal network, detect all the time, including individual hosts, and make sure all data is encrypted all the time, ensure integrity, use a hash as a signature, and always have a backup.
- Administration responsibilities include MFA password policies, Training, patch management, and principles of privilege.
- By type: Physical, Technical, and Administrative, and then by Function: Preventive, Detective, and Corrective
- **Standards, Frameworks, Checklists:** Checklists fossilize procedures, Set can/should be reviewed, think of them as a synchronization point, allow training and practice.
- Management & Process.
  ISO/IEC 27000 series: how to set up a correct security setup and how the process goes. 
- NIST CSF: the U.S. standard for security methods.
- GPFR - General Data Protection Regulation - every country in the EEA is required to follow this. 
  NIS2 directive: imported into the government, for example.
  CRA -  Cyber Resilience Act: Critical for developers on the EU market.
- Digital Operational Resilience Act (DORA) is a standard for Europe, also.
- PCI-DSS: credit card security.
- HIPAA medical data security
- SOC2: SaaS/Cloud security
- **Incident Response & Recovery**: How do we react? When things go south, you don't really have a plan for how to respond, so you need one. What should I do? IRP Incident Response Plan: The “Fire Drill”. Make sure to have a plan
- Chain of custody: preserving evidence for legal action.
- RPO: Recovery point objective, how much data can we afford to lose?
  Determined by backup frequency.
- RTO: (Recovery Time Objective)
  How long can the system be down?
- Backups: 3 copies of data, 2 Different media types, and 1 Copy offsite, offline (Physically separated).
- Immutable Backups: backups that cannot be altered or deleted.
- CTF: capture the flag, to see, is a cybersecurity exercise where participants solve challenges to find 🔗 a hidden string of text, known as the “Flag”.
- Bug bounty People pay people to find bugs/vulnerabilities on their service. 
- CTF, you are authorized to have full access, but sometimes there are scope constraints, for example, only test dev.example.com. DO not perform DDoS. Do not access user data.
- International: The Budapest Convention, 
- **Summary:** Zero trust architecture: “Never trust, always verify.”
- Stay informed:
	- [Exploit db](https://www.exploit-db.com/google-hacking-database/)
	- [Microsoft Secure](https://cloudblogs.microsoft.com/microsoftsecure/)
	- [National Vulnerability Database (USA)](https://nvd.nist.gov/)
	- [Internet Storm Center](https://isc.sans.edu/)
	- [Common Vulnerabilities and Exposures](https://cve.mitre.org/) (CVE)
	- [Complete Disclosure Mailing Lists](seclists.org): fulldisclosure@seclists.org 
- Mindset, Risk, Design, Architecture, and Resilience
- **Lab today**
	- Try to jailbreak LLM.