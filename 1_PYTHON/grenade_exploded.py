class Grenade:
    def __init__(self,attack):
        self.attack = attack
    def explode(self,demage_target):
        if not isinstance(demage_target,Demageable):
            raise ValueError("如果不是子类，则报错")
        print("**********爆炸**********")
        demage_target.demage(self.attack)


class Demageable:
    def __init__(self,name):
        self.name = name
    def demage(self,value):
        raise NotImplementedError("如果子类不重写，则异常")

class Player(Demageable):
    def __init__(self,name,blood):
        super().__init__(name)
        self.blood = blood
    def demage(self,value):
        self.blood -= value
        print("玩家受伤啦")
        print("碎屏")

class Enemy(Demageable):
    def __init__(self,name,blood):
        super().__init__(name)
        self.blood = blood
    def demage(self,value):
        self.blood -= value
        print("敌人受伤喽")
        print("头顶爆字")

class Duck(Demageable):
    def __init__(self,name,blood):
        super().__init__(name)
    def demage(self,value):
        print("鸭子死掉")

class House(Demageable):
    def __init__(self,name,blood):
        super().__init__(name)
    def demage(self,value):
        print("房子倒塌")

grenade01 = Grenade(100)
player01 = Player("孙悟空",100000000)
enemy01 = Enemy("牛魔王",10000000)
duck01 = Duck("唐老鸭",1000)
house01 = House("白宫",10)
grenade01.explode(player01)
grenade01.explode(enemy01)
grenade01.explode(duck01)
grenade01.explode(house01)











