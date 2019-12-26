"""
效率测试：
    multiprocess CPU: 6.703024387359619
    multiprocess IO: 5.291054964065552
"""
from test_import import *
from multiprocessing import Process
import time

# CPU密集型
# list_jobs = []
# time_stamp_1 = time.time()
# for i in range(10):
#     p = Process(target = count,args = (1,1))
#     list_jobs.append(p)
#     p.start()
# for item in list_jobs:
#     item.join()
# time_stamp_2 = time.time()
# print("multiprocess CPU:",time_stamp_2 - time_stamp_1)

# IO密集型
list_jobs = []
time_stamp_1 = time.time()
for i in range(10):
    p = Process(target = io)
    list_jobs.append(p)
    p.start()
for item in list_jobs:
    item.join()
time_stamp_2 = time.time()
print("multiprocess IO:",time_stamp_2 - time_stamp_1)
