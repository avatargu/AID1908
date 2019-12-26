from socket import *
ADDR = ("127.0.0.1",8888)

sockfd = socket(AF_INET,SOCK_DGRAM)

# sockfd的两个方法:bind,sendto,recvfrom
n = sockfd.sendto(b"hello",ADDR)
data,addr = sockfd.recvfrom(1024)
print("客户端接收:", data.decode())

sockfd.close()
