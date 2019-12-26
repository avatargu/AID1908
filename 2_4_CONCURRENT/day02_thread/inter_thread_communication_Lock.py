"""
同步互斥方法:
    1. Event()
    2. Lock()

Lock():
    1. l.acquire()
    2. l.release()
"""
from threading import Thread
from threading import Lock

a = b = 0

lock = Lock()

print("返回值")
print("lock.acquire()",lock.acquire())
# print("lock.acquire()",lock.acquire()) # 若已上锁则阻塞
print("lock.release()",lock.release())
print("返回值")

def value():
    while True:
        lock.acquire() # 上锁第一种方法(阻塞函数)
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release() # 解锁第一种方法

t = Thread(target=value)

t.start()

# while True:
#     with lock: # 上锁、解锁第二种方法
#         a += 1
#         b += 1

# t.join()
