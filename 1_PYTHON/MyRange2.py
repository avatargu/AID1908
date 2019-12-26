# class NumberIterator:
#     def __init__(self,stop):
#         self.__stop = stop
#         self.__index = 0
#
#     def __next__(self):
#         if self.__index == self.__stop:
#             raise StopIteration("索引越界")
#         self.__index += 1
#         return self.__index - 1


class MyRange:
    def __init__(self,stop):
        self.__stop = stop

    def __iter__(self):
        # return NumberIterator(self.__stop)

        # yield作用：将下列代码改为迭代器模式的代码

        # 生成迭代器代码的大致规则：
        # １，将yield以前的语句定义在next方法中
        # ２，将yield后面的数据作为next方法返回值

        number = 0
        while number < self.__stop:
            yield number                     # yield
            number += 1

# for item in MyRange(10):
#     print(item)
iterator = MyRange(10).__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break