"""
chat room(第一种方法：函数封装)

服务器：
1. 处理请求
2. 发送管理员消息

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

ADDR = ("0.0.0.0",8888) # 服务器地址

# 敏感词列表
list_sensitive_words = ["artificial","intelligence"]

# 服务器维护用户信息：
# {name:[address_client,number_warning],...}
user = {} # 存储用户地址, {name:[address_client,number_warning],...}

def handle_login(s,name,addr): # 第三层函数，第三层封装
    """
    处理客户端的登录请求
    :param s: UDP套接字
    :param name: 用户姓名
    :param addr: 用户地址
    """
    
    # 1,是否允许进入
    if "管理员" in name or name in user: # 正确顺序
        s.sendto("该用户存在".encode(),addr)
        return
    else:
        s.sendto(b"IN",addr) # 可以进入聊天室

    # 2,允许进入则通知其他人（先）
    msg = "\n欢迎“%s”进入聊天室"%name
    for key in user:
        s.sendto(msg.encode(),user[key][0])

    # 3,同时存储该用户的地址，警告计数初始为零（后）
    user[name] = [addr,0]

def handle_chat(s,name,text): # 第三层函数，第三层封装
    """
    处理客户端的聊天请求
    :param s: UDP套接字
    :param name: 用户姓名
    :param text: 用户消息
    """
    
    # 格式化消息
    msg = "\n%s: %s"%(name,text)

    # 要么警告计数加一
    for sensitive_word in list_sensitive_words:
        if sensitive_word in text:
            user[name][1] += 1
            break # 跳出循环
    # 要么转发消息（除了发送消息的人）
    else:
        for key in user:
            if key != name:
                s.sendto(msg.encode(),user[key][0])
        return # 跳出函数

    # 在警告计数加一的情况下
    if user[name][1] >= 3:
        # 通知发送消息的人
        s.sendto("你被移出群聊".encode(),user[name][0])

        s.sendto(b"OUT",user[name][0])

        del user[name]

        # 通知其他人
        for key in user:
            s.sendto(("移出 " + name).encode(), user[key][0])
    else:
        # 通知发送消息的人
        s.sendto(("你被第%d次警告"%user[name][1]).encode(),user[name][0])

        # 通知其他人
        for key in user:
            if key != name:
                s.sendto(("第%d次警告%s"%(user[name][1],name)).encode(), user[key][0])

def handle_quit(s,name): # 第三层函数，第三层封装
    """
    处理客户端的退出请求
    :param s: UDP套接字
    :param name: 用户姓名
    """
    
    # 通知其他人（先）
    msg_one = "OUT"                      # 发送给退出者
    msg_others = "\n'%s'退出了聊天室"%name # 发送给其他人
    for key in user:
        if key != name:
            s.sendto(msg_others.encode(),user[key][0])
        else:
            s.sendto(msg_one.encode(),user[key][0])
    
    #  删除该用户的地址（后）
    del user[name] 

def handle_request(s): # 第二层函数，第二层封装
    """
    处理客户端的请求
    :param s: UDP套接字
    """
    while True:
        # 服务器崩了怎么办?(2)
        data,addr = s.recvfrom(1024) # 阻塞于此
        list_data = data.decode().split()
        if list_data[0] == "LOGIN":
            handle_login(s,list_data[1],addr)
        elif list_data[0] == "CHAT":
            text = " ".join(list_data[2:])
            handle_chat(s,list_data[1],text)
        elif list_data[0] == "QUIT":
            handle_quit(s,list_data[1])

def main(): # 第一层函数，第一层封装
    """
    主函数
    """

    # 创建套接字, 搭建网络
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    # 创建子进程, 避免阻塞
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0: # 子进程发送管理员消息
        while True:
            # 服务器崩了怎么办?(1)
            msg = input("管理员消息：") # 阻塞于此
            msg = "CHAT 管理员 " + msg
            # 子进程的user恒空
            s.sendto(msg.encode(),ADDR) # 自己发送给自己，即子进程发送给父进程
    else: # 父进程转发用户消息
        handle_request(s)

if __name__ == "__main__":
    main()
