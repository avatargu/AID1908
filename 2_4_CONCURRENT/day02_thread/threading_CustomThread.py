"""
自定义线程类:
    简单的, 用函数封装
    复杂的, 用类封装

    1. 创建步骤:
        a. 继承Thread类
        b. 重写父类__init__()方法: 添加自己的属性, 使用super()加载父类的属性
        c. 重写父类run()方法

    2. 使用方法:
        a. 实例化对象
        b. 调用start()自动执行run()方法
        c. 调用join()回收线程
"""
from threading import Thread

class CustomThread(Thread):
    def __init__(self,*args,**kwargs):
        self.attr = args[0] # no use
        super().__init__()

    def step_one(self):
        print("step one")

    def step_two(self):
        print("step two")

    def step_three(self):
        print("step three")

    def run(self):
        self.step_one()
        self.step_two()
        self.step_three()

t = CustomThread("no use")
t.start()
t.join()
