"""
    内存图，深浅拷贝
"""

# 引用：变量引用数据的内存地址

# list01 = [10,20,30]
# list02 = list01
# print(list01,list02)
# list01[0] = 1000
# print(list01,list02)
# list02.append("hello")
# print(list01,list02)

# list01 = [10,20,30]
# list02 = list01.copy()
# print(list01,list02)
# list01[0] = 1000
# print(list01,list02)

# ---------------------------------------------

# list01 = [10,20,[30,40]]
# list02 = list01
# print(list01,list02)
# list01[2][0] = 300
# print(list01,list02)

# list01 = [10,20,[30,40]]
# list02 = list01.copy()
# print(list01,list02)
# list01[0] = 100
# print(list01,list02)
# list01[2][0] = 300
# print(list01,list02)

import copy
# list01 = [10,20,[30,40]]
# list02 = copy.deepcopy(list01)
# print(list01,list02)
# list01[0] = 100
# print(list01,list02)
# list01[2][0] = 300
# print(list01,list02)

# ---------------------------------------------

# list01 = []
# for i in range(4):
#     list01.append([1,2,3])
# print(list01)
# list01[0][1] = 100
# print(list01)
# # compare -----------------------
# list02 = [1,2,3]
# list03 = []
# for i in range(4):
#     list03.append(list02)
# print(list03)
# list03[0][1] = 100
# print(list03)







