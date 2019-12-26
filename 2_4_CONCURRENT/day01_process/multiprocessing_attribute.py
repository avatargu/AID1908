from multiprocessing import Process
import time

def tm():
    for i in range(3):
        time.sleep(1)
        print(time.ctime())

p = Process(target = tm)

# 进程名称
print("default name:",p.name) # Process-1
p = Process(target = tm,name = "clock")
print("set name method 1:",p.name) # clock
p.name = "clk"
print("set name method 2:",p.name) # clk

# p.daemon　设置父子进程的退出关系
# 若设置为True,则子进程会随着父进程的退出而退出
# 在start()前设置
# 若True则不join()
p.daemon = True

p.start()

# 子进程的PID
print("pid:",p.pid)

# 子进程是否在生命周期中
print("is alive:",p.is_alive())

# p.join()
