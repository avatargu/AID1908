import multiprocessing as mp
from time import sleep

def function():
    print("子进程开始")
    sleep(3)
    print("子进程结束")

p = mp.Process(target = function)
p.start()

print("join()之前的父进程开始")
sleep(1)
print("join()之前的父进程结束")

"""
join()之前的父进程join()之前执行
join()之后的父进程join()之后执行
"""
p.join()

print("join()之后的父进程开始")
sleep(1)
print("join()之后的父进程结束")

# 注
#===========================================================
# 可以使用signal模块处理子进程退出
#===========================================================
