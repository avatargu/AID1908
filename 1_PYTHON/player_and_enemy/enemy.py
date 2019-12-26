class Enemy:
    def __init__(self, name, base_damage, blood, *equipment):
        self.name = name
        self.base_damage = base_damage
        self.blood = blood
        self.equipment = equipment

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def base_damage(self):
        return self.__base_damage
    @base_damage.setter
    def base_damage(self,base_damage):
        if 0 <= base_damage <=100:
            self.__base_damage = base_damage
        else:
            raise ValueError("这是ｂｕｇ的攻击力")

    @property
    def blood(self):
        return self.__blood
    @blood.setter
    def blood(self,blood):
        if 0 <= blood <=200:
            self.__blood = blood
        else:
            raise ValueError("这是ｂｕｇ的血量")

    @property
    def equipment(self):
        return self.__equipment
    @equipment.setter
    def equipment(self,equipment):
        self.__equipment = equipment

    def attack(self,somebody):
        somebody.injure(self)

    def injure(self,somebody):
        self.blood -= somebody.base_damage
        if self.blood <= 0:
            self.__die(somebody)

    def __die(self,somebody):
        print(self.name,"死亡！",sep = "")
        list_equipment_player = list(somebody.equipment)
        list_equipment_enemy = list(self.equipment)
        list_equipment_player.extend(list_equipment_enemy)
        somebody.equipment = tuple(list_equipment_player)
        self.equipment = ()
        somebody.score += 1

if __name__ == "__main__":
    enemy01 = Enemy("敌人",100,100,"屠龙刀","倚天剑")
    print(enemy01.name)
    print(enemy01.base_damage)
    print(enemy01.blood)
    print(enemy01.equipment)































































