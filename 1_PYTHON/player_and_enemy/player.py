class Player:
    def __init__(self, name, base_damage, blood, score, *equipment):
        self.name = name
        self.base_damage = base_damage
        self.blood = blood
        self.score = score
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
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError("这是ｂｕｇ的分数")

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
        self.__crack_screen()
        if self.blood <= 0:
            self.__die()

    def __crack_screen(self):
        print(self.name, "碎屏",sep = "")

    def __die(self):
        print("游戏结束！")

if __name__ == "__main__":
    player01 = Player("玩家",100,100,0)
    print(player01.name)
    print(player01.base_damage)
    print(player01.blood)
    print(player01.score)
    print(player01.equipment)



















