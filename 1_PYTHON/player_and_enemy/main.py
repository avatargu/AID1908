"""
    请用面向对象思想，描述以下场景：
    玩家（攻击力）攻击敌人（血量），敌人受伤（掉血），还可能死亡（掉装备，加分）；
    敌人（攻击力）攻击玩家（血量），玩家受伤（掉血／碎屏），还可能死亡（游戏结束）．
"""

from player import Player
from enemy import Enemy

# import player
# import enemy

if __name__ == "__main__":
    player01 = Player("玩家",100,100,0)
    enemy01 = Enemy("敌人",100,100,"屠龙刀","倚天剑")
    print(player01.name)
    print(player01.base_damage)
    print(player01.blood)
    print(player01.score)
    print(player01.equipment)
    print("****************")
    print(enemy01.name)
    print(enemy01.base_damage)
    print(enemy01.blood)
    print(enemy01.equipment)
    print("****************")
    print("****************")
    player01.attack(enemy01)
    print("****************")
    enemy01.attack(player01)
    print("****************")
    print("****************")
    print(player01.blood)
    print(player01.score)
    print(player01.equipment)
    print("****************")
    print(enemy01.blood)
    print(enemy01.equipment)




























































