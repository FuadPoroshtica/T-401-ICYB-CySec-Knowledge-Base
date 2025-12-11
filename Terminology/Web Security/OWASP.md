---
aliases: [Open Web Application Security Project]
date created: Monday, 8. December 2025, 11:12
date modified: Thursday, 11. December 2025, 09:12
---

# OWASP

The Open Web Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software.

They provide resources, tools, and best practices for web application security.

## OWASP Top 10

One of their most well-known projects is the **OWASP Top Ten**/ **OWASP Top 10**, which is a list of the most critical web application security risks.

The OWASP Top Ten is updated every few years to reflect the evolving threat landscape.

The last version was released in 2021, and the latest version is currently being developed for 2025, though it’s basically been finalized.

Here’s the current list of 2025 OWASP Top 10:

| Rank     | Category                                                                                                                                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A01:2025 | Broken Access Control ([OWASP](https://owasp.org/Top10/2025/0x00_2025-Introduction/?utm_source=chatgpt.com "Introduction - OWASP Top 10:2025 RC1"))                                                                            |
| A02:2025 | Security Misconfiguration ([OWASP](https://owasp.org/Top10/2025/0x00_2025-Introduction/?utm_source=chatgpt.com "Introduction - OWASP Top 10:2025 RC1"))                                                                        |
| A03:2025 | Software Supply Chain Failures ([OWASP](https://owasp.org/Top10/2025/0x00_2025-Introduction/?utm_source=chatgpt.com "Introduction - OWASP Top 10:2025 RC1"))                                                                   |
| A04:2025 | Cryptographic Failures ([Orca Security](https://orca.security/resources/blog/owasp-top-10-2025-key-changes/?utm_source=chatgpt.com "OWASP Top 10 2025: Key Changes & What They Mean"))                                         |
| A05:2025 | Injection ([OWASP](https://owasp.org/Top10/2025/0x00_2025-Introduction/?utm_source=chatgpt.com "Introduction - OWASP Top 10:2025 RC1"))                                                                                        |
| A06:2025 | Insecure Design ([Invicti](https://www.invicti.com/blog/web-security/owasp-top-10?utm_source=chatgpt.com "OWASP Top 10 update for 2025"))                                                                                      |
| A07:2025 | Authentication Failures ([Orca Security](https://orca.security/resources/blog/owasp-top-10-2025-key-changes/?utm_source=chatgpt.com "OWASP Top 10 2025: Key Changes & What They Mean"))                                        |
| A08:2025 | Software or Data Integrity Failures ([OWASP](https://owasp.org/Top10/2025/0x00_2025-Introduction/?utm_source=chatgpt.com "Introduction - OWASP Top 10:2025 RC1"))                                                              |
| A09:2025 | Logging & Alerting Failures ([OWASP](https://owasp.org/Top10/2025/0x00_2025-Introduction/?utm_source=chatgpt.com "Introduction - OWASP Top 10:2025 RC1"))                                                                      |
| A10:2025 | Mishandling of Exceptional Conditions ([fastly.com](https://www.fastly.com/blog/new-2025-owasp-top-10-list-what-changed-what-you-need-to-know?utm_source=chatgpt.com "The New 2025 OWASP Top 10 List: What Changed, and ...")) |

1. **Broken Access Control**: Restrictions on what authenticated users are allowed to do are often not properly enforced.
2. **Security Misconfiguration**: Insecure default configurations, incomplete, or ad hoc configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages containing sensitive information.
3. **Software Supply Chain Failures**: Vulnerabilities in third-party components, libraries, and frameworks.
4. **Cryptographic Failures**: Inadequate protection of data in transit and at rest.
5. **Injection**: Flaws such as SQL, NoSQL, [OS](Operating System.md), and LDAP injection occur when untrusted data is sent to an interpreter as part of a command or query.
6. **Insecure Design**: Lack of security controls and design flaws.
7. **Authentication Failures**: Broken authentication and session management.
8. **Software or Data Integrity Failures**: Code and infrastructure that does not protect against integrity violations.
9. **Logging & Alerting Failures**: Insufficient logging and monitoring, coupled with missing or ineffective integration with incident response.
10. **Mishandling of Exceptional Conditions**: Errors and exceptions that are not properly handled, leading to information leakage or system crashes.
The highest ones aren’t necessarily the most common, but the most critical if they were to occur.
