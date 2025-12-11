---
aliases: []
date created: Thursday, 27. November 2025, 09:11
date modified: Thursday, 11. December 2025, 18:12
---

# 2025-11-27 Operational Systems (Kim)

# Operating System Basics - Enhanced Study Guide

## What is an [OS](<../Terminology/Systems & Plaforms/Operating System.md>)?

### The Operating System (Kernel)

- *Event-driven* program that manages the hardware state.
- Acts as a bridge between applications and hardware.
- **The Kernel:**
    - The core component of the [OS](<../Terminology/Systems & Plaforms/Operating System.md>).
    - Runs in *Privileged Mode* (Kernel Mode).
    - Has direct access to hardware instructions and memory.
- **User Space:**
    - Where your applications run.
    - Runs in *Restricted Mode* (User Mode).

### Visualizing Kernel Mode vs User Mode

Think of a building with two floors:

```
┌─────────────────────────────────────┐
│   KERNEL MODE (Ring 0) - BASEMENT   │
│   ═══════════════════════════════   │
│   • Can touch hardware directly     │
│   • Full access to ALL memory       │
│   • Can do ANYTHING                 │
│   • OS kernel lives here            │
│   • Device drivers live here        │
└─────────────────────────────────────┘
         ↕ System Call (elevator)
┌─────────────────────────────────────┐
│  USER MODE (Ring 3) - GROUND FLOOR  │
│  ───────────────────────────────────│
│  • Your apps run here (Chrome,      │
│    calculator, games)                │
│  • Restricted - can't touch         │
│    hardware directly                 │
│  • Must ask kernel for help via     │
│    system calls                      │
└─────────────────────────────────────┘
```

**Example flow when you save a file:**
1. You click “Save” in a text editor (User Mode)
2. App makes a system call: “Hey kernel, please write this to disk”
3. CPU switches to Kernel Mode
4. Kernel talks to the hard drive hardware
5. Kernel writes the data
6. CPU switches back to User Mode
7. Your app gets confirmation

---

## Abstraction

**Problem:** Raw hardware interfaces (registers, disk controllers) are complex and inconsistent.

> Solution: System Calls
>
> - The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) wraps hardware instructions in clean software APIs.
> - API is consistent across platforms, independent of the actual hardware.
> - When you call `printf()` or `fopen()`, you trigger a System Call.
> - The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) switches to Kernel Mode, performs the hardware task, and returns the result.

---

## Arbitration / Resource Management

**Problem:** Resources (CPU cycles, RAM, I/O) are finite; multiple programs want them simultaneously.

> 💡 What’s I/O?
I/O = Input/Output. Any interaction with devices outside the CPU:
- Reading a file from disk (Input)
- Printing to screen (Output)
- Getting keyboard input (Input)
- Sending data over network (Output)
>

> Solution: Multiplexing
>
> - **Time Multiplexing:** Scheduling different processes on the CPU over time.
> - **Space Multiplexing:** Dividing RAM and Disk space among processes and users.
> - **Isolation:** Ensuring a bug in Process A does not crash or starve Process B.

---

# Key Functionalities

## Process Management (Scheduling)

- **Program vs. Process:**
    - “*Program*”: Static instructions on disk (like a recipe)
    - “*Process*”: A program in execution (like actually cooking - loaded into RAM with a specific program counter, stack pointer, and registers)
- **Context Switching:**
    - The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) halts the current process.
    - Saves the CPU register state to a Process Control Block (PCB) in RAM.
    - Loads the saved state of the next process.
- **Result:** The illusion of parallelism on a single core.

---

## Memory Management (Virtualization)

- The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) provides the abstraction of Virtual Memory.
- **Address Spaces**: Every process believes it has access to a contiguous map of memory (e.g., 0x0000 to 0xFFFF).
- **Translation**: The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) + Hardware (MMU) map virtual addresses to physical RAM addresses.
    - Basically, what process_1 calls “memory 0x0001”, it might be mapped to like 0x0251 or something in actual memory, and what process_1 sees as “memory 0x0002” might actually be mapped to 0x0571 etc.
    - Basically, they just get like block 1, block 2, block 3 etc. which are mapped and spread out across the whole memory.
