
from enum import Enum

class TokenType(Enum):
  INTEGER = 'INTEGER'
  PLUS = 'PLUS'
  MINUS = 'MINUS'
  EOF = 'EOF'


class Token:
  def __init__(self, type: TokenType, value):
    self.type = type
    self.value = value

class Calculator:


  def __init__(self, text: str):
    self.text = text 


  def tokenize(self):
    pass


  def parse(self):
    pass 


  def interpret(self):
    pass 



  def expr(self):
    # tokenize the text
    # parse the tokens
    # interpret the result


    # We expect an integer (a term) then
    # any number of operator-term pairs. 
    pass 

