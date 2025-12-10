---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 18:12
---

# Incident Response & Recovery 🚨🛠️
In case shit still hit the fan, how do we react?
Assume you have no time when this happens.
Assume you will be (or already are) breached:
- **Incident Response Plan (IRP):** The “Fire Drill”. Who do you call? What do you turn off?
	- During the Akira attack here at HR, they tried to contact everyone they needed to, and tried to go on Microsoft Teams, but they couldn’t because it was down. So they had to go on Facebook to find everyone. This shouldn’t happen.
- **Chain of Custody:** Preserving evidence for legal action. Don’t just reboot the server!
	- Logging and forensics is important.

## Recovery: RPO and RTO ⏱️
**[RPO](Recovery%20Point%20Objective%20(RPO).md) (Recovery Point Objective)** 📂
- How much data can we afford to lose?
- Determined by backup frequency. Backing up all the data once an hour, once a day, etc.

**[RTO](Recovery%20Time%20Objective%20(RTO).md) (Recovery Time Objective)** 🕰️
- How long can the system be down?
- Determined by redundancy and failover speed.

## Resilience: [The 3-2-1 Backup Rule](The%203-2-1%20Backup%20Rule.md) 💾
[Ransomware](../Attacks/Malware/Ransomware.md) targets backups first. Don’t keep a backup just on your computer.

> [!info] The 3-2-1 Rule
> - **3** copies of data.
> - **2** Different media types (e.g., disk + tape/cloud)
> - **1** Copy offline (physically separated)

**Immutable backups:** Backups that cannot be altered or deleted, even by an administrator, for a set period.
