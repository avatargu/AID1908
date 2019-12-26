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

print("# 1 -----------------------------------------------------------------------------------------")

def get_skill01(list_target):
    for item in list_target:
        if item.atk_ratio > 6:
            yield item
for item in get_skill01(list_skill):
    print(item)

for item in (item for item in list_skill if item.atk_ratio > 6):
    print(item)

print("# 2 -----------------------------------------------------------------------------------------")

def get_skill02(list_target):
    for item in list_target:
        if 4 < item.duration < 11:
            yield item
for item in get_skill02(list_skill):
    print(item)

for item in (item for item in list_skill if 4 < item.duration < 11):
    print(item)

print("# 3 -----------------------------------------------------------------------------------------")

def get_skill03(list_target):
    for item in list_target:
        if item.id == 102:
            return item
print(get_skill03(list_skill))

print("# 4 -----------------------------------------------------------------------------------------")

def get_skill04(list_target):
    for item in list_target:
        if len(item.name) > 4 and item.duration < 6:
            yield item
for item in get_skill04(list_skill):
    print(item)