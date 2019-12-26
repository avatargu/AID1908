"""
在终端运行 ps -aux
"""
"""
如何避免僵尸进程产生

方法一：使用wait函数处理子进程退出

pid,status = os.wait()
功能：
    在父进程中阻塞等待处理子进程退出
返回值：
    pid    退出子进程的pid
    status 子进程的退出状态*256
"""
import os,sys
from time import sleep

ON = 1
OFF = 0

switch_wait = ON
# switch_wait = OFF

pid = os.fork()

if pid < 0:
    print("创建子进程失败,返回负数：",pid)
elif pid == 0:
    print("====== 子进程开始 ======")

    sleep(1)

    print("子进程的PID:",os.getpid())
    print("父进程的PID:",os.getppid())

    # sys.exit("子进程退出") # 打印红色
    # sys.exit(2)
    # sys.exit(4)
    try:
        sys.exit("子进程退出") # 打印黑色
        # sys.exit(2)
        # sys.exit(4)
    except SystemExit as e:
        print(e)

    print("====== 子进程结束 ======")
else:
    if switch_wait:
        """
        Wait for completion of a child process.

        Returns a tuple of information about the child process:
            (pid, status)
        """
        pid,status = os.wait() # 阻塞函数

        print("====== 父进程开始 ======")

        """
        Wait for completion of a given child process.

        Returns a tuple of information regarding the child process:
            (pid, status)
        """
        """
        If pid is greater than 0, 
        waitpid() requests status information 
        for that specific process.
        
        If pid is 0, 
        the request is for the status of any child 
        in the process group of the current process.
        
        If pid is -1, 
        the request pertains to any child 
        of the current process.
        
        If pid is less than -1, 
        status is requested for any process 
        in the process group -pid (the absolute value of pid).
        """
        """
        os.WNOHANG
        The option for waitpid() to return immediately
        if no child process status is available immediately.
        The function returns (0, 0) in this case.
        """
        # pid,status = os.waitpid(-1,os.WNOHANG) # 阻塞函数

        print("pid:",pid)
        print("status:",status)

    # while True: # 父进程不退出
    #     pass # 子进程先于父进程退出，父进程又没有处理子进程的退出状态，子进程成为僵尸进程

    print("====== 父进程结束 ======")
