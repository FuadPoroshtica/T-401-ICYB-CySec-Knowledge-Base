---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Monday, 8. December 2025, 11:12
---
# Passive Leakage in LLMs

**Definition**: _Passive leakage_ in Large Language Models occurs when the model unintentionally reveals sensitive, proprietary, or private information that was present in its training data, without any active exploitation by an attacker. The leakage happens naturally through normal model outputs.

**Context/Example**: A user asks an LLM a general question, and the model responds with text that resembles private conversations, internal code, or confidential documents that were part of its training set—despite the user not attempting any attack. The model “passively” leaks memorized data due to overfitting or insufficient data filtering.

**Related Concepts**: Data Memorization, Overfitting, Privacy Leakage, Training Data Contamination, Red-Teaming, Model Auditing