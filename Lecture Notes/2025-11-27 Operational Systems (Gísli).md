---
aliases: []
date modified: Thursday, 11. December 2025, 09:12
date created: Monday, 1. December 2025, 20:12
---

# Operating System Basics

# What is an [OS](Operating System.md)?

## The Operating System

- Event-driven program that manages the hardware state.
- Acts as a bridge between applications and hardware.
- The [Kernel](../Terminology/Systems & Plaforms/Kernel.md):
    - The core component of the [OS](Operating System.md).
    - Runs in Privileged Mode ([Kernel](../Terminology/Systems & Plaforms/Kernel.md) Mode).
    - Has direct access to hardware instructions and memory.
- User Space:
    - Where your applications run.
    - Runs in Restricted Mode (User Mode). :)

## Abstraction

Problem: Raw hardware interfaces (registers, disk controllers) are complex and inconsistent.

> [!check] Solution: System Calls
>
> - The [OS](Operating System.md) wraps hardware instructions in clean software APIs.
> - API is consistent across platforms, independent of the actual hardware.
> - When you call `printf()` or `fopen()`, you trigger a System Call.
> - The [OS](Operating System.md) switches to [Kernel](../Terminology/Systems & Plaforms/Kernel.md) Mode, performs the hardware task, and returns the result.

## Arbitration / Resource Management

Problem: Resources (CPU cycles, RAM, I/O) are finite; multiple programs

want them simultaneously.

> [!check] Solution: Multiplexing
>
> - Time Multiplexing: Scheduling different processes on the CPU over time.
> - Space Multiplexing: dividing RAM and Disk space among processes and users.
> - Isolation: Ensuring a bug in Process A does not crash or starve Process B.

# Key Functionalities

## Process Management (Scheduling)

- Program vs. Process:
    - “*Program*”: Static instructions on disk.
    - “*Process*”: A program in execution (loaded into RAM with a specific program counter, stack pointer, and registers).
- Context Switching:
    - The [OS](Operating System.md) halts the current process.
    - Saves the CPU register state to a Process Control Block (PCB) in RAM.
    - Loads the saved state of the next process.
- Result: The illusion of parallelism on a single core.

## Memory Management ([Virtualization](<../Terminology/Virtualization/Virtualization.md>))

- The [OS](Operating System.md) provides the abstraction of Virtual Memory.
- **Address Spaces**: Every process believes it has access to a contiguous map of memory (e.g., 0x0000 to 0xFFFF).
- **Translation**: The [OS](Operating System.md) + Hardware (MMU) map virtual addresses to physical RAM addresses.
    - Basically, what process_1 calls “memory 0x0001”, it might be mapped to like 0x0251 or something in actual memory, and what process_1 sees as “memory 0x0002” might actually be mapped to 0x0571 etc.
    - Basically, they just get like block 1, block 2, block 3 etc. which are mapped and spread out across the whole memory.
- **Protection**:
    - Process A cannot access Process B’s physical memory pages (or segments).
    - A user process cannot access [Kernel](../Terminology/Systems & Plaforms/Kernel.md) memory.
    - “*Segfault*” (*segmentation fault*): Occurs when a process tries to access an address that *has no mapping to a physical address*.

## I/O and Interrupt Management

*Architecture context*: I/O can be millions of times slower than a CPU cycle. We cannot use busy-waiting.

1. **Request**🫴: User program requests I/O (System Call).
2. **Sleep**😴: [OS](Operating System.md) puts the process in a “Waiting” state and yields the CPU to another process.
3. **Interrupt**🫸: When hardware is ready, it sends an electrical signal (Interrupt) to the CPU.
4. **ISR (Interrupt Service Routine)** 🚫: CPU jumps to the OS’s Interrupt Service Routine (essentially a function in the [Kernel](../Terminology/Systems & Plaforms/Kernel.md)).
5. **Wake**😱: [OS](Operating System.md) moves the original process back to the “Ready” queue.

