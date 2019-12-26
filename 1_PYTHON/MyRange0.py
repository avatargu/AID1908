class NumberIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0

    def __next__(self):                          # __index__
        if self.__index > len(self.__target) - 1:
            raise StopIteration("索引越界")
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


class MyRange:
    def __init__(self,stop):  #　right or wrong
        self.__list_number = []
        self.__i = 0
        while self.__i < stop:
            self.__list_number.append(self.__i)
            self.__i += 1

    def __iter__(self):                          # __iter__
        return NumberIterator(self.__list_number)

for item in MyRange(10):
    print(item)