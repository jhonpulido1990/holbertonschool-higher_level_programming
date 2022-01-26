#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        

    def test_float(self):
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 4.3)

    def test_strin(self):
        self.assertIsInstance(max_integer([1, 2, 3, 4]), int)

if __name__ == "__main__":
    unittest.main()