## File Systems📂 / Storage Abstraction

- **[Physical View](../Terminology/Physical View)**: A hard drive is an array of millions of generic blocks (sectors).
- **Logical View**: The [OS](Operating System.md) creates the concept of Files, Directories, and Paths.
- **Responsibility**:
    - Mapping filenames to physical block addresses.
    - Managing metadata (permissions, timestamps).
    - ensuring consistency (journaling) in case of power loss.

## Protection🛡️ (Ring 0 vs Ring 3)

Hardware architectures (like x86) support privilege levels.

In practice, only these 2 rings are used:

**Ring 0 ([Kernel](../Terminology/Systems & Plaforms/Kernel.md) Mode)**

- Full access to all hardware instructions.
- Can manipulate memory maps and disable interrupts.

**Ring 3 (User Mode)**

- Restricted subset of instructions.
- Cannot directly access hardware.

**Traps**: If user code attempts a privileged instruction, the CPU hardware “traps” the attempt and hands control to the [OS](Operating System.md) to handle the violation (usually by killing the process).

# Common Operating Systems

## Unix / Linux

**Origins**: Developed at AT&T Bell Labs (late 60s).

> The Unix Philosophy
“Everything is a file.”
>
> - Hardware, sockets, and data are accessed via **file descriptors**.
> - Focus on small, modular tools piped together.

**Linux** 🐧:

- Technically just the ***[Kernel](../Terminology/Systems & Plaforms/Kernel.md)*** (Linus Torvalds, 1991).
    - He used to work with MS-DOS (Microsoft), but he didn’t like that it wasn’t open-source.
- **Distro (short for “distribution”)**: [Kernel](../Terminology/Systems & Plaforms/Kernel.md) + GNU Tools + Package Manager + Desktop.
- Architecture: Monolithic [Kernel](../Terminology/Systems & Plaforms/Kernel.md) (drivers in [Kernel](../Terminology/Systems & Plaforms/Kernel.md) space).
**macOS** 🍎:
- Based on the **Darwin** [Kernel](../Terminology/Systems & Plaforms/Kernel.md) (Hybrid XNU [Kernel](../Terminology/Systems & Plaforms/Kernel.md): Mach Unix + BSD Unix).
- It is [POSIX](../Terminology/Systems & Plaforms/POSIX) compliant (i.e. compatible with standard Unix APIs).

## Windows 🪟 (compared to Unix)

Slightly different to Linux.

- **Architecture: Hybrid Kernel**
    - Performance critical parts (filesystem, networking) run in [Kernel](../Terminology/Systems & Plaforms/Kernel.md) Mode.
    - Other subsystems run in User Mode (has a Microkernel-like influence).
        - Everything we really need is run in [Kernel](../Terminology/Systems & Plaforms/Kernel.md) mode, and the rest is in user mode.
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
        - Resources are treated as abstract Objects managed via Handles (references).
        Side note: Windows since XP is based on the *Windows NT* architecture which is what we mostly mean these days, unlike Windows 95, 98, ME which were based on MS-DOS.

## Android 🤖📱

Often misunderstood as “Just Linux.” It uses the Linux [Kernel](../Terminology/Systems & Plaforms/Kernel.md), but the user-space is unique.

It is ***the*** most deployed [OS](Operating System.md) in the world (billions of devices). Because unlike iOS, Android is open-source and used by many manufacturers, not just for phones but also tablets, TVs, cars, etc.

> The Android Stack
>
> 1. **Top**: Android Runtime (ART). Apps compile to Bytecode (DEX), not native machine code. So each app runs in its own instance of the ART VM (like Java).
> 2. **Middle**: Native Libraries & Hardware Abstraction Layer (HAL). So things like OpenGL, SQLite, Media codecs, etc.
> 3. **Bottom**: Linux [Kernel](../Terminology/Systems & Plaforms/Kernel.md) (Memory, Scheduling, Drivers). So all the low-level stuff is handled by the Linux [Kernel](../Terminology/Systems & Plaforms/Kernel.md).

