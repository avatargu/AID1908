"""
效率测试：
    prime sum: 34.15005373954773
"""
from prime_import import *
import time
from multiprocessing import Process

# 质数之和
list_jobs = []
time_stamp_1 = time.time()
for i in range(40):
    p = Process(target = sum_prime,args = (i * 2500 + 1,i * 2500 + 2500))
    list_jobs.append(p)
    p.start()
for item in list_jobs:
    item.join()
time_stamp_2 = time.time()

print("prime sum:",time_stamp_2 - time_stamp_1)
