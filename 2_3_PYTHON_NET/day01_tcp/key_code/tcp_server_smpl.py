from socket import *

sockfd = socket()

# sockfd的三个方法:bind,listen,accept
sockfd.bind(("127.0.0.1",8888))
sockfd.listen(8)
connfd,addr = sockfd.accept()

# connfd的两个方法:recv,send
data = connfd.recv(1024)
print("服务端接收：",data.decode())
n = connfd.send(b"world")

connfd.close()
sockfd.close()
