#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a unittest class for the max integer module
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([107, 37, 40, 20]), 107)
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4})
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            max_integer([1, 2.0, 3.4, 5])
