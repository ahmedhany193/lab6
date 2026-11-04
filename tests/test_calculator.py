import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calculator.add(-2, -3), -5)

    def test_add_decimals(self):
        self.assertAlmostEqual(self.calculator.add(0.1, 0.2), 0.3)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calculator.subtract(8, 3), 5)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calculator.subtract(3, 8), -5)

    def test_subtract_equal_numbers(self):
        self.assertEqual(self.calculator.subtract(4, 4), 0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calculator.multiply(4, 3), 12)

    def test_multiply_negative_number(self):
        self.assertEqual(self.calculator.multiply(-4, 3), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calculator.multiply(5, 0), 0)

    def test_divide_evenly(self):
        self.assertEqual(self.calculator.divide(12, 3), 4)

    def test_divide_fractional_result(self):
        self.assertAlmostEqual(self.calculator.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
