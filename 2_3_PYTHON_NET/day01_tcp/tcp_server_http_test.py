"""
HTTP请求响应测试

浏览器：127.0.0.1:8000
"""
from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(("0.0.0.0",8000))
sockfd.listen(8)
print("Waiting for connection...")
connfd,addr = sockfd.accept()
print("Connected from",addr)

data = connfd.recv(4096)
print("服务端接收：",data.decode())

response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello World</h1>
"""

n = connfd.send(response.encode())
print("服务端发送了%d字节"%n)

connfd.close()
sockfd.close()
