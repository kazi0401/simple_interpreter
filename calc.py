from enum import Enum

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

class TokenType(Enum):
   INTEGER = 'INTEGER'
   PLUS = 'PLUS'
   MINUS = 'MINUS'
   EOF = 'EOF'



class Token(object):
  def __init__(self, type: TokenType, value):
    self.type = type
    # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
    self.value = value

  def __str__(self):
    """String representation of the class instance.

    Examples:
      Token(INTEGER, 3)
      Token(PLUS '+')
    """

    return f'Token({self.type}, {self.value})'
  

  def __repr__(self):
    return self.__str__()


class Interpreter(object):
  def __init__(self, text):
    # client string input, e.g. "3+5"
    self.text = text
    # self.pos is an index into self.text
    self.pos = 0
    # current token instance
    self.current_token = None
    self.current_char = self.text[self.pos]

  def error(self):
    raise Exception('Error parsing input')
  
  def advance(self):
      """Advance the 'pos' pointer and set the 'current_char' variable."""
      self.pos += 1
      if self.pos > len(self.text) - 1:
          self.current_char = None  # Indicates end of input
      else:
          self.current_char = self.text[self.pos]

  def integer(self):
     result = ''

     while self.current_char is not None and self.current_char.isdigit():
        result += self.current_char
        self.advance() 
    
     return int(result)

  def skip_white_space(self):
     while self.current_char is not None and self.current_char.isspace():
        self.advance()

  def get_next_token(self):
      """Lexical analyzer (also known as scanner or tokenizer)

      This method is responsible for breaking a sentence
      apart into tokens. One token at a time.
      """

      # if the character is a digit then convert it to
      # integer, create an INTEGER token, increment self.pos
      # index to point to the next character after the digit,
      # and return the INTEGER token
      if self.current_char == None:
         return Token(TokenType.EOF, None)

      if self.current_char == ' ':
         self.skip_white_space()
         return self.get_next_token()
      
      if self.current_char.isdigit():
          return Token(TokenType.INTEGER, self.integer())
        

      if self.current_char == '+':
          self.advance()
          return Token(TokenType.PLUS, self.current_char)
      
      if self.current_char == '-':
         self.advance()
         return Token(TokenType.MINUS, self.current_char)
      


      self.error()

  def eat(self, token_type):
      # compare the current token type with the passed token
      # type and if they match then "eat" the current token
      # and assign the next token to the self.current_token,
      # otherwise raise an exception.
      if self.current_token.type == token_type:
          self.current_token = self.get_next_token()
      else:
          self.error()


  def expr(self):
      """expr -> INTEGER PLUS INTEGER"""
      # set current token to the first token taken from the input

      self.current_token = self.get_next_token()

      # we expect the current token to be an integer
      left = self.current_token
      self.eat(TokenType.INTEGER)

      # we expect the current token to be a '+' token
      op = self.current_token
      match op.type:
         case TokenType.PLUS: 
            self.eat(TokenType.PLUS)
         case TokenType.MINUS:
            self.eat(TokenType.MINUS)

      # we expect the current token to be an integer
      right = self.current_token
      self.eat(TokenType.INTEGER)

      match op.type:
         case TokenType.PLUS:
            return left.value + right.value 
         case TokenType.MINUS:
            return left.value - right.value


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        if text == 'q': break
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


def test(): 
   interpreter = Interpreter('23 + 21')
   print(interpreter.expr())


if __name__ == '__main__':
    test()