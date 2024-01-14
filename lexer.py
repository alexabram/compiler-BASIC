class Lexer:
  self.source = source + '\n' # Source code to lex as a string. Append a newline to simplify lexing/parsing the last token/statement.
  self.curChar = ''   # Current character in the string.
  self.curPos = -1    # Current position in the string.
  self.nextChar()

  def __init__(self, source):
    pass

  # Process the next character.
  def nextChar(self):
    pass

  # Return the lookahead character.
  def peek(self):
    pass

  # Invalid token found, print error message and exit.
  def abort(self, message):
    pass
  
  # Skip whitespace except newlines, which we will use to indicate the end of a statement.
  def skipWhitespace(self):
    pass
  
  # Skip comments in the code.
  def skipComment(self):
    pass

  # Return the next token.
  def getToken(self):
    pass