- **Protection**:
    - Process A cannot access Process B’s physical memory pages (or segments).
    - A user process cannot access kernel memory.
    - “*Segfault*” (*segmentation fault*): Occurs when a process tries to access an address that *has no mapping to a physical address*.

---

## I/O and Interrupt Management

*Architecture context*: I/O can be millions of times slower than a CPU cycle. We cannot use busy-waiting.

1. **Request**🫴: User program requests I/O (System Call).
2. **Sleep**😴: [OS](<../Terminology/Systems & Plaforms/Operating System.md>) puts the process in a “Waiting” state and yields the CPU to another process.
3. **Interrupt**🫸: When hardware is ready, it sends an electrical signal (Interrupt) to the CPU.
4. **ISR (Interrupt Service Routine)** 🚫: CPU jumps to the OS’s Interrupt Service Routine (essentially a function in the kernel).
5. **Wake**😱: [OS](<../Terminology/Systems & Plaforms/Operating System.md>) moves the original process back to the “Ready” queue.

---

## File Systems📂 / Storage Abstraction

- **Physical View**: A hard drive is an array of millions of generic blocks (sectors).
- **Logical View**: The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) creates the concept of Files, Directories, and Paths.
- **Responsibility**:
    - Mapping filenames to physical block addresses.
    - Managing metadata (permissions, timestamps).
    - Ensuring consistency (journaling) in case of power loss.

---

## Protection🛡️ (Ring 0 vs Ring 3)

Hardware architectures (like x86) support privilege levels.
In practice, only these 2 rings are used:

**Ring 0 (Kernel Mode)**
- Full access to all hardware instructions.
- Can manipulate memory maps and disable interrupts.

**Ring 3 (User Mode)**
- Restricted subset of instructions.
- Cannot directly access hardware.

**Traps**: If user code attempts a privileged instruction, the CPU hardware “traps” the attempt and hands control to the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) to handle the violation (usually by killing the process).

---

# Common Operating Systems

## Unix / Linux

**Origins**: Developed at AT&T Bell Labs (late 60s).

> 💡 What are Unix-like systems?
Operating systems that follow Unix design principles - they share similar commands, file structure, and philosophy. Examples: Linux, macOS, BSD, Solaris.
>

> The Unix Philosophy
“Everything is a file.”
>
> - Hardware, sockets, and data are accessed via **file descriptors**.
> - Focus on small, modular tools piped together.

**Linux** 🐧:
- Technically just the ***Kernel*** (Linus Torvalds, 1991).
- He used to work with MS-DOS (Microsoft), but he didn’t like that it wasn’t open-source.
- **Distro (short for “distribution”)**: Kernel + GNU Tools + Package Manager + Desktop.
- Architecture: Monolithic Kernel (drivers in kernel space).

**macOS** 🍎:
- Based on the **Darwin** kernel (Hybrid XNU kernel: Mach Unix + BSD Unix).
- **Darwin** is the core (kernel) that macOS is built on
- It is POSIX compliant (i.e. compatible with standard Unix APIs).

---

## Windows 🪟 (compared to Unix)

Slightly different to Linux.

- **Architecture: Hybrid Kernel**
    - Performance critical parts (filesystem, networking) run in Kernel Mode.
    - Other subsystems run in User Mode (has a Microkernel-like influence).
        - Everything we really need is run in kernel mode, and the rest is in user mode.

> 💡 “Windows uses Objects instead of files”
- Unix philosophy: “Everything is a file” - even your keyboard and printer are accessed like files (e.g., /dev/mouse)
- Windows approach: Things are “Objects” with properties and methods
- Example: In Windows, you’d use a Mouse Object with properties like .Position and methods like .Click()
- Resources are treated as abstract Objects managed via Handles (references)
>
- **Configuration: The Registry**
    - *Unix*: Uses text files (e.g., `/etc/config`). Most configuration is done via plain text files.
        - Pros: Simple, easy to back up/restore.
        - Cons: Slower access, scattered management.
    - *Windows*: Uses a centralized hierarchical database (The Registry). So all configuration settings are stored in one place.
        - Pros: Faster access, centralized management.
        - Cons: More complex, harder to back up/restore.
