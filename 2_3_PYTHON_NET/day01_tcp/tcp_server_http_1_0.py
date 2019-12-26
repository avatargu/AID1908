"""
v1.0

浏览器：127.0.0.1:8000

一个服务器对一个浏览器

函数封装

HTTP：应用层协议

TCP：传输层协议

HTTP请求格式（request）：
1. 请求行（必要）：具体的请求类别和请求内容
      GET      /   HTTP/1.1
    请求类别 请求内容 协议版本

    请求类别：
        GET：获取网络资源
        POST：提交信息，得到反馈
        HEAD：只获取网络资源的响应头
        PUT：更新服务器资源
        DELETE：删除服务器资源

    请求内容：
        /：首页
2. 请求头：对请求的进一步描述
    key:value\r\n
3. 空行（必要）
4. 请求体
    请求参数或者提交内容

HTTP响应格式（response）：
1. 响应行（必要）：基本的响应情况
    HTTP/1.1  200    OK
    版本信息 响应码 附加信息

    响应码：
    200 请求成功
    404 请求失败
2. 响应头：对响应的进一步描述
    key:value\r\n
3. 空行（必要）
4. 响应体
    响应的主体内容
"""
from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(("0.0.0.0",8000))
sockfd.listen(8)

def request(connfd):
    data = connfd.recv(4096) # 接收浏览器的请求
    if not data: # 防止浏览器异常退出
        return
    request_line = data.decode().split("\n")[0]
    request_dir = request_line.split()[1]
    if request_dir == "/":
        with open("index.html") as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry...</h1>"
    connfd.send(response.encode()) # 发送响应给浏览器

while True:
    print("Waiting for connection...")
    connfd,addr = sockfd.accept()
    print("Connected from",addr)

    request(connfd)

    connfd.close()

# sockfd.close()
