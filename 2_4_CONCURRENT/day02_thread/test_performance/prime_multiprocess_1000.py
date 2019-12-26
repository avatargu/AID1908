"""
效率测试：
    prime sum: 32.49749279022217
"""
from prime_import import *
import time
from multiprocessing import Process

# 质数之和
list_jobs = []
time_stamp_1 = time.time()
for i in range(1000):
    p = Process(target = sum_prime,args = (i * 100 + 1,i * 100 + 100))
    list_jobs.append(p)
    p.start()
for item in list_jobs:
    item.join()
time_stamp_2 = time.time()

print("prime sum:",time_stamp_2 - time_stamp_1)
