import os
import types
from init import ExprNode
from tokenizer import get_token

token = ()
current_char = " "
input = None


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
    tree_list = []

    while token[0] != "NONTOKEN":
        tree_list.extend(Statement())
        MatchToken("SEMICO")
    return tree_list
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
    tree_list = []
    MatchToken("ORIGIN")
    MatchToken("IS")
    MatchToken("L_BRACKET")
    tree_list.append(Expression())
    MatchToken("COMMA")
    tree_list.append(Expression())
    MatchToken("R_BRACKET")

    return tree_list

def RotStatement():
    tree_list = []
    MatchToken("ROT")
    MatchToken("IS")
    tree_list.append(Expression())

    return tree_list


def ScaleStatement():
    tree_list = []
    MatchToken("SCALE")
    MatchToken("IS")
    MatchToken("L_BRACKET")
    tree_list.append(Expression())
    MatchToken("COMMA")
    tree_list.append(Expression())
    MatchToken("R_BRACKET")

    return tree_list


def ForStatement():
    tree_list = []
    MatchToken("FOR")
    MatchToken("T")
    MatchToken("FROM")
    tree_list.append(Expression())
    MatchToken("TO")
    tree_list.append(Expression())
    MatchToken("STEP")
    tree_list.append(Expression())
    MatchToken("DRAW")
    MatchToken("L_BRACKET")
    tree_list.append(Expression())
    MatchToken("COMMA")
    tree_list.append(Expression())
    MatchToken("R_BRACKET")

    return list_tree


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
    global token

    left = None
    if token[0] == "CONST_ID":
        token_tmp = token[0]
        MatchToken(token_tmp)
        left = ExprNode("CONST_ID", token[2])
    elif token[0] == "T":
        token_tmp = token[0]
        MatchToken(token_tmp)
        left = ExprNode("T", None)
    elif token[0] == "FUNC":
        MatchToken("FUNC")
        MatchToken("L_BRACKET")
        child = Expression()
        MatchToken("R_BRACKET")
        left = ExprNode("FUNC", token[3], child)
    elif token[0] == "L_BRACKET":
        MatchToken("L_BRACKET")
        left = Expression()
        MatchToken("R_BRACKET")
    else:
        SyntaxError(0)

    return left



def down(root, level):
    sub_level = level
    if root.__str__ == "NULL" or root.__str__ == "None" or type(root) is types.StringType or type(root) is types.NoneType or type(root) is types.FloatType:
        return
    print "\t\t\t\t"[0:level] + str(root)

    for item in root.content.values():
        down(item, sub_level+1)


def show(tree_list):
    level = 0
    for root in tree_list:
        print "\n" + "this is tree of " + str(tree_list.index(root))
        down(root,level)

def Parser(table_input):
    global input
    tree_list = []

    input = table_input
    FetchToken()
    tree_list.extend(Program())
    show(tree_list)