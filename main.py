# -*- coding: utf-8 -*-
__author__ = 'Sunever Liu'

from tokenizer import get_token

filename = "testfile.txt"

input = open(filename)

currentChar = ' '

if input == 0:
    print "The file can't be opened!"

print u"记号类别    字符串      常数值      函数指针"
print "____________________________________________"

while (True):
    token, currentChar = get_token(input,currentChar)

    if (token[0] != 'ERRTOKEN'):
        print token[0],\
            '           '[0:(11-len(token[0]))],token[1],\
            '           '[0:(11-len(token[1]))],token[2],\
            '           '[0:(11-len(str(token[2])))],\
            token[3]
    else:
        break

print  "____________________________________________"

input.close()