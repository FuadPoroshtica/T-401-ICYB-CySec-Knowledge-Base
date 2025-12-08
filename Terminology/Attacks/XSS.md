---
aliases: 
date created: Monday, 8. December 2025, 09:12
date modified: Monday, 8. December 2025, 09:12
---
**Definition**: A “Cross Site Scripting” attack, someone manages to execute a script on the client-side, can give access to session tokens and cookies.
 
**Context/Example**: An attacker types:
```HTML
<img src=”x” onerror="alert(document.cookie)">
```
Into an unprotected input field on a website. The DOM then interoperates this as an img tag. The src  is set to “x” which means it *always* executes the onerror code.

**Related Concepts**: Session cookie, Cookies
z