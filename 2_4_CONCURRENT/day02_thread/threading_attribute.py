from threading import Thread
from time import sleep
from time import ctime

def tm():
    for i in range(3):
        sleep(1)
        print(ctime())

t = Thread(target = tm)

# 线程名称
print("default name:",t.name) # Thread-1
t = Thread(target = tm,name = "clock")
print("set name method 1:",t.name) # clock
t.name = "clk"
print("set name method 2:",t.name) # clk
# 附加
t.setName("c")
print("set name method 3:",t.getName()) # c

# t.daemon 设置主线程和分支线程的退出关系
# 若设置为True,则分支线程会随着主线程的退出而退出
# 在start()前设置
# 若True则不join()
# t.daemon = True
# 附加
t.setDaemon(True) # 设置daemon属性值
print("daemon:",t.isDaemon()) # 查看daemon属性值

t.start()

# 分支线程是否在生命周期中
print("is alive:",t.is_alive())

# t.join()
