"""
IO多路复用：
2. poll（重点代码）

linux unix
"""
from socket import *
from select import *

# 创建io对象
sockfd = socket() # 创建监听套接字，作为监控IO
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(8)

# 创建poll对象
p = poll()

"""
p.register(fd, event)
    功能
        关注IO事件
    参数
        fd    文件描述符
        event 事件类型
            POLLIN  读IO事件
            POLLOUT 写IO事件
            POLLERR 异常IO事件  

p.unregister(fd)
p.unregister(sockfd)
    功能
        取消关注
    参数
        IO对象或者IO对象的fileno
"""
p.register(sockfd, POLLIN | POLLERR)
fdmap = {sockfd.fileno() : sockfd}

print("循环监控IO")
while True:
    """
    events = p.poll()
        功能
            阻塞等待监控的IO事件发生
        返回值
            发生的IO事件
            格式
                [(fileno,event),(),...]
                    fileno 文件描述符
                    event  事件类型
    """
    events = p.poll()
    print("events:",events)

    # 分别遍历返回值列表，分类处理就绪的IO
    for fd,event in events:
        if fd == sockfd.fileno(): # sockfd
            # 处理就绪的IO事件
            print("Waiting for connection ...")
            connfd,addr = fdmap[fd].accept()
            print("Connected from",addr)

            # 关注新的IO事件
            p.register(connfd,POLLIN | POLLERR)
            fdmap[connfd.fileno()] = connfd
        elif event & POLLIN:      # connfd(只在POLLIN就绪时执行)
            data = fdmap[fd].recv(1024).decode()
            if not data: # 客户端退出
                # 取消关注
                p.unregister(fd)
                # p.unregister(connfd)

                fdmap[fd].close()

                # 维护字典
                del fdmap[fd]

                continue
            print(data)
            fdmap[fd].send(b"OK")
