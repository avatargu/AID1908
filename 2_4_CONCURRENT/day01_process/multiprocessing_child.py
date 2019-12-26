import multiprocessing as mp
from time import sleep
import os

def function():
    print("子进程开始")
    sleep(1)
    print("子进程结束")

# 封装前,面向过程
pid = os.fork()
if pid == 0:
    function()
    os._exit(0)
else:
    os.wait()

# 封装后,面向对象
p = mp.Process(target = function) # 第一步：进程对象
p.start() # 第二步：启动进程
p.join() # 第三步：回收进程

# 注
#===========================================================
# 阻塞函数
# def join(self, timeout=None):
#     pass

# 阻塞函数
# def wait(*args, **kwargs): # real signature unknown
#     """
#     Wait for completion of a child process.
#
#     Returns a tuple of information about the child process:
#         (pid, status)
#     """
#     pass
#===========================================================
