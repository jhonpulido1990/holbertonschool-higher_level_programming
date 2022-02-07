#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):
    def test_rectangle_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 8)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 9)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_from_json_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

