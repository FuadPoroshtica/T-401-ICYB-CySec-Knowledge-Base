---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Monday, 8. December 2025, 11:12
---
# k-Anonymity

**Definition**: _k-anonymity_ is a privacy model that ensures each individual in a released dataset is indistinguishable from at least **k − 1** other individuals based on a set of identifying attributes (quasi-identifiers). This reduces the risk of re-identification.

**Context/Example**: A hospital publishes patient records for research. Instead of releasing exact ages, ZIP codes, and birth dates, they generalize or suppress these fields so that every combination of quasi-identifiers appears in at least **k** records. For example, instead of “Age 27, ZIP 12345,” they release “Age 20–30, ZIP 123**.” Now, at least 10 people share the same pattern, making re-identification harder.

**Related Concepts**: Quasi-Identifiers, Data Anonymization, l-Diversity, t-Closeness, Re-identification Attacks, Privacy Models