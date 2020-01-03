"""
模拟网站后端应用工作流程
"""
from socket import *
from select import select
import json
from settings import *
from urls import *

# 应用类
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []

        self.host = frame_ip
        self.port = frame_port

        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               DEBUG)
        self.sockfd.bind((self.host,self.port))

    # 启动服务
    def start(self):
        self.sockfd.listen(8)
        print("Listening port %d"%self.port)        

        self.rlist.append(self.sockfd)
        
        while True:
            rs,ws,xs = select(self.rlist,
                              self.wlist,
                              self.xlist)

            for r in rs:
                if r is self.sockfd: # sockfd
                    print("Waiting for connection ...")
                    connfd,addr = r.accept()
                    print("Connected from", addr)
                                       
                    self.rlist.append(connfd) # 关注新的IO事件
                else: # connfd
                    self.handle(r)
                    
                    self.rlist.remove(r) # 已经关闭，取消关注

    # 具体处理httpserver请求
    def handle(self,connfd):
        json_request = connfd.recv(1024).decode()
        dict_request = json.loads(json_request)
        
        if dict_request["method"] == "GET":
            if dict_request["info"] == "/" or dict_request["info"][-5:] == ".html":
                dict_response = self.get_html(dict_request["info"])
            else:
                dict_response = self.get_data(dict_request["info"])
        elif dict_request["method"] == "POST":
            pass
        
        json_response = json.dumps(dict_response)
        connfd.send(json_response.encode())
        
        connfd.close() # 关闭套接字

    # 处理网页
    def get_html(self,info):
        if info == "/":
            filename = STATIC_DIR+"/index.html"
        else:
            filename = STATIC_DIR+info

        try:
            fd = open(filename)
        except Exception as e:
            print(e)
            fd = open(STATIC_DIR+"/404.html")
            return {"status":"404","data":fd.read()}
        else:
            return {"status":"200","data":fd.read()}

    # 处理数据
    def get_data(self,info):
        for url,func in urls:
            if url == info:
                return {"status":"200","data":func()}

        return {"status":"404","data":"Sorry ..."}

if __name__ == "__main__":
    app = Application()
    app.start() # 启动服务（serve_forever, start or run）
