---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 11:12
---

# Model Inversion, Extraction, Poisoning
## Model Inversion, Extraction, Poisoning
**Model Inversion (Privacy):**
- Querying the model to reconstruct sensitive training data.
- *Example*: Asking specifically crafted questions to force the model to leak PII (emails, SSNs) seen during training.
- *Mitigation*: Differential Privacy during training to limit memorization of specific data points.
**Model Extraction (IP Theft):**
- Querying an API extensively to train a “Student Model” that mimics the proprietary “Teacher Model.”
- *Example*: Using thousands of API calls to replicate a paid LLM service.
- *Mitigation*: Rate limiting, monitoring unusual query patterns.
**Data Poisoning:**
- Manipulating the training data or fine-tuning data to introduce backdoors or bias.
- *Example*: Injecting malicious code snippets into the training data of a coding assistant LLM.
- *Mitigation*: Data validation, robust training techniques.
