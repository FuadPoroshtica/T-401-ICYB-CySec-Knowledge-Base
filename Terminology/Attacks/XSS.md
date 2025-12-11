---
aliases: [Cross-Site Scripting, Cross Site Scripting, Cross-Site Scripting (XSS), Cross–Site Scripting, Cross–Site Scripting (XSS)]
date created: Monday, 8. December 2025, 09:12
date modified: Thursday, 11. December 2025, 14:12
---

# XSS
**Definition**: Cross-Site Scripting (XSS) is a type of attack where an attacker injects malicious scripts into content from otherwise trusted websites. This allows the attacker to execute scripts in the victim’s browser, potentially stealing cookies, session tokens, or other sensitive information.

**Context/Example**: An attacker types:
```HTML
<img src=”x” onerror="alert(document.cookie)">
```

Into an unprotected input field on a website. The DOM then interoperates this as an img tag. The src is set to “`x`” which means it *always* executes the onerror code.

**Related Concepts**: Session cookie, Cookies

## Mitigation

Convert special characters to HTML entities before displaying user input on web pages.

For example,

- convert `<` to `&lt;`,
- `>` to `&gt;`,
- and `&` to `&amp;`.
And so on. This prevents the browser from interpreting them as HTML or JavaScript.

## XSS Variants
**Reflected XSS**: The malicious script is reflected off a web server, such as in an error message, search result, or any other response that includes some or all of the input sent to the server as part of the request.

> [!example] Reflected XSS example
> An attacker sends a link to a victim that includes a malicious script in the URL. When the victim clicks the link, the script is reflected off the server and executed in the victim’s browser.

**Attribute Injection**: The attacker injects malicious code into HTML attributes, such as `onerror` or `onclick`. Breaking out of HTML attributes to add event handlers.

> [!example] Attribute Injection example
> - Code: `<img src="user.jpg" alt="USER INPUT">`
> - Input: `" onload="alert(1)`
> - Result: `<img ... alt="" onload="alert(1)">`

## XSS Defenses

Context-Aware Encoding is the main defense.
