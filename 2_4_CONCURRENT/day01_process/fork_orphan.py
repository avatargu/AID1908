"""
需要在终端运行
"""
import os, sys
from time import sleep

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# 创建子进程
pid = os.fork()
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

if pid < 0:
    print("创建子进程失败,返回负数：", pid)
elif pid == 0:
    sleep(1)
    print("子进程的PID:", os.getpid())  # 87422
    print("父进程的PID:", os.getppid()) # 87421
else:
    # ********** 父进程先于子进程退出，子进程成为孤儿进程 **********
    print("子进程的PID:", pid)          # 87422
    print("父进程的PID:", os.getpid())  # 1787

os._exit(0) # 退出进程
