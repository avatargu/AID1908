"""
如何避免僵尸进程产生

使用signal模块处理子进程退出

原理：
当子进程退出时，
发送信号给父进程，
若父进程忽略子进程信号，
则系统自动处理子进程退出

方法：在父进程创建子进程前
import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

特点：
非阻塞，不影响父进程
可以处理所有子进程退出
"""
import os,sys

# 当子进程退出时，发送信号给父进程，父进程忽略子进程信号，系统自动处理子进程退出
import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN) # child ignore

pid = os.fork()

if pid < 0:
    print("创建子进程失败,返回负数：",pid)
elif pid == 0:
    print("子进程的PID:",os.getpid())
    print("父进程的PID:",os.getppid())
    sys.exit("子进程退出")
    # sys.exit(2)
    # sys.exit(4)
else:
    while True: # 父进程不退出
        pass # 子进程先于父进程退出，父进程又没有处理子进程的退出状态，子进程却没有成为僵尸进程
