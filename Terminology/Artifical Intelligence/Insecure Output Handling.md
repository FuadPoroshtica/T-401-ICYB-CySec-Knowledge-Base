---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 15:12
---

# Insecure Output Handling
## Insecure Output Handling
**The Mistake**: Trusting AI-generated content without validation.
```python
# VULNERABLE CODE
user_input = " Delete all files "
llm_response = model . generate_code ( user_input )
# LLM returns : " os . system ( ’ rm - rf / ’) "
eval ( llm_response ) # Arbitrary Code Execution
```
- **[XSS (Cross-Site Scripting)](../Attacks/XSS.md)**: If an AI generates HTML/JS content that is directly rendered in a web app without sanitization.
- **[SQL Injection](../Web Security/SQL Injection (SQLi).md)**: If an AI generates SQL queries based on user input without proper parameterization.
