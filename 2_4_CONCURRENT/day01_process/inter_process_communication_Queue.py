"""
IPC:
    Inter Process Communication(进程间通信)

消息队列:
    1. def put(self, obj, block=True, timeout=None):
           pass

        其中:
            block:  是否阻塞
            timeout:超时检测

    2. def get(self, block=True, timeout=None):
           pass

        其中:
            block:  是否阻塞
            timeout:超时检测

    3. 写入消息 q.put() --> 消息队列满则阻塞
    4. 读出消息 q.get() --> 消息队列空则阻塞
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(3)

def put_ball():
    for i in range(7):
        sleep(1)
        counter = 0
        list_number = []
        while counter < 6:
            number = randint(1,33)
            if number not in list_number:
                list_number.append(number) # 六个红球
                counter += 1
        list_number.sort()
        list_number.append(randint(1,16)) # 一个蓝球
        q.put(list_number) # 双色球入队
        print("qsize after putting:", q.qsize())
        print("full:", q.full())

def get_ball():
    while True:
        try:
            sleep(2)
            list_number = q.get(timeout=2) # 双色球出队
            print("qsize after getting:", q.qsize())
            print("empty:", q.empty())
            print(list_number)
        except:
            return

p1 = Process(target = put_ball)
p2 = Process(target = get_ball)
p1.start()
p2.start()
p1.join()
p2.join()

# 关闭消息队列
q.close()
