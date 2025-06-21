import unittest
from calc_scratch import Interpreter


class TestAddition(unittest.TestCase):
  def test_single_digits(self):
    input = '7+8'
    expected = 15 

    self.assertEqual(Interpreter(input).expr(),
                     expected)
  
  def test_whitespace_variation_tabs(self):
      input = ' 56  + 78  '
      expected = 134
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_whitespace_mixed(self):
      input = '  90 + 10  '
      expected = 100
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_multi_digit_small(self):
      input = '12+34'
      expected = 46
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_multi_digit_large(self):
      input = '1234+5678'
      expected = 6912
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_multi_digit_very_large(self):
      input = '123456+654321'
      expected = 777777
      self.assertEqual(Interpreter(input).expr(), expected)

class TestSubtraction(unittest.TestCase):
  def test_subtraction_single_digits(self):
      input = '9-4'
      expected = 5
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_subtraction_multi_digit(self):
      input = '100-75'
      expected = 25
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_subtraction_with_whitespace(self):
      input = '   1000   -   999 '
      expected = 1
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_subtraction_result_negative(self):
      input = '50 - 100'
      expected = -50
      self.assertEqual(Interpreter(input).expr(), expected)

class TestMultiplication(unittest.TestCase):
  def test_multiplication_single_digits(self):
    input = '3*4'
    expected = 12
    self.assertEqual(Interpreter(input).expr(), expected)

  def test_multiplication_multi_digit(self):
      input = '12*34'
      expected = 408
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_multiplication_with_whitespace(self):
      input = '  7   *    6  '
      expected = 42
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_multiplication_large_numbers(self):
      input = '123*456'
      expected = 56088
      self.assertEqual(Interpreter(input).expr(), expected)

class TestDivision(unittest.TestCase):
  def test_division_single_digits(self):
      input = '8/2'
      expected = 4
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_division_multi_digit(self):
      input = '144/12'
      expected = 12
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_division_with_whitespace(self):
      input = '   100   /   5  '
      expected = 20
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_division_result_fraction(self):
      input = '7/2'
      expected = 3
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_division_large_numbers(self):
      input = '100000/100'
      expected = 1000
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_division_result_zero(self):
      input = '0/999'
      expected = 0
      self.assertEqual(Interpreter(input).expr(), expected)

class TestMultipleAdditionsAndSubtractions(unittest.TestCase):
  def test_multiple_additions(self):
    input = '1+2+3+4+5'
    expected = 15
    self.assertEqual(Interpreter(input).expr(), expected)

  def test_multiple_subtractions(self):
      input = '20-3-4-5'
      expected = 8
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_mixed_addition_and_subtraction(self):
      input = '10+5-3+2-4'
      expected = 10
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_with_whitespace_arbitrary_operations(self):
      input = '  100 +   20 -  30 +  10 '
      expected = 100
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_all_zeros(self):
      input = '0+0-0+0'
      expected = 0
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_large_expression(self):
      input = '1000+2000-500+300-100+50'
      expected = 2750
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_expression_with_negatives(self):
      input = '10 - 20 + 5 - 2'
      expected = -7
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_expression_long_no_spaces(self):
      input = '1+2+3+4+5+6+7+8+9+10'
      expected = 55
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_expression_alternating_signs(self):
      input = '100 - 50 + 25 - 10 + 5 - 2'
      expected = 68
      self.assertEqual(Interpreter(input).expr(), expected)

class TestMultipleMultsAndDivs(unittest.TestCase):
  def test_multiple_multiplications(self):
      input = '2*3*4'
      expected = 24
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_multiple_divisions(self):
      input = '100/5/2'
      expected = 10  # Assuming left-to-right integer division: (100 / 5) = 20, (20 / 2) = 10
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_mixed_multiplication_and_division(self):
      input = '8*4/2'
      expected = 16  # 8*4 = 32, 32/2 = 16
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_mixed_with_whitespace(self):
      input = '  10 *  5   /  2  '
      expected = 25
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_long_expression_mul_div(self):
      input = '2*3*4/2/2'
      expected = 6  # ((2*3)=6, *4=24, /2=12, /2=6)
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_expression_result_zero(self):
      input = '0*100/5'
      expected = 0
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_expression_leading_zero_dividend(self):
      input = '0/1/1'
      expected = 0
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_division_that_truncates(self):
      input = '7/3'
      expected = 2
      self.assertEqual(Interpreter(input).expr(), expected)

  def test_large_numbers_multiplication_and_division(self):
      input = '1000*1000/100'
      expected = 10000
      self.assertEqual(Interpreter(input).expr(), expected)



if __name__ == '__main__':
  unittest.main()

