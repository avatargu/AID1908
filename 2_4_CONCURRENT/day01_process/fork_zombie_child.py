"""
如何避免僵尸进程产生

方法二：创建二级子进程处理僵尸进程

父进程创建子进程
子进程创建二级子进程，子进程退出
二级子进程成为孤儿，二级子进程和原来父进程一同执行事件
"""
import os
from time import sleep

def f1():
    for i in range(3):
        sleep(1)
        print("写代码")

def f2():
    for i in range(2):
        sleep(2)
        print("测代码")

pid = os.fork()
if pid < 0:
    print("父进程创建子进程失败,返回负数：",pid)
elif pid == 0:                             # 子进程
    pid_orphan = os.fork()
    if pid_orphan < 0:
        print("子进程创建二级子进程失败,返回负数：",pid)
    elif pid_orphan == 0:                  # 二级子进程
        f1() # 二级子进程执行f1
    else:                                  # 子进程
        os._exit(0)          # 子进程退出
else:                                      # 父进程
    os.wait()                # 等待子进程退出
    f2()     # 父进程执行f2
