---
aliases: []
date created: Monday, 8. December 2025, 08:12
date modified: Tuesday, 9. December 2025, 09:12
---

# IntroToCySec-Hreimur
## Cyber Defense
Attack surfaces, basically everything that has any form of input or control over software or machine, example: Email, networks, usb, sms, software dists and downloads
Computer security involves: preventing and detecting unwanted acces, use of computer and theft of data and prevention of unauthorized modifications and or injection of data catagories include unauth access, modification, and disclosure denial of auth access forgery, repudiation - -rep basically, spoofing - fakes being a legit entity
Evolution of computer security prevent attacks with better programing and design quality and test dawg
Extra Reading <br>

## **Creeper (1971)**
**How it worked?** All happened on ARPANET, it used the FTP to send a copy of itself to a new host, and after that would delete it self from the sender <br>
**Impact?** Totally harmless just displayed the message “Im the creeper catch me if you can” <br>
**Which weakness it used?** used a weakness in FTP? <br>

## **Morris Worm (1988)**
**How it worked?** used a backdoor in sendmail program to spread, and a bug in the finger program to identify network users, but it targeted specific version of Unix [OS](<../Terminology/Systems & Plaforms/Operating System.md>)’s with known flaws and it used weak passwords to its advantage to gain access to other systems where the same user had an account <br>
**Impact?** Since the worm was instructed to replicate itself 14% of the time, some machines were infected a few times causing them to become slower and slower and eventually unusable and crashing, some lame US office said total economic impact was between 100k and 10ms <br>
**Which weakness it used?** A hole in the debug mode of the Unix sendmail program, and a buffer overflow or overrun hole in the finger network service and weak passwords <br>

## **Vladimir Citibank 10ms!!**
**How it worked?** kind of unknown, but people are guessing Packet sniffing/network interception, social engineering and insider info to access legitimate credenstials of high level accounts <br>
**Impact?** mfs lost 10ms <br>
**What weakness it used?** he accessed accounts of large corporate customers of citibank from their dailup wire transfer services <br>

## **Melissa Email Worm**
**How it worked?** By sending itself trough email with word docs from infected users, when someone opened it, it would send itself to the first 50 people in the infected persons outlook address book <br>
**Impact?** Huge increase in network traffic and slowing systems down world wide. Many companies had to shutdown their email systems to stop the spread, experts say hundreds of millions in damages <br>
**What weakness it used?** The list.doc file contains a Visual Basic Script that copies the infected file into a template file used by word for custom settings and default macros. If a recipient opens the attachment the infected file will be read into the computer storage. Then the virust createes and Outlook object and reads the first 50 names in each outlook global addres book and sends a copy of its self <br>

## **Operation Olympic Games (2009)**
**How it worked?** STUXNET BAAAABY! Stuxnet had 3 modules, a worm that executed the main part or the payload, a link file that automatically executes the propagated copies of the worm and a rootkit that hid all malicious files and processes to help hide the worm. The initial infection was delivered through USB (using LNK exploit), when inside it spread across the network looking for specific Siemens controllers. Then the payload specifically targeted frequency converter drivers controlling centrifuge speeds. It would make them spin to fast or too slow while reporting normal operation to operators. Then the rootkit component is important, it hid the malicious activity from both the Windows system and the STEP 7 monitoring the PLCs <br>
**Impact?** Stuxnet reportedly destroyed one fifth of Irans nuclear centrifuges and infected over 200k computers and caused 1k machines to physically degrade. This was the first known malware to cause physical destruction of equipment and set back Irans nuclear program by an estimated 1-2 years. It also raised the concept of cyber warfare from theoretical to real <br>
**What weakness it used?** It exploited 4 zero-day exploits on machines using Windows, and Siemens STEP 7 software. It also used stolen digital certificates from legitimate companies to appear trusted <br>

## **Ukrainian Power Grid Shutdown (23rd December 2015)** - Sandworm (Russian GRU)
**How it worked?** It started with Spear phishing emails with malicious Microsoft Office attachments containing BlackEnergy malware, the attackers spent months inside the networks poking around stealing credentials and learning the SCADA systems. Then on December 23rd attackers manually took control of the SCADA systems and opened circuit breakers remotely, cutting power. Then they deployed KillDisk malware to wipe systems and corrupt master boot records making recovery after the attack harder. They also attacked the firmware of serial to ethernet converters to brick them and launched a telephone DoS attack against to power companies to block incoming calls to report outages for extra nasty points <br>
**Impact?** About 225k people lost power for 1-6 hours. Three power distributors were hit at the same time. This was also the first confirmed power outage caused by a cyberattack and demonstrated that the critical infrastructure is vulnerable to coordinated cyber operations <br>
**What weakness it used?** It used a few ways like Social engineering through the spear phishing emails, Macros in Office documents which was the initial payload delivery. Stolen credentials (Like VPN and legitimate access), lack of network segmentation since the IT and operational technology networks were not segmented properly and then legitimate remote access tools that were already in place for SCADA management <br>

## **WannaCry Ransomware Attack (2017)** - Lazarus Group (North Korean APT)
**How it worked?** It used EternalBlue exploit which is a leaked NSA tool (Shadow brokers) that exploited Windows SMB vulnerability (MS17-010). It combined worm capabilities with ransomware, since it could self propagate across networks without user interaction. Once infected, it would encrypt files and demand a payment of 300-600 USD in bitcoin to decrypt. It did have a kill switch, a hardcoded domain name that if registered would stop the malware from running (This was an oversight since the worm was not ready to be released when it was and the URL kept it in a “Sandbox” mode meaning it would just run wild.) but even with the kill switch variants without it continued to spread. <br>
**Impact?** It infected about 200k+ computers in 150+ countries in just a few days. It hit major organizations like NHS, where they cancelled surgeries and appointments, FedEx, Renault factories, Telefónica, universities and government agencies. The estimated global damage is around 4-8 billion USD! But despite massive infection the attackers only collected about 130k USD in ransom (lol) but this became a wake up call about critical patch management <br>
**What weakness it used?** EternalBlue (Love it) was the main exploit used, but unpatched systems also played a role since Microsoft had released a patch 2 months before the attack but many orgs had not applied it. Lack of network segmentation also played a role allowing the worm to spread rapidly, and also poor backup practices <br>
