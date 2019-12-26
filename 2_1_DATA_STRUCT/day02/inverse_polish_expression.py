"""
逆波兰表达式

1 2 + 3 - p
"""
from sstack import *

sstack = SStack()

while True:
    str_expr = input("请输入逆波兰表达式：") # "1 2 + 3 - p"
    list_tmp = str_expr.split(" ") # ['1','2','+','3','-','p']
    for item in list_tmp:
        if item not in ["+","-","*","/","p"]:
            sstack.push(float(item))
        elif item == "+":
            y = sstack.pop()
            x = sstack.pop()
            sstack.push(x + y)
        elif item == "-":
            y = sstack.pop()
            x = sstack.pop()
            sstack.push(x - y)
        elif item == "*":
            y = sstack.pop()
            x = sstack.pop()
            sstack.push(x * y)
        elif item == "/":
            y = sstack.pop()
            x = sstack.pop()
            sstack.push(x / y)
        elif item == "p":
            print(sstack.get_top())
