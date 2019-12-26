"""
套接字属性

一切皆文件
"""
from socket import *

# TCP或UDP
sockfd = socket()

# 在绑定地址之前设置端口可以立即重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 1
print("套接字选项值：",sockfd.getsockopt(SOL_SOCKET,SO_REUSEADDR))

# AddressFamily.AF_INET
print("套接字地址类型：",sockfd.family)
# SocketKind.SOCK_STREAM
print("套接字类型：",sockfd.type)

# 3
print("获取套接字文件描述符：",sockfd.fileno())

sockfd.bind(("127.0.0.1",8888))

# ('127.0.0.1', 8888)
print("套接字绑定地址：",sockfd.getsockname())

sockfd.listen(8)

connfd,addr = sockfd.accept()

# ('127.0.0.1', 60734)
print("客户端连接套接字之连接客户端地址：",connfd.getpeername())
# ('127.0.0.1', 60734)
print("客户端连接套接字之连接客户端地址：",addr)
