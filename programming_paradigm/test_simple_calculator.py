import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 0), 100)
        self.assertEqual(self.calc.add(0, 100), 100)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(4, 10), -6)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(7, 1), 7)

    def test_divide(self):
        """Test the divide method for valid inputs."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        # Using assertAlmostEqual for floating point comparisons can be safer
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333) 

    def test_divide_by_zero(self):
        """Test the divide method for division by zero."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

if __name__ == '__main__':
    unittest.main()