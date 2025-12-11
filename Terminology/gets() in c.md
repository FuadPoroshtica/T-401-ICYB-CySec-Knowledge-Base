---
aliases: []
date created: Thursday, 27. November 2025, 10:11
date modified: Thursday, 11. December 2025, 14:12
---

# gets() in C

**Definition**: *`gets()`* is a C standard library function used to read a line of text from standard input into a buffer. It is considered highly dangerous because it does not perform bounds checking on the buffer, allowing users to input more data than the buffer can hold, which leads to buffer overflows. This is also the case for the stdlib function `scanf()`

**Context/Example**: Using `gets()` like this:

```c
char buffer[10];
gets(buffer);
```

**Mitigation**: Use a non deprecated C function that actually has boundaries, `fgets()` is a pretty good alternative, it accepts a size parameter:
```c
#include <stdio.h>
int main() {
	char buff[100];
	int n = 10;
	printf("input: ");
	
	// read input with fgets
	fgets(buff, n, stdin);
	
	printf("you inputed: %s", buff);
}
```
