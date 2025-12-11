---
aliases: [Insecure Direct Object References, IDOR]
date created: Monday, 8. December 2025, 11:12
date modified: Thursday, 11. December 2025, 18:12
---

# Insecure Direct Object References (IDOR)

A surprisingly common problem in web applications.

The problem is that the application provides access to objects based on the URL they’re going to, but the application might forget to check if the user is authorized to go there/do that (yes, you can sometimes do things with just a URL).

## Mitigation

Mitigation of
