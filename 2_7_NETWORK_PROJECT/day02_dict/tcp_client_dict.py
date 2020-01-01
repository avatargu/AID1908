"""
只能在终端运行
不能在PyCharm运行

一级界面　--> 注册　登录　退出
二级界面　--> 查询单词　历史记录　注销
"""
from socket import *
import sys
from getpass import getpass # 只能在终端运行，不能在PyCharm运行

# 全局变量
ADDR = ("127.0.0.1",8000)
s = socket()
s.connect(ADDR)

# 查询单词
def handle_query(name):
    while True:
        word = input("单词：")
        if word == "##": # 结束单词查询
            break

        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())

        data = s.recv(2048).decode()
        print(data)

# 历史记录
def handle_view(name):
    msg = "V " + name
    s.send(msg.encode())

    data = s.recv(128).decode()
    if data == "SUCCESS":
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print("没有历史记录")

def login(name):
    while True:
        
        # 二级界面
        print("""
        ============query============
        1.查询单词   2.历史记录   3.注销
        =============================
        """)
        
        cmd = input("请输入选项：")
        if cmd == "1":
            handle_query(name)
        elif cmd == "2":
            handle_view(name)
        elif cmd == "3":
            return
        else:
            print("请输入正确选项！")

# 注册处理
def handle_register():
    while True:
        # 输入用户名
        name = input("Name:")

        # 输入密码
        password = getpass()
        password_again = getpass("Again:")
        if password != password_again:
            print("两次输入密码不一致！")
            continue

        # 用户名和密码的合法性检测
        if " " in name or " " in password:
            print("用户名和密码都不能有空格！")
            continue

        # 发送消息
        msg = "R %s %s"%(name,password)
        s.send(msg.encode())
        
        # 接收消息
        data = s.recv(128).decode()
        if data == "SUCCESS":
            print("注册成功")
            login(name)
        else:
            print("注册失败")

        return

# 登录处理
def handle_login():
    name = input("Name:")
    
    password = getpass()
    
    msg = "L %s %s"%(name,password)
    s.send(msg.encode()) 
    
    data = s.recv(128).decode() 
    if data == "SUCCESS":
        print("登录成功")
        login(name)
    else:
        print("登录失败")

def main():
    while True:
        
        # 一级界面
        print("""
        ========welcome========
        1.注册   2.登录   3.退出
        =======================
        """)
        
        cmd = input("请输入选项：")
        if cmd == "1":
            handle_register()
        elif cmd == "2":
            handle_login()
        elif cmd == "3":
            s.send(b"E")
            sys.exit("谢谢使用")
        else:
            print("请输入正确选项！")

if __name__ == "__main__":
    main()
