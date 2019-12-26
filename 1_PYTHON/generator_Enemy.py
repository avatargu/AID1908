from common.list_helper import *


class Enemy:
    counter = 0
    def __init__(self,name,blood,base_damage,defense):
        self.name = name
        self.blood = blood
        self.base_damage = base_damage
        self.defense = defense
        Enemy.counter += 1

    def print_self_info(self):
        print("第%d个敌人%s的血量是%d,基础攻击力是%d,防御力是%d"%(Enemy.counter,self.name,self.blood,self.base_damage,self.defense))

    def __str__(self):
        return "敌人是：%s,%d,%d,%d"%(self.name,self.blood,self.base_damage,self.defense)

    def get_name(self):
        return self.name
    @property
    def blood(self):
        return self.__blood
    @property
    def base_damage(self):
        return self.__base_damage
    @property
    def defense(self):
        return self.__defense

    def set_name(self,name):
        self.name = name
    @blood.setter
    def blood(self,blood):
        if 0 <= blood <= 100:
            self.__blood = blood
        else:
            raise ValueError("我不要")
    # blood = property(get_blood,set_blood)
    @base_damage.setter
    def base_damage(self,base_damage):
        if 0 <= base_damage <= 1000:
            self.__base_damage = base_damage
        else:
            raise ValueError("我不要")
    # base_damage = property(get_base_damage,set_base_damage)
    @defense.setter
    def defense(self,defense):
        if 0 <= defense <= 10000:
            self.__defense = defense
        else:
            raise ValueError("我不要")
    # defense = property(get_defense,set_defense)

list_enemy = [
    Enemy("豺", 10, 19, 66),
    Enemy("狼", 12, 11, 77),
    Enemy("虎", 0, 9, 88),
    Enemy("豹", 16, 1, 99)
]

# print("####################################################################")
# for item in ListHelper.get_all(list_enemy, lambda element:element.base_damage > 10):
#     print(item)
# print(ListHelper.get_one(list_enemy, lambda item:item.name == "豹"))
# print(ListHelper.get_quantity(list_enemy, lambda item:item.blood > 0))
# print(ListHelper.is_in(list_enemy, lambda item:item.name == "虎"))
# print(ListHelper.is_in(list_enemy, lambda element:element.base_damage < 1 or element.defense > 100))
# print("####################################################################")
# print(ListHelper.get_sum(list_enemy, lambda item:item.blood))
# print(ListHelper.get_sum(list_enemy, lambda item:item.base_damage))
# print(ListHelper.get_sum(list_enemy, lambda item:item.defense))
# print("####################################################################")
# for item in ListHelper.get_property(list_enemy, lambda item:item.name):
#     print(item)
# for item in ListHelper.get_property(list_enemy, lambda item:item.blood):
#     print(item)
# for item in ListHelper.get_property(list_enemy, lambda item:item.base_damage):
#     print(item)
# for item in ListHelper.get_property(list_enemy, lambda item:item.defense):
#     print(item)
# for item in ListHelper.get_property(list_enemy, lambda item:(item.name,item.blood)):
#     print(item)
# for item in ListHelper.get_property(list_enemy, lambda item:(item.name,item.blood,item.base_damage)):
#     print(item)
# for item in ListHelper.get_property(list_enemy, lambda item:(item.name,item.blood,item.base_damage,item.defense)):
#     print(item)
# print("####################################################################")
# print(ListHelper.get_max(list_enemy, lambda item:item.blood))
# print(ListHelper.get_max(list_enemy, lambda item:item.base_damage))
# print(ListHelper.get_max(list_enemy, lambda item:item.defense))
# print(ListHelper.get_min(list_enemy, lambda item:item.blood))
# print(ListHelper.get_min(list_enemy, lambda item:item.base_damage))
# print(ListHelper.get_min(list_enemy, lambda item:item.defense))
# print("####################################################################")
# ListHelper.sorted_by_property(list_enemy, lambda item:item.blood)
# for item in list_enemy:
#     print(item)
# ListHelper.sorted_reverse(list_enemy, lambda item:item.defense)
# for item in list_enemy:
#     print(item)
print("####################################################################")
ListHelper.remove_all(list_enemy, lambda item:item.defense < 80)
for item in list_enemy:
    print(item)


# print(" map ********************************************************************")
# for item in ListHelper.get_property(list_enemy, lambda item:item.name):
#     print(item)
# for element in map(lambda element:element.name, list_enemy):
#     print(element)
# print(" filter ********************************************************************")
# for item in ListHelper.get_all(list_enemy, lambda item:item.blood == 0):
#     print(item)
# for element in filter(lambda element:element.blood == 0, list_enemy):
#     print(element)
# print(" sorted ********************************************************************")
# ListHelper.sorted_by_property(list_enemy, lambda item: item.blood)
# for item in list_enemy:
#     print(item)
# for element in sorted(list_enemy, key = lambda element:element.blood):
#     print(element)
# ListHelper.sorted_reverse(list_enemy, lambda item: item.blood)
# for item in list_enemy:
#     print(item)
# for element in sorted(list_enemy, key = lambda element:element.blood, reverse = True):
#     print(element)
# print(" max ********************************************************************")
# print(ListHelper.get_max(list_enemy, lambda item:item.blood))
# print(max(list_enemy, key = lambda item:item.blood))
# print(" min ********************************************************************")
# print(ListHelper.get_min(list_enemy, lambda item:item.blood))
# print(min(list_enemy, key = lambda item:item.blood))
