#!/usr/bin/python
# encoding: utf-8
from __future__ import division, print_function, unicode_literals
import unittest
import numpy as np

from QML.numpy_helpers import v

class TestHelpers(unittest.TestCase):
    def test_v_shape(self):
        self.assertEqual(v("1").shape, (1,))
        self.assertEqual(v("1 2 3").shape, (3,))
        self.assertEqual(v("1 2 3 4 5 6").shape, (6,))

    def test_v_integer_values(self):
        x = v("1 -2 3")
        self.assertTrue(np.all(x == [1, -2, 3]))
    
    def test_v_float_values(self):
        x = v("0.3 -.4 6e-2 7E4")
        self.assertTrue(np.all(x == [0.3, -0.4, 0.06, 70000]))

    def test_v_is_numpy_array(self):
        x = v("1 2 3")
        self.assertTrue(isinstance(x, np.ndarray))

if __name__ == "__main__":
    unittest.main()
