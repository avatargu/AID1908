"""
多个分支线程：
1. 主线程创建分支线程和回收分支线程
2. 分支线程执行事件
"""
from threading import Thread
from time import sleep

def function(second,name):
    print("%s开始执行"%name)
    sleep(second)
    print("%s执行完毕"%name)

list_threads = []

for i in range(5):
    t = Thread(target=function,args=(2,),kwargs={"name":"T%d"%i})
    list_threads.append(t)
    t.start()

for item in list_threads:
    item.join()
