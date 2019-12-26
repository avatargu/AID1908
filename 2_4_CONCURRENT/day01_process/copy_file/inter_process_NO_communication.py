"""
创建两个进程，
分别复制一个文件的上半部分和下半部分，
到一个新的文件中
"""
from multiprocessing import Process
import os

filename = "./picture_all.jpg"
file_size = os.path.getsize(filename)

# file_read = open(filename, "rb")  # 重点：进程间不通信

# 复制上半部分
def copy_upper():
    file_read = open(filename,"rb")
    file_write = open("picture_upper.jpg","wb")

    n = file_size // 2
    file_write.write(file_read.read(n))

    file_read.close()
    file_write.close()

# 复制下半部分
def copy_lower():
    file_read = open(filename,"rb")
    file_write = open("picture_lower.jpg","wb")

    n = file_size // 2
    file_read.seek(n,0)
    file_write.write(file_read.read())

    file_read.close()
    file_write.close()

process_upper = Process(target = copy_upper)
process_lower = Process(target = copy_lower)

process_upper.start()
process_lower.start()

process_upper.join()
process_lower.join()
