# from my_project.common.double_list_helper import DoubleListHelper
from common.double_list_helper import *


class SkillImpactEffect:
    def impact(self):
        """
            技能影响效果
        """
        raise NotImplementedError()


class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """
    def __init__(self,value):
        self.value = value

    def impact(self):
        print("扣你血量")


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力
    """
    def __init__(self,value,time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低%d防御力，持续%d秒" % (self.value,self.time))


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕
    """
    def __init__(self,time):
        self.time = time

    def impact(self):
        print("眩晕%d秒" % self.time)
