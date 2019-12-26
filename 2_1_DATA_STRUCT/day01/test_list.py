"""
列表
"""
from linklist import *
import time

range01 = range(999999)
list01 = list(range01)

# 列表遍历时间测试：2.9430460929870605
# tm = time.time()
# for item in list01:
#     print(item)
# print("time:",time.time() - tm)

# 列表尾插时间测试：3.337860107421875e-06
# tm = time.time()
# list01.append(20190905)
# print("time:",time.time() - tm)

# 列表头插时间测试：0.0015270709991455078
# tm = time.time()
# list01.insert(0,20190905)
# print("time:",time.time() - tm)

# 列表删除时间测试：0.0006580352783203125
tm = time.time()
list01.remove(1)
print("time:",time.time() - tm)
