---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Thursday, 11. December 2025, 09:12
---

# Defense in Depth
## Defense in Depth 🧅
### The Layered Approach (The Onion) 🧅

The idea is that this is a layered approach.

No single control is infallible. If one layer fails, others are still there and catch the threat.

1. **Physical controls:** Locks, guards, cameras. 🏢🔒
2. **Technical controls:** [Firewalls](<./Firewall.md>), encryption, [Access Control](Access Control.md). 💻🛡️
	- **Perimeter/Network defenses:** Firewalls, IDS/IPS, DMZ, VPN, Intrusion Detection Systems.
	- **Host/Endpoint defenses:** Antivirus, Monitoring
	- **Application defenses:** Input validation, secure coding practices.
	- **Data defenses:** Encryption, backups, hashing
3. **Administrative controls:** Policies, training, incident response plans. 📋
	- **People:** Training, awareness programs, MFA (Multi-Factor Authentication), password policies.
	- **Technology:** Patch management, risk assessments, audits.
	- **Operations:** Principle of least privilege, change management, incident response.
*Scenario:* If a laptop is stolen (physical security fail), the hard drive encryption (data layer) protects the information.

### Classifying Controls 📊

By type: 🧩

- **Physical controls:** Locks, guards, cameras.
- **Technical controls:** Firewalls, encryption, [Access Control](Access Control.md).
- **Administrative controls:** Policies, training, incident response plans.

By function: 🎯

- **Preventive controls:** Stop attacks before they happen (e.g., [Firewalls](<./Firewall.md>), [Access Control](Access Control.md)).
- **Detective controls:** Identify and log attacks (e.g., Intrusion Detection System (IDS), monitoring).
- **Corrective controls:** Respond to and recover from attacks (e.g., backups, incident response).