- **Resource Model:**
    - *Unix*: Everything is a file (including devices, sockets).
    - *Windows*: Uses Objects (files, devices, processes) managed by the Object Manager.
        - Side note: Windows since XP is based on the *Windows NT* architecture which is what we mostly mean these days, unlike Windows 95, 98, ME which were based on MS-DOS.

---

## Android 🤖📱

Often misunderstood as “Just Linux.” It uses the Linux Kernel, but the user-space is unique.
It is ***the*** most deployed [OS](<../Terminology/Systems & Plaforms/Operating System.md>) in the world (billions of devices). Because unlike iOS, Android is open-source and used by many manufacturers, not just for phones but also tablets, TVs, cars, etc.

> The Android Stack
>
> 1. **Top**: Android Runtime (ART). Apps compile to Bytecode (DEX), not native machine code. So each app runs in its own instance of the ART VM (like Java).
> 2. **Middle**: Native Libraries & Hardware Abstraction Layer (HAL). So things like OpenGL, SQLite, Media codecs, etc.
> 3. **Bottom**: Linux Kernel (Memory, Scheduling, Drivers). So all the low-level stuff is handled by the Linux kernel.

**Key Mechanism: Binder IPC**
- Apps are strictly sandboxed (security).
- They communicate via Binder (Inter-Process Communication) to talk to the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) or other apps. Which means that apps can’t directly access each other’s memory or data.

---

## Embedded and RTOS (Real-Time Operating Systems)

There are many other kinds of operating systems designed for specific use-cases, especially in embedded systems (IoT (Internet of Things) devices, automotive systems, industrial machines).

*General Purpose [OS](<../Terminology/Systems & Plaforms/Operating System.md>) (Windows/Linux) Goal*: Throughput.
*RTOS Goal*: Determinism / Consistency.

- **RTOS (Real-Time Operating System):**
    - Examples: FreeRTOS, VxWorks, QNX.
    - **Hard Real-Time**: A delayed calculation is a system failure (e.g., car brakes, pacemaker).
    - **Features**: Tiny kernels, fast interrupt handling, often no virtual memory (to avoid paging latency).
- **Embedded Linux:**
    - Standard Linux stripped down (e.g., Raspberry Pi).
    - Used when complex networking or GUIs are needed, but strict microsecond-timing isn’t required.

---

## What is POSIX?

**POSIX** = **P**ortable **O**perating **S**ystem **I**nterface (the **X** is for Unix).

> The Concept: An API Contract
POSIX is an IEEE (Institute of Electrical and Electronics Engineers) standard that defines an interface between User Space applications and the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) Kernel.
>
> - It does not tell the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) how to implement a feature.
> - It tells the [OS](<../Terminology/Systems & Plaforms/Operating System.md>): “If you want to be Unix-compatible, you must support these function names and behaviors.”

**The Motivation (The “Unix Wars”)**
- In the 80s, Unix fragmented (BSD, System V, etc.). Code written for one Linux machine wouldn’t compile on another.
- Goal: Source code portability. A C program written using POSIX standards will compile on Linux, macOS, and BSD without changes (mostly).

### Components and Adoption

**What does POSIX actually define?**

- **System Call APIs (C Headers):**
    - File I/O: `open()`, `read()`, `write()` (vs Windows `CreateFile`).
    - Process Control: `fork()`, `exec()`, `wait()`.
    - Threading: `pthreads` (`<pthread.h>`).
- **Shell & Utilities:**
    - Standardizes behavior of CLI tools (`ls`, `grep`, `awk`) so scripts are portable.

**Who is Compliant?**

| OS | Status |
| --- | --- |
| macOS | **Certified**. Actually fully POSIX compliant. |
| Linux | **De Facto**. Mostly compliant, but people rarely pay for the certification. |
| Windows | **No**. Uses Win32 API. Needs WSL (Subsystem for Linux). |

