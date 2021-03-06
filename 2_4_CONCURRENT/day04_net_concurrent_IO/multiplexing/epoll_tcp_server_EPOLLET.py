"""
注掉elif分支
下移print("循环监控IO")

运行服务器
运行客户端
客户端发送消息
查看现象

改为边缘触发

运行服务器
运行客户端
客户端发送消息
查看现象
"""
from socket import *
from select import *

# 创建io对象
sockfd = socket() # 创建监听套接字，作为监控IO
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(8)

# 创建poll对象
ep = epoll()

"""
ep.register(fd, event)
    功能
        关注IO事件
    参数
        fd    文件描述符
        event 事件类型
            EPOLLIN  读IO事件
            EPOLLOUT 写IO事件
            EPOLLERR 异常IO事件  
            EPOLLET  边缘触发

ep.unregister(fd)
ep.unregister(sockfd)
    功能
        取消关注
    参数
        IO对象或者IO对象的fileno
"""
ep.register(sockfd, EPOLLIN | EPOLLERR)
fdmap = {sockfd.fileno() : sockfd}

while True:
    print("循环监控IO")
    """
    events = ep.poll()
        功能
            阻塞等待监控的IO事件发生
        返回值
            发生的IO事件
            格式
                [(fileno,event),(),...]
                    fileno 文件描述符
                    event  事件类型
    """
    events = ep.poll()
    print("events:",events)

    # 分别遍历返回值列表，分类处理就绪的IO
    for fd,event in events:
        if fd == sockfd.fileno(): # sockfd
            # 处理就绪的IO事件
            print("Waiting for connection ...")
            connfd,addr = fdmap[fd].accept()
            print("Connected from",addr)

            # 关注新的IO事件
            # ep.register(connfd,EPOLLIN | EPOLLERR)
            ep.register(connfd,EPOLLIN | EPOLLET) # 边缘触发
            fdmap[connfd.fileno()] = connfd
            # elif event & EPOLLIN:      # connfd(只在EPOLLIN就绪时执行)
            #     data = fdmap[fd].recv(1024).decode()
            #     if not data: # 客户端退出
            #         # 取消关注
            #         ep.unregister(fd)
            #         # p.unregister(connfd)
            #
            #         fdmap[fd].close()
            #
            #         # 维护字典
            #         del fdmap[fd]
            #
            #         continue
            #     print(data)
            #     fdmap[fd].send(b"OK")
