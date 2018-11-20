#!/usr/bin/python

import unittest
import subprocess

class test(unittest.TestCase):
    def test(self):
	lines = open("solution1.txt", "r").read().split("\n")
	value = [l.split(" ") for l in lines if not(l.startswith("#"))][0]
	res = subprocess.check_output(["./main"] + value)
        self.assertTrue(res.find("pwd0") >= 0)


if __name__ == '__main__':
    unittest.main()

