import os
from init import ExprNode
from tokenizer import get_token
from drawer import GetExprValue, draw

token = ()
current_char = " "
input = None

Parameter = 'T'
Origin_x = 0.0
Origin_y = 0.0
Rot_ang = 0.0
Scale_x = 1
Scale_y = 1
Start = 0.0
End = 0.0
Step = None
x_ptr = "sin"
y_ptr = "cos"


def FetchToken():
    global token, current_char, input
    token, current_char = get_token(input, current_char)

    if token[0] != "NONTOKEN":
        while token[0] == 'ENTER':
            token, current_char = get_token(input, current_char)
    else:
        SyntaxError(1)


def MatchToken(true_token):
    global token

    if token[0] == true_token:
        FetchToken()
    else:
        SyntaxError(0)


def SyntaxError(error_num):
    if error_num == 0:
        print "Syntax Error"
        os._exit(-1)
    elif error_num == 1:
        print "NONTOKEN!!!"
        print "DONE!!!"
    else:
        return


def Program():
    global token

    while token[0] != "NONTOKEN":
        Statement()
        MatchToken("SEMICO")


def Statement():
    global token

    if token[0] == "ORIGIN":
        return OriginStatement()
    elif token[0] == "SCALE":
        return ScaleStatement()
    elif token[0] == "ROT":
        return RotStatement()
    elif token[0] == "FOR":
        return ForStatement()


def OriginStatement():
    global Origin_x, Origin_y

    MatchToken("ORIGIN")
    MatchToken("IS")
    MatchToken("L_BRACKET")
    Origin_x = GetExprValue(Expression())
    MatchToken("COMMA")
    Origin_y = GetExprValue(Expression())
    MatchToken("R_BRACKET")


def RotStatement():
    global Rot_ang

    MatchToken("ROT")
    MatchToken("IS")
    Rot_ang = GetExprValue(Expression())



def ScaleStatement():
    global Scale_x, Scale_y

    MatchToken("SCALE")
    MatchToken("IS")
    MatchToken("L_BRACKET")
    Scale_x = GetExprValue(Expression())
    MatchToken("COMMA")
    Scale_y = GetExprValue(Expression())
    MatchToken("R_BRACKET")


def ForStatement():
    global Start, End, Step, x_ptr, y_ptr
    MatchToken("FOR")
    MatchToken("T")
    MatchToken("FROM")
    Start = GetExprValue(Expression())
    MatchToken("TO")
    End = GetExprValue(Expression())
    MatchToken("STEP")
    Step = GetExprValue(Expression())
    MatchToken("DRAW")
    MatchToken("L_BRACKET")
    x_ptr = GetExprValue(Expression())
    MatchToken("COMMA")
    y_ptr = GetExprValue(Expression())
    MatchToken("R_BRACKET")
    draw()


def Expression():
    global token

    left = Term()
    while token[0] == "PLUS" or token[0] == "MINUS":
        token_tmp = token[0]
        MatchToken(token_tmp)
        right = Term()
        left = ExprNode(token_tmp, left, right)

    return left


def Term():
    global token

    left = Factor()
    while token[0] == "MUL" or token[0] == "DIV":
        token_tmp = token[0]
        MatchToken(token_tmp)
        right = Factor()
        left = ExprNode(token_tmp, left, right)

    return left


def Factor():
    global token

    if token[0] == "PLUS" or token[0] == "MINUS":
        left = ExprNode("CONST_ID", 0.0)
        token_tmp = token[0]
        MatchToken(token_tmp)
        right = Factor()
        left = ExprNode(token_tmp, left, right)
    else:
        left = Component()
    return left


def Component():
    global token

    left = Atom()
    if token[0] == "POW":
        token_tmp = token[0]
        MatchToken(token_tmp)
        right = Component()
        left = ExprNode(token_tmp, left, right)
    return left


def Atom():
    global token, Parameter

    left = None
    if token[0] == "CONST_ID":
        token_tmp = token[0]
        token_num = token[2]
        MatchToken(token_tmp)
        left = ExprNode("CONST_ID", token_num)
    elif token[0] == "T":
        token_tmp = token[0]
        MatchToken(token_tmp)
        left = ExprNode("T", Parameter)
    elif token[0] == "FUNC":
        func_name = token[3]
        MatchToken("FUNC")
        MatchToken("L_BRACKET")
        child = Expression()
        MatchToken("R_BRACKET")
        left = ExprNode("FUNC", func_name, child)
    elif token[0] == "L_BRACKET":
        MatchToken("L_BRACKET")
        left = Expression()
        MatchToken("R_BRACKET")
    else:
        SyntaxError(0)

    return left



# def down(root, level):
#     sub_level = level
#     if root.__str__ == "NULL" or root.__str__ == "None" or type(root) is types.StringType or type(root) is types.NoneType or type(root) is types.FloatType or type(root) is types.IntType:
#         return
#     print "\t\t\t\t"[0:level] + str(root) + ' ' + str(root.content.values())
#
#     for item in root.content.values():
#         down(item, sub_level+1)


# def show(tree_list):
#     level = 0
#     for root in tree_list:
#         print "\n" + "this is tree of " + str(tree_list.index(root))
#         down(root,level)
#         print GetExprValue(root)

def Parser(table_input):
    global input
    # tree_list = []

    input = table_input
    FetchToken()
    Program()

    print "END!"
    # tree_list.extend(Program())
    # show(tree_list)