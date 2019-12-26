"""
粘包
"""

from socket import *
from time import sleep

sockfd = socket()

sockfd.bind(("0.0.0.0",8888))
sockfd.listen(8)
print("Waiting for connection...")
connfd,addr = sockfd.accept()
print("Connected from",addr)

# 粘包问题
# while True:
#     sleep(1)
#     data = connfd.recv(1024)
#     print(data.decode())

# 解决方法
# while True:
#     data = connfd.recv(1024)
#     print(data.decode())

connfd.close()
sockfd.close()
