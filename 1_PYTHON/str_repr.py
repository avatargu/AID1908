"""
    __str__和__repr__没有发现区别
"""
class Enemy:
    def __init__(self,name,blood,base_damage,defense):
        self.name = name
        self.blood = blood
        self.base_damage = base_damage
        self.defense = defense

    def __str__(self):
        return "敌人%s的血量有%d,基础攻击力是%d,防御力是%d．"%(self.name,self.blood,self.base_damage,self.defense)
        # return "Enemy('%s',%d,%d,%d)" % (self.name, self.blood, self.base_damage, self.defense)

    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)"%(self.name,self.blood,self.base_damage,self.defense)
        # return "敌人%s的血量有%d,基础攻击力是%d,防御力是%d．" % (self.name, self.blood, self.base_damage, self.defense)
        # return "Enemy(%s,%d,%d,%d)"%(self.name,self.blood,self.base_damage,self.defense)
        # return "'%s',%d,%d,%d"%(self.name,self.blood,self.base_damage,self.defense)
        # return "%s,%d,%d,%d"%(self.name,self.blood,self.base_damage,self.defense)

enemy = Enemy("牛魔王",100,100,100)

print(enemy)
print(str(enemy))
print(repr(enemy))

# enemy_new = eval(repr(enemy));print(enemy_new);enemy_new.name = "铁扇公主"
#
# print(enemy.name)
# print(enemy_new.name)







