**Key Mechanism: Binder IPC**

- Apps are strictly sandboxed (security).
- They communicate via Binder (Inter-Process Communication) to talk to the [OS](Operating System.md) or other apps. Which means that apps can’t directly access each other’s memory or data.

## Embedded and RTOS (Real-Time Operating Systems)

There are many other kinds of operating systems designed for specific use-cases, especially in embedded systems (IoT (Internet of Things) devices, automotive systems, industrial machines).

*General Purpose [OS](Operating System.md) (Windows/Linux) Goal*: Throughput.
*RTOS Goal*: Determinism / Consistency.

- **RTOS (Real-Time Operating System):**
    - Examples: FreeRTOS, VxWorks, QNX.
    - **Hard Real-Time**: A delayed calculation is a system failure (e.g., car brakes, pacemaker).
    - **Features**: Tiny kernels, fast interrupt handling, often no virtual memory (to avoid paging latency).
- **Embedded Linux:**
    - Standard Linux stripped down (e.g., Raspberry Pi).
    - Used when complex networking or GUIs are needed, but strict microsecond-timing isn’t required.

## What is POSIX?

**POSIX** = **P**ortable **O**perating **S**ystem **I**nterface (the **X** is for Unix).

> The Concept: An API Contract
POSIX is an IEEE (Institute of Electrical and Electronics Engineers) standard that defines an interface between User Space applications and the [OS](Operating System.md) [Kernel](../Terminology/Systems & Plaforms/Kernel.md).
>
> - It does not tell the [OS](Operating System.md) how to implement a feature.
> - It tells the [OS](Operating System.md): “If you want to be Unix-compatible, you must support these function names and behaviors.”

The Motivation (The “Unix Wars”)

- In the 80s, Unix fragmented (BSD, System V, etc.). Code written for one Linux machine wouldn’t compile on another.
- Goal: Source code portability. A C program written using POSIX standards will compile on Linux, macOS, and BSD without changes (mostly).

## Components and Adoption

What does POSIX actually define?

- System Call APIs (C Headers):
    - File I/O: `open()`, `read()`, `write()` (vs Windows `CreateFile`).
    - Process Control: `fork()`, `exec()`, `wait()`.
    - Threading: `pthreads` (`<pthread.h>`).
- Shell & Utilities:
    - Standardizes behavior of CLI tools (`ls`, `grep`, `awk`) so scripts are portable.
    Who is Compliant?

| [OS](Operating System.md)      | Status                                                                                           |
| ------- | ------------------------------------------------------------------------------------------------ |
| macOS   | **Certified**. Actually fully [POSIX](../Terminology/Systems & Plaforms/POSIX.md) compliant. |
| Linux   | **De Facto**. Mostly compliant, but people rarely pay for the certification.                     |
| Windows | **No**. Uses Win32 API. Needs WSL (Subsystem for Linux).                                         |

So if they’re POSIX compliant, that means they support the same system calls and APIs, making it easier for developers to write cross-platform applications.

# Operating Systems and Security

## The [OS](Operating System.md) and the Trusted Computing Base

> [!definition] Trusted Computing Base (TCB)
“... is the totality of protection mechanisms within a computer system – including hardware, firmware, and software – that is responsible for enforcing a security policy. TCB is all components that must work correctly for the system to be secure. If any part is broken, the security of the entire system is broken.”
>

**The Reference Monitor**
The [OS](Operating System.md) acts as a gatekeeper between Subjects (Users, Processes) and Objects (Files, Hardware).
Every system call (e.g., `open()`) is intercepted to check:
1. **Authentication**: *Who* are you?
2. **Authorization**: Are you *allowed to do this*?

## Authentication: “Who are you?”

**Identification vs. Verification**

- *Identification*: Claiming an identity (Username).
- *Verification*: *Proving* it (Password, Biometric, Key).

