import threading
from time import sleep
import os

def music_child():
    for i in range(3):
        sleep(3)
        print(os.getpid(),"分支线程播放《我爱你中国》")

def music_main():
    for i in range(2):
        sleep(1)
        print(os.getpid(), "主线程播放《我的中国心》")

t = threading.Thread(target = music_child) # 第一步：线程对象

# 非阻塞回收线程法
# t.setDaemon(True)

t.start() # 第二步：启动线程

music_main()

# 阻塞回收线程法
t.join() # 第三步：回收线程

print("若采用阻塞回收线程法，则阻塞直到分支线程执行完毕")
print("若采用非阻塞回收线程法，则没有阻塞")
