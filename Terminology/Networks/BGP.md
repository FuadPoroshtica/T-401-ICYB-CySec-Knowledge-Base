---
aliases: [Border Gateway Protocol]
date created: Tuesday, 2. December 2025, 19:12
date modified: Tuesday, 2. December 2025, 19:12
---

# BGP
- Used between routes of neighboring [Autonomous Systems (ASes)](AS.md) to exchange routing information (info about available routes).
- Routing is based on local criteria, such as path attributes, not necessarily the shortest path (efficiency criteria).
	- E.g., company A has a peering agreement with company B, so it prefers routes through B even if they are longer.
	- Price of having traffic carried on a particular route.
	- Route length
	- Politics
- Data entry is often manual (network administrators configure routing policies, potential for human error).
- BGP lacks basic authentication and security features, making it vulnerable to various attacks (e.g., route hijacking).

**Possible attack: BGP Hijacking.**
BGP operates on trust. If a malicious [AS](AS.md) advertises that it has the best route to a particular [IP](TCP%20IP%20Model/IP.md) prefix, other ASes may accept this information and route traffic through the malicious [AS](AS.md). So an attacker can exploit the Longest Prefix Match rule to divert traffic.
- **The attack**: The victim announces `10.0.0.0./8`. The attacker announces `10.1.0.0/16` (a sub-prefix of the victim’s prefix). Because of longest prefix match, traffic destined for it will be routed to the attacker.
- **The result**: Traffic interception, data theft, traffic analysis, denial of service.
- **Mitigation**: RPKI (Resource Public Key Infrastructure) to cryptographically verify route announcements

In 2008, Pakistan Telecom attempted to block access to YouTube within Pakistan by announcing a more specific route for YouTube’s IP address range (a /24 prefix) than the legitimate route announced by YouTube (a /22 prefix). However, this announcement was propagated beyond Pakistan’s borders, causing global traffic destined for YouTube to be misrouted to Pakistan Telecom. This incident resulted in a significant portion of global YouTube traffic being diverted to Pakistan, leading to widespread service disruption until the issue was resolved.
