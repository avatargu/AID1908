"""
客户端模拟程序：
telnet 127.0.0.1 8888
"""
from socket import *
from time import ctime,sleep

# 日志文件
file_object = open("log.txt","a+")

# 创建流式套接字
sockfd = socket()
sockfd.bind(("127.0.0.1",8888))
sockfd.listen(8)

"""
通过修改IO属性，使阻塞IO变成非阻塞IO:
    sockfd.setblocking(bool)
    sockfd.settimeout(second)
"""

"""
sockfd.setblocking(True) is equivalent to sockfd.settimeout(None) 
sockfd.setblocking(False) is equivalent to sockfd.settimeout(0.0)
"""

# 方法一：设置套接字为非阻塞IO
sockfd.setblocking(False)

# 方法二：设置套接字的最长阻塞时间
# sockfd.settimeout(3)

# 三件事
while True:
    try:
        print("Waiting for connection ...")
        connfd,addr = sockfd.accept() ###### 只有sockfd调用的函数非阻塞(只设置sockfd为非阻塞IO) ######
        print("事件Ａ")
    except (BlockingIOError,timeout) as e: # 同时捕获多个异常要加括号
        sleep(1)
        file_object.write("%s : %s\n"%(ctime(),e))
        file_object.flush()
        print("事件Ｂ")
    else:
        print("Connected from",addr)
        data = connfd.recv(1024) ###### 而connfd调用的函数仍然阻塞(只设置sockfd为非阻塞IO) ######
        print("服务端接收：",data.decode())
        print("事件Ｃ")
