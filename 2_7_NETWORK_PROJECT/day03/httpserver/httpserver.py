"""
v3.0

从前到后：
    从浏览器接收http请求
    解析http请求
    发送请求给WebFrame
从后到前：
    从WebFrame接收反馈数据
    组织反馈数据
    发送数据给浏览器

import json
json.dumps(dict) # 从dict到json
    json.dumps({"status":"200","data":"xxx"})
    json.dumps({"method":"GET","info":"/"})
json.loads(json) # 从json到dict

httpserver --> webframe
    {"method":"GET","info":"/"}
webframe --> httpserver
    {"status":"200","data":"xxx"}
"""
from socket import *
from threading import Thread
import json,re
from config import *

# 交互webframe
def connect_frame(dict_request):
    s = socket() # 第二个套接字：httpserver作为客户端，webframe作为服务端
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return

    json_request = json.dumps(dict_request)
    s.send(json_request.encode()) # c.发送请求给WebFrame

    json_response = s.recv(4096 * 4096).decode() # d.从WebFrame接收反馈数据
    dict_response = json.loads(json_response)

    return dict_response

class HTTPServer:
    # =============================================================
    def __init__(self):
        self.host = HOST
        self.port = PORT

        self.create_socket()
        self.bind()

    # 1,创建流式套接字(socket)
    def create_socket(self):
        self.sockfd = socket() # 第一个套接字：httpserver作为服务端，浏览器作为客户端
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               DEBUG)

    # 2,绑定本机网络地址(bind)
    def bind(self):
        self.sockfd.bind((self.host,self.port))
    # =============================================================
    # -------------------------------------------------------------
    def serve_forever(self): # 启动服务

        # 3,设置监听(listen)
        self.sockfd.listen(8)
        print("Listening port %d"%self.port)

        # 死循环，流式套接字永不关闭
        while True:

            # 4,服务端等待客户端的连接请求(accept)
            print("Waiting for connection ...")
            connfd,addr = self.sockfd.accept() # 若为self.connfd，则为全局变量，导致共享资源争夺
            print("Connected from", addr)

            client = Thread(target=self.handle,
                            args=(connfd,))
            client.setDaemon(True) # 分支线程会随着主线程的退出而退出
            client.start()

    # 具体处理客户端请求
    def handle(self,connfd):

        # 5,接收消息(recv)
        request = connfd.recv(4096).decode() # a.从浏览器接收http请求，例如：GET / HTTP/1.1
        print("request:",request)

        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)" # 捕获请求类型和请求内容
        try:
            # 匹配目标字符串开始位置
            dict_request = re.match(pattern,request).groupdict() # b.解析http请求，例如：{"method": "GET", "info": "/"}
            print("dict_request:",dict_request)
        except: # 客户端断开
            # 6,关闭客户端连接套接字(close)
            connfd.close()
            return
        else:
            dict_response = connect_frame(dict_request) # 交互webframe
            print("dict_response:",dict_response)

            if dict_response:
                self.response_browser(connfd,dict_response) # 响应browser
    # -------------------------------------------------------------

    # 响应browser
    def response_browser(self,connfd,dict_response):
        # dict_response --> {"status":"200","data":"xxx"}
        if dict_response["status"] == "200":
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"

            responseBody = dict_response["data"]
        elif dict_response["status"] == "404":
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"

            responseBody = dict_response["data"]
        elif dict_response["status"] == "500":
            pass

        response = responseHeaders + responseBody # e.组织反馈数据
        print("response:",response)

        # 5,发送消息(send)
        connfd.send(response.encode()) # f.发送数据给浏览器

if __name__ == "__main__":
    httpd = HTTPServer()
    httpd.serve_forever() # 启动服务
