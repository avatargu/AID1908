"""
基于fork的多进程网络并发模型（重点代码）

父进程负责循环连接 accept
子进程负责循环收发 recv

The C10K problem
"""
from socket import *
import os
import signal

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 可以不传参，进程可以，线程不能
def handle(c):
    """
    循环处理客户端的收发请求（子进程有子进程的循环）
    :param c: 客户端连接套接字
    """
    s.close()  # 子进程关闭流式套接字　
    while True: # 客户端长期占有服务器
        data = c.recv(1024) # 阻塞函数（子进程有子进程的阻塞）
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close() # 子进程关闭客户端连接套接字

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(ADDR)
s.listen(8)

"""
原理：
当子进程退出时，
发送信号给父进程，
若父进程忽略子进程信号，
则系统自动处理子进程退出
"""
signal.signal(signal.SIGCHLD,signal.SIG_IGN) # 避免僵尸进程产生

print("Listening port 8888 ...")

while True: # 循环处理客户端的连接请求（父进程有父进程的循环）
    try:
        print("Waiting for connection ...")
        c,addr = s.accept() # 阻塞函数（父进程有父进程的阻塞）
        print("Connected from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 上面连接一个客户端
    # 下面创建一个子进程

    pid = os.fork()
    if pid == 0: # 子进程　　　　
        handle(c) # 循环处理客户端的收发请求（子进程有子进程的循环）
        os._exit(0) # 及时销毁子进程，防止子进程进入父进程的循环
    else: # pid < 0 or pid > 0　
        c.close() # 父进程关闭客户端连接套接字

# s.close() # 父进程关闭流式套接字
