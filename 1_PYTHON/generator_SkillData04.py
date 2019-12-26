"""
    测试 通用模块　list_helper
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

print("# Functional programming +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def func_condition01(item):
    return item.name == "葵花宝典"
def func_condition02(item):
    return item.id == 101
def func_condition03(item):
    return item.duration > 0

print(ListHelper.get_one(list_skill, func_condition01))
print(ListHelper.get_one(list_skill, func_condition02))
print(ListHelper.get_one(list_skill, func_condition03))

