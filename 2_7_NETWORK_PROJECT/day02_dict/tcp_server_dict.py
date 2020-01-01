"""
服务端
"""
from socket import *
from time import sleep

from multiprocessing import Process
import signal,sys

from database import Database

# 全局变量
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST,PORT)
db = Database(database="dict") # 1. 创建连接

# 注册处理
def handle_register(c,data):
    list_data = data.split(" ")
    name = list_data[1]
    password = list_data[2]
    
    if db.register(name,password): # 返回True表示注册成功，返回False表示注册失败
        c.send(b"SUCCESS")
    else:
        c.send(b"FAILURE")

# 登录处理
def handle_login(c,data):
    list_data = data.split(" ")
    name = list_data[1]
    password = list_data[2]
    
    if db.login(name, password): # 返回True表示登录成功，返回False表示登录失败
        c.send(b"SUCCESS")
    else:
        c.send(b"FAILURE")

# 查询单词
def handle_query(c,data):
    list_data = data.split(" ")
    name = list_data[1]
    word = list_data[2]

    db.insert_history(name,word) # 插入历史记录

    meaning = db.query(word) # 没有找到返回None，找到返回单词解释
    if not meaning:
        c.send("没有找到该单词".encode())
    else:
        msg = "%s:%s"%(word,meaning)
        c.send(msg.encode())

# 历史记录
def handle_view(c,data):
    list_data = data.split(" ")
    name = list_data[1]

    record = db.view(name)
    if not record:
        c.send(b"FAILURE")
        return
    else:
        c.send(b"SUCCESS")

    for item in record: # item --> (name,word,time)
        msg = "%s %-16s %s"%item
        sleep(0.1) # 防止粘包
        c.send(msg.encode())

    sleep(0.1) # 防止粘包
    c.send(b"##") # 发送结束标志

# 具体处理客户端请求
def handle_request(c):
    db.create_cursor() # 2. 创建游标

    # 循环接收客户端请求，分配处理函数
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(),":",data)
        
        if not data or data[0] == "E":
            db.close_cursor() # 关闭游标

            sys.exit("客户端退出") # 退出子进程
        elif data[0] == "R":
            handle_register(c,data)
        elif data[0] == "L":
            handle_login(c,data)
        elif data[0] == "Q":
            handle_query(c,data)
        elif data[0] == "V":
            handle_view(c,data)

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(8)

    """
    当子进程退出时，
    发送信号给父进程，
    若父进程忽略子进程信号，
    则系统自动处理子进程退出
    """
    signal.signal(signal.SIGCHLD,signal.SIG_IGN) # (配合daemon)

    print("Listening port 8000 ...")

    while True:
        try:
            print("Waiting for connection ...")
            c, addr = s.accept()
            print("Connected from", addr)
        except KeyboardInterrupt:
            db.close() # 关闭数据库
            s.close() # 关闭套接字

            sys.exit("服务端退出") # 退出父进程
        except Exception as e:
            print(e)
            continue

        # 一个c，一个客户端，一个子进程
        p = Process(target=handle_request,args=(c,))
        p.daemon = True # 子进程会随着父进程的退出而退出(配合signal)
        p.start()

if __name__ == "__main__":
    main()
