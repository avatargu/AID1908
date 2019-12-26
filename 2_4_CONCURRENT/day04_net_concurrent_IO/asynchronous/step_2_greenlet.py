"""
协程模块：greenlet
"""
from greenlet import greenlet

# 协程函数
def function_1():
    print("开始function_1")
    gr2.switch()
    print("结束function_1")
    gr2.switch()

# 协程函数
def function_2():
    print("开始function_2")
    gr1.switch()
    print("结束function_2")

# 协程对象
gr1 = greenlet(function_1)

# 协程对象
gr2 = greenlet(function_2)

# 执行第一个协程函数
gr1.switch()
