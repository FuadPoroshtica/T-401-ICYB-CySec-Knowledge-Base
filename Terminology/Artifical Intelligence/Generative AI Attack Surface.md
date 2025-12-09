---
aliases: []
date created: Monday, 8. December 2025, 11:12
date modified: Monday, 8. December 2025, 15:12
---

# Generative AI Attack Surface
The places where attacks can happen:

## Supply Chain (Training Phases)
Security vulnerabilities can be introduced during any stage of the training process of AIs:
1. **Pre-Training (The foundation):**
	- During this stage the AI model is trained on literal petabytes (quadrillions of bytes) of data from the internet.
	- *Risk*: Data Poisoning. Baking bad data into the model itself.
    	- Example: If you want to make an AI that is biased against a certain group, you can poison the training data with negative content about that group.
	- *Mitigation*: Data Curation. Carefully selecting and cleaning the training data to remove harmful or biased content.
2. **Fine-Tuning (The specialization):**
	- Training on specific tasks, like coding, medical diagnosis, etc.
    - *Risk*: Model Manipulation. Changing the model’s behavior in specific ways.
    	- Example: If you want to make an AI that gives wrong medical advice, you can fine-tune it on incorrect medical data.
	- *Mitigation*: Robust Fine-Tuning. Using techniques that make it harder to manipulate the model during fine-tuning.
3. **RLHF (Reinforcement Learning from Human Feedback) (The Safety Layer):**
	- Humans teach the model to refuse harmful requests.
	- *Risk*: Jailbreaking is essentially bypassing RLHF alignment.
    	- Example: [Prompt Injection](Prompt%20Injection.md) attacks.
	- *Mitigation*: Advanced Alignment Techniques. Using more sophisticated methods to align the model with human values.

## The Mechanism (Why injection works)
- **Tokenization**: [LLMs](LLM.md) break down input text into smaller pieces called tokens. These tokens can be words, subwords, or even characters.
- **Context Window (Short Term Memory)**: LLMs have a limited context window, meaning they can only consider a certain number of tokens at a time when generating responses.
- *Risk*: [Prompt Injection](Prompt%20Injection.md) Attacks
    - Attackers can craft inputs that exploit the tokenization and context window limitations to manipulate the model’s behavior.
    - Example: An attacker could input a prompt that tricks the model into ignoring its safety instructions and generating harmful content.

Comparison of injection methods:
- **[Buffer Overflow](../Attacks/Buffer%20Overflow.md) code injection**: Overwrite specific memory locations to change program behavior.
- **[SQL Injection](../Web%20Security/SQL%20Injection%20(SQLi).md)**: User input is interpreted as an SQL command.
- **LLM Injection**: User input is interpreted as a System Instruction
