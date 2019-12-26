"""
TCP套接字客户端流程（重点代码）
"""
from socket import *

# 1,创建流式套接字(socket)
sockfd = socket()

# 4,客户端请求连接服务端的网络地址(connect)
sockfd.connect(("127.0.0.1",8888))
# 5,收发消息(recv/send)
data = input("Msg>>")
n = sockfd.send(data.encode())
print("客户端发送了%d字节"%n)
data = sockfd.recv(1024)
print("客户端接收:",data.decode())

# 6,关闭流式套接字(close)
sockfd.close()
