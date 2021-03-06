"""
TCP套接字服务端流程（重点代码）
"""
from socket import *

# 1,创建流式套接字(socket)
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 只有 tcp 有，只有 server　有

# 2,绑定本机网络地址(bind)
sockfd.bind(("127.0.0.1",8888)) # sockfd.bind(("0.0.0.0",8888))

# 3,设置监听(listen)
sockfd.listen(8) # 一个监听套接字可以同时连接多个客户端，也可以重复连接

while True: # 循环《创建客户端连接套接字，循环<收发消息>，关闭客户端连接套接字》
    try:
        # 4,服务端等待客户端的连接请求(accept)
        print("Waiting for connection ...")
        connfd,addr = sockfd.accept()
        print("Connected from",addr)
    except KeyboardInterrupt:
        print("Server exited")
        break
    except Exception as e:
        print(e)
        continue

    while True: # 循环<收发消息>
        # 5,收发消息(recv/send)
        data = connfd.recv(1024)
        """
        客户端退出，
        服务端recv立即返回空字符串，
        服务端send，
        服务端recv再次返回空字符串，
        服务端再次send，BrokenPipeError
        """
        if not data: # 判空
            break
        print("服务端接收：",data.decode())
        n = connfd.send(b"Thanks")
        print("服务端发送了%d字节"%n)

    # 6,关闭客户端连接套接字和流式套接字(close)
    connfd.close()

sockfd.close()
