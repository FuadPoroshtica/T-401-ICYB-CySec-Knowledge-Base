---
aliases: [Cross-Site Scripting, Cross Site Scripting, XSS]
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 11:12
---

# Cross-Site Scripting (XSS)
## Cross-Site Scripting (XSS)
XSS attacks occur when an attacker is able to inject malicious scripts into content that is then delivered to other users.
Example scenario:
Suppose you have a message board that shows what users have posted. Then a user posts a comment:
```html
Hey guys what's up? <script>sendCookiesToAttacker()</script>
```
This code in the comment becomes part of the code of the page.
When other users view that comment, their browsers will execute the script, which could send their cookies to the attacker.

### Mitigation
Convert special characters to HTML entities before displaying user input on web pages.
For example,
- convert `<` to `&lt;`,
- `>` to `&gt;`,
- and `&` to `&amp;`.
And so on. This prevents the browser from interpreting them as HTML or JavaScript.

### XSS Variants
**Reflected XSS**: The malicious script is reflected off a web server, such as in an error message, search result, or any other response that includes some or all of the input sent to the server as part of the request.

> [!example] Reflected XSS example
> An attacker sends a link to a victim that includes a malicious script in the URL. When the victim clicks the link, the script is reflected off the server and executed in the victim’s browser.

**Attribute Injection**: The attacker injects malicious code into HTML attributes, such as `onerror` or `onclick`. Breaking out of HTML attributes to add event handlers.

> [!example] Attribute Injection example
> - Code: `<img src="user.jpg" alt="USER INPUT">`
> - Input: `" onload="alert(1)`
> - Result: `<img ... alt="" onload="alert(1)">`

### XSS Defenses
Context-Aware Encoding is the main defense.
