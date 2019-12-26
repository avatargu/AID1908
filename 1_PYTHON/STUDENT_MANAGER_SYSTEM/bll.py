"""
    业务逻辑处理
"""

from model import *


class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """

    # 类变量，表示初始编号
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list
    # @stu_list.setter
    # def stu_list(self,stu_list):
    #     self.__stu_list = stu_list

    def add_student(self,student_info):
        """
            添加一个新学生
        :param student_info:没有编号的学生信息
        """
        student_info.id = self.__generate_id()
        self.__stu_list.append(student_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self,id):
        """
            根据编号移除学生信息
        :param id: 编号
        :return: True表示移除成功，False表示移除失败
        """
        for item in self.stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True # 表示移除成功
        return False #  表示移除失败

    def update_student(self,student_info):
        """
            根据student_info.id更新其他信息
        :param student_info: 新的学生对象
        :return: True表示更新成功，False表示更新失败
        """
        for item in self.stu_list:
            if item.id == student_info.id:
                item.name = student_info.name
                item.age = student_info.age
                item.score = student_info.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩对self.stu_list进行升序排列
        """
        for r in range(len(self.stu_list) - 1):
            for c in range(r + 1,len(self.stu_list)):
                if self.stu_list[r].score > self.stu_list[c].score:
                    self.stu_list[r],self.stu_list[c] = self.stu_list[c],self.stu_list[r]