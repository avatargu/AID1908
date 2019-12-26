"""
难点：传参
"""
from threading import Thread
from time import sleep,ctime

# 自定义线程类
class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs={}): # 模仿父类__init__()方法的参数定义(此处不拆解,所以不用星)
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.target(*self.args,**self.kwargs) # 模仿父类_target()方法的参数定义(此处拆解,所以用星)

# 线程函数
def player(second,song):
    for i in range(3):
        print("Playing %s : %s"%(song,ctime()))
        sleep(second)

t = MyThread(target=player,args=(1,),kwargs={"song":"《怒放的生命》"})
t.start()
t.join()
