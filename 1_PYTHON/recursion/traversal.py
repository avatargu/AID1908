"""
    有一个多层嵌套的列表 A = [1,2,[3,4,[‘434’,[…]]]],请写一段代码遍历A中的每个元素并打印出来
"""


A = [1,2,[3,4,["434",[5,6,[7,8,"abc"]]]]]

def traversal(mylist):
    list_result = []
    for item in mylist:
        if type(item) != list:
            list_result.append(item)
        else:
            list_result.extend(traversal(item))
    return list_result

print(traversal(A))


