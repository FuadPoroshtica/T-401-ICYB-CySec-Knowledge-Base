---
aliases: []
date created: Monday, 1. December 2025, 20:12
date modified: Monday, 1. December 2025, 21:12
---

# Lab 4 (Gísli) Operating Systems

Created time: November 27, 2025 3:16 PM
Created by: Gísli Hrafn Halldórsson
Last edited time: November 27, 2025 3:22 PM
Last edited by: Gísli Hrafn Halldórsson

# Lab 4

What I did:

(First, since I didn’t have it installed, I had to do:

```bash
sudo apt install auditd audispd-plugins
```

and then I had it installed.)

To start the `auditd` thing, I did:

```bash
sudo systemctl enable auditd
sudo systemctl start auditd
```

Then, to create the audit rule (?) called `forestwatch`, I did:

```bash
sudo auditctl -w /home/kali/Desktop/forest_97e1ca89/forest_97e1ca89 -p war -k forestwatch
```

(`/home/kali/Desktop/forest_97e1ca89/forest_97e1ca89` is where the stuff was happening.)
Then, to review that specific rule (the `forestwatch` rule I made) I did:

```bash
sudo ausearch -k forestwatch -i
```

And this command will show some more stuffff….:

```bash
sudo aureport -f
```
