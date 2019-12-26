import multiprocessing as mp
from time import sleep

def work(second,name):
    for i in range(3):
        sleep(second)
        print("I'm %s"%name)
        print("I'm working")

# 元组位置传参
# p = mp.Process(target = work,args = (1,"Bob"))
# 字典关键字传参
# p = mp.Process(target = work,kwargs = {"name":"Bob","second":1})
# 混合传参
p = mp.Process(target = work,args = (1,),kwargs = {"name":"Bob"})

p.start()

p.join()
