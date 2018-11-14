#!/usr/bin/python
from insecure_hash import hash_string
from Crypto.Cipher import AES
import random
import string


def find_collision(message):
    key = "Thisisarandomkey"
    hashValue = hash_string(message)
    cipher = AES.new(key)
    result = cipher.encrypt(hashValue)
    result = result + key
    return result

if __name__ == '__main__':
    message = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb"
    print ("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print ("Hash of %s is %s" % (collision, hash_string(collision)))

