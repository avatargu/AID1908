"""
粘包
"""

from socket import *
from time import sleep

sockfd = socket()

sockfd.connect(("127.0.0.1",8888))

# 粘包问题
# while True:
#     sleep(0.5)
#     sockfd.send(b"msg")

# 解决方法一：控制发送速度
# for i in range(10):
#     sleep(0.1)
#     sockfd.send(b"msg")

# 解决方法二：添加消息边界
# for i in range(10):
#     sockfd.send(b"msg#")

sockfd.close()
