"""
效率测试：
    multithread CPU: 14.633472681045532
    multithread IO: 8.330322980880737
"""
from test_import import *
from threading import Thread
import time

# CPU密集型
# list_jobs = []
# time_stamp_1 = time.time()
# for i in range(10):
#     t = Thread(target = count,args = (1,1))
#     list_jobs.append(t)
#     t.start()
# for item in list_jobs:
#     item.join()
# time_stamp_2 = time.time()
# print("multithread CPU:",time_stamp_2 - time_stamp_1)

# IO密集型
list_jobs = []
time_stamp_1 = time.time()
for i in range(10):
    t = Thread(target = io)
    list_jobs.append(t)
    t.start()
for item in list_jobs:
    item.join()
time_stamp_2 = time.time()
print("multithread IO:",time_stamp_2 - time_stamp_1)
