class Skill:
    pass


class SkillManager:
    def __init__(self):
        self.__list_skill = []

    def add_skill(self,skill):
        self.__list_skill.append(skill)

    def __iter__(self):
        return SkillIterator(self.__list_skill)


class SkillIterator:
    def __init__(self,list_target):
        self.__list_target = list_target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__list_target) - 1:
            raise StopIteration
        temp = self.__list_target[self.__index]
        self.__index += 1
        return temp

skill_manager = SkillManager()
skill_manager.add_skill(Skill())
skill_manager.add_skill(Skill())
skill_manager.add_skill(Skill())

# for item in skill_manager:
#     print(item)
iterator = skill_manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break









