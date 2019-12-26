import multiprocessing as mp
from time import sleep
import os

def function01():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def function02():
    sleep(2)
    print("睡觉")
    print(os.getppid(),"--",os.getpid())

def function03():
    sleep(1)
    print("打豆豆")
    print(os.getppid(),"--",os.getpid())

list_functions = [function01,function02,function03]
list_processes = []

for function in list_functions:
    p = mp.Process(target = function)
    list_processes.append(p)
    p.start()

# 可能生成僵尸
for process in list_processes:
    process.join()

# 注
#===========================================================
# 多个子进程：
# 父进程创建子进程和回收子进程
# 子进程执行事件
#===========================================================
