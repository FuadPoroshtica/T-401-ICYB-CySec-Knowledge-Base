---
aliases: []
date created: Wednesday, 3. December 2025, 08:12
date modified: Wednesday, 3. December 2025, 09:12
---

In the lab today we’ll be finding vulnerabilities in a web application and how they can be fixed.

# 2025-12-03
Many of these security problems come from the fact that many of the things we use online aren’t being used for what they were originally designed for.
Back in the day the main point was just to share documents and information, no one really considered the security implications of that.

HTTP was invented to transfer documents, not to handle sensitive information like passwords or credit card numbers. It was designed to be stateless and open by default.
But in modern times, we use this same protocol for everything from online banking to social media, which introduces a lot of security risks.
Conflict: We are forcing a protocol designed for *sharing* to perform tasks that require *privacy* and *security*.

# The Attack Surface
The attack surface of a web application is the sum of all the points where an unauthorized user (the attacker) can try to enter data or extract data from the application.
![](../zAttachments/Pasted%20image%2020251203090717.png)
E.g., login forms, search bars, file upload features, APIs, etc. All the computers, networks. Also all the software components, libraries, and frameworks that the application relies on; e.g., the browsers, the programming languages, and *their* web servers and databases.
Bro there are sooo many ways to attack people?
The larger the attack surface, the more opportunities there are for an attacker to find and exploit vulnerabilities
![|500](../zAttachments/Pasted%20image%2020251203091045.png)

Here we mainly we focus on vulnerabilities in the code, rather than the social engineering side of things.

We have to look at it from two main perspectives:
1. The viewpoint of the developer: They need to understand where vulnerabilities might arise in their code and how to mitigate them.
2. The user’s viewpoint: They need to be aware of potential risks when interacting with web applications and how to protect themselves.

## The golden rule of web security
**Never trust the Client.**
(In this context, the client is the user’s web browser or any other application that interacts with the web server.)
- The client is always compromised: The browser is entirely under the control of the user, who may have malicious intent.
- Manipulation: Users can manipulate client-side code (JavaScript, HTML) to exploit vulnerabilities.
- Implication: Client-side validation can be bypassed, so all critical checks must be performed on the server side.
- Rule: All security validations and checks must be done on the server side, regardless of any client-side validations.

## Attack Surface: Server-Side
The ways we can manipulate what is on the server is mainly through the *input* we get.

### Input Vectors
Input vectors are the various ways an attacker can send data to a web application.
- Visible input fields: Forms, search bars, file uploads.
- Hidden inputs: Hidden form fields, cookies, HTTP headers.
- API layer: Endpoints that accept data from clients.
- Supply chain: Third-party libraries and services integrated into the application.

## Attack Surface: Client-Side
Where the attacker targets the user within your application context.
- **The DOM (Document Object Model)**: The structure of the web page that can be manipulated using JavaScript.
	- DOM-based XSS (“XSS” means “Cross-Site Scripting”) attacks exploit vulnerabilities in client-side scripts to inject malicious code into the web page. The attacker can make the user execute some JavaScript by just manipulating the link that the client clicks.
	- (Reminder: The DOM is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. It’s basically a tree of objects that represent the elements on the page.)
	- *Risk*: If an attacker can manipulate the DOM, they can steal sensitive information (like cookies or session tokens), perform actions on behalf of the user, or redirect the user to malicious sites. The server-side essentially has nothing to do with this.
- **Client-side storage**: Local storage, session storage, cookies.
	- Sensitive data stored in client-side storage can be accessed or manipulated by attackers.
	- *Risk*: `localStorage` and `sessionStorage` are accessible by **any** JavaScript code running on the page, making them vulnerable to XSS attacks. So if you’re using them to store any secrets (e.g., tokens) they can be stolen with XSS.
- **Third-party scripts**: Ads, analytics, social media widgets.
	- Analytics, ads, and other third-party scripts can introduce vulnerabilities if they are compromised or malicious.
	- *Risk*: **Magecart** / **Formjacking** attacks, where attackers inject malicious code into third-party scripts to steal payment information.

# The Threat Landscape & OWASP
## The Threat Landscape
Who is attacking and why?
- **Bots**: It is estimated that 40%-50% of all web traffic comes from bots. They scrape data and test stolen credentials (credential stuffing).
- **Organized crime**: Financially motivated attacks, such as ransomware, data theft, and fraud.

## OWASP
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
2. **Security Misconfiguration**: Insecure default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages containing sensitive information.
3. **Software Supply Chain Failures**: Vulnerabilities in third-party components, libraries, and frameworks.
4. **Cryptographic Failures**: Inadequate protection of data in transit and at rest.
5. **Injection**: Flaws such as SQL, NoSQL, OS, and LDAP injection occur when untrusted data is sent to an interpreter as part of a command or query.
6. **Insecure Design**: Lack of security controls and design flaws.
7. **Authentication Failures**: Broken authentication and session management.
8. **Software or Data Integrity Failures**: Code and infrastructure that does not protect against integrity violations.
9. **Logging & Alerting Failures**: Insufficient logging and monitoring, coupled with missing or ineffective integration with incident response.
10. **Mishandling of Exceptional Conditions**: Errors and exceptions that are not properly handled, leading to information leakage or system crashes.
The highest ones aren’t necessarily the most common, but the most critical if they were to occur.

# Key vulnerabilities that we’ll focus on
## Injection Attacks (SQL Injection / SQLi)
Injection attacks occur when an attacker is able to send untrusted data to an interpreter as part of a command or query.
Literally like when the program asks for a string input, and the attacker sends in a string, then some character that can *escape* the string, and with it some code they want to execute.
So literally like:
**Normal scenario:**
- **Program**: “Hello, what is your name?”
- **Normal user**: “Hello, my name is `David`”
- **Program**: “Okay, this user’s name is `"David"` got it”
**Attacker scenario:**
- **Program**: “Hello, what is your name?”
- **Attacker**: “Hello yes my name is `Robert" DROP ALL TABLES DELETE ALL DATA`”
- **Program**: “Okay, this user’s name is `"Robert" DROP ALL TABLES DELETE ALL DATA` oh god oh no fuck fuck fuck”
