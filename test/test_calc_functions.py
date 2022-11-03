import unittest
import sys


sys.path.append('app')

import calc_functions


class TestSum(unittest.TestCase):
    def test_sum(self):
        """
        """
        result = calc_functions.sum(1, 2)
        self.assertEqual(result, 3.0)


class TestSubstract(unittest.TestCase):
    def test_sub(self):
        """
        """
        result = calc_functions.substract(1, 2)
        self.assertEqual(result, -1)


class TestMultiply(unittest.TestCase):
    def test_mul(self):
        """
        """
        result = calc_functions.multiply(1, 2)
        self.assertEqual(result, 2)


class TestDivide(unittest.TestCase):
    def test_div(self):
        """
        """
        result = calc_functions.divide(1, 2)
        self.assertEqual(result, 0.5)


if __name__ == '__main__':
    unittest.main()
