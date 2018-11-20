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
        self.assertTrue(res.find("root:") >= 0)
        self.assertTrue(res.find("student:") >= 0)


if __name__ == '__main__':
    unittest.main()

