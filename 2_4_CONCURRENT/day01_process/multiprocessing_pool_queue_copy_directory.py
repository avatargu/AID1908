"""
使用进程池拷贝一个目录
每个进程池事件拷贝一个文件
使用进程间通信方法
实时显示拷贝百分比
"""
from multiprocessing import Queue,Pool
import os

# 进程间通信
queue = Queue()

def copy_file(file,dir_old,dir_new):
    fr = open(dir_old+'/'+file,'rb')
    fw = open(dir_new+'/'+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        size_file = fw.write(data) # 1024
        queue.put(size_file) # 1024
    fr.close()
    fw.close()

def main():
    path_base = "/home/tarena/"
    dir_target = input("请输入您要拷贝的目录名称:")

    folder_old = path_base + dir_target

    folder_new = folder_old+'-备份'
    os.mkdir(folder_new)

    list_files = os.listdir(folder_old)
    print("该目录包含的文件列表：",list_files)

    pool = Pool() # 创建进程池

    size_dir = 0
    for file in list_files:
        size_dir += os.path.getsize(folder_old+'/'+file)
        pool.apply_async(copy_file,args=(file,folder_old,folder_new))
        
    pool.close() # 关闭进程池
    
    size_copied = 0
    while True:
        size_copied += queue.get() # 1024
        print("拷贝了%.1f%%"%(size_copied/size_dir*100))
        if size_copied >= size_dir:
            break

    pool.join() # 回收进程池

if __name__ == '__main__':
    main()
