__author__ = 'Sunever Liu'

tokenTable = (
    ( 'CONST_ID', "PI", 3.1415926, 'NULL' ),
    ( 'CONST_ID', "E", 2.71828, 'NULL' ),
    ( 'T', "T", 0.0, 'NULL' ),
    ( 'FUNC', "SIN", 0.0, 'sin' ),
    ( 'FUNC', "COS", 0.0, 'cos' ),
    ( 'FUNC', "TAN", 0.0, 'tan' ),
    ( 'FUNC', "LN", 0.0, 'log' ),
    ( 'FUNC', "EXP", 0.0, 'exp' ),
    ( 'FUNC', "SQRT", 0.0, 'sqrt' ),
    ( 'ORIGIN', "ORIGIN", 0.0, 'NULL' ),
    ( 'SCALE', "SCALE", 0.0, 'NULL' ),
    ( 'ROT', "ROT", 0.0, 'NULL' ),
    ( 'IS', "IS", 0.0, 'NULL' ),
    ( 'FOR', "FOR", 0.0, 'NULL' ),
    ( 'FROM', "FROM", 0.0, 'NULL' ),
    ( 'TO', "TO", 0.0, 'NULL' ),
    ( 'STEP', "STEP", 0.0, 'NULL' ),
    ( 'DRAW', "DRAW", 0.0, 'NULL' )
)

class ExprNode(object):

    def __init__(self, opCode, *content):
        self.opCode = opCode

        if opCode == "CONST_ID":
            self.content = {"CaseConst":content[0]}
        elif opCode == "T":
            self.content = {"CaseParmPtr":content[0]}
        elif opCode == "FUNC":
            self.content = {"MathFuncPtr": content[0],"Child": content[1]}
        else:
            self.content = {"Left":content[0],"Right":content[1]}

    def __str__(self):
        return self.opCode