from socket import *
ADDR = ("127.0.0.1",8888)
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("Word>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)

    data,addr = sockfd.recvfrom(1024)
    print("客户端接收数据:", data.decode())

sockfd.close()
