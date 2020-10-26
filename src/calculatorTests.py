import unittest
from calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1,1),2)

    def test_subtraction(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(1,1),0)

    def test_results_property(self):
        calculator = Calculator()
        calculator.add(2, 1)
        self.assertEqual(calculator.result, 3)

    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 3), 6)

    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 3), 2)

    def test_square(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(2), 4)

    def test_sqrt(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(4), 2)


if __name__ == '__main__':
    unittest.main()
