"""
同步互斥方法:
    1. Event()
    2. Lock()

Event():
    1. e.wait()
    2. e.set()
"""
from threading import Thread
from threading import Event

global_variable = None

e = Event()

def set_global_variable():
    print("同步互斥")
    global global_variable
    global_variable = "Python"
    # e.set() # 置位
    # print("set:",e.is_set())
    # e.clear() # 复位
    # print("set:",e.is_set())

def get_global_variable():
    if global_variable == "Python":
        print("yes")
    else:
        print("no")

t = Thread(target = set_global_variable)

t.start()

# e.wait([timeout])
# 对于e.wait(3),若e.set(),则返回True
# 对于e.wait(3),若时间到,则返回False
# print("e.wait(3)",e.wait(3))
# e.wait() # 阻塞函数,等待e.set()
get_global_variable()

t.join()
