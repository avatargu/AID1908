"""
在一段文字中，有()[]{}，编写一个接口程序，判断括号是否匹配正确
"""
from lstack import *

parens = "()[]{}"        # 目标字符集
left_parens = "([{"      # 入栈字符集
# right_parens = ")]}"

opposite = {"}":"{", "]":"[", ")":"("}

# 存储括号的栈
ls = LStack()

# 生成器，遍历字符串，提供括号及位置
def generate_parens(text):
    index,len_text = 0,len(text)

    # 双 while 循环
    while True:
        while index < len_text and text[index] not in parens: # 两个条件：只有当第一个条件为真时，第二个条件才不报错
            index += 1

        if index >= len_text:                                 # 第一个条件
            return
        else:                                                 # 第二个条件
            yield text[index],index # 生成器
            index += 1

# 功能函数，判断提供的括号是否匹配
def verify():
    for paren,index in generate_parens(text):
        if paren in left_parens:                              # 左括号入栈
            ls.push((paren,index))
        elif ls.is_empty() or ls.pop()[0] != opposite[paren]: # 右括号匹配
            print("Unmatching is found at %d for %s" % (index,paren))
            break
    else:
        if ls.is_empty():
            print("All parentheses are matched")
        else:
            remaining = ls.pop()
            print("Unmatching is found at %d for %s" % (remaining[1],remaining[0]))

if __name__ == "__main__":
    text = "Python is an easy to learn, (powerful programming language.) It has efficient high-level data structures( and a simple but effective {approach to} object-oriented programming). Python’s {elegant [syntax and] dynamic} typing, [together with its interpreted nature,] make it an ideal {language [for (scripting) and] rapid} application development in many areas on {most} platforms."

    # 遍历生成器
    for i, j in generate_parens(text):
        print(i, j)

    verify()
