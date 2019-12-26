# from my_project.skill_system.skill_manager import *
from skill_system.skill_manager import *


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self,name):
        self.name = name
        # 加载配置文件　{技能名称:[效果1,效果2,...],...}
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_objects = self.__create_effect_objects()

    def __load_config_file(self):
        # 加载文件...
        return {
            "降龙十八掌":["DamageEffect(200)","LowerDeffenseEffect(-10,5)","DizzinessEffect(6)"],
            "六脉神剑":["DamageEffect(100)","DizzinessEffect(6)"],
        }

    def __create_effect_objects(self):
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            effect_object = eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object

    # 生成技能（执行效果）
    def generate_skill(self):
        print(self.name,"技能释放啦")
        for item in self.__effect_objects:
            item.impact()