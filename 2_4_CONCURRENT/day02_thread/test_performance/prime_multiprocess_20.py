"""
效率测试：
    prime sum: 40.59303569793701
"""
from prime_import import *
import time
from multiprocessing import Process

# 质数之和
list_jobs = []
time_stamp_1 = time.time()
for i in range(20):
    p = Process(target = sum_prime,args = (i * 5000 + 1,i * 5000 + 5000))
    list_jobs.append(p)
    p.start()
for item in list_jobs:
    item.join()
time_stamp_2 = time.time()

print("prime sum:",time_stamp_2 - time_stamp_1)
