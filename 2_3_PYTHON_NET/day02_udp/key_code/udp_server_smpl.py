from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

# sockfd的三个方法:bind,recvfrom,sendto
sockfd.bind(("127.0.0.1",8888))
data,addr = sockfd.recvfrom(1024)
print("服务端接收：", data.decode())
n = sockfd.sendto(b"world",addr)

sockfd.close()
