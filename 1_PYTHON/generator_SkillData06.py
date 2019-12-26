"""
    lambda 匿名函数
"""

from common.list_helper import *

class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是：%d，%s，%d，%d" % (self.id,self.name,self.atk_ratio,self.duration)

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2)
]

# 优点：紧耦合

print(ListHelper.get_one(list_skill, lambda item: item.name == "葵花宝典"))
print(ListHelper.get_one(list_skill, lambda item: item.id == 101))
print(ListHelper.get_one(list_skill, lambda item: item.duration > 0))


