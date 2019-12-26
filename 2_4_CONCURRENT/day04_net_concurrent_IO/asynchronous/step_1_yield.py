"""
协程原理：yield

协程就是可以暂停执行的函数
"""
def function():
    print("start")
    yield 1
    print("stop")

# 不打印
generator = function()
# 打印 start 1
print(generator.__next__())
# 打印 start 1 stop StopIteration
print(generator.__next__())
