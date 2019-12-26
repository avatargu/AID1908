"""
链表
"""
from linklist import *
import time

range01 = range(999999)
link01 = LinkList()
link01.init_list(range01)

# 链表遍历时间测试：3.170316696166992
# tm = time.time()
# link01.show()
# print("time:",time.time() - tm)

# 链表尾插时间测试：0.047974348068237305
# tm = time.time()
# link01.append(20190905)
# print("time:",time.time() - tm)

# 链表头插时间测试：7.3909759521484375e-06
# tm = time.time()
# link01.head_insert(20190905)
# print("time:",time.time() - tm)

# 链表删除时间测试：8.106231689453125e-06
tm = time.time()
link01.remove(1)
print("time:",time.time() - tm)
