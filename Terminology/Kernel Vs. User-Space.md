The Kernel has access to all hardware, the user calls the kernel with specific systemcalls, (e.g., 0 for read and 1 for write) this is usually done with specific subroutines in the C Standard Library (e.g., `fopen()` eventually executes syscall 0 for read).
Diagram of Kernel Vs. User-Space:
![](../zAttachments/Pasted%20image%2020251211183911.png)