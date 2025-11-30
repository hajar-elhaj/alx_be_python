import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Create a calculator instance for all tests
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-10, 5), -15)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_by_zero(self):
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)  # matches your class behavior
        

if __name__ == "__main__":
    unittest.main()