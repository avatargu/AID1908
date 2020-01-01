"""
Exit the interpreter by raising SystemExit(status).
If the status is omitted or None, it defaults to zero (i.e., success).
If the status is an integer, it will be used as the system exit status.
If it is another kind of object, it will be printed and the system
exit status will be one (i.e., failure).
"""
import os
from time import sleep
import sys

a = 0
print("在fork之前：a =", a)

pid = os.fork()

if pid < 0:
    print("创建子进程失败")
elif pid == 0:
    sleep(1)
    a = 1
    print("在子进程中：a=",a)
else:
    sleep(2)
    a = 10
    print("在父进程中：a=", a)

a = 100
print("在if之后：a=", a)

# 父子进程的退出互相独立
sys.exit("退出进程")

# print("unreachable")
