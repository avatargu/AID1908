"""
IPC:
    Inter Process Communication(进程间通信)

信号量:
    1. 信号量减一 s.acquire()
    2. 信号量增一 s.release()
"""
from multiprocessing import Process,Semaphore
from time import sleep
import os

# 创建信号量（最多允许num个任务同时执行）
sem = Semaphore(3)

# 任务函数
def handle():
    sem.acquire() # 信号量减一,若为零，则阻塞
    print("减一之后：",sem.get_value())
    print("%s执行任务开始"%os.getpid())

    sleep(2)

    print("%s执行任务结束"%os.getpid())
    sem.release() # 信号量加一
    print("加一之后：",sem.get_value())

# n个任务需要执行
for i in range(6):
    p = Process(target=handle)
    p.start()
    # p.join()
