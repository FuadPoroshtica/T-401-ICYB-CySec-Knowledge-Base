---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Monday, 8. December 2025, 11:12
---
# gets() in C

**Definition**: _`gets()`_ is a C standard library function used to read a line of text from standard input into a buffer. It is considered highly dangerous because it does not perform bounds checking on the buffer, allowing users to input more data than the buffer can hold, which leads to buffer overflows.  

**Context/Example**: Using `gets()` like this:  

```c
char buffer[10];
gets(buffer);
