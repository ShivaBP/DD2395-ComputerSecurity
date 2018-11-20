#!/usr/bin/python

import unittest
import subprocess

class test(unittest.TestCase):
    def test(self):
	try:
		subprocess.check_output("unbuffer make attack > res.txt", shell=True)
	except:
		pass
	res = open("res.txt").read()
	print res
        self.assertTrue(res.find("your pwd is: pwd0") >= 0)


if __name__ == '__main__':
    unittest.main()

