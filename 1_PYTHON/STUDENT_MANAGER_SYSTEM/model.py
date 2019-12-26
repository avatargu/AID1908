"""
    定义数据模型
"""

class StudentModel:
    """
        学生模型
    """
    def __init__(self,name = "",age = 0,score = 0,id = 0):
        """
            创建学生对象
        :param name: 姓名，str类型．
        :param age: 年龄，int类型．
        :param score: 分数，float类型．
        :param id: 编号（该学生对象的唯一标识）
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if 0 <= age <= 150:
            self.__age = age
        else:
            raise ValueError("年龄错误")

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("分数错误")

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        if 0 <= id <= 5000000:
            self.__id = id
        else:
            raise ValueError("id错误")