"""
UDP套接字服务端流程（重点代码）
"""
from socket import *

# 1,创建数据报套接字(socket)
sockfd = socket(AF_INET,SOCK_DGRAM)

# 2,绑定本机网络地址(bind)
sockfd.bind(("127.0.0.1",8888)) # sockfd.bind(("0.0.0.0",8888))
# 3,收发消息(recvfrom/sendto)
data,addr = sockfd.recvfrom(1024)
print("服务端接收数据：", data.decode())
print("服务端接收地址：", addr)
n = sockfd.sendto(b"Thanks",addr)
print("服务端发送了%d字节"%n)

# 4,关闭数据报套接字(close)
sockfd.close()
