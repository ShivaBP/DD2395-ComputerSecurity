#!/usr/bin/python

import unittest
import subprocess

class test(unittest.TestCase):
    def test(self):
	lines = open("solution2.txt", "r").read().split("\n")
	value = [l.split(" ") for l in lines if not(l.startswith("#"))][0]
        self.assertTrue(value[1] != "pwd0")
	res = subprocess.check_output(["./main"] + value)
        self.assertTrue(res.find("non authorized") < 0)


if __name__ == '__main__':
    unittest.main()

