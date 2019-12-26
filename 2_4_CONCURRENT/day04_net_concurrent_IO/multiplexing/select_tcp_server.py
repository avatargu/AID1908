"""
IO多路复用：
1. select（重点代码）

windows linux unix

rlist, wlist, xlist = select(rlist, wlist, xlist[, timeout])

关注
    append
取消关注
    remove

The C10K problem
"""
from socket import *
from select import select

# 创建监听套接字，作为监控IO
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(8)

# 存放关注的等待发生的IO事件(包括读)
rlist = [sockfd]         # 经常用

# 存放关注的主动处理的IO事件(包括写)
wlist = []               # 很少用

# 存放关注的等待异常发生的IO事件
xlist = []               # 从不用

print("循环监控IO")
while True:
    rs,ws,xs = select(rlist,wlist,xlist) # 阻塞函数
    # print("rs:",rs)
    # print("ws:",ws)
    # print("xs:",xs)

    # 分别遍历返回值列表，分类处理就绪的IO(就绪即发生)
    for r in rs:
        if r is sockfd: # sockfd
            # 处理就绪的IO事件
            print("Waiting for connection ...")
            connfd,addr = r.accept()
            print("Connected from",addr)

            # 关注新的IO事件
            rlist.append(connfd)
        else:           # connfd
            data = r.recv(1024).decode()
            if not data: # 客户端退出
                rlist.remove(r) # 取消关注

                r.close()

                continue
            print(data)
            # r.send(b"OK") # 第一种方法
            wlist.append(r) # 第二种方法

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)

    for x in xs:
        pass
