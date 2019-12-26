from math import pi


class FigureManager:
    def __init__(self):
        self.__list_figure = []

    @property
    def list_figure(self):
        return self.__list_figure

    def add_figure(self,figure):
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
        return FigureIterator(self.__list_figure)


class Figure:
    def calculate_area(self):
        pass


class FigureIterator:
    def __init__(self,list_figure):
        self.__list_figure = list_figure
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__list_figure) - 1:
            raise StopIteration("索引越界")
        temp = self.__list_figure[self.__index]
        self.__index += 1
        return temp

# --------------------------------------------------------------------------------------------------------------------------


class Circular(Figure):
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

print(FigureManager.__bases__)











