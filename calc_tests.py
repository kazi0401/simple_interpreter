import unittest
from calc import Interpreter


class Tests(unittest.TestCase):


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
    
    



if __name__ == '__main__':
  unittest.main()

