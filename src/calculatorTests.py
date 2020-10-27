import unittest
from calculator import Calculator
from CSVReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("testdata/UnitTestAddition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(float(row['Value 2']), float(row['Value 1'])), result)

        # self.assertEqual(self.calculator.add(1, 1), 2)

    def test_subtraction(self):
        test_data = CsvReader("testdata/UnitTestSubtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(float(row['Value 2']), float(row['Value 1'])), result)
            # self.assertEqual(self.calculator.result, result)
        # self.assertEqual(self.calculator.subtract(1, 1), 0)

    def test_results_property(self):
        self.calculator.add(2, 1)
        self.assertEqual(self.calculator.result, 3)

    def test_multiply(self):
        test_data = CsvReader("testdata/UnitTestMultiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(float(row['Value 2']), float(row['Value 1'])), result)
        # self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        test_data = CsvReader("testdata/UnitTestDivision.csv").data
        for row in test_data:
            result = format(float(row['Result']), '.9f')
            # print('Result is: ' + result)
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), result)
        # self.assertEqual(self.calculator.divide(6, 3), 2)

    def test_dividebyzero(self):
        self.assertEqual(self.calculator.divide(6, 0), 0)

    def test_square(self):
        test_data = CsvReader("testdata/UnitTestSquare.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
        # self.assertEqual(self.calculator.divide(6, 3), 2)
        # self.assertEqual(self.calculator.square(2), 4)

    def test_sqrt(self):
        test_data = CsvReader("testdata/UnitTestSquareRoot.csv").data
        for row in test_data:
            result = format(float(row['Result']), '.8f')
            # print('Result is: ' + result)
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)
        self.assertEqual(self.calculator.sqrt(4), 2)


if __name__ == '__main__':
    unittest.main()