**Secure Storage (Hashing)**

- **Rule #1**: The [OS](Operating System.md) never stores passwords in plain text.
- **Hashing**: The [OS](Operating System.md) stores a cryptographic hash (e.g., SHA-256) of the password.
    - On login: `InputHash = Hash(UserInput)`.
    - If `InputHash == StoredHash`, access is granted.
- **Salting** 🧂:
    - To prevent “Rainbow Table” attacks (pre-computed hash databases), the [OS](Operating System.md) adds a random string (salt) before hashing.
        - This ensures that even if two users have the same password, their stored hashes differ.
    - `StoredValue = Hash(Password + Salt)`.

## [Access Control](../Terminology/Defense & Control/Access Control):”What can you do?”

Once authenticated, the [OS](Operating System.md) uses a **User ID (UID)** to enforce permissions.

- **DAC (Discretionary Access Control):**
    - The **Owner** of the file decides permissions.
    - Example: Linux `chmod`. You can make your file readable by everyone.
    - Risk: [Malware](<../Terminology/Attacks/Malware/Malware.md>) running as “You” can change your file permissions.
- **MAC (Mandatory Access Control):**
    - The **System Policy** decides permissions. Users cannot override this.
    - Used in High Security (SELinux) and Mobile (iOS/Android).
    - Example: A web-server process cannot read the `/home` directory, even if run by root.

## The Principle of Least Privilege

> Golden Rule of [OS](Operating System.md) Architecture
A process should only have the absolute minimum privileges necessary to do its job.
>

Why?

- It limits the “Blast Radius.”
- If a calculator app is hacked, it shouldn’t have permission to read the network driver or [Kernel](../Terminology/Systems & Plaforms/Kernel.md) memory.
- This is enforced via CPU modes (User Mode vs. [Kernel](../Terminology/Systems & Plaforms/Kernel.md) Mode).
- (Also: modern OSes use techniques like **Sandboxing** and **[Containers](../Terminology/Virtualization/Virtualization methods/Container)** to isolate applications further.)

## System Logs

The “Flight Recorder” of the [OS](Operating System.md).

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

## File Integrity & System Auditing

Going deeper than standard logs:

- System Auditing ([Kernel](../Terminology/Systems & Plaforms/Kernel.md) Level):
    - Hooks into the [Kernel](../Terminology/Systems & Plaforms/Kernel.md) to track System Calls.
    - *Example*: Not just “User logged in”, but “Process 402 attempted `open()` on `/etc/shadow` and was denied.”
    - Required for strict compliance to various standards (PCI-DSS, HIPAA).
- File Integrity Monitoring (FIM):
    - *Threat*: Attackers replacing system binaries (like `/bin/login`) with [Trojan horses](<../Terminology/Attacks/Malware/Trojan.md>).
    - *Defense*: Calculate checksums (hashes) of critical files.
    - If the hash of /bin/login changes, the [OS](Operating System.md) triggers an alarm immediately.

We’ll be doing this in today’s lab!

## Enable System Auditing

### Enable System Auditing: Windows🪟

System Auditing is a granular policy managed via the Local Security Policy tool.

- GUI Method:
    1. Run secpol.msc as Administrator.
    2. Navigate to: Local Policies → Audit Policy.
    3. Double-click a category (e.g.,”Audit logon events” or”Audit object access”).
    4. Check Success (log when it works) and/or Failure (log when it is denied).
- Command Line Method (PowerShell/CMD): Using the `auditpol` tool.

> Example Command
>
>
> ```
> \>auditpol /set /subcategory:“Logon” /success:enable
> /failure:enable
> ```
>

Logs are viewed in the **Event Viewer** or using `Get-EventLog` in PowerShell.

### Enable System Auditing: Linux🐧

Linux uses the Linux Audit Framework. It listens to the [Kernel](../Terminology/Systems & Plaforms/Kernel.md) for specific system calls and file changes.

