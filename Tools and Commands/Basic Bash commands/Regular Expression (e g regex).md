---
aliases: []
date created: Tuesday, 25. November 2025, 17:11
date modified: Thursday, 11. December 2025, 13:12
---

# Regular Expression (e.g. regex)

Regular Expression is a filtering method used in many linux/unix commands.

| Symbol   | Use                                             |
| -------- | ----------------------------------------------- |
| a*       | Zero or many As                                 |
| .        | Any Single Character                            |
| [abc]    | Any single character of a, b or c               |
| [^abc]   | Any single character except a, b or c           |
| [a-z]    | Any single character between a and z            |
| ^{a-z]   | Any single character not between a and z        |
| [A-Za-Z] | Any single character between a and z or A and Z |
| a\|b     | Any string matching a or b                      |
| a?       | zero or one of a                                |
| a+       | one or more of a                                |
| a{n}     | exactly $n$ of a, $n \in \mathbb{z}$            |
| a{n, m}  | between n and m of a, $n, m \in \mathbb{z}$     |
| ^        | start of string                                 |
| $        | end of string                                   |
