__author__ = 'Sunever Liu'

from init import tokenTable

def get_token(input, currentChar):
    tokenBuffer = ""

    char = currentChar
    if char == ' ':
        char = input.read(1)

        while(char < 40 or char == '\n'):
            char = input.read(1)

    tokenBuffer += char

    if char.isalpha():
        char = input.read(1)

        while (char.isalpha()):
            tokenBuffer = tokenBuffer + char
            char = input.read(1)


        for item in tokenTable:
            if tokenBuffer == item[1]:
                return item, char

    elif char.isdigit():
        char = input.read(1)

        while (char.isdigit()):
            tokenBuffer = tokenBuffer + char
            char = input.read(1)

        return ('CONST_ID', tokenBuffer, float(tokenBuffer), 'NULL'), char

    elif char == '*':
        char = input.read(1)
        if(char == '*'):
            return ('POW', '**', 0.0, 'NULL'), char
        else:
            return ('MUL', '*', 0.0, 'NULL'), char

    elif char == '/':
        char = input.read(1)
        if(char == '/'):
            input.readline()
            return ('ENTER', '', 0.0, 'NULL'), char
        else:
            return ('DIV', '/', 0.0, 'NULL'), char

    elif char == '-':
        char = input.read(1)
        if(char == '-'):
            input.readline()
            ('ENTER', '', 0.0, 'NULL'), char
        else:
            return ('MINUS', '-', 0.0, 'NULL'), char

    elif char == '+':
        char = input.read(1)
        return ('PLUS', '+', 0.0, 'NULL'), char
    elif char == ',':
        char = input.read(1)
        return ('COMMA', ',', 0.0, 'NULL'), char
    elif char == ';':
        char = input.read(1)
        return ('SEMICO', ';', 0.0, 'NULL'), char
    elif char == '(':
        char = input.read(1)
        return ('L_BRACKET', '(', 0.0, 'NULL'), char
    elif char == ')':
        char = input.read(1)
        return ('R_BRACKET', ')', 0.0, 'NULL'), char
    elif char == '\n':
        char = input.read(1)
        return ('ENTER', 'ENTER', 0.0, 'NULL'), char
    else:
        return ('ERRTOKEN', '', 0.0, 'NULL'), char