So if they’re POSIX compliant, that means they support the same system calls and APIs, making it easier for developers to write cross-platform applications.

---

# Operating Systems and Security

## The OS and the Trusted Computing Base

> Trusted Computing Base (TCB)
“… is the totality of protection mechanisms within a computer system – including hardware, firmware, and software – that is responsible for enforcing a security policy. TCB is all components that must work correctly for the system to be secure. If any part is broken, the security of the entire system is broken.”
>

**The Reference Monitor**
The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) acts as a gatekeeper between Subjects (Users, Processes) and Objects (Files, Hardware).
Every system call (e.g., `open()`) is intercepted to check:

1. **Authentication**: *Who* are you?
2. **Authorization**: Are you *allowed to do this*?

---

## Authentication: “Who are you?”

**Identification vs. Verification**
- *Identification*: Claiming an identity (Username).
- *Verification*: *Proving* it (Password, Biometric, Key).

### Secure Storage (Hashing)

> 💡 What’s a hash?
A one-way mathematical function that turns any input into a fixed-length string. Like a fingerprint for data:
- “password123” → ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
- Even a tiny change creates a completely different hash
- One-way: You can’t reverse it to get the original password back
>
- **Rule #1**: The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) never stores passwords in plain text.
- **Hashing**: The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) stores a cryptographic hash (e.g., SHA-256) of the password.
    - On login: `InputHash = Hash(UserInput)`.
    - If `InputHash == StoredHash`, access is granted.
- **Salting** 🧂:
    - To prevent “Rainbow Table” attacks (pre-computed hash databases), the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) adds a random string (salt) before hashing.
        - This ensures that even if two users have the same password, their stored hashes differ.
    - `StoredValue = Hash(Password + Salt)`.

> 💡 What’s a Rainbow Table Attack?
A pre-computed database of hashes:
- Attacker creates a huge table: “password” → hash1, “123456” → hash2, etc.
- If they steal your password database, they just look up the hash in their table
- Defense: Add salt (random data) before hashing, so each user’s hash is unique even with same password
>

---

## Access Control: “What can you do?”

Once authenticated, the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) uses a **User ID (UID)** to enforce permissions.

- **DAC (Discretionary Access Control):**
    - The **Owner** of the file decides permissions.
    - Example: Linux `chmod`. You can make your file readable by everyone.
    - Risk: Malware running as “You” can change your file permissions.
- **MAC (Mandatory Access Control):**
    - The **System Policy** decides permissions. Users cannot override this.
    - Used in High Security (SELinux) and Mobile (iOS/Android).
    - Example: A web-server process cannot read the `/home` directory, even if run by root.

---

## The Principle of Least Privilege

> Golden Rule of [OS](<../Terminology/Systems & Plaforms/Operating System.md>) Architecture
A process should only have the absolute minimum privileges necessary to do its job.
>

**Why?**
- It limits the “Blast Radius.”
- If a calculator app is hacked, it shouldn’t have permission to read the network driver or kernel memory.
- This is enforced via CPU modes (User Mode vs. Kernel Mode).
- (Also: modern OSes use techniques like **Sandboxing** and **Containers** to isolate applications further.)

---

## System Logs

The “Flight Recorder” of the [OS](<../Terminology/Systems & Plaforms/Operating System.md>).

> 💡 What is System Auditing?
Recording detailed logs of what happens on the system at the kernel level - who did what, when, and whether it succeeded or failed. Goes beyond regular logs to track specific system calls.
>
- **What**: High-level textual records of events.
- **Content**: (Failed) logins, sudo usage, Service crashes.
- **Locations (where they live)**:
    - Linux: `/var/log/syslog`, `/var/log/auth.log`
        - `var/log/syslog`: General system messages, including system errors, informational messages, and warnings.
        - `var/log/auth.log`: Authentication-related events, such as login attempts and sudo usage.
    - macOS: `/var/log/system.log`
    - Windows: Event Viewer
