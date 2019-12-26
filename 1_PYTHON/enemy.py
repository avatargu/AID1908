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
        if 0 < blood < 100:
            self.__blood = blood
        else:
            raise ValueError("我不要")
    # blood = property(get_blood,set_blood)
    @base_damage.setter
    def base_damage(self,base_damage):
        if 0 < base_damage < 1000:
            self.__base_damage = base_damage
        else:
            raise ValueError("我不要")
    # base_damage = property(get_base_damage,set_base_damage)
    @defense.setter
    def defense(self,defense):
        if 0 < defense < 10000:
            self.__defense = defense
        else:
            raise ValueError("我不要")
    # defense = property(get_defense,set_defense)


# enemy01 = Enemy("灭霸",100,99,98)
# enemy01.print_self_info()
# enemy02 = Enemy("死亡",0,88,88)
# print(enemy02.get_name())
# enemy03 = Enemy("Rot",0,77,8)
# enemy04 = Enemy("卡魔拉",70,66,68)
# list_enemy = [enemy01,enemy02,enemy03,enemy04]

# enemy_target = None
# for item in list_enemy:
#     if item.get_name() == "灭霸":
#         enemy_target = item
# print(enemy_target.get_name())
#
# list_enemy_target = []
# for item in list_enemy:
#     if item.get_blood() == 0:
#         list_enemy_target.append(item)
# for item in list_enemy_target:
#     print(item.get_name(),end = " ")
# print()
#
# sum_base_damage = 0
# for item in list_enemy:
#     sum_base_damage += item.get_base_damage()
# average_base_damage = sum_base_damage / len(list_enemy)
# print(average_base_damage)
#
# print("切记删除倒着走")
# for i in range(len(list_enemy)-1,-1,-1):
#     if list_enemy[i].get_defense() < 10:
#         del list_enemy[i]
# for item in list_enemy:
#     print(item.get_name(),end = " ")
# print()
#
# for item in list_enemy:
#     item.set_base_damage(item.get_base_damage() + 50)
# for item in list_enemy:
#     print(item.get_base_damage(),end = " ")
# print()

enemy001 = Enemy("自己",10,99,98)
enemy001.print_self_info()


print(enemy001.__dict__)
print(dir(enemy001))

print(Enemy.__dict__)
print(dir(Enemy))


