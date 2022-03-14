#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import unittest
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):
    def test_rectangle_int(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 13)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_Rectangle_display(self):
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(r1.display(), None)

    def test_from_json_error(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_base_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    
    