"""
基于thread的多线程网络并发模型（重点代码）

主线程负责循环连接 accept
分支线程负责循环收发 recv
"""
from socket import *
from threading import Thread
import sys

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 不能不传参，进程可以，线程不能
def handle(c):
    """
    循环处理客户端的收发请求（分支线程有分支线程的循环）
    :param c: 客户端连接套接字
    """
    # s.close()  # 分支线程不能关闭流式套接字，全局变量
    while True: # 客户端长期占有服务器
        data = c.recv(1024) # 阻塞函数（分支线程有分支线程的阻塞）
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close() # 分支线程关闭客户端连接套接字

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(ADDR)
s.listen(8)

print("Listening port 8888 ...")

while True: # 循环处理客户端的连接请求（主线程有主线程的循环）
    try:
        print("Waiting for connection ...")
        c,addr = s.accept() # 阻塞函数（主线程有主线程的阻塞）
        print("Connected from",addr)
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    # 上面连接一个客户端
    # 下面创建一个分支线程

    t = Thread(target=handle,args=(c,))

    t.setDaemon(True) # 没有join()，有setDaemon()（，分支线程随着主线程的退出而退出）

    t.start()

    # c.close() # 主线程不能关闭客户端连接套接字，全局变量

    # p.join() # 阻塞主线程，所以不能有

# s.close() # 主线程关闭流式套接字