- **Forensics**: The first place admins look after a breach. Beyond real-time monitoring, logs provide a historical record to trace back an attacker’s actions.
    - But beware: attackers may try to delete or alter logs to cover their tracks. Hence, secure log management practices are essential.

---

## File Integrity & System Auditing

Going deeper than standard logs:

> 💡 What’s a checksum?
A hash used to verify file integrity. Like a seal on a package:
- You download a file and calculate its checksum
- Compare it to the official checksum
- If they match, the file wasn’t tampered with
>
- **System Auditing (Kernel Level):**
    - Hooks into the kernel to track System Calls.
    - *Example*: Not just “User logged in”, but “Process 402 attempted `open()` on `/etc/shadow` and was denied.”
    - Required for strict compliance to various standards (PCI-DSS, HIPAA).
- **File Integrity Monitoring (FIM):**
    - *Threat*: Attackers replacing system binaries (like `/bin/login`) with Trojan horses.
    - *Defense*: Calculate checksums (hashes) of critical files.
    - If the hash of `/bin/login` changes, the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) triggers an alarm immediately.

We’ll be doing this in today’s lab!

---

## Enable System Auditing

### Enable System Auditing: Windows🪟

System Auditing is a granular policy managed via the Local Security Policy tool.

- **GUI Method:**
    1. Run `secpol.msc` as Administrator.
    2. Navigate to: Local Policies → Audit Policy.
    3. Double-click a category (e.g., “Audit logon events” or “Audit object access”).
    4. Check Success (log when it works) and/or Failure (log when it is denied).
- **Command Line Method (PowerShell/CMD):** Using the `auditpol` tool.

> Example Command
>
>
> ```
> >auditpol /set /subcategory:"Logon" /success:enable /failure:enable
> ```
>

Logs are viewed in the **Event Viewer** or using `Get-EventLog` in PowerShell.

---

### Enable System Auditing: Linux🐧

Linux uses the Linux Audit Framework. It listens to the kernel for specific system calls and file changes.

**Installation:**
- Install: `sudo apt install auditd` (Debian/Ubuntu) or `yum install audit` (RHEL/CentOS).
- Start: `sudo systemctl start auditd`.
- Defining Rules: You use `auditctl` to add rules to the kernel in real-time.

> Example: Watch for changes to passwords
>
>
> ```bash
> $ sudo auditctl -w /etc/shadow -p wa -k password-change
> ```
>
> - `w`: Watch this file path.
> - `p wa`: Trigger on write or attribute change.
> - `k`: Tag log entries with a search key.

Logs are stored in `/var/log/audit/audit.log`, queried via `ausearch` or `aureport`.

---

### Enable System Auditing: macOS🍎

macOS uses the Basic Security Module (BSM), an advanced auditing system derived from TrustedBSD.

- **Configuration:**
    - Config file is located at `/etc/security/audit_control`.
    - Controls “flags” for events (e.g., `lo` for login, `ad` for administrative actions).
- **Activation:** The audit daemon (`auditd`) usually runs by default. To reload configuration changes:
`bash $ sudo audit -s`
- **Binary Logs:** Unlike Linux, macOS audit logs are binary (to prevent tampering). You cannot read them with `cat`.

> Viewing Logs
Use the praudit tool to parse the binary log to text:
>
>
> ```bash
> $ sudo praudit /var/audit/current
> ```
>

---

# Common Vulnerabilities and Exploits

## Memory Safety: Buffer Overflows

Stems from the C/C++ programming languages allowing direct memory manipulation without bounds checking. So if you allocate a buffer of size 10, and write 20 bytes into it, the extra 10 bytes will overflow into adjacent memory.

### Visual Example: Stack Smashing

Imagine a row of boxes on a shelf:

```
Before overflow:
┌───────┬───────┬───────┬──────────────┐
│ Box 1 │ Box 2 │ Box 3 │ Return Addr  │  ← Stack
│"Hello"│  ---  │  ---  │ → 0x1234     │
└───────┴───────┴───────┴──────────────┘

You're supposed to fill Box 1 with 5 letters.

After overflow attack:
┌───────┬───────┬───────┬──────────────┐
│ Box 1 │ Box 2 │ Box 3 │ Return Addr  │
│"Hello"│"AAAAA"│"AAAAA"│ → 0xBADC0DE  │ ← Overwritten!
└───────┴───────┴───────┴──────────────┘

Attacker puts in 20 letters instead of 5!
The overflow spills into adjacent memory,
overwriting the "return address" that tells
the CPU where to go next.
```

