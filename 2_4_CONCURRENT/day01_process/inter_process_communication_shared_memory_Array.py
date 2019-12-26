"""
IPC:
    Inter Process Communication(进程间通信)

共享内存:
    1. Value()
    2. Array()

i f c
"""
from multiprocessing import Process,Array

# 创建共享内存
# shm = Array("i",[1,2,3,4]) # [1,2,3,4]
# shm = Array("i",4) # [0,0,0,0]
shm = Array("c",b"hello,world.") # 字节串

def fun():
    for item in shm: # 可迭代对象
        print(item)
    # shm[0] = 10000
    shm[0] = b"H"

p = Process(target = fun)
p.start()
p.join()

# 打印字节串
for item in shm:
    print(item)

# 整体打印字节串，只对字节串有效
print(shm.value)
