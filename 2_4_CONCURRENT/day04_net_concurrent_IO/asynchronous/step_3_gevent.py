"""
协程模块：gevent
"""
import gevent
from gevent import monkey
"""
运行monkey脚本：
    将普通的IO阻塞转换为可以触发gevent协程跳转的IO阻塞

monkey.patch_socket()：
    转换socket模块中所有的IO阻塞
        
monkey.patch_all()：
    转换所有可转换的IO阻塞
"""
monkey.patch_time() # 在导入time模块之前，运行monkey脚本
from time import sleep

# 协程函数
def foo(a,b):
    print("start foo",a,b)
    # gevent.sleep(2)
    sleep(2)
    print("stop foo")

# 协程函数
def bar():
    print("start bar")
    # gevent.sleep(3)
    sleep(3)
    print("stop bar")

# 协程对象
f = gevent.spawn(foo,1,2) # 不定参

# 协程对象
b = gevent.spawn(bar)

"""
只有当遇到gevent指定的阻塞时
才会自动地在协程之间进行跳转
如gevent.joinall()和gevent.sleep()带来的阻塞
"""

# 执行两个协程函数
# gevent.joinall([f,b]) # 阻塞等待协程列表执行完毕
gevent.sleep(6) # 阻塞等待n秒
