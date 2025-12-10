---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 15:12
---

# Hallucination Squatting
## Hallucination Squatting
A.k.a. *Package Hallucinations*:
1. [LLMs](LLM.md) often hallucinate (invent) code libraries or packages that *sound* real but don’t actually exist. (Which is in-general just how LLMs work; they generate plausible-sounding text based on patterns in training data.)
2. The attack:
      1. Attackers query LLMs to find these common hallucinations.
      2. They register the package name on package repositories (like npm, PyPI).
      3. They upload malicious code to these packages.
3. The victim: Developers who copy-paste code from LLMs without verifying the existence of the packages then run `npm install` or `pip install` on the hallucinated package, thereby installing [Malware](../Attacks/Malware/Malware.md).
