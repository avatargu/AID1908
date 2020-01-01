"""
协程原理：yield

生成器是可以暂停执行的函数
协程就是可以暂停执行的函数
"""
def function():
    print("start")
    yield 1
    print("doing")
    yield 2
    print("stop")

# for item in function():
#     print(item)

# 不打印
generator = function()

# 方法一：打印 start 1　
print(generator.__next__())
# 方法二：打印 start 1
# print(next(generator))

# 打印 start 1 doing 2
print(generator.__next__())

# 打印 start 1 doing 2 stop StopIteration
print(generator.__next__())
