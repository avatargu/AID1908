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

服务器多线程
"""
from socket import *
import os,sys
import time
from threading import Thread

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 文件目录
FTP = "/home/tarena/FTP/"

# 自定义线程类
class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def handle_list(self):
        # 获取文件列表
        list_files = os.listdir(FTP)

        # 第二次握手，发送响应
        if not list_files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1) # 防止粘包，第二次握手的b"OK"和第三次握手的str_files.encode()的粘包

        # 获取文件字符串
        str_files = ""
        for file in list_files:
            if file[0] != "." and os.path.isfile(FTP+file): # 排除隐藏文件和文件夹
                str_files += file + "\n"

        # 第三次握手，发送内容
        self.connfd.send(str_files.encode())

    def handle_download(self,filename):
        # 第二次握手，发送响应
        try:
            file_object = open(FTP + filename,"rb") # 局部变量，自动销毁
        except Exception as e: # 打开失败，文件不存在
            print(e)
            self.connfd.send("文件不存在".encode())
            return
        else: # 打开成功，文件存在
            self.connfd.send(b"OK")
            time.sleep(0.1) # 防止粘包，第二次握手的b"OK"和第三次握手的data的粘包

        # 没有return，说明打开成功，文件存在

        # 第三次握手，发送内容
        while True:
            data = file_object.read(1024)
            if not data:
                time.sleep(0.1) # 防止粘包，结束标志b"##"和文件内容data的粘包
                self.connfd.send(b"##") # 因为不能传输空
                break
            self.connfd.send(data)

        file_object.close() # 可有可无

    def handle_upload(self,filename):
        # 第二次握手，发送响应
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b"OK")

        # 第三次握手，接收内容
        file_object = open(FTP + filename,"wb") # 局部变量，自动销毁
        while True:
            data = self.connfd.recv(1024)
            if data == b"##": # 因为不能传输空
                break
            file_object.write(data)
        file_object.close() # 可有可无

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode() # 第一次握手，接收请求

            # 本来应该是handle_quit，此处却不能封装，因为要跳出while循环
            if not data or data == "QUIT":# 有两种退出方式：一种是"Ctrl+C"，另一种是"QUIT"

                # 关闭套接字
                self.connfd.close()

                # 退出线程
                return # 其实是join()实现的

            if data == "LIST":
                self.handle_list()
            elif data[:8] == "DOWNLOAD":
                filename = data.split(" ")[-1]
                self.handle_download(filename)
            elif data[:6] == "UPLOAD":
                filename = data.split(" ")[-1]
                self.handle_upload(filename)

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(8)

    print("Listening port 8888 ...")

    while True:
        # 循环创建客户端连接套接字
        try:
            print("Waiting for connection ...")
            connfd, addr = sockfd.accept()
            print("Connected from", addr)
        except KeyboardInterrupt:
            sys.exit("退出服务器") # 退出唯一的进程
        except Exception as e:
            print(e)
            continue

        # 循环创建分支线程
        response = FTPServer(connfd)
        response.setDaemon(True) # 非阻塞
        response.start()
        # response.join() # 阻塞

if __name__ == "__main__":
    main()
