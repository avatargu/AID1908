"""
效率测试：
    single CPU: 15.356608867645264
    single IO: 15.610089302062988
"""
from test_import import *
import time

# CPU密集型
# time_stamp_1 = time.time()
# for i in range(10):
#     count(1,1)
# time_stamp_2 = time.time()
# print("single CPU:",time_stamp_2 - time_stamp_1)

# IO密集型
time_stamp_1 = time.time()
for i in range(10):
    io()
time_stamp_2 = time.time()
print("single IO:",time_stamp_2 - time_stamp_1)
