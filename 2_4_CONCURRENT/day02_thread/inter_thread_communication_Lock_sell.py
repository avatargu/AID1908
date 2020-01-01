"""
有10个窗口(W1~W10)
卖50张票(T1~T50)
出票顺序升序
出票时间0.2秒
假设每个窗口都是一个线程
"""
from threading import Thread,Lock
from time import sleep,ctime

lock = Lock()

list_tickets = []
for i in range(1,51):
    list_tickets.append("T%d"%i)

def sell(window):
    while True:
        sleep(0.1)
        with lock:
            if list_tickets:
                ticket = list_tickets.pop(0)
                sleep(0.1)
                print("%s窗口 %s 出售%s"%(window,ctime(),ticket))
            else:
                break
                
list_jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("W%d"%i,))
    list_jobs.append(t)
    t.start()

[job.join() for job in list_jobs]
