---
aliases: []
date created: Wednesday, 3. December 2025, 08:12
date modified: Thursday, 4. December 2025, 11:12
---

# 2025-12-03  Web Security & Attack Surfaces (Fuad)

**Sources:** Lecture Slides 8 & 8a

---

## 1. Context: Documents vs. Applications
The fundamental difficulty in web security arises from a conflict in design versus usage.
- **Original Design:** HTTP was invented to share static, public documents. It was designed to be stateless and “open by default” [1].
- **Modern Reality:** We use this same protocol for banking, healthcare, and critical infrastructure [1].
- **The Conflict:** We are forcing a protocol designed for *sharing* to perform tasks requiring *secrecy and rigid control* [2].

---

## 2. Core Security Principles
- **The Golden Rule:** **“Never Trust the Client.”**
    - The browser is entirely under the user’s control. Users can manipulate HTML, bypass JS validation, edit cookies, and change headers [2].
    - *Implication:* Client-side validation is strictly for User Experience (UI). All security validation must happen on the Server [2].
- **Defense in Depth:** Layered security. If the firewall fails, authentication must hold. If Auth fails, input validation must hold [3].
- **Least Privilege:** Servers should not run as root; database users should not have unnecessary rights (e.g., `DROP TABLE`) [3].
- **Avoid “Security by Obscurity”:** Hiding API URLs or relying on secret implementation details does not make a system safe [4].
- **Linus’s Law:** Rely on open-source, popular approaches because “Given enough eyeballs, all bugs are shallow” [4].
- **Don’t Roll Your Own Crypto:** Use well-tested external libraries and delegation standards like OAuth 2.0 [5], [6].

---

## 3. The Attack Surface
The attack surface is the sum of all points (vectors) where an unauthorized user can attempt to enter or extract data [7].

### A. Server-Side Surface
- **Visible Inputs:** Search forms, login fields, file uploads (risk of Webshells) [7].
- **Hidden Inputs:** URL parameters (e.g., `?id=5`), HTTP Headers (User-Agent, Referer), and Cookies [7].
- **API Layer:** Exposed REST/GraphQL endpoints. Risk of Broken Object Level Authorization (BOLA) [7], [8].
- **Supply Chain:** Vulnerabilities in third-party libraries (e.g., `node_modules` or `requirements.txt`) [8].

### B. Client-Side Surface
- **The DOM:** Attackers target the Document Object Model (e.g., DOM-based XSS) [8].
- **Storage:** `localStorage` and `sessionStorage` are accessible by any JavaScript on the page. Storing secrets here is risky [8].
- **Third-Party Scripts:** Analytics or chat widgets can be compromised (Magecart/Formjacking) to steal data like credit cards [9].

### C. Network & User Surface
- **Network:** HTTP transmits headers, passwords, and session IDs in clear text. HTTPS encrypts this but is not 100% safe [4], [6].
- **Social Engineering:** Targeting the human element (users) is a valid attack vector [10].

---

## 4. The Threat Landscape & OWASP
- **Actors:**
    - **Bots:** 40–50% of web traffic (scraping, credential stuffing) [9].
    - **Organized Crime:** Focused on ransomware and data theft for profit [9].
- **OWASP (Open Web Application Security Project):** A non-profit foundation tracking critical risks [9].
- **OWASP Top 10:** A standard awareness document. Key persistent risks include Broken Access Control, Security Misconfiguration, and Software Supply Chain Failures [11].

---

## 5. Key Vulnerabilities

### A. SQL Injection (SQLi)
- **Concept:** Untrusted data is sent to an interpreter as part of a command (concatenating strings) [11].
- **The Attack:** Inputting `' OR '1'='1` causes the query to return all records (e.g., Admin login bypass) [12].
- **The Fix:** Use **Parameterized Queries (Prepared Statements)**. The database treats input strictly as data, not executable code [12].

### B. Insecure Direct Object References (IDOR)
- **Concept:** The application uses user-supplied input (like an ID in a URL) to access objects without verifying authorization [12].
- **The Attack:** Changing `?id=10050` to `?id=10051` to view another student’s grades [13].
- **The Fix:** Always verify server-side that the `current_user.id` matches the requested resource owner. Use UUIDs instead of sequential integers [13].

### C. Broken Authentication
- **Causes:** Logic errors, weak passwords (“123456”), lack of lockout mechanisms (brute force), or exposing session IDs in URLs [5].
- **The Fix:** Multi-Factor Authentication (MFA) and standard session management libraries [5].

### D. Cross-Site Scripting (XSS)
- **Concept:** Attacking *other users* by injecting malicious scripts that execute in their browser [5].
- **The Kill Chain:**
    1. Script reads `document.cookie` (Session ID).
    2. Script exfiltrates data to the attacker.
    3. Attacker hijacks the user’s session [14].
- **Variants:**
    - *Reflected:* Input returned immediately (e.g., search results) [15].
    - *Attribute Injection:* Breaking out of HTML attributes (e.g., `onload="alert(1)"`) [15].
- **Defenses:**
    1. **Context-Aware Encoding:** Convert special characters (`<`) to HTML entities (`&lt;`) [15].
    2. **HttpOnly Cookies:** Prevents JavaScript from reading cookies [16].
    3. **Content Security Policy (CSP):** Whitelists allowed script sources [16].

---

## 6. The Security Toolbox
**⚠️ LEGAL WARNING:** Only use these tools on localhost projects or environments where you have explicit written permission (e.g., OWASP Juice Shop) [3].

### Phase 1: Reconnaissance (Passive)
- **Browser DevTools (<kbd>F12</kbd>):** Inspect network requests, headers, and local storage [17].
- **Wappalyzer:** Identifies technology stacks and versions (e.g., PHP 5.6) [17].
- **DNSDumpster:** Maps attack surfaces (subdomains) passively [18].

### Phase 2: Discovery & Enumeration (Active)
- **Nmap:** Network discovery. Can detect open ports and known vulnerabilities via the NSE script engine [18].
- **Gobuster / Dirb:** Brute-forces URLs to find hidden directories (e.g., `/admin`, `/backup`, `/.git`) [18].

### Phase 3: Interception & Exploitation
- **Burp Suite / OWASP ZAP:** Proxy tools that sit between the browser and server. Allows “Man-in-the-Middle” manipulation of requests [19].
- **SQLMap:** Automates SQL injection detection and database dumping [19].
- **Nikto:** Scans web servers for outdated versions and insecure configurations [19].

---

## 7. Further Study Topics
- **CSRF (Cross-Site Request Forgery):** How it differs from XSS [20].
- **SSRF (Server-Side Request Forgery):** Risks and mitigations [20].
- **Insecure Deserialization:** How modifying serialized objects leads to Remote Code Execution (RCE) [20].
