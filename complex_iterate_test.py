import unittest
from foo import *

class TestCalculation(unittest.TestCase):
    """
    Unit Test cases for the do_calculation(..)
    """
    def test_do_calculation_a(self):
        num = 1 + 1j
        seed = 2 + 3j
        result = do_calculation(num, seed)
        print(result)
        self.assertEqual(result, 2 + 5j)
    def test_do_calculation_b(self):
        num = 1
        c = 0.285 + 0.01j
        result = do_calculation(num, c)
        print(result)
        self.assertEqual(result, 1.285+0.01j)
    def test_do_calculation_c(self):
        num = -1 - 3j
        c = -0.8+0.156j
        result = do_calculation(num, c)
        print(result)
        self.assertEqual(result, -8.8+6.156j)
    def test_do_calculation_d(self):
        num = 1.25 + -1.67j
        c = -0.7269+0.1889j
        result = do_calculation(num, c)
        print(result)
        self.assertEqual(result, -1.9533-3.9861j)

class TestIterate(unittest.TestCase):
    """
    Unit Test cases for the do_iterate(..)
    """
    def test_do_iteration_a(self):
        num = 1 + 1j
        seed = 2 + 3j
        result = do_iteration(num, seed)
        print(result)
        self.assertEqual(result, 1)
    def test_do_iteration_b(self):
        num = .8 +.5j
        c = -.5 + 0.06j
        result = do_iteration(num, c)
        print(result)
        self.assertEqual(result, 8)
    def test_do_iteration_c(self):
        num = 1 + -.1j
        c = -0.7269+0.1889j
        result = do_iteration(num, c)
        print(result)
        self.assertEqual(result, 136)
    def test_do_iteration_d(self):
        num = 1
        c = 0.285 + 0.01j
        result = do_iteration(num, c)
        print(result)
        self.assertEqual(result, 3)
    def test_do_iteration_e(self):
        num = -.21 + .01j
        c = 0.1285 + 0.01j
        result = do_iteration(num, c)
        print(result)
        self.assertEqual(result, 255)
if __name__ == '__main__':
    unittest.main()
