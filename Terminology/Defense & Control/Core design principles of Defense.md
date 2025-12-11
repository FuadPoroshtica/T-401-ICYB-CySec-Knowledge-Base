---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Thursday, 11. December 2025, 09:12
---

# Core design principles of Defense
## Core design principles 🧱

The most important ones from Saltzer & Schroeder are:

- 🔑**Least privilege:** Give each user/process the minimum privileges needed to perform its function.
	- E.g., a web server process should not run as root.
	- Why? Because if the process is compromised, the attacker only gets limited access.
- ⚠️**Fail-safe defaults:** Default to no access, unless explicitly granted.
	- E.g., file permissions in Unix are by default restrictive.
	- Why? Because it’s easier to grant access than to revoke it.
	- Also, you’ll notice better when people don’t have *enough* access, because they’ll complain immediately. But no one complains when they have *too much* access.
- 🧩**Economy of mechanism:** Keep the design as simple and small as possible. Complexity hides vulnerabilities.
	- E.g., a simple protocol is easier to analyze for security flaws.
- 🔍**Complete mediation:** Every access to every resource must be checked for authorization.
	- E.g., a filesystem must check permissions on every file access.
	- Why? Because if some accesses are not checked, they can be exploited.
- 📖**Open design:** The security of a system should not depend on the secrecy of its design or implementation.
	- E.g., open-source software can be reviewed by many experts.
	- Why? Because security through obscurity is not reliable.
	- **Avoid:** Security by obscurity.
