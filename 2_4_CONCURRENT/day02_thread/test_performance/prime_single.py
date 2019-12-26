"""
效率测试：
    prime sum: 152.7247612476349
"""
from prime_import import *
import time

# 质数之和
time_stamp_1 = time.time()
sum_prime(1,100000)
time_stamp_2 = time.time()

print("prime sum:",time_stamp_2 - time_stamp_1)
