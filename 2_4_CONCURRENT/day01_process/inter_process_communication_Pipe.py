"""
IPC:
    Inter Process Communication(进程间通信)

管道：
    1. 父进程创建管道
    2. 子进程复制管道
    3. 一端发送 p.send()
    4. 一端接收 p.recv() --> 管道空则阻塞
    5. n次发送
    6. n次接收
"""
from multiprocessing import Process,Pipe

# fd1,fd2 = Pipe(duplex = True)
# duplex = True --> 双向管道
# duplex = False --> 单向管道
# 返回管道两端的读写对象
# 如果是双向管道,fd1、fd2均可读写
# 如果是单向管道,fd1只读、fd2只写
# 其中,fd是file descriptor,文件描述符
fd1,fd2 = Pipe() # 默认创建双向管道

def app_tianmao(): # 一个进程只用fd1
    fd1.send("天猫的登录请求")
    data = fd1.recv() # 阻塞函数
    if data:
        print("天猫登录成功:",data)

def app_zhifubao(): # 一个进程只用fd2
    data = fd2.recv() # 阻塞函数
    print("支付宝收到:",data)
    fd2.send(("迪丽热巴","123456")) # 可以发送Python任意类型数据，不仅仅是字节串

p1 = Process(target = app_tianmao)
p2 = Process(target = app_zhifubao)
p1.start()
p2.start()
p1.join()
p2.join()
