class NumberIterator:
    def __init__(self,stop):
        self.__stop = stop
        self.__index = 0

    def __next__(self):
        if self.__index == self.__stop:
            raise StopIteration("索引越界")
        self.__index += 1
        return self.__index - 1


class MyRange:
    def __init__(self,stop):
        self.__stop = stop

    def __iter__(self):
        return NumberIterator(self.__stop)

for item in MyRange(10):
    print(item)