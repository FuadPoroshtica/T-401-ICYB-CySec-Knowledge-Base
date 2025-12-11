---
aliases: [SQL Injection, SQLi]
date created: Monday, 8. December 2025, 11:12
date modified: Thursday, 11. December 2025, 09:12
---

# SQL Injection
## Injection (SQL Injection / SQLi)

An SQL Injection (SQLi) is a code injection technique that exploits a security vulnerability occurring in the database layer of an application.

The vulnerability is present when user input is either incorrectly filtered for string literal escape characters embedded in SQL statements or user input is not strongly typed and unexpectedly executed. This allows an attacker to interfere with the queries that an application makes to its database.

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

Mitigation of SQLi involves several best practices and techniques to prevent attackers from injecting malicious SQL code:

- Use Prepared Statements (Parameterized Queries): Ensure that SQL queries are defined with placeholders for parameters, and user input is bound to these parameters. This prevents the input from being treated as executable code.
- Use Stored Procedures: Encapsulate SQL queries within stored procedures on the database server, which can help separate data from code.
- Input Validation: Validate and sanitize all user inputs to ensure they conform to expected formats and types.
- Least Privilege Principle: Limit database user permissions to only what is necessary for the application to function.
- Use ORM (Object-Relational Mapping) Frameworks: These frameworks often provide built-in protection against SQL injection.
- Regular Security Testing: Conduct code reviews, penetration testing, and use automated tools to detect SQL injection vulnerabilities.
- Keep Software Updated: Ensure that database management systems and related software are up to date with security patches.
