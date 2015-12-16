from math import sin,cos,pow
from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, sin, tan, log, sqrt, exp
import gparser

__author__ = 'Sunever Liu'

fig = plt.figure(figsize=(10,10), facecolor='gray')
ax = fig.add_axes([0,0,1,1], frameon=True, aspect=1)
plt.xlim(0,1000)
plt.ylim(0,1000)

def GetExprValue(root):
    if root is None:
        return 0.0
    if root.opCode == "PLUS":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '+' + str(right) + ')'
        return left + right
    elif root.opCode == "MINUS":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '-' + str(right) + ')'

        return left - right
    elif root.opCode == "MUL":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '*' + str(right) + ')'
        return left * right
    elif root.opCode == "DIV":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '/' + str(right) + ')'

        if right == 0:
            return left
        else:
            return left / right
    elif root.opCode == "POW":
        left = GetExprValue(root.content["Left"])
        right = GetExprValue(root.content["Right"])

        if isinstance(left, str) or isinstance(right, str):
            return '(' + str(left) + '**' + str(right) + ')'

        return pow(int(left), right)
    elif root.opCode == "FUNC":
        if root.content["Child"].opCode == "T":
            return root.content["MathFuncPtr"] + "(T)"

        child = GetExprValue(root.content["Child"])

        if isinstance(child, str):
            return root.content["MathFuncPtr"] + child


        temp = 0
        exec("temp = " + str(root.content["MathFuncPtr"]) + '(' + str(GetExprValue(root.content["Child"])) + ')')
        return temp

    elif root.opCode == "CONST_ID":
        return root.content["CaseConst"]

    elif root.opCode == "T":
        return "T"


def draw():
    seq = np.arange(gparser.Start, gparser.End, gparser.Step)

    x_new = gparser.x_ptr
    y_new = gparser.y_ptr

    # x_new = x_new.strip('(')
    # if x_new[0] == '0':
    #     x_new = x_new[0:-1]
    #
    # y_new = y_new.strip('(')
    # if y_new[0] == '0':
    #     y_new = y_new[0:-1]

    print x_new
    print y_new

    # if x_new == 'T':
    #     x_new = seq
    # elif x_new[0] == '0':
    if isinstance(x_new, str):
        if x_new == 'T':
            x_new = 'seq'
        else:
            while x_new.find('T') > 0:
                x_new = x_new[0:x_new.find('T')] + 'seq' + x_new[x_new.find('T')+1:]
        exec("x_new = " + x_new)
    else:
        temp = x_new
        x_new = []
        for index in range(len(seq)):
            x_new.append(temp)


    if isinstance(y_new, str):
        if y_new == 'T':
            y_new = 'seq'
        else:
            while y_new.find('T') > 0:
                y_new = y_new[0:y_new.find('T')] + 'seq' + y_new[y_new.find('T')+1:]
        exec("y_new = " + y_new)
    else:
        temp = y_new
        y_new = []
        for index in range(len(seq)):
            y_new.append(temp)
    # elif isinstance(x_new, str):
    #     x_new = x_new[0:x_new.find('T')] + 'seq' + x_new[x_new.find('T')+1:]
    #     exec("x_new = " + x_new)
    # else:
    #     for index in range(len(seq)):
    #         seq[index] = int(x_new)
    #     x_new = seq



    # if y_new == 'T':
    #     y_new = seq
    # elif y_new[0] == '0':
    #     if y_new[-1] == 'T' and len(y_new) < 9:
    #         exec("y_new = " + '-' + 'seq')
    #     else:
    #         y_new = y_new[0:y_new.find('T')] + 'seq' + y_new[y_new.find('T')+1:]
    #         exec("y_new = " + y_new[4:])
    # elif isinstance(y_new, str):
    #     y_new = y_new[0:y_new.find('T')] + 'seq' + y_new[y_new.find('T')+1:]
    #     exec("y_new = " + y_new)
    # else:
    #     for index in range(len(seq)):
    #         seq[index] = int(y_new)
    #     y_new = seq


    print x_new, y_new

    for index in range(len(seq)):
        x_new[index] = x_new[index] * gparser.Scale_x
        y_new[index] = y_new[index] * gparser.Scale_y
        temp = x_new[index] * cos(gparser.Rot_ang) + y_new[index] * sin(gparser.Rot_ang)
        y_new[index] = y_new[index] * cos(gparser.Rot_ang) - x_new[index] * sin(gparser.Rot_ang)
        x_new[index] = temp
        x_new[index] = x_new[index] + gparser.Origin_x
        y_new[index] = y_new[index] + gparser.Origin_y



    print len(x_new), len(y_new)

    ax.plot(x_new, y_new)

    ax.set_xticks([])
    ax.set_yticks([])


def show():
    plt.show()