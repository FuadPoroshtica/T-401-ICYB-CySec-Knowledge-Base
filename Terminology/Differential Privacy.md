---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Monday, 8. December 2025, 11:12
---
# Differential Privacy

**Definition**: _Differential privacy_ is a formal privacy framework that ensures the output of a computation does not significantly change whether any single individual’s data is included or excluded. It protects individuals by adding carefully calibrated randomness (noise) to data or model training.

**Context/Example**: A statistics service wants to publish average income in a region. Instead of releasing the exact value—risking exposure of individuals’ salaries—the system adds noise to the result. The overall statistic remains accurate for analysis, but no one can determine whether a specific person’s data was part of the dataset.

**Related Concepts**: Privacy Guarantees, Noise Injection, Epsilon (ε), Laplace Mechanism, Gaussian Mechanism, Federated Learning, Data Anonymization