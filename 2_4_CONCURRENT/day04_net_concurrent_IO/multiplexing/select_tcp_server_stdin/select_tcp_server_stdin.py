from socket import *
from select import select
import sys
import time

# 打开日志文件
f = open('server.log','a')

# 创建监听套接字，作为监控IO
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(8)

# 监控"监听套接字对象"和"标准输入对象"
rlist = [sockfd,sys.stdin] # 只能监控标准输入对象，不能监控input()方法
wlist = []
xlist = []

print("请输入：", end="")
sys.stdout.flush()

# 循环监控IO
while True:
    rs,ws,xs = select(rlist,wlist,xlist)

    # 分别遍历返回值列表，分类处理就绪的IO(就绪即发生)
    for r in rs:
        if r is sockfd: # sockfd
            # 处理就绪的IO事件
            print("\nWaiting for connection ...")
            connfd,addr = r.accept()
            print("Connected from",addr)

            # 关注新的IO事件
            rlist.append(connfd)
        elif r is sys.stdin: # sys.stdin
            # 终端输入数据
            print("请输入：", end="")
            sys.stdout.flush()
            data = r.readline().strip('\n')

            # 数据写入日志
            f.write(time.ctime()+':'+data+'\n')
            f.flush()
        else: # connfd
            # 客户发送端消息
            data = r.recv(1024).decode()
            if not data: # 客户端退出
                rlist.remove(r) # 取消关注
                r.close()
                continue

            # 消息写入日志
            f.write(time.ctime()+':'+data+'\n')
            f.flush()
