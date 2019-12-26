from socket import *

sockfd = socket()

# sockfd的三个方法:connect,send,recv
sockfd.connect(("127.0.0.1",8888))
n = sockfd.send(b"hello")
data = sockfd.recv(1024)
print("客户端接收:",data.decode())

sockfd.close()
