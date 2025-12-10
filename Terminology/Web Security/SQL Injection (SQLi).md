---
aliases: [SQL Injection, SQLi]
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 11:12
---

# SQL Injection
## Injection (SQL Injection / SQLi)
Injection attacks occur when an attacker is able to send untrusted data to an interpreter as part of a command or query.
Literally like when the program asks for a string input, and the attacker sends in a string, then some character that can *escape* the string, and with it some code they want to execute.
So literally like:
**Normal scenario:**
- **Program**: “Hello, what is your name?”
- **Normal user**: “Hello, my name is `David`”
- **Program**: “Okay, this user’s name is `username = "David"` got it”
**Attacker scenario:**
- **Program**: “Hello, what is your name?”
- **Attacker**: “Hello yes my name is `Robert"; DROP ALL TABLES DELETE ALL DATA;`”
- **Program**: “Okay, this user’s name is `username = "Robert"; DROP ALL TABLES DELETE ALL DATA;` oh god oh no *fuck fuck fuck* WHAT HAVE YOU DONE?!?! YOU TRICKED ME!!!!”

### Mitigation
To mitigate the threat of SQLi
