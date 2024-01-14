class Lexer:
    def __init__(self, source):
        self.source = (
            source + "\n"
        )  # Source code to lex as a string. Append a newline to simplify lexing/parsing the last token/statement.
        self.curChar = ""  # Current character in the string.
        self.curPos = -1  # Current position in the string.
        self.nextChar()

    # Process the next character.
    def nextChar(self):
        self.curPos += 1
        self.curChar = (
            "\0" if self.curPos >= len(self.source) else self.source[self.curPos]
        )

    # Return the lookahead character.
    def peek(self):
        return (
            "\0"
            if self.curPos + 1 >= len(self.source)
            else self.source[self.curPos + 1]
        )

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
        # Check the first character of this token to see if we can decide what it is.
        # If it is a multiple character operator (e.g., !=), number, identifier, or keyword then we will process the rest.
        if self.curChar == "+":
            pass  # Plus token.
        elif self.curChar == "-":
            pass  # Minus token.
        elif self.curChar == "*":
            pass  # Asterisk token.
        elif self.curChar == "/":
            pass  # Slash token.
        elif self.curChar == "\n":
            pass  # Newline token.
        elif self.curChar == "\0":
            pass  # EOF token.
        else:
            # Unknown token!
            pass

        self.nextChar()
