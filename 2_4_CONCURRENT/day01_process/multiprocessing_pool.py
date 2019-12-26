"""
进程池
"""
from multiprocessing import Pool
from time import sleep,ctime

def work(msg):
    sleep(2)
    print(ctime(),"--",msg)

# 创建进程池
# pool = Pool() # 默认进程数量
pool = Pool(4) # 指定进程数量

for i in range(10):
    msg = "event %d"%i
    # 事件入进程池队列
    '''
    Asynchronous version of `apply()` method.
    '''
    pool.apply_async(func = work,args = (msg,)) # 元组位置传参
    # pool.apply_async(func = work,kwds = {"msg":msg}) # 字典关键字传参

# 拓展
# ===============================================================
    '''
    Equivalent of `func(*args, **kwds)`.
    '''
    # pool.apply(func = work,args = (msg,)) # 元组位置传参
    # pool.apply(func = work,kwds = {"msg":msg}) # 字典关键字传参

    '''
    Asynchronous version of `map()` method.
    '''
    # pool.map_async(work,[x for x in range(5)])

    '''
    Apply `func` to each element in `iterable`, collecting the results
    in a list that is returned.
    '''
    # pool.map(work,[x for x in range(5)])
# ===============================================================

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
