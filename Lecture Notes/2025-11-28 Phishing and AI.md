---
aliases: []
date created: Friday, 28. November 2025, 09:11
date modified: Monday, 8. December 2025, 18:12
---

# 2025-11-28 [Phishing](<../Terminology/Attacks/Phishing.md>) and AI

(Friday, 28 November 2025 09:00 - Week 1)

# Phishing and AI (guest lecture)

Speaker: Dr. Giovanni Apruzzese
He’s going to give us an idea of how cyberattacks and AI can be used in conjunction in modern phishing attacks.
Outline:

- Using Machine Learning for Phishing Websites Detection
- Trivially evading ML-based Phishing Website Detectors
- Using ML to evade ML-based Phishing Website Detectors
- The viewpoint of an attacker

He’ll also show us that doing many of these things can be very, very simple.

## Phishing website detection (via ML)

The current landscape of phishing is that, in truth, it’s everywhere these days.
People are constantly targeted by phishing attacks, which are becoming more sophisticated with the help of AI and Machine Learning.
Every year, new phishing attacks are created, and many of them evade traditional detection methods.
PhishTank is a popular repository of phishing websites, a popular resource for researchers and practitioners to get data about phishing websites. It’s an up-to-date list of phishing URLs. ([https://phishtank.org/](https://phishtank.org/))
These blocklists are integrated into various production systems to help protect users from phishing attacks. So you really can’t afford to make a mistake when building these systems.
*Question*: How do you think such blocklists are kept up to date?
*Answer*: They are often updated via user submissions, but mostly by automated detection systems. They use crawlers (and ML?) to find new phishing websites.
However, attackers can evade these blocklists using various techniques.

On PhishTank, you can see a list of many different suspicious websites. The list is automatically populated by crawlers that identify potential phishing websites, and users verify them. Only trustworthy users can verify them.
(One example: the **real** klarna.com URL is “**https**://www.klarna.com”, but one verified phishing URL that was found was **http**://www.klarna.com – note the lack of http**s**)

## Current landscape of phishing - countermeasures

Counter phishing websites can be done via data-driven approaches.
Example: a website is sent to preprocessing, then to analysis, then to classification, which outputs whether it’s phishing or not.
Preprocessing: extract features from the website (e.g., URLs, HTML content).
Analysis: analyze the features to determine if they are indicative of phishing.
Classification: Use a Machine Learning model to classify the website as phishing or not phishing.

### Current landscape of phishing - countermeasures (ML)

- Counter phishing websites can be done via data-driven approaches.
- Such methods include (also) Machine Learning-based approaches.
    - We train the ML model on a dataset of phishing and legitimate websites.
    - The model learns to distinguish between phishing and legitimate websites using features extracted during preprocessing.
    - Once trained, the model can be used to classify new websites as either phishing or non-phishing.
- ML-based phishing website detectors have demonstrated high accuracy in detecting phishing websites.
    - However, like with all ML approaches, they are not foolproof and can be evaded by attackers using various techniques.
- The detection of a phishing web page can entail the analysis of various elements, e.g.:
    - The URL of the web page (e.g., long URLs, suspicious domain names, etc.)
    - The HTML content of the web page (e.g., presence of forms, scripts, phishing web pages, etc.) has many elements hosted under a different domain, etc.)
    - The ‘reputation’ of the web page (e.g., known phishing domains, or whether it is reputable because it has been active for a long time, etc.)
    - The visual appearance of the web page (through reference-based detectors) (e.g., similarity to legitimate websites, etc.)
    - The network behavior of the web page (e.g., redirections, external resources, etc.)
- These analyses can be done via ML-based classifiers.
    - To apply ML for phishing website detection, we typically follow these steps:
        - Data collection: Collect a dataset of phishing and legitimate websites.
        - Feature extraction: extract relevant features from websites (e.g., URL features, HTML features).
        - Model training: train a machine learning model on the extracted features.
        - Model evaluation: evaluate the model’s performance on a separate test dataset.
        - Deployment: deploy the trained model to classify new websites as phishing or not phishing.
- These models can achieve high accuracy in detecting phishing websites, but they are not immune to evasion techniques.

He shows a PDF with a list of common patterns and features of phishing websites. We can find the list on the “Feature-based PWD” slide.

Phishing websites are usually taken down quickly, so attackers often use techniques to evade detection. The moment they are reported in a blocklist, they become useless.
Most phishing attacks fail.

- Phishers are well aware of this fact... but they (clearly) keep doing it.
    - Hence, they “have to” evade detection mechanisms to increase their chances of success.
    - (And as a result, we have to keep improving our detection mechanisms)
    - ...but they cannot invest “a lot of resources” into evasion techniques for every website they create.
- Attackers have to evade the detection of both the ML *and* the user they’re trying to phish.
    - If the user is suspicious of the website, they might not fall for the phishing attack, regardless of whether the ML model detects it.
    - Therefore, attackers must balance evading ML detection with maintaining a convincing appearance to fool users.

## Evasion techniques

Attackers can use various techniques to evade ML-based phishing website detectors.
Some common evasion techniques include:

- URL obfuscation: using techniques like URL shortening, using IP addresses instead of domain names, adding random characters to the URL, etc.
- Manipulating HTML content: adding benign elements to the HTML content, removing suspicious elements, etc. “Perturbation”, adding noise to the HTML code to confuse the ML model. No user sees them, but the ML model does, and is convinced it’s a legitimate website because of it.

Evading “logo-based” detectors:

- These detectors analyze the visual appearance of the website, specifically looking for logos of legitimate websites.
- Attackers can evade these detectors by slightly modifying the logos (e.g., changing colors, adding noise) so that the ML model does not recognize them, yet they still appear convincing to users.
- Example: adding noise to the logo image so that it is not recognized by the ML model, but still looks convincing to users.
- Because we want to avoid false positives as much as possible, these detectors have to be very strict in what they consider a logo match.

Adversarial logos:

- Attackers can use adversarial techniques to create logos that are specifically designed to evade ML-based detectors.
- These logos are generated by adding imperceptible perturbations to the original logo image, which can fool ML models but are imperceptible to humans.
- The attack applies “Generative Adversarial Perturbations” to the logo image to create a new image that is visually similar to — or even identical to — the original logo to humans, but is classified differently by the ML model.

Gap:...and user studies
Typical workflow of a user study on “phishing assessment”:

1. Craft/collect a set of phishing and legitimate websites.
2. Recruit participants for the study.
3. Show participants the websites one by one.
4. Ask participants to classify each website as phishing or legitimate.
5. Collect and analyze the results.
Results from such studies show that users can be easily fooled by phishing websites, especially when the websites are well-designed and convincing.
