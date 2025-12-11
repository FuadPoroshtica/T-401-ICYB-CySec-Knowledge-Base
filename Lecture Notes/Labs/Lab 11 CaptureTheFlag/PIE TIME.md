Have to use first file tool to see that is the security of the binary file, use gdb to see where is what saved in the memory,
Use rabin2 to find where is each variable function located | grep main or win to make it easier to find.

We need to calculate the offset between win and main.
Than we add our offset to the address that is curr in main, and we enter it in a field. You should get a flag;