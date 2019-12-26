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
    return item.atk_ratio > 6
def func_condition02(item):
    return 4 < item.duration < 11
def func_condition04(item):
    return len(item.name) > 4 and item.duration < 6

print("# 1 -----------------------------------------------------------------------------------------")

for item in ListHelper.get_all(list_skill,func_condition01):
    print(item)

print("# 2 -----------------------------------------------------------------------------------------")

for item in ListHelper.get_all(list_skill,func_condition02):
    print(item)

print("# 4 -----------------------------------------------------------------------------------------")

for item in ListHelper.get_all(list_skill,func_condition04):
    print(item)