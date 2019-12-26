"""
两个线程
一个打印 1-52
另一个打印 A-Z
要求打印顺序是 12A34B...5152Z
"""
from threading import Thread,Lock

lock_1 = Lock()
lock_2 = Lock()

# 打印数字
def print_num():
    for i in range(1,52,2):
        lock_1.acquire()
        print(i)
        print(i+1)
        lock_2.release()

# 打印字母
def print_chr():
    for i in range(65,91):
        lock_2.acquire()
        print(chr(i))
        lock_1.release()

thread_1 = Thread(target=print_num)
thread_2 = Thread(target=print_chr)

# 先打印数字
lock_2.acquire()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
