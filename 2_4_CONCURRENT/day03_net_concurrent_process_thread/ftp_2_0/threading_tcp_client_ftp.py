"""
ftp 文件服务器(第二种方法：类封装)

功能：
1. 查看
2. 下载
3. 上传

协议：
LIST     查看文件
DOWNLOAD 下载文件
UPLOAD   上传文件
QUIT     退出

模仿三次握手

客户端单线程
"""
from socket import *
import sys
import time

# 区别于第一版
from threading import Thread

# 服务器地址
HOST = "127.0.0.1"
PORT = 8888
ADDR = (HOST,PORT)

# 区别于第一版
# 线程信号量
# 同时下载数量限制
number_limit = 0

# “非”自定义线程类
class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def handle_list(self):
        self.sockfd.send(b"LIST") # 第一次握手，发送请求

        data = self.sockfd.recv(1024).decode() # 第二次握手，接收响应

        if data == "OK":
            data = self.sockfd.recv(1024) # 第三次握手，接收内容
            print(data.decode())
        else:
            print(data)

    def handle_quit(self):
        self.sockfd.send(b"QUIT") # 唯一的一次握手，发送请求

        # 关闭唯一的套接字
        self.sockfd.close()

        # 退出唯一的进程
        sys.exit("谢谢使用") # Exit the interpreter by raising SystemExit(status).

    def handle_download(self,filename):

        # 区别于第一版
        global number_limit

        self.sockfd.send(("DOWNLOAD " + filename).encode()) # 第一次握手，发送请求

        data = self.sockfd.recv(1024).decode() # 第二次握手，接收响应

        if data == "OK":
            file_object = open(filename,"wb") # 局部变量，自动销毁
            while True:
                data = self.sockfd.recv(1024) # 第三次握手，接收内容
                if data == b"##": # 因为不能传输空
                    break
                file_object.write(data)
            file_object.close() # 可有可无
        else:
            print(data)

        # 区别于第一版
        number_limit -= 1

    def handle_upload(self,filename):
        try:
            file_object = open(filename,"rb") # 局部变量，自动销毁
        except Exception as e:
            print(e)
            print("文件不存在")
            return

        filename = filename.split("/")[-1]

        self.sockfd.send(("UPLOAD " + filename).encode()) # 第一次握手，发送请求

        data = self.sockfd.recv(1024).decode() # 第二次握手，接收响应

        if data == "OK":
            while True:
                data = file_object.read(1024)
                if not data:
                    time.sleep(0.1) # 防止粘包，结束标志b"##"和文件内容data的粘包
                    self.sockfd.send(b"##") # 因为不能传输空
                    break
                self.sockfd.send(data) # 第三次握手，发送内容
        else:
            print(data)

        file_object.close() # 可有可无

def main():

    # 区别于第一版
    global number_limit

    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    request = FTPClient(sockfd)

    while True:
        # GUI
        print("===========命令选项==========")
        print("******      list      ******")
        print("****** download  file ******")
        print("******  upload  file  ******")
        print("******      quit      ******")
        print("============================")

        cmd = input("请输入命令：")
        if cmd.strip() == "list":
            request.handle_list()
        elif cmd.strip() == "quit":
            request.handle_quit()
        elif cmd[:8] == "download":

            # 区别于第一版
            if number_limit > 4:
                print("同时下载文件数量超出限制")
                continue

            filename = cmd.strip().split(" ")[-1]

            # 区别于第一版
            t = Thread(target=request.handle_download,args=(filename,))
            t.setDaemon(True)  # 非阻塞
            t.start()
            number_limit += 1
            # t.join() # 阻塞

        elif cmd[:6] == "upload":
            filename = cmd.strip().split(" ")[-1]
            request.handle_upload(filename)
        else:
            print("请输入正确的命令")

if __name__ == "__main__":
    main()
