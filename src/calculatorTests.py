import unittest
from calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        self.assertEqual(self.calculator.add(1, 1), 2)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(1, 1), 0)

    def test_results_property(self):
        self.calculator.add(2, 1)
        self.assertEqual(self.calculator.result, 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)

    def test_dividebyzero(self):
        self.assertEqual(self.calculator.divide(6, 0), 0)

    def test_square(self):
        self.assertEqual(self.calculator.square(2), 4)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)


if __name__ == '__main__':
    unittest.main()
