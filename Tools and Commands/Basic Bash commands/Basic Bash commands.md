---
aliases: []
date created: Tuesday, 25. November 2025, 17:11
date modified: Monday, 1. December 2025, 21:12
---

# Basic Bash commands

## Navigation & file searching (TODO)

| Action            | Bash/Zsh        | PowerShell                   |
| ----------------- | --------------- | ---------------------------- |
| Print directory   | `pwd`           | `pwd` (`Get-Location`)       |
| List Files        | `ls`            | `ls` / `dir`                 |
| List Hidden Files | `ls -a`         | `ls -Force`                  |
| Change Dir        | `cd <path>`     | `cd <path>` (`Set-Location`) |
| Create File       | `touch <file>`  | `ni <file>` (`New-Item`)     |
| Copy              | `cp`            | `cp` / `copy` (`Copy-Item`)  |
| Move/Rename       | `mv`            | `mv` / `move` (`Move-Item`)  |
| Delete            | `rm`            | `rm` / `del` (`Remove-Item`) |
| Force Delete      | `rm -rf`        | `rm -Recurse -Force`         |
| Show the manual   | `man <command>` | `help`, `man` (`Get-Help`)   |
| History           | `history`       | `history` (`Get-History`)    |

## Reading & Searching (TODO)

| Action                 | Bash/Zsh           | PowerShell                                                                |
| ---------------------- | ------------------ | ------------------------------------------------------------------------- |
| Read file content      | `cat <file>`       | `cat` / `type` (`Get-Content`)                                            |
|                        |                    |                                                                           |
| one page at a time     | `less <file>`      | `more`                                                                    |
| First $n$ lines        | `head -n 10`       | `select -first 10` (`Select-Object -First 10`)                            |
| Last $n$ lines         | `tail -n 10`       | `select -last 10` (`Select-Object -Last 10`)                              |
| Live Log               | `tail -f`          | `Get-Content -Wait`                                                       |
| Search Text with Regex | `grep "txt"`       | `sls "txt"` (`Select-String`)                                             |
| Find File              | `find . -name "X"` | `ls -r -filter "X"` (`Get-ChildItem -Recurse -Filter`)                    |
| Find File by Content   | `grep -R "txt"`    | `ls -r sls "txt"` (`Get-ChildItem -Recurse Select-String -Pattern "txt"`) |
