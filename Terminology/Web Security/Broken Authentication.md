---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 11:12
---

# Broken Authentication
Usually a logic or configuration error, not a code bug.
**Common mistakes:**
- Weak password policies. Programs shouldn’t allow users to have weak passwords. The characteristics of a weak password are:
	- Contains segments that are easy to guess (like words from the dictionary)
	- Only contains letters (no mix of letters and special symbols and/or numbers)
	- Only contains lowercase letters
	- The password is *short*.
- No lockout mechanism. The system should time you out if you type the wrong password, it shouldn’t give you like 10,000 tries or something.
- Session IDs in the URL. Session IDs should be stored in cookies, not in the URL, because URLs can be logged and leaked. Session IDs here are like tokens that prove you are logged in.

## Mitigation
- Multi-factor authentication (MFA): Require users to provide two or more verification factors to gain access to a resource.
- Use standard libraries for session management and authentication.
- Don’t roll your own authentication system; use well-established frameworks and libraries.
- Don’t roll your own cryptography; use established libraries and protocols.
- Don’t reinvent the wheel.
- Implement strong password policies (minimum length, complexity requirements).
- Implement account lockout mechanisms after a certain number of failed login attempts.
- Use secure cookies for session management (HttpOnly, Secure, SameSite attributes).
- Regularly review and update authentication mechanisms to address new threats.
