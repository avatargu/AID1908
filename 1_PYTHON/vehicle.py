class Vehicle:
    def transport(self,str_position):
        pass


class Person:
    def __init__(self,name):
        self.name = name
    def go_to(self,vehicle,str_position):
        vehicle.transport(str_position)


class Car(Vehicle):
    def transport(self,str_position):
        print("汽车 开到",str_position)


class Airplane(Vehicle):
    def transport(self,str_position):
        print("飞机 飞到",str_position)

person01 = Person("老张")
car01 = Car()
airplane01 = Airplane()
person01.go_to(car01,"东北")
person01.go_to(airplane01,"东北")

