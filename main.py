# -*- coding: utf-8 -*-
from gparser import Parser
from drawer import draw
__author__ = 'Sunever Liu'

# from tokenizer import get_token

filename = "testfile.txt"
input = open(filename)
if input == 0:
    print "The file can't be opened!"

# currentChar = ' '


# print u"记号类别    字符串      常数值      函数指针"
# print "____________________________________________"

# while True:
Parser(input)
draw()
    # token, currentChar = get_token(input,currentChar)
    #
    # if token[0] != 'NONTOKEN':
    #     if token[0] != 'ENTER':
    #         print token[0],\
    #             '           '[0:(11-len(token[0]))],token[1],\
    #             '           '[0:(11-len(token[1]))],token[2],\
    #             '           '[0:(11-len(str(token[2])))],\
    #             token[3]
    # else:
    #     break

# print  "____________________________________________"

input.close()