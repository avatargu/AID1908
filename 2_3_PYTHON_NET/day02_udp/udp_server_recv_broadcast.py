"""
广播定义：一端发送多端接收

广播地址：每个网段的最大地址，向该地址发送数据，网段内的所有主机都能接收
"""
from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)
# 设置套接字可以接收广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

sockfd.bind(("0.0.0.0",8888))

while True:
    data,addr = sockfd.recvfrom(1024)
    print("服务端接收：", data.decode())

# sockfd.close()
