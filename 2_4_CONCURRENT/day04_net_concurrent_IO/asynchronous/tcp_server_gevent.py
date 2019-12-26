"""
基于协程的TCP并发

思路：
    1. 定义对每个客户端发送消息请求的处理行为为协程函数
    2. 转换socket模块中所有的IO阻塞为可以触发gevent协程跳转的IO阻塞
"""
import gevent
from gevent import monkey
monkey.patch_socket()
from socket import *

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"OK")

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(8)

while True:
    print("Waiting for connection ...")
    c,addr = s.accept()
    print("Connected from",addr)
    # handle(c)
    gevent.spawn(handle,c)
