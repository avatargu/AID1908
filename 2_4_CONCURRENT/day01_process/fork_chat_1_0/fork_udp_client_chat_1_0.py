"""
chat room

客户端：
1. 发送请求
2. 展示结果

数据流动方式：转发
客户端 --> 服务端 --> 其他客户端

通信协议设置：
1. 客户端发送, 服务端接收：
登录请求：LOGIN
聊天请求：CHAT
退出请求：QUIT
2. 服务端发送, 客户端接收：
登录响应：IN
退出响应：OUT
"""
from socket import *
import os,sys

ADDR = ("127.0.0.1",8888) # 服务器地址

def send_msg(s,name): # 第二层函数，第二层封装
    """
    循环发送请求
    :param s: UDP套接字
    :param name: 用户姓名
    """
    while True:
        try: # 客户端崩了怎么办(1)
            text = input("发言：") # 阻塞于此
        except KeyboardInterrupt: # KeyboardInterrupt 即 Ctrl+C
            text = "quit" # 输入 quit 或者 Ctrl+C 退出

        if text.strip() == "quit": # 发送退出请求, 其中strip方法用来去掉字符串两端可能会有的空格
            msg = "QUIT %s"%name
            s.sendto(msg.encode(),ADDR)
            sys.exit("您退出了聊天室") # 退出发送进程
        else: # 发送聊天请求
            msg = "CHAT %s %s"%(name,text)
            s.sendto(msg.encode(),ADDR)

def recv_msg(s): # 第二层函数，第二层封装
    """
    循环展示结果
    :param s: UDP套接字
    """
    while True:
        try: # 客户端崩了怎么办(2)
            data,addr = s.recvfrom(4096) # 阻塞于此
        except KeyboardInterrupt: # KeyboardInterrupt 即 Ctrl+C
            data = b"OUT"

        if data.decode() == "OUT": # 展示退出结果
            sys.exit() # 退出接收进程
        else: # 展示群消息
            print(data.decode() + "\n发言：",end = "")

def main(): # 第一层函数，第一层封装
    """
    主函数
    """

    # 创建套接字, 搭建网络
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        # 发送登录请求
        name = input("请输入姓名：")
        msg = "LOGIN %s"%name
        s.sendto(msg.encode(),ADDR)
        # 展示登录结果
        data,addr = s.recvfrom(128)
        if data.decode() == "IN":
            print("您已进入聊天室")
            break # 跳出while循环表示已进入聊天室
        else:
            print(data.decode())

    # 创建子进程, 避免阻塞
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0: # 子进程循环发送消息
        send_msg(s,name) # 直接给服务器发送name, 服务器由value(address)找key(name)不方便
    else:
        recv_msg(s) # 父进程循环接收消息

if __name__ == "__main__":
    main()
