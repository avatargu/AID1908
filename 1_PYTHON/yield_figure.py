from math import pi


class FigureManager:
    def __init__(self):
        self.__list_figure = []

    @property
    def list_figure(self):
        return self.__list_figure               # 2,关联（部分与整体的关系，耦合度居中，成员）：FigureManager类与Figure类关联（聚合/组合）

    def add_figure(self,figure):                # 3,依赖（合作关系，耦合度最低，参数）：FigureManager类依赖Figure类
        if isinstance(figure,Figure):
            self.__list_figure.append(figure)
        else:
            raise ValueError("类型错误！")

    def delete_figure(self,number):
        del self.__list_figure[number]

    def get_sum_of_areas(self):
        sum_of_areas = 0
        for item in self.list_figure:
            sum_of_areas += item.calculate_area()
        return sum_of_areas

    def __iter__(self):
        # return FigureIterator(self.__list_figure)

        # １，调用当前方法不执行（内部创建迭代器对象）
        # ２，调用__next__方法才执行
        # ３，执行到yield语句暂时离开
        # ４，再次调用__next__方法继续执行
        # ５，重复第３／４步骤直至最后

        # 方法一　****************************************
        # index = 0
        # while index < len(self.list_figure):
        #     yield self.list_figure[index]
        #     index += 1
        # 方法二　****************************************
        # for i in range(len(self.list_figure)):
        #     yield self.list_figure[i]
        # 方法三　****************************************
        for item in self.list_figure:
            yield item


class Figure:
    def calculate_area(self):
        pass


# class FigureIterator:
#     def __init__(self,target):
#         self.__target = target
#         self.__index = 0
#
#     def __next__(self):
#         if self.__index > len(self.__target) - 1:
#             raise StopIteration("索引越界")
#         temp = self.__target[self.__index]
#         self.__index += 1
#         return temp

# --------------------------------------------------------------------------------------------------------------------------


class Circular(Figure):             # 1,泛化（子类与父类的关系，耦合度最高，一种）：Circular类泛化Figure类
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Figure):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Figure):
    def __init__(self,bottom,height):
        super().__init__()
        self.bottom = bottom
        self.height = height

    def calculate_area(self):
        return self.bottom * self.height * 0.5

circular = Circular(3)
rectangle = Rectangle(8,4)
triangle = Triangle(6,10)
figure_manager = FigureManager()
figure_manager.add_figure(circular)
figure_manager.add_figure(rectangle)
figure_manager.add_figure(triangle)
# print(figure_manager.get_sum_of_areas())

# for item in figure_manager:
#     print(item)
iterator = figure_manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break