**Real code example:**

```c
char buffer[10];gets(buffer);  // Dangerous! No length check// If user types 50 characters, it overflows
```

- **The Flaw:**
    - A program allocates a fixed buffer.
    - The [OS](<../Terminology/Systems & Plaforms/Operating System.md>)/Program fails to check input size, allowing writes past the buffer end.
- **The Exploit (Stack Smashing):**
    - Attacker overflows the stack to overwrite the **Return Address**.
    - CPU jumps to malicious code (shellcode) instead of returning to the main function.
- **Mitigation:**
    - **ASLR (Address Space Layout Randomization)**: Randomizes memory layout so addresses are hard to guess.
    - **DEP/NX (Data Execution Prevention / No Execute)**: Marks stack memory as “Non-Executable.”

---

## Race Conditions

> Example: TOCTOU (Time-of-Check to Time-of-Use)
Because OSes multitask, a gap exists between checking the file permissions and using it.
>

### Visual Example: The Bait-and-Switch

```
Timeline:

1. [10:00:00] OS checks: "Can user write to temp.txt?"
              Answer: YES ✓

2. [10:00:01] ← ATTACKER STRIKES HERE!
              Quickly deletes temp.txt
              Creates symlink: temp.txt → /etc/shadow
              (The password file!)

3. [10:00:02] OS proceeds: "OK, writing to temp.txt"
              But temp.txt now points to /etc/shadow!
              OS overwrites the password file!
```

**The technical steps:**
1. **Check**: [OS](<../Terminology/Systems & Plaforms/Operating System.md>) confirms User A can write to `temp.txt`.
2. **The Gap (Context Switch)**: Attacker quickly swaps `temp.txt` with a symbolic link to `/etc/shadow` (password file).
3. **Use**: [OS](<../Terminology/Systems & Plaforms/Operating System.md>) resumes the process and writes to the target, overwriting the password file because the check already passed.

A research task we have today is how to mitigate and prevent these.

---

## Command Injection 💉

Occurs when the Shell is tricked into executing unintended commands.

### Visual Example: Hidden Commands

```
Script expects: rm file.txt
Attacker types:  file.txt; rm -rf /

What the shell sees:
  rm file.txt    ← legitimate command
  ;              ← command separator
  rm -rf /       ← DELETE EVERYTHING!

Both commands execute!
```

**Real web form example:**

```
Website: "Enter filename to delete:"
User types: invoice.pdf; cat /etc/passwd
Server runs: delete invoice.pdf; cat /etc/passwd
              ↑ expected        ↑ attacker's secret command
```

- **The Flaw:** Passing unsanitized user input directly to a system command.
- **The Exploit:**
    - Script expects a filename: `rm $filename`
    - Attacker inputs: `file.txt; rm -rf /`
    - The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) interprets `;` as a command separator and executes both.

---

## Privilege Escalation

The attacker’s goal: Move from Ring 3 (User) to Ring 0 (Kernel).

### Visual Example: SUID Exploitation

```
Normal scenario:
┌──────────────────────┐
│  User: Master        │  ← You (no special powers)
│  Runs: calculator    │
│  Privileges: Limited │
└──────────────────────┘

SUID scenario:
┌──────────────────────┐
│  User: Master           │  ← Still you
│  Runs: /bin/passwd   │  ← Has SUID bit set
│  Privileges: ROOT!   │  ← Temporarily becomes superuser
└──────────────────────┘

If /bin/passwd has a bug, attacker can:
1. Trigger the bug (e.g., buffer overflow)
2. Inject malicious code
3. Code runs as ROOT (because of SUID)
4. Attacker gets a root shell!
```

