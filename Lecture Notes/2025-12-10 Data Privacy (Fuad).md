---
aliases: 
date created: Wednesday, 10. December 2025, 08:12
date modified: Wednesday, 10. December 2025, 09:12
---

# 2025-12-10 Data Privacy (Fuad)
## **Definitions**
- Unauthorized instruction
	- Unauthorized network access
	- Unauthorized data access
	- Unauthorized surveillance
	- Unauthorized system behavior
- Privacy vs security: Think like your data is gold,
	- Privacy - who has access?
	- Security - how to get access
- I need to maintain my identity privately
- I need to maintain security by verifying everyone’s identity.
- Security goes around privacy.
- Law makers: GDPR (Europe), CCPA (California, USA), and PIPEDA (Canada)
- CS: Anonymization techniques and Differential privacy

## **Myths**
- **Myth 1:** My data is not personal, so does it count?
	- Used to justify metadata collection
	- Assumes only explicit identifiers matter
- **Attack:**
- loc3 = 2 > t0, loc3 (Trajectory 1), loc3 (Trajectory 2)
- At night, people are less likely to move places which is why they got this formula:
		![](../zAttachments/Pasted%20image%2020251210091739.png)

- They try to figure out the next move, ![](../zAttachments/Pasted%20image%2020251210092029.png)
- **Myth 2:** You have zero privacy anyway - get over it.
	- You can be captured on CCTV without consent, for example, or Covid 19 getting notification that the next person in your vicinity has the virus
- The Europe General Data Protection Regulation (GDPR) has explicitly made Data Protection by Design and by Default an obligation for data controllers
	- Considered from the earliest design stages.
	- Preventing data from being collected for one specific purpose is easily reused for another purpose
	- Built-in privacy safeguards.
	- Privacy beyond purely technical components, addressing organizational procedures and business models.
- **Myth 3:** “If you’re not doing anything wrong...”
- **Frames privacy as secrecy:**
	- Only individuals engaging in wrongdoing need privacy, and if you have nothing to fear, you have nothing to hide
- **Normalizes surveillance**
- **Right vs Wrong**
	- The premise assumes that the ethical status of an action is easily answered: either you did something bad, or there is nothing to worry about.
	- The distinction between ”right” and ”wrong” is complex, depending on legal constraints, cultural context, and jurisdiction
	- Example: sexual orientation or smoking cannabis
	- The common assumption that only wrongdoing requires privacy is often perpetuated by those who try to exploit the data collected
- **Myth 4:** “We Always Need to Know Who You Are.”
	- Assumes identity is required everywhere.
	- Assumes that accessing most online resources necessarily requires users to fully identify themselves (name, address, etc.)
	- Encourages unnecessary tracking
	- Do we need to give our fingerprints to access the gym?
- Authentication is NOT identification
- Systems can be designed to allow individuals to prove they meet a requirement without revealing their complete identity.
- Anonymous and pseudonymous options exist.
- For many services, it is sufficient to know whether a user has a specific attribute.
- **Myth 5:** “Your Data Is Safe With Us.”
	- Companies overestimate their security
	- Large companies frame privacy as merely a security issue to be solved through centralized control.
	- Users cannot verify claims.
- **Reality: Data Is a Liability**
- Breaches are inevitable
	- Privacy is defined by the individual being in control of their data, not by trusting a massive, centralized entity.
- Insiders and third-party vendors introduce risk
- Not sharing location unless it is really needed.
- Data not collected cannot be breached
- Centralized vs Distributed
	- Decentralized or fully distributed peer-to-peer designs provide strong privacy by processing data locally on the user’s device.
- Caveat: Although decentralization is powerful, techniques such as federated learning still enable the system as a whole to predict, evaluate, and nudge the user, even when personal data is processed locally.
- **Myth 6:** “Privacy Competes With Innovation”
	- Frames privacy as a barrier
	- Used to justify over-collection
	- Privacy, utility, security, and functionality are opposing, irreconcilable goals, meaning that achieving one requires sacrificing the others.

## **Privacy Enhancing Techniques**
- K-Anonymity: ![](../zAttachments/Pasted%20image%2020251210094802.png)
- Differential Privacy:![](../zAttachments/Pasted%20image%2020251210095218.png)
- Differential Privacy 2: ![](../zAttachments/Pasted%20image%2020251210095346.png)

## **Future Challenges: Large Language Models**

**Large Language Models** - attack strategies
- Passive Leakage: Sensitive Inquiries ![](../zAttachments/Pasted%20image%2020251210095700.png)
- A PhD student accessed Samsung's data, noting that it relies on a third-party company, and that the information he obtained was also private. This was a huge mistake made by Samsung.
- Passive Leakage: Contextual Leakage![](../zAttachments/Pasted%20image%2020251210095750.png)
- Mental and sensitive data should not be revealed with LLM. - Law is not the same as any authorized person, like the police, can have access to that data.
- Passive Leakage: Personal Preferences Leakage ![](../zAttachments/Pasted%20image%2020251210095833.png)
- A big LLM will soon start using your data to create an advertisement, which will lead to your data being used.
- Active Attacks: Jailbreak Attack ![](../zAttachments/Pasted%20image%2020251210100401.png)
- Yu, Zhiyuan, et al. ”Don’t listen to me: Understanding and exploring jailbreak prompts of large language models.” 33rd USENIX Security Symposium (USENIX Security 24). 2024.
- Active Attacks: Jailbreak Attack 2![](../zAttachments/Screenshot%202025-12-10%20at%2010.04.50.png)
## **Large Language Models**
**Attack Targets**
- Attack Target: Membership Inference Attacks![](../zAttachments/Screenshot%202025-12-10%20at%2010.06.15.png)
- They need to know about previous data to learn more about you, 
- Attack Target: Model Inversion ![](../zAttachments/Screenshot%202025-12-10%20at%2010.08.20.png)
**Takeaways**
- Lessons:
	- Privacy is a technical and ethical requirement
	- Tracking is embedded deeply in modern architectures
- By now, you should be able to:
	- Explain why privacy matters in computing systems
	- Identify privacy risks from a technical and societal lens
	- Develop critical perspectives on tech design decisions
    
**Food for Thought**
- Are ’free’ services ethically acceptable?
- Should CS professionals be liable for privacy harms?
- What should students prioritize: innovation or safety?
- Importance of privacy-by-design development
> T-722-PRIV, Foundations of Data Privacy: A Legal and Technical Perspective
	Fatimae@ru.is
	