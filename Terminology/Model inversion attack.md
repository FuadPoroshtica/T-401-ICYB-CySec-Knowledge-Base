---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Monday, 8. December 2025, 11:12
---
# Model Inversion Attack

**Definition**: A _model inversion attack_ is when an attacker uses access to a machine learning model to reconstruct sensitive information about the training data, effectively “inverting” the model to reveal private details.

**Context/Example**: With access to a facial recognition model, an attacker queries it repeatedly and uses the output probabilities to reconstruct an approximate image of a person whose face was used to train the model.

**Related Concepts**: Reconstruction Attacks, Overfitting, White-Box vs Black-Box Models