> 💡 What is root?
The superuser account in Unix/Linux. Has unlimited power - can do anything, access everything. Like having the master key to every room in a building.
>
- **Vertical Escalation:**
    - Exploiting bugs in “SetUID” programs (programs that run as root, like `sudo` or `passwd`).
- **Kernel Exploits:**
    - Crashing or manipulating the Kernel itself.
    - **Weak Link**: Third-party **Drivers**. They run with full privileges but often have less rigorous code quality than the core kernel.

---

## Rootkits and Zero-Days

### Rootkits

Malware that modifies the system to hide its own existence by intercepting system calls.

### Visual Example: The Dishonest Accountant

```
What really exists:        What you see:
┌──────────────┐          ┌──────────────┐
│ file1.txt    │          │ file1.txt    │
│ file2.txt    │          │ file2.txt    │
│ MALWARE.exe  │   →      │              │ ← Hidden!
│ myprocess    │          │ myprocess    │
│ hacker_shell │          │              │ ← Hidden!
└──────────────┘          └──────────────┘

Rootkit intercepts system calls:
  You type: ls
  Normal ls would show everything
  Rootkit filters output, hides malware
```

**How it works:**

```
You: "Show me all files!" (ls command)
  ↓
Rootkit intercepts the system call
  ↓
Rootkit: "Let me filter this list first..."
  ↓
Rootkit shows you fake output (malware hidden)
```

- Essentially, it’s malware that’s designed to be stealthy and avoid detection by traditional security measures. It gets the operating system to lie to the user or security software about what’s really happening on the system.
- Example: When you run `ls` or `ps`, the rootkit filters the output of the underlying system calls to hide the hacker’s files and processes. The [OS](<../Terminology/Systems & Plaforms/Operating System.md>) lies to the user.
- **Defense**: Use trusted boot mechanisms and integrity checks to detect unauthorized changes to system binaries.

---

### Zero-Day Vulnerabilities

- A flaw known to the attacker but unknown to the vendor (0 days to fix).

> 💡 What is Speculative Execution?
CPU optimization where the processor guesses which code will run next and starts executing it early:
- Like a chef preparing the most common dishes before orders come in
- Meltdown/Spectre exploited this by making the CPU speculatively execute code it shouldn’t, then reading the CPU cache to see what it tried to access
>
- **Defense**: “Defense in Depth”. You cannot patch it, so you must rely on firewalls, strict access control, procedures, etc. to contain it.

---

# Commands for Sysadmins

| Action | Linux Command | PowerShell / Windows |
| --- | --- | --- |
| Execute asroot / Admin | `sudo [cmd]` | `Start-Process -Verb RunAs`(Or open Terminal asAdmin) |
| Change FilePermissions | `chmod 755 file` | `icacls file /grant...`(Or `Set-Acl`) |
| View Permissions | `ls -l` | `icacls [file]`(Or `Get-Acl`) |
| Change Ownership | `chown user file` | `takeown /f file`(Or `Set-Acl`) |
| Change Password | `passwd` | `Set-LocalUser` |

*(Note from teacher: “I’m not a particularly well-versed Windows user, so take the Windows commands with a grain of salt.”)*

---

![image.png](Operational Systems 2025-11-27/image.png)

## File Permissions: Linux vs. Windows

### Linux (POSIX Model)

- **Simple Structure:** Permissions apply to three rigid categories:
    1. User (Owner)
    2. Group
    3. Others (World)
- **The Bits:** Read (`r`), Write (`w`), Execute (`x`).

> 💡 What are rwx bits?
File permissions in Unix:
- r = read (can view contents)
- w = write (can modify)
- x = execute (can run as program)
>
>
> Example: `rwxr-xr--`
> - Owner: read, write, execute
> - Group: read, execute
> - Others: read only
>  
- **Representation:** Often represented symbolically (`rwxr-xr-x`) or with a 3-digit octal (base-8) number (`755`).
    - `rwxr-xr-x` = `7` (`rwx`) `5` (`r-x`) `5` (`r-x`)
