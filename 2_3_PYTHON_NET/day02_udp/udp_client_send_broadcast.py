from socket import *
from time import sleep
dest = ("192.168.12.255",8888) # 广播地址

sockfd = socket(AF_INET,SOCK_DGRAM)
# 设置套接字可以发送广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = """
    ***********
      唯快不破
    ***********
"""
while True:
    sleep(2)
    sockfd.sendto(data.encode(),dest)

# sockfd.close()
