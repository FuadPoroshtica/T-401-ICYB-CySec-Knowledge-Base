---
aliases: []
date created: Thursday, 11. December 2025, 11:12
date modified: Thursday, 11. December 2025, 15:12
---

# Group README and Reflection Document

> [!quote] **Group Readme/Reflection Document Assignment description**
> A brief (1-2 page) document, ideally within your collaborative workspace or as a separate PDF, summarizing:
>
> - **Group Members:** Full names and student IDs.
> - **Chosen Tool:** Which collaborative platform did you use and why did your group select it?
> - **Organization Overview:** Briefly describe how you structured your information within the chosen tool.
> - **Collaborative Process Reflection:** Reflect on your group’s collaborative process. What worked well? What challenges did you face and how did you overcome them? How did each member contribute?

## Group Members

Here are the names of all the students in this group (`kb_group_7`), including their student emails:

- Alexander Joseph Emilsson: `alexanderje24@ru.is`
- Alfa Reynisdóttir: `alfar24@ru.is`
	- GitHub username: `alfa98516`
- Daníela Tebé Fannarsdóttir: `danielaf24@ru.is`
	- GitHub username: `DanielaTebe`
- Ema Pracková: `ema25@ru.is`
	- GitHub username: `prackema`
- Fuad Poroshtica: `fuad23@ru.is`
	- GitHub username: `FuadPoroshtica`
- Gísli Hrafn Halldórsson: `gislih24@ru.is`
	- GitHub username: `gislih24`
- Hreimur Logi Kristjánsson: `hreimur24@ru.is`
	- GitHub username: `Accent8`
- Ivan Ilanic: `ivan23@ru.is`
	- GitHub username: `IvanIlanic`
- Jón Ingi Birgisson: `jonb24@ru.is`
- Kim Anna Hudson: `kim24@ru.is`
- Kormákur Snorrason: `kormakur24@ru.is`
	- GitHub username: `kormakursnorras`
- Nastassia Herman: `nastassia25@ru.is`
	- GitHub username: `krakengard`
	-


Our collaborative project for the CySec Knowledge Base was a high-speed effort, requiring quick adaptation.

### Chosen Tool

We initially aimed to use **Notion** because we felt its visual organization tools would be ideal for structuring the complex topics in the course. However, when we ran into issues securing a student discount for Notion, we had to swiftly change our plan. Given the three-week time frame, we quickly switched to Obsidian and GitHub. This proved to be a practical decision, as Obsidian offered easy, real-time co-editing that everyone was already familiar with, removing any delays associated with learning a new platform. Discord served as our central hub for quick decisions and coordination.

### Organization Overview

We organized our information to be maximally efficient for exam lookup, dividing the course content into major, easy-to-navigate sections. We structured the document to follow the flow of the material, moving from foundational principles to system security, and then to advanced, modern threats.

The structure ensured that concepts such as the **CIA Triad** (Confidentiality, Integrity, and Availability) and **Defense in Depth** were defined clearly at the beginning. We then built upon this foundation by dedicating separate sections to highly technical areas like **Operating System Mechanics** (Kernel/User Space, Auditing) and **Network Protocols** (IP, TCP/UDP, BGP). Finally, we grouped the modern and non-technical risks, including **Web Vulnerabilities** (XSS, SQLi) , **AI Security Threats** (Prompt Injection) , and **Operational Security (OPSEC)**. We made sure to clarify core ideas, such as always checking for authorization in **IDOR** vulnerabilities and using prepared statements for **SQLi**.

### Collaborative Process Reflection

Our three-week schedule presented significant time constraints, which required strict discipline and coordination.

**What Worked Well:**

- **Adaptability:** The decision to quickly switch from Notion to Obsidian minimized downtime and ensured all members could contribute immediately without a steep learning curve.
   
- **Continuous Feedback:** We relied heavily on Discord for rapid checks and clarifications. If one member encountered confusing terminology or inconsistent information across different lecture sources (e.g., confirming the correct mitigation for a specific vulnerability), a quick question on Discord ensured everyone stayed aligned.
 
**Challenges and How We Overcame Them:**

- **Information Volume and Consistency:** The sheer amount of information, especially specific command syntax and complex acronyms (like ASLR, DEP/NX, BGP, POSIX), was difficult to manage. We overcame this by dedicating time after every major lecture block to a final review session. During this session, we cross-referenced all notes against the original slides to verify key definitions and tool usage, ensuring high accuracy.
    