- **Example:** `chmod 755 file.txt` means:
    - Owner: Read, Write, Execute
    - Group: Read, Execute
    - Others: Read, Execute

---

### Windows (ACL Model)

- **Complex Structure:** Uses Access Control Lists (ACLs).
- **Granular:** You can assign distinct permissions to 50 different users individually.
- **Inheritance:** Files heavily inherit rules from parent folders.
- **The Rights:** Full Control, Modify, Read & Execute, List, Read, Write.

*Everything is a file, the directory is a file.* (This applies to Linux/Unix systems. With Windows, it’s a bit different as it uses objects and handles, but the concept of files and directories still exists.)

---

## Advanced Permissions: SUID & SGID

> 💡 What is SUID?
<abbr title="Set User ID">SUID</abbr> = Set User ID. Special permission that makes a program run with the file owner’s privileges, not yours.
>

**Concept:** <abbr title="Set User ID">SUID</abbr> (Set User ID) allows a user to execute a file with the permissions of the file owner, rather than their own.

**Use Case: `passwd`**
- **Problem**: Standard users cannot write to the password database (`/etc/shadow`).
- **Solution**: The `passwd` binary is owned by root and has <abbr title="Set User ID">SUID</abbr> set.
- **Result**: When run, the process promotes to root temporarily to save changes.

### Danger: Why SUID is a Security Risk

```bash
$ find / -perm -4000  # Find all SUID programs/usr/bin/passwd       # Expected/usr/bin/sudo         # Expected/tmp/mysterious_tool  # ← Attacker planted this!
```

- <abbr title="Set User ID">SUID</abbr> is a major vector for **Privilege Escalation**.
- If an <abbr title="Set User ID">SUID</abbr> root binary has a bug (e.g., buffer overflow), an attacker can exploit it to gain a Root Shell.
- Attackers scan for these immediately: `find / -perm -4000`

**Command:** `chmod u+s file`**Indicator:** `-rwsr-xr-x 1 root root 64152 maí 30 2024 /usr/bin/passwd`

---

## Process & Service Management

| Action | Linux Command | PowerShell / Windows |
| --- | --- | --- |
| Start/StopServices | `systemctl start [svc]` | `Start-Service [svc]`(`Get-`, `Stop-`, `Set-`) |
| List Pro-cesses(Snapshot) | `ps aux` | `Get-Process` |
| Real-time | `top` / `htop` | `Get-Process \| Sort CPU`(Or GUI `taskmgr`) |
| Kill Process | `kill -9 [PID]` | `Stop-Process -Id [PID]` |

---

## Disk & File System Management

| Action | Linux Command | PowerShell / Windows |
| --- | --- | --- |
| Free Space | `df -h`(Disk Free) | `Get-Volume`(or `Get-PSDrive`) |
| Disk Usage | `du -sh [folder]` | `gci -Recurse \| Measure -Property Length -Sum` |
| Search | `find /path -name x` | `Get-ChildItem -Recurse -Filter "x"` |
| Archive | `tar -czvf x.tar.gz`(or `zip`, `rar`, etc) | `Compress-Archive`(Win10+ has `tar.exe`) |

---

## Logs

| Action | Linux Command | PowerShell / Windows |
| --- | --- | --- |
| Followchanges live | `tail -f log.txt` | `Get-Content log.txt -Wait`(Alias: `cat -Wait`) |
| Search | `grep "Error"` | `Select-String "Error"`(Alias: `sls`) |
| … or both | `tail -f log.txt \| grep "Error"` | `Get-Content log.txt -Wait \| Select-String "Error"` |

---

## Scheduling & Maintenance

| Action | Linux Command | PowerShell / Windows |
| --- | --- | --- |
| ScheduleTasks | `crontab -e`(opens the cron table in aneditor) | `Register-ScheduledTask` |
| Install Updates | `apt update && apt upgrade`(Depending on Distro) | `winget upgrade --all`(Only for apps, not the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) itself!) |

---

# Up Next…

---

[Cybersecurity_Research_Advanced_Topics](<../Terminology/Cybersecurity_Research_Advanced_Topics.md>)

---

---