**Installation:**

- Install: `sudo apt install auditd` (Debian/Ubuntu) or `yum install audit` (RHEL/CentOS).
- Start: `sudo systemctl start auditd`.
- Defining Rules: You use `auditctl` to add rules to the [Kernel](../Terminology/Systems & Plaforms/Kernel.md) in real-time.

> [!example] Example: Watch for changes to passwords
>```bash
> $ sudo auditctl -w /etc/shadow -p wa -k password-change
> ```
>
>
> - `-w`: Watch this file path.
> - `-p wa`: Trigger on write or attribute change.
> - `-k`: Tag log entries with a search key.
>

Logs are stored in `/var/log/audit/audit.log`, queried via `ausearch` or `aureport`.

### Enable System Auditing: macOS🍎

macOS uses the Basic Security Module (BSM), an advanced auditing system derived from TrustedBSD.

- Configuration:
    - Config file is located at `/etc/security/audit control`.
    - Controls”flags” for events (e.g., lo for login, ad for administrative actions).
- Activation: The audit daemon (`auditd`) usually runs by default. To reload configuration changes:
`$ sudo audit -s`
- Binary Logs: Unlike Linux, macOS audit logs are binary (to prevent tampering). You cannot read them with cat.

> [!info] Viewing Logs
Use the praudit tool to parse the binary log to text:
>
>
> ```bash
> $ sudo praudit /var/audit/current
> ```
>

# Common Vulnerabilities and Exploits

## Memory Safety: [Buffer Overflows](../Terminology/Attacks/Buffer Overflow)

Stems from the C/C++ programming languages allowing direct memory manipulation without bounds checking. So if you allocate a buffer of size 10, and write 20 bytes into it, the extra 10 bytes will overflow into adjacent memory.

- **The Flaw:**
    - A program allocates a fixed buffer.
    - The [OS](Operating System.md)/Program fails to check input size, allowing writes past the buffer end.
- **The Exploit (Stack Smashing):**
    - The attacker overflows the stack to overwrite the **Return Address**.
    - CPU jumps to malicious code (shellcode) instead of returning to the main function.
- **Mitigation:**
    - **ASLR (Address Space Layout Randomization)**: Randomizes memory layout so addresses are hard to guess.
    - **DEP/NX (Data Execution Prevention / No Execute)**: Marks stack memory as “Non-Executable.”

## [Race Conditions](../Terminology/Attacks/Race condition)

> [!example] Example: TOCTOU (Time-of-Check to Time-of-Use)
Because OSes multitask, a gap exists between checking the file permissions and using it.
>
> 1. **Check**: [OS](Operating System.md) confirms User A can write to `temp.txt`.
> 2. **The Gap (Context Switch)**: Attacker quickly swaps `temp.txt` with a symbolic link to `/etc/shadow` (password file).
> 3. **Use**: [OS](Operating System.md) resumes the process and writes to the target, overwriting the password file because the check already passed.

A research task we have today is how to mitigate and prevent these.

## Command Injection 💉

Occurs when the Shell is tricked into executing unintended commands.

- The Flaw: Passing unsanitized user input directly to a system command.
- The Exploit:
    - Script expects a filename: `rm $filename`
    - Attacker inputs: `file.txt; rm -rf /`
    - The [OS](Operating System.md) interprets ; as a command separator and executes both.

## Privilege Escalation

The attacker’s goal: Move from Ring 3 (User) to Ring 0 ([Kernel](../Terminology/Systems & Plaforms/Kernel.md)).

- Vertical Escalation:
    - Exploiting bugs in “SetUID” programs (programs that run as root, like `sudo` or `passwd`).
- [Kernel](../Terminology/Systems & Plaforms/Kernel.md) Exploits:
    - Crashing or manipulating the [Kernel](../Terminology/Systems & Plaforms/Kernel.md) itself.
    - **Weak Link**: Third-party **Drivers**. They run with full privileges but often have less rigorous code quality than the core kernel.

