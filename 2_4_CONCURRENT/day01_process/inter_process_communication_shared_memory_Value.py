"""
IPC:
    Inter Process Communication(进程间通信)

共享内存:
    1. Value()
    2. Array()

i f c
"""
from multiprocessing import Process,Value
import time
import random

# 创建共享内存
money = Value("i",5000)

def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100,800)

p1 = Process(target = man)
p2 = Process(target = girl)
p1.start()
p2.start()
p1.join()
p2.join()

print("月余：",money.value)
