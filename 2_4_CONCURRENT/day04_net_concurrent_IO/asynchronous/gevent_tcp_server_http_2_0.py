"""
v2.0

浏览器：127.0.0.1:8000

gevent：一个服务器对多个浏览器

类封装：
1. 站在用户的角度进行设计
    * 方便用户继承
    * 不能替用户决定的属性，让用户传参（或配置文件）
    * 不能替用户决定的方法，让用户重写
2. 确定功能，参数，使用方法

用户需求：
通过HTTPServer类快速搭建服务，
展示自己的网页
"""
import gevent
from gevent import monkey
monkey.patch_socket()
from socket import *

class HTTPServer:
    def __init__(self,host="0.0.0.0",port=8000,dir=None):

        # 属性 ======================================

        self.host = host
        self.port = port
        self.dir = dir

        self.address = (host,port)

        # 方法 ======================================

        # 在方法里增加属性
        self.create_socket() # 创建流式套接字

        # 在方法里设置增加的属性
        self.bind_address() # 绑定本机网络地址

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    # 绑定地址
    def bind_address(self):
        self.sockfd.bind(self.address)

    def get_html(self,connfd,info):
        if info == "/": # 请求主页：info == "/"
            filename = self.dir + "/index.html"
        else: # 请求网页：info[-5:] == ".html"
            filename = self.dir + info

        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry ...</h1>"
        else:
            # 网页存在
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += fd.read()
        finally:
            # 发送HTTP响应
            connfd.send(response.encode())

    def get_data(self,connfd,info):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Waiting for tcp_server_http_3_0</h1>"
        connfd.send(response.encode())

    def handle(self,connfd):

        # 接收HTTP请求
        request = connfd.recv(4096)
        if not request: # 排除客户端断开的情况
            connfd.close()
            return

        """
        string 
        bytes
        
        split("\n") 
        splitlines()
        """
        # 获取请求行
        request_line = request.splitlines()[0]
        # 获取请求内容
        info = request_line.decode().split(" ")[1]

        """
        getpeername() -> address info

        Return the address of the remote endpoint.  For IP sockets, the address
        info is a pair (hostaddr, port).
        """
        # connfd.getpeername()获取连接客户端的地址
        print(connfd.getpeername(),":",info)

        if info == "/" or info[-5:] == ".html":
            self.get_html(connfd,info)
        else:
            self.get_data(connfd,info)

    # 启动服务，相当于main()函数
    def server_forever(self):
        self.sockfd.listen(8) # 设置监听
        print("Listening port %d"%self.port)

        while True:
            print("Waiting for connection ...")
            connfd, addr = self.sockfd.accept()
            print("Connected from", addr)
            gevent.spawn(self.handle, connfd)

# 用户代码
if __name__ == "__main__":

    # 用户决定的属性
    HOST = "0.0.0.0"
    PORT = 8000
    DIR = "/home/tarena/static" # 用户网页存储位置

    http_server = HTTPServer(HOST,PORT,DIR)
    http_server.server_forever() # 启动服务