## Rootkits and Zero-Days

### Rootkits

- [Malware](<../Terminology/Attacks/Malware/Malware.md>) that modifies the system to hide its own existence.
- e.g., by just diverting or intercepting system calls.
- Essentially, it’s malware that’s designed to be stealthy and avoid detection by traditional security measures. It gets the [Operating System](<../Terminology/Systems & Plaforms/Operating System.md>) to lie to the user or security software about what’s really happening on the system.
- Example: When you run `ls` or `ps`, the rootkit filters the output of the underlying system calls to hide the hacker’s files and processes. The [OS](Operating System.md) lies to the user.
- **Defense**: Use trusted boot mechanisms and integrity checks to detect unauthorized changes to system binaries.

### Zero-Day Vulnerabilities

- A flaw known to the attacker but unknown to the vendor (0 days to fix).
- **Defense**: “[Defense in Depth](../Terminology/Defense & Control/Defense in Depth.md)”. You cannot patch it, so you must rely on [firewalls](../Terminology/Defense & Control/Firewall), strict [access control](../Terminology/Defense & Control/Access Control), procedures, etc. to contain it.

# Commands for Sysadmins

| Action                 | Linux Command     | PowerShell / Windows                                  |
| ---------------------- | ----------------- | ----------------------------------------------------- |
| Execute asroot / Admin | `sudo [cmd]`      | `Start-Process -Verb RunAs`(Or open Terminal asAdmin) |
| Change FilePermissions | `chmod 755 file`  | `icacls file /grant...`(Or `Set-Acl`)                 |
| View Permissions       | `ls -l`           | `icacls [file]`(Or `Get-Acl`)                         |
| Change Ownership       | `chown user file` | `takeown /f file`(Or `Set-Acl`)                       |
| Change Password        | `passwd`          | `Set-LocalUser`                                       |

`ls -l` access modifiers and their meanings:

![image](<../zAttachments/image.png>)

## File Permissions: Linux vs. Windows

**Linux ([POSIX](../Terminology/Systems & Plaforms/POSIX) Model)**

- Simple Structure: Permissions apply to three rigid categories:
1. User (Owner)
2. Group
3. Others (World)
- The Bits: Read (`r`), Write (`w`), Execute (`x`).
- Representation: often represented symbolically (`rwxr-xr-x`) or with a 3-digit octal (base-8) number (`755`). (`rwxr-xr-x` = `7` (`rwx`) `5` (`r-x`) `5` (`r-x`))
- Example: `chmod 755 file.txt` means:
    - Owner: Read, Write, Execute
    - Group: Read, Execute
    - Others: Read, Execute

**Windows (ACL ([Access Control](../Terminology/Defense & Control/Access Control) List) Model)**

- **Complex Structure**: Uses Access Control Lists (ACLs).
- **Granular**: You can assign distinct permissions to 50 different users individually.
- **Inheritance**: Files heavily inherit rules from parent folders.
- **The Rights**: Full Control, Modify, Read & Execute, List, Read, Write.

Everything is a file, the directory is a file. (This applies to Linux/Unix systems. With Windows, it’s a bit different as it uses objects and handles, but the concept of files and directories still exists.)

## Advanced Permissions: SUID & SGID

Concept: SUID (Set User ID) allows a user to execute a file with the permissions of the file owner, rather than their own.

Use Case: `passwd`

- **Problem**: Standard users cannot write to the password database (`/etc/shadow`).
- **Solution**: The `passwd` binary is owned by root and has SUID set.
- **Result**: When run, the process promotes to root temporarily to save changes.

Danger

- SUID is a major vector for **Privilege Escalation**.
- If an SUID root binary has a bug (e.g., [buffer overflow](../Terminology/Attacks/Buffer Overflow)), an attacker can exploit it to gain a Root Shell.
- Attackers scan for these immediately:
`find / -perm -4000`

Command: `chmod u+s file`

