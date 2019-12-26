"""
IPC:
    Inter Process Communication(进程间通信)

不同的父进程
"""
import multiprocessing
import os

def work_dict(dictionary, key, value):
    dictionary[key] = value

def work_list(listing):
    listing.append(os.getpid())

if __name__ == "__main__":
    with multiprocessing.Manager() as manager: # manager = multiprocessing.Manager()
        dict_manager = manager.dict() # 用于进程间通信的字典
        list_manager = manager.list() # 用于进程间通信的列表

        jobs_dict = [multiprocessing.Process(target=work_dict, args=(dict_manager, i, i ** 2)) for i in range(10)]
        jobs_list = [multiprocessing.Process(target=work_list, args=(list_manager,)) for i in range(10)]

        for job in jobs_dict:
            job.start()
        for job in jobs_list:
            job.start()

        for job in jobs_dict:
            job.join()
        for job in jobs_list:
            job.join()

        print(dict_manager)
        print(list_manager)
