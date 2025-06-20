
from enum import Enum

class TokenType(Enum):
  INTEGER = 'INTEGER'
  PLUS = 'PLUS'
  MINUS = 'MINUS'
  MULT = 'MULT'
  DIV = 'DIV'

  @classmethod
  def operators(cls):
    return {TokenType.PLUS, TokenType.MINUS, TokenType.MULT, TokenType.DIV}

class Token:
  def __init__(self, type: TokenType, value):
    self.type = type
    self.value = value
  
  def __repr__(self):
    return f'Token({self.type}, {self.value})'

class Interpreter:


  def __init__(self, text: str):
    self.text = text 

  def error(self):
    raise Exception('Error parsing input') 
  
  def tokenize_integer(self, pos: int):
    # Concatenates all digits following the given position, 
    # and returns the position it last left off, with the integer value it found.

    result = ''

    for pos in range(pos, len(self.text)):
      if self.text[pos].isdigit():
        result += self.text[pos]
      else: break

    return pos, int(result) 
    
  def tokenizer(self):
    position = 0

    while position < len(self.text):
      # If it's not a digit or an operator, we just keep iterating
      # Implicitly skips white spaces

      if self.text[position].isdigit():
        position, integer = self.tokenize_integer(position)
        yield Token(TokenType.INTEGER, integer)
      if self.text[position] == '+':
        yield Token(TokenType.PLUS, '+')
      
      position += 1

  def expect(self, token: Token, *expected_types: TokenType) -> bool:

    # if any expected types match, then we're good!
    for expected_type in expected_types:
      if expected_type == token.type:
        return True
      
    # if none of them match, raise an error
    self.error()
    return False
  
  def calculate(self, left: Token, operator: Token, right: Token) -> Token:

    match operator.type:
      case TokenType.PLUS:
        result = left.value + right.value 
      case TokenType.MINUS:
        result = left.value - right.value 
      case TokenType.MULT:
        result = left.value * right.value 
      case TokenType.DIV:
        result = left.value / right.value
    
    return Token(TokenType.INTEGER, result)
  
  def expr(self):
      
    tokens = list(self.tokenizer())

    left = tokens[0]
    self.expect(left, TokenType.INTEGER)

    i = 1
    while i < len(tokens) - 1:
      operator = tokens[i]
      self.expect(operator, *TokenType.operators())
      i += 1

      right = tokens[i]
      self.expect(right, TokenType.INTEGER)
      i += 1

      result = left = self.calculate(left, operator, right)
    
    return result.value

    



if __name__ == '__main__':
  c = Interpreter('   12+11    ').expr()
  print(c)