Indicator: `-rwsr-xr-x 1 root root 64152 maí 30 2024 /usr/bin/passwd`

## Process & Service Management

| Action                    | Linux Command           | PowerShell / Windows                           |                             |
| ------------------------- | ----------------------- | ---------------------------------------------- | --------------------------- |
| Start/StopServices        | `systemctl start [svc]` | `Start-Service [svc]`(`Get-`, `Stop-`, `Set-`) |                             |
| List Pro-cesses(Snapshot) | `ps aux`                | `Get-Process`                                  |                             |
| Real-time                 | `top` / `htop`          | `Get-Process \\                                | Sort CPU`(Or GUI `taskmgr`) |
| Kill Process              | `kill -9 [PID]`         | `Stop-Process -Id [PID]`                       |                             |

## Disk & File System Management

| Action     | Linux Command                              | PowerShell / Windows                     |                                |
| ---------- | ------------------------------------------ | ---------------------------------------- | ------------------------------ |
| Free Space | `df -h`(Disk Free)                         | `Get-Volume`(or `Get-PSDrive`)           |                                |
| Disk Usage | `du -sh [folder]`                          | `gci -Recurse \\                         | Measure -Property Length -Sum` |
| Search     | `find /path -name x`                       | `Get-ChildItem -Recurse -Filter "x"`     |                                |
| Archive    | `tar -czvf x.tar.gz`(or `zip`, `rar`, etc) | `Compress-Archive`(Win10+ has `tar.exe`) |                                |

## Logs

| Action             | Linux Command       | PowerShell / Windows                            |                               |                        |
| ------------------ | ------------------- | ----------------------------------------------- | ----------------------------- | ---------------------- |
| Followchanges live | `tail -f log.txt`   | `Get-Content log.txt -Wait`(Alias: `cat -Wait`) |                               |                        |
| Search             | `grep "Error"`      | `Select-String "Error"`(Alias: `sls`)           |                               |                        |
| … or both          | `tail -f log.txt \\ | grep "Error"`                                   | `Get-Content log.txt -Wait \\ | Select-String "Error"` |

## Scheduling & Maintenance

| Action          | Linux Command                                    | PowerShell / Windows                                      |
| --------------- | ------------------------------------------------ | --------------------------------------------------------- |
| ScheduleTasks   | `crontab -e`(opens the cron table in aneditor)   | `Register-ScheduledTask`                                  |
| Install Updates | `apt update && apt upgrade`(Depending on Distro) | `winget upgrade --all`(Only for apps, not the [OS](Operating System.md) itself!) |

# Up Next ..

## Further Studies

- Find examples of attacks that used root kits and discuss what role the rootkits played in the attacks.
- [Side-Channel Attacks](../Terminology/Virtualization/Side-Channel Attack) (Meltdown & Spectre): These famous vulnerabilities exploited Speculative Execution in the CPU hardware. How did they allow a User Mode process to read Kernel Mode memory without ever technically triggering a privilege violation?
- DMA (Direct Memory Access) Attacks: Peripheral devices (like a GPU or Network Card) use DMA to access RAM without asking the CPU. How can a malicious device (e.g., a compromised USB drive) use DMA to read system memory, bypassing the [OS](Operating System.md) entirely?
- Which mitigation means exist to avoid the problem of SUID opening the system up for privilege escalation attacks?

## Lab today and Guest Lecture tomorrow

- Lab 4: Use auditing (turn it on!) to find ”malicious” processes modifying the file system.
- Guest Lecture tomorrow by **Giovanni Apruzzese** on [Phishing](<../Terminology/Attacks/Phishing.md>).

Day before the exam will be a recap lecture.

Exam (Friday, 12th of December) will be later in the day? Around noon or later?

Knowledge base in the exam: we might just get a print-out. It shouldn’t be too big.

[Lab 4 (Gísli) Operating Systems](Labs/Lab 4 (Gísli)%20Operating%20Systems.md)
