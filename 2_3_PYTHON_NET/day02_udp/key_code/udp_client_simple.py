"""
UDP套接字客户端流程（重点代码）
"""
from socket import *
ADDR = ("127.0.0.1",8888)

# 1,创建数据报套接字(socket)
sockfd = socket(AF_INET,SOCK_DGRAM)

# 2,收发消息(recvfrom/sendto)
data = input("Msg>>")
n = sockfd.sendto(data.encode(),ADDR)
print("客户端发送了%d字节" % n)
data,addr = sockfd.recvfrom(1024)
print("客户端接收数据:", data.decode())
print("客户端接收地址:", addr)

# 3,关闭数据报套接字(close)
sockfd.close()
