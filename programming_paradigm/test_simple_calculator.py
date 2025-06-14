import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

  def setUp(self):
    """Set up the SimpleCalculator instance before each test."""
    self.calc = SimpleCalculator()

  # Test addition
  def test_addition(self):
    self.assertEqual(self.calc.add(6, 5), 11)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(0, 0), 0)
    self.assertEqual(self.calc.add(-5, -5), -10)

  # Test subtraction
  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(6, 5), 1)
    self.assertEqual(self.calc.subtract(-1, 1), -2)
    self.assertEqual(self.calc.subtract(0, 0), 0)
    self.assertEqual(self.calc.subtract(-5, -5), 0)

  # Test multiplication
  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(6, 5), 30)
    self.assertEqual(self.calc.multiply(2, 1), 2)
    self.assertEqual(self.calc.multiply(0, 10), 0)
    self.assertEqual(self.calc.multiply(-5, -5), 25)

  # Test division
  def test_division(self):
    self.assertEqual(self.calc.divide(10, 5), 2)
    self.assertEqual(self.calc.divide(-10, 2), -5)

  # Test Zero division
    self.assertIsNone(self.calc.divide(10, 0), None)

  def test_edge_cases(self):
    """Test some additional edge cases for the calculator."""
    # Edge case for division by 1
    self.assertEqual(self.calc.divide(20, 1), 20)
    # Edge case for multiplying by zero
    self.assertEqual(self.calc.multiply(20, 0), 0)

if _name_ == "_main_":
  unittest.main()