- **Synthesizing Overlapping Concepts:** Many core principles, such as **Least Privilege** and **Defense in Depth**, appeared in the context of Operating Systems, Networks, and Web Security. To avoid repetition, we decided to define these fundamental concepts once in a core section and simply reference them when discussing their technical implementation (e.g., discussing SUID as an enforcement of Least Privilege).
    

cd 
You can see how much each member contributed to the knowledge base on the [contributors page](https://github.com/FuadPoroshtica/T-401-ICYB-CySec-Knowledge-Base/graphs/contributors).

You can see how much each member contributed to the knowledge base on the [contributors page](https://github.com/FuadPoroshtica/T-401-ICYB-CySec-Knowledge-Base/graphs/contributors), which shows the Git-based version history for the project.

## Chosen Tool

We felt that a “wiki”-like approach would be most appropriate for a [Cyber Security](Terminology/Cyber Security.md) knowledge base, because it lets us dynamically link together a large number of related topics in an intuitive way. A wiki (like Wikipedia) allows you to add as much information as you want without being constrained by a rigid folder hierarchy, since connections between concepts are handled through links and backlinks rather than through deep folder nesting. This matches the assignment goals of building a navigable, interlinked knowledge base of notes, terminology, tools, and resources.

We initially started with Notion, a well-known collaborative Markdown-style editor with support for internal links. We chose it at first because:

- it works directly in the browser,
- it is easy to onboard new users,
- and we assumed we would have access to a free premium student tier.

However, we eventually ran into its paywall, and continuing with our existing workspace would have required paying for additional seats ($120 in total). Instead of paying the fee, we exported our content and migrated to **Obsidian**, another popular Markdown-based, wiki-style editor.

We chose Obsidian for the final version of the knowledge base because:

- It is completely free for personal and educational use.
- It works locally, so there are no surprises with quotas or paywalls.
- Its support for **wikilinks** (`Page name`, e.g., [Side-Channel Attack](Terminology/Virtualization/Side-Channel Attack.md)).
- It integrates well with **Git and GitHub**, giving us proper version control and an easy way to share our work with instructors. Additionally, it lets us view it online during the final exam itself using GitHub’s “wiki” feature.
- There is a large ecosystem of community plugins, which we could use if needed (though we mostly stuck to core features for this assignment).

The main disadvantage of Obsidian compared to Notion is that it requires installing a desktop application and having some basic familiarity with Git. This has created a small learning curve for some group members, but it is currently quite straightforward and stable.

## Organization Overview

We organized our knowledge base using a relatively shallow folder structure and relied heavily on Obsidian’s internal links and search to connect related topics. This allowed us to keep the system flexible while still satisfying the assignment requirements.

The top-level structure is:

- `/Lecture notes/`
	- Contains collaboratively written notes for each lecture. Each file corresponds to a specific lecture date or topic. Inside these notes we:
		- summarize key concepts and definitions,
		- highlight important takeaways,
		- link to terminology entries and tools mentioned in the lecture,
		- and occasionally add diagrams or code snippets when they help clarify an idea.

- `/Terminology/`
	- Contains our glossary of cyber security terms. Entries are loosely grouped by topic (e.g., networking, web security, operating system security) but we intentionally kept the folder structure simple. Each glossary note typically includes:
		- a definition,
		- context or examples,
		- related terms (linked via Obsidian wikilinks),
		- and sometimes links to external resources or relevant tools.

- `/Resources/`
	TODO

- `/Tools and Commands/`
	- A compendium of security tools and common commands, grouped by purpose (e.g., scanning, log analysis, forensics, etc.). For each tool or command we try to include:
		- a short description of what it does,
		- example usage,
		- typical operating system(s),
		- and a link to official documentation.

Although these folders exist, we did not want the folder hierarchy to become a bottleneck. Instead, we relied on:

- consistent naming conventions (e.g., `Lecture YYYY-MM-DD Topic`, `Term – XYZ`),
- and Obsidian’s graph/backlinks view.

This approach let us quickly jump from a lecture note to the relevant glossary term, see all tools associated with a particular topic, and keep the knowledge base usable even as it grew.

## Collaborative Process Reflection

TODO

