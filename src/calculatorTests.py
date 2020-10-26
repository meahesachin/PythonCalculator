import unittest
from calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_additon(self):
        calculator = Calculator()
        self.assertEq(calculator.add(1,1),2)

    def test_subtraction(self):
        calculator = Calculator()
        self.assertEq(calculator.subtract(1,1),0)

    def test_results_property(self):
        calculator = Calculator()
        calculator.add(2, 1)
        self.assertEqual(calculator.result, 3)

if __name__ == '__main__':
    unittest.main()
