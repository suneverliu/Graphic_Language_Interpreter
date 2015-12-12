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
        return GetExprValue(root.content["Left"]) + GetExprValue(root.content["Right"])
    elif root.opCode == "MINUS":
        return GetExprValue(root.content["Left"]) - GetExprValue(root.content["Right"])
    elif root.opCode == "MUL":
        return GetExprValue(root.content["Left"]) * GetExprValue(root.content["Right"])
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
    ax = fig.add_axes([0,0,0.5,0.5], frameon=False, aspect=1)

    x_seq = np.arange(gparser.Start, gparser.End, gparser.Step)
    y_seq = np.arange(gparser.Start, gparser.End, gparser.Step)

    x_new = gparser.x_ptr
    y_new = gparser.y_ptr

    if x_new in ["cos", "sin", "tan", "log", "sqrt", "exp"]:
        exec("x_new = " + gparser.x_ptr + '(' + 'x_seq' + ')')
    elif x_new == 'T':
        x_new = x_seq
    else:
        for index in range(len(x_seq)):
            x_seq[index] = int(x_new)
        x_new = x_seq
    if y_new in ["cos", "sin", "tan", "log", "sqrt", "exp"]:
        exec("y_new = " + gparser.y_ptr + '(' + 'y_seq' + ')')
    elif y_new == 'T':
        y_new = y_seq
    else:
        for index in range(len(y_seq)):
            y_seq[index] = int(y_new)
        y_new = y_seq

    for index in range(len(x_new)):
        x_new[index] = (x_new[index] * gparser.Scale_x + gparser.Origin_x) / 100.0

    print x_new

    for index in range(len(y_new)):
        y_new[index] = (y_new[index] * gparser.Scale_y + gparser.Origin_y) / 100.0

    print y_new

    ax.plot(x_new, y_new)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()