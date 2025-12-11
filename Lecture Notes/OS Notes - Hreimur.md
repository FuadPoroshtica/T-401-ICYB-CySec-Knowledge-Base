**What is an OS?** Core definition: Event driven program that manages hardware state, Acts as a bridge between applications and hardware
**Key Components:** Kernel (Ring 0): Core OS component, runs in privileged mode with direct hardware access. User Space (Ring 3): Where applications run in restricted mode
**Two main fuctions**
Abstraction via system calls: Wraps complex hardware in clean software APIs. Provides consistent interface across platforms. Examples printf(), fopen() trigger system calls. OS switched to kernel mode > performs task > returns result
Arbitration/Resource Management:
Times multiplexing: scheduling processes on CPU, Space multiplexing: Dividing ram/disk among processes. Isolation: Ensuring process A does not crash process B
#### Key OS Functions
**Process Management  (Scheduling)** Program: Static instructions on disk, Process: Program in execution (RAM + CPU state)
**Context Switching** OS halts current process, Saves CPU registers to Process Control Block (PCB), Loads saved state of next process, Result: Illusion of parellelism
**Memory Management (Virtualization)** Virtual Memory: each process sees contiguous memory space. Translation OS + MMU map virtual > physical address. Protection: Process A cant access Process Bs memory. Segfault: Access to unmapped address
**I/O and Interrupt Management**
Problem I/O is millions of times slower than CPU, Solution: 1. Request" User program request I/O (system call). 2. Sleep: OS puts process in waiting state. 3. Interrupt Hardware send signal when ready. 4. ISR cpu jumps to interrupt service routine. 5. Wake OS moves process back to Ready queue.
**File Systems** Physical: Array of disk blocks/sectors, Logical: Files, Directories and paths. Responsibilities: Mapping filenames > blocks, metadata, journaling
**Protection (Ring 0 vs Ring 3)** Ring 0 (Kernel): full hardware access, can manipulate memory/interrupts. Ring 3 (User): Restricted instructions, no direct hardware access. Traps: CPU hardware catches privilege violations > OS handles (just kills process)
#### Common OS's
**Unix/Linux**: Philosophy: Everything is a file (hardware, sockets, data via file descriptors). Linux: Just the Kernel (Linus Torvalds 1991). Distro: Kernel + GNU Tools + Package manager + desktop. Architecture: Monolithic kernel (drivers in kernel space)
**MacOS**: Based on Darwin (Hybrid XNU kernel: Mach + BSD). POSIX compliant
**Windows** Architecture: Hybrid kernel (performance critical in kernel mode, subsystems in user mode) Config: Registry (vs Unix text files) Resource Model: Abstract objects managed via handles. Modern: Based on Windows NT (not MS-DOS like Win 95/98/Me)
**Android** Uses Linux kernel but unique user space. Stack: ART (android runtime) > native libraries/hal > Linux kernel. Apps: complite to dex bytecode (not native). Key mechanism: Binder IPC for sandboxed apps to communicated
**Embedded/RTOS**: Goal: Determinism/Consistency (not throughput), Hard real time: delayed caluclations = system failure (car breaks, pacemaker) Features: Tiny kernels, fast interrupts and often no virtual memory
**POSIX**: Portable operating system interface (IEEE standard), Purpose: API contract for UNIX compatibility, Defines system call APIs (open, fork, pthreads) shell utils. Compliance: MacOS certified, Linux mostly compliant and Windows requires WSL
#### OS and Security
**Trusted Computing Base (TCB)** All protection mechanisms (hardware + firmware + software) that enforce security policy, Critical if any part breaks, entire system security breaks
**The reference monitor** OS acts as a gatekeeper checking: 1. Authentication: Who are you?. 2. Authorization: Are you allowed? **Authentication** Identification: Claiming idenity (username) Verifcation: Proving it (password/bimetric/key)
**Secure Storage**: Never store passwords in plaintext. Use cryptographic hashing (SHA-256), add **salt** (random string) before hashing to prevent rainbow table attacks and store: Hash(password + salt)
**Access Control**
**DAC (Discretionary Access Control)** Owner decides permissions, Example Linux chmod command. Risk: Malware running as you can change permissions.
**Mac (Mandatory Access Control)** System policy decides (users cant override), Used in SELinux, ios/android. Examples web server cant read /home even if you run by root
**Principle of least privilege** Rule: Process should have only minimum privileges necessary. Why: Limits "blast radius" if compromised. Enforcement: CPU mode (Ring 0 vs Ring 3)
**System Logs** What? High level event records (login, sudo and crashes) Linux: var/log/syslog and /var/log/auth.log Windows: Event Viewer. Use: First place admins look after breach
**System Auditing (Kernel Level)** Hooks into kernel to track system calls, Example: "Proccess 402 attempted open() on /etc/shadow - denied" Required for PCI-DSS, HIPPA compliance
**Linux:** auditd framework
```bash
sudo auditctl -w /etc/shadow -p wa -k password-change
```
**Windows:** auditpol tool
```cmd
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
```
**MacOS:** BSM (Basic security Module) binary logs (use praudit to read)
**File integrity monitoring (FIM)** Threat: attackers replacing system binaries like /bin/login. Defense: Calculate checksums/hashes of critical files, Alert: if hash changes trigger alarm
#### Common Vulnerabilties and Exploits
**Buffer overflows** C/C++ allows direct memory maniulation without bounds checking
Exploit (Stack smashing) 1. Program allocates fixed buffer, 2. attacker overflows to overwrite return address on stack, 3. CPU jumps to malicious shellcode instead of returning. Mitigation: <abbr title="Address Space Layout Randomization">ASLR</abbr>: randomizes memory layout, DEP/NX: marks stack as non executable
**Race conditions (TOCTOU)** Time of Checks to Time Of Use: 1. Check OS confirms user can write to temp.txt, 2. Gap: context switch - attacker swaps temp.txt with symlink to /etc/shadow. 3. Use OS writes to target (check already passed)
**Command injection** Passing unsanitized user input to system commands. Example: Script expects: rm $filename. Attacker inputs file.txt; rm -rf /. OS interprets : as command separator
**Privilege Excalation** Goal: Move from Ring 3 (User) to Ring 0 (Kernel). Methods: Exploiting SetUID programs (sudo, passwd). Kernel Exploits and Weaklinks: Third party drivers (run with full privileges, less rigorous code)
**Rootkits**: Malware that modifies system to hide itself. Intercepts system calls (e.g. ls, ps) to filter output. OS lies to the user
**Zero-Day Vulnerabilties** Flaw known to attack but unknown to vendor (0 days to fix) Defense: "Defense in depth" - firewalls, strict access control and procedures
#### Commands for Sysadmins

| Action                  | Linux           | Windows                   |
| ----------------------- | --------------- | ------------------------- |
| Execute as root/admin   | sudo cmd        | Start-Process -Verb RunAs |
| Change file permissions | chmod 755 file  | icacls file /grant ...    |
| View permissions        | ls -l           | icacls file               |
| Change ownership        | chown user file | takeown /f file           |
| Change password         | passwd          | Set-LocalUser             |
**Linux File Permissions (POSIX Model)**
Structure: User/Group/Other bits: Read (r), Write (w), Execute(x) Representation: Octal (755) or symbolic (rwxr-xr-x)
**SUID/SGID (Advanced):** <abbr title="Set User ID">SUID</abbr>: Execute file with owners permission (not your own) Use Case: paswd needs to be <abbr title="Set User ID">SUID</abbr> root to modify /etc/shadow. Command chmod u+s file. Indicator: -rwsr-xr-x (look at the s). Danger: Major privilege excalation vector if <abbr title="Set User ID">SUID</abbr> binary has bugs. Scanner: find / -perm -4000 (attackers use this)
**Windows File Permissions (ACL Model)** Structure Access control lists, Granular: Assign distinct permissions to many users individually. Inheritance: Files inherit from parent folders. Rights: Full control, modify, read and execute, list, read , write.
**Process and Service Management**

| Action              | Linux               | Windows                 |
| ------------------- | ------------------- | ----------------------- |
| Start/Stop Services | systemctl start svc | Start-Service svc       |
| List processes      | ps aux              | Get-Process             |
| Real time monitor   | top/htop            | Get-Process \| Sort CPU |
| Kill process        | kill -9 PID         | Stop-Process -Id PID    |
**Disk and File System**

| Action     | Linux              | Windows                                       |
| ---------- | ------------------ | --------------------------------------------- |
| Free Space | df -h              | Get-Volume                                    |
| Disk Usage | du -sh folder      | gci -Recurse \| Measure -Property Length -Sum |
| Search     | find /path -name x | Get-ChildItem -Recurse -Filter "x"            |
| Archive    | tar -czvf x.tar.gz | Compress-Archive                              |
**Logs**

| Action      | Linux                           | Windows                                            |
| ----------- | ------------------------------- | -------------------------------------------------- |
| Follow Live | tail -f log.txt                 | Get-Content log.txt -Wait                          |
| Search      | grep "Error"                    | Select-String "Error"                              |
| Combined    | tail -f log.txt \| grep "Error" | Get-Content log.txt -Wait \| Select-String "Error" |
**Scheduling and Maintenance**

| Action          | Linux                     | Windows                |
| --------------- | ------------------------- | ---------------------- |
| Schedule Tasks  | crontab -e                | Register-ScheduledTask |
| Install Updates | apt update && apt upgrade | winget upgrade --all   |
#### Quick Reference Tables Summary
**OS Comparison:** Unix/Linux: Monolithic kernel "everything is a file", text config files. **Windows**: Hybrid kernel, registry, object/handle model. **MacOS**: Hybrid XNU, POSIX compliant, Darwin Based. **Andriod:** Linux kernel + unique user space + Binder IPC. **RTOS** Determinism over throughput, tiny kernels, no virtual memory.
**Security Model:** **DAC:** Owner decides (flexible, risky), **MAC** system decides (strict, secure). **TCB:** All security mechanisms must work or entire system fails
**Common Attack Vectors:** 1. Buffer overflow > stack smashing. 2. Race conditions > TOCTOU. 3. Command Injection > unsanitized input. 4. Privilege escalation > <abbr title="Set User ID">SUID</abbr> exploits, kernel bugs. 5. Rootkits > system call interception. 6. Zero Days > unknown vulnerabilities
#### RootKit Attacks
**What are they?** Malicious software providing unauthorized privileged access to systems while hiding its presence. Operates at different privilege levels: Usermode (Ring 3), Kernel mode (Ring 0), Hypervisor (Ring -1). Modifies system files, alters system calls, and uses stealth techniques to evade detection. Can hide files, processes, network connections, and registry keys from users and security software.
**Famous historical Examples:** **Sony BMG Rootkit Scandal (2005)** What happened? Sony BMG secretly installed rootkit DRM software on 22+ million music CDs. How it worked? When CDs played on windows PCs rootkit installed automatically without user consent to prevent copying. Security Impact? Hid files starting with "sys" from users and antivirus, Created vulnerabilities exploited by other malware, Slowed computers and made them susceptible to attacks. Consequences: Class action lawsuits, CD recalls, FTC settlement, US-CERT advisory, massive PR disaster
**Detection Challenges:** Rootkits subvert detection software by controlling what the system reports. Specialized anti rootkit tools required (signature scanning, difference-based detection, memory dump analysis) Best detection: Boot from trusted OS or use hardware based analysis
#### Meltdown and Spectre vulnerabilities
**Core Concept Speculative execution:** Modern CPUs use speculative execution for performance optimization: CPU predicts which code branch will execute and runs it before knowing if the prediction is correct. If wrong results discarded - but side effects remain in CPU cache. Attackers exploit these side effects using cache timing attacks to steal data
**Meltdown (CVE-2017-5754)** What it exploits? Out-of-order execution + permission check timing issue. Intel processors check permissions after reading memory (speculative execution). Data brought into cache before CPU realizes user shouldnt acces it
**Attack mechanism:** 1. User process tries to read kernel memory (forbiden) 2. CPU reads memory speculatively BEFORE checking permissions. 3. Data loaded into cache. 4. Permission check fails, instruction discarded. 5. BUT data remains in cache - attacker measures cache timing to extract it. **Impact:** breaks fundemental isolation between user applications and OS. Allows reading all system memory including passwords, encryption keys, sensitive data. Affects virtually all Intel x86 processors (1995-present) and some ARM processors
**Mitigation:** KPTI (Kernel Page Trable Isolation) - formerly KAISER. Separates kernel and user virtual address space. Removes kernel memory from page tables when user code runs. Performance cost: Extra work during system class (~5-30% slowdown)
#### DMA (Direct Memory Access) Attacks
**What is DMA?** feature allowing hardware devices to access system memory directly without CPU involvement. Used by GPUs, NIC, storage devices, peripherals for high speed data transfer. Security problem: Bypasses OS security, MMU and virtual memory protections.
**Attack Concept** Normal access: Applications > OS > CPU > Memory. DMA attack: Malicious device > Physical memory bypassing all OS security.
**Attack Vectors**: **Physical access attacks:** Thunderbolt, FireWire, ExpressCard, PCIe ports provide DMA capability. Attacker connects rogue device to DMA enabled port. Device reads/writes system memory directly. Can steal encryption keys, install malware, bypass login screens. **"EVIL MAID" Attack scenario:** Brief physical access to victim laptop (hotel room, airport). Connect DMA attack device via thunderbolt. Extract passwords encryption keys from RAM. Install persistent backdoor. All within minutes, systems appears untouched. **Remote/Network DMA:** RDMA (Remote direct memory access): Used in data centers for performance. Attacker compromises network device (NIC) firmware. Performs DMA attacks over network without physical access. Throwhammer: Triggers Rowhammer bit flips remotely via network packets. **Mitigation Strategies:** Hardware level: IOMMU (I/O Memory Management Unit) Maps device memory access through virtual addresses. Limits Memory ranges DMA devices can access. Not foolproof - Thunderspy bypasses some IOMMU protections. **Firmware/bios** **OS Settings** **Physical security** **Best practices:** remove unnecessary <abbr title="Set User ID">SUID</abbr> permission from binaries. Never allow thunderbolt devices from untrusted sources. Enterprise: require user authentication for DMA capable connections. Data center: Isolate RDMA traffic, monitor for anomalies. **Key Takeaway:** DMA attacks remain viable in todays age despite vendor protections. Evil maid scenarios, compromised firmware, and remote RDMA attacks make this relevant for enterprise security.
#### SUID Bit Mitigation Techniques
**Common SUID explot techniques:** Command execution binaries like find, vim, nano, less, more, awk, sed exploited by using built in shell execution features:
```bash
find . -exec /bin/bash -p \; # spawns root shell
vim -c ':!/bin/bash'
```
File Read/Write binaries: cp, mv, cat, tail, head exploit by overwriting sensitive system files
```bash
# if cp has SUID bit:
cp /etc/passwd /tmp/passwd # copy for editing
echo 'attacker::0:0:root:/root:/bin/bash' >> /tmp/passwd
cp /tmp/passwd /etc/passwd # Overwrite original - now were root!
```
PATH Variable Manipulation: If <abbr title="Set User ID">SUID</abbr> program calls other programs without absolute paths. Exploit: Create malicious version in /tmp,modify $PATH
```bash
echo '/bin/bash' > /tmp/ls
chmod +x /tmp/ls
export PATH=/tmp:$PATH
./vulnerable_suid_program # Execuites /tmp/ls instead of /bin/ls
```
Symlink Attacks: If <abbr title="Set User ID">SUID</abbr> program writes to user-controllable file. Exploit: Replace destination with symlink to /etc/passwd or /etc/shadow
```bash
ln -s /etc/passwd /tmp/target_file
./vulnerable_suid_program /tmp/target_file # writes to /etc/passwd
```
**Mitigation Strats** Find all <abbr title="Set User ID">SUID</abbr> and SGID binaries and compare to baseline and remove all custom <abbr title="Set User ID">SUID</abbr> binaries if not necessary. Remove unneccessary <abbr title="Set User ID">SUID</abbr> permissions. Use Linux capabilities instead, More fine grained than <abbr title="Set User ID">SUID</abbr>, If compromised attacker only gets that ONE capability not full root.
**Nice Notes** **Rootkits** hide at kernel level: detection requires specialized tools, trusted OS or hardware analysis. **Stuxnet** was first cyberweapon causing physical damage via rootkit. **Sony BMG scandal** exposed 22m users to security risks with DRM rootkit. **Meltdown breaks OS kernel isolation** - All intel CPUs vulnerable fixed by KPTI. **Spectre harder to fix** nearly universal CPU vulnerability, partial mitigations only. **Speculative execution side effect** leak data through cahce timing. **DMA bypasses all OS security** direct physical memory access. **PCILeech** is primary DMA attack tool (Thunderbolt/PCIe). **Thunderspy breaks thunderbolt 3 security** on all 2011-2020 systems. **IOMMU provides DMA protection** but not fool proof. **SUDI mitigation** remove unnecessary, use capabilities, audit regularly, monitor execution. **Never give <abbr title="Set User ID">SUID</abbr> to:** cp, find, vim or any command execution binaries.