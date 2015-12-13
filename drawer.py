from math import sin,cos,pow
from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, sin, tan, log, sqrt, exp
import gparser

__author__ = 'Sunever Liu'


def GetExprValue(root):
    if root is None:
        return 0.0
    if root.opCode == "PLUS":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        # if isinstance(left, str) or isinstance(right, str):
        #     return left + '+' + right
        return left + right
    elif root.opCode == "MINUS":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        if isinstance(left, str) or isinstance(right, str):
            return str(left) + '-' + str(right)
        return left - right
    elif root.opCode == "MUL":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        # if isinstance(left, str) or isinstance(right, str):
        #     return str(left) + '*' + str(right)
        return left * right
    elif root.opCode == "DIV":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])
        if right == 0:
            return left
        else:
            return left / right
    elif root.opCode == "POW":
        return pow(int(GetExprValue(root.content["Left"])), GetExprValue(root.content["Right"]))
    elif root.opCode == "FUNC":
        if root.content["Child"].opCode == "T":
            return root.content["MathFuncPtr"]
        temp = 0
        exec("temp = " + str(root.content["MathFuncPtr"]) + '(' + str(GetExprValue(root.content["Child"])) + ')')
        return temp
    elif root.opCode == "CONST_ID":
        return root.content["CaseConst"]
    elif root.opCode == "T":
        if root.content["CaseParmPtr"] is None:
            return 1
        return root.content["CaseParmPtr"]
    else:
        return 0.0


def draw():
    fig = plt.figure(figsize=(10,10), facecolor='gray')
    ax = fig.add_axes([0,0,1,1], frameon=True, aspect=1)
    plt.xlim(0,1000)
    plt.ylim(0,1000)

    seq = np.arange(gparser.Start, gparser.End, gparser.Step)

    x_new = gparser.x_ptr
    y_new = gparser.y_ptr

    print x_new
    print y_new

    if x_new == 'T':
        x_new = seq
    elif x_new[0] == '0':
        if x_new[-1] == 'T':
            exec("x_new = " + '-' + 'seq')
        else:
            exec("x_new = " + '-' + gparser.x_ptr[4:] + '(' + 'seq' + ')')
    elif isinstance(x_new, str):
        exec("x_new = " + gparser.x_ptr + '(' + 'seq' + ')')
    else:
        for index in range(len(seq)):
            seq[index] = int(x_new)
        x_new = seq



    if y_new == 'T':
        y_new = seq
    elif y_new[0] == '0':
        if y_new[-1] == 'T':
            exec("y_new = " + '-' + 'seq')
        else:
            exec("y_new = " + '-' + gparser.y_ptr[4:] + '(' + 'seq' + ')')
    elif isinstance(y_new, str):
        exec("y_new = " + gparser.y_ptr+ '(' + 'seq' + ')')
    else:
        for index in range(len(seq)):
            seq[index] = int(y_new)
        y_new = seq


    print x_new, y_new

    for index in range(len(x_new)):
        x_new[index] = (x_new[index] * gparser.Scale_x + gparser.Origin_x)


    for index in range(len(y_new)):
        y_new[index] = (y_new[index] * gparser.Scale_y + gparser.Origin_y)


    print x_new, y_new

    ax.plot(x_new, y_new)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()