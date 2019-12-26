"""
一秒打印一次当前时间
"""
##################################################
import time

f = open("log.txt","a+")
f.seek(0,0) # 文件偏移量从结尾移动到开头

n = 0
for line in f:
    n += 1

while True:
    time.sleep(1)

    n += 1
    s = "%d. %s\n"%(n,time.ctime())

    f.write(s)
    f.flush() # 缓冲刷新方法1
##################################################
import time

f = open("log.txt","a+",1) # 缓冲刷新方法2
f.seek(0,0) # 文件偏移量从结尾移动到开头

n = 0
for line in f:
    n += 1

while True:
    time.sleep(1)

    n += 1
    s = "%d. %s\n"%(n,time.ctime())

    f.write(s)
##################################################