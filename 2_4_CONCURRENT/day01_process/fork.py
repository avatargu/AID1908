"""
1. Linux查看PID ： ps -aux
2. Linux查看进程树 ： pstree

子进程复制父进程的全部内存空间
"""
import os,sys
from time import sleep

# 只有父进程执行
a = 0
print("在fork之前：a =", a)

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# 创建子进程
pid = os.fork()
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

if pid < 0:
    print("创建子进程失败,返回负数：",pid)
elif pid == 0:
    print("创建子进程成功,在子进程中返回0：",pid)

    sleep(1)
    print("子进程的PID:",os.getpid())
    print("父进程的PID:",os.getppid())

    a = 1
    print("在子进程中：a=",a)
else:
    print("创建子进程成功,在父进程中返回子进程的PID：",pid)

    sleep(2)
    print("子进程的PID:",pid)
    print("父进程的PID:",os.getpid())

    a = 10
    print("在父进程中：a=", a)

# 父子进程都执行
a = 100
print("在if之后：a=", a)

# 父子进程的退出互相独立
# os._exit(0) # 退出进程
sys.exit("退出进程")

# print("unreachable")
