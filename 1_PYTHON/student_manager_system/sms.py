class StudentModel:



    # 模拟模型层存储的数据
    stu_list = []


    def __init__(self,name = "",age = 0,score = 0,id = 0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id # 没意义

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


class StudentManagerController:



    # 类变量，表示初始编号
    __init_id = 1000

    def __init__(self):
        self.__stu_list = StudentModel.stu_list
        # self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,student_info):
        student_info.id = self.__generate_id()
        # self.stu_list.append(student_info)　# 也可以？
        self.__stu_list.append(student_info)

    def __generate_id(self): #　生成器？
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


class StudentManagerView:
    def __init__(self):
        self.__student_manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        while True: # 持久
            item = input("请输入数字１～５：")
            if item == "1":
                self.__input_student()
                name = input("请输入姓名：")
                age = int(input("请输入年龄："))
                score = int(input("请输入成绩："))
                stu= StudentModel(name,age,score)
            elif item == "2":
                self.__output_students(self.__student_manager.stu_list)
            elif item == "3":
                self.__delete_student()
            elif item == "4":
                self.__modify_student()
            elif item == "5":
                self.__output_student_by_score()

    def main(self):
        """
            界面视图入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        student = StudentModel(name,age,score)
        self.__student_manager.add_student(student)

    def __output_students(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        while True:
            id = input("请输入编号：")
            if id == "":
                break
            elif self.__student_manager.remove_student(int(id)):
                print("删除成功")
                break
            else:
                print("删除失败")

    def __modify_student(self):
        student = StudentModel()
        student.id = int(input("请输入需要修改的学生编号："))
        student.name = input("请输入新的学生姓名：")
        student.age = int(input("请输入新的学生年龄："))
        student.score = int(input("请输入新的学生成绩："))
        if self.__student_manager.update_student(student):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__student_manager.order_by_score()
        self.__output_students(self.__student_manager.stu_list)


student_manager_view = StudentManagerView()
student_manager_view.main()



def main():
    view = StudentManagerView
    view.main()
    view.main()


if __name__ == "__main__":
    student_model01 = StudentModel("张无忌",27,99)
    student_model02 = StudentModel("赵敏",23,88)
    student_model03 = StudentModel("金毛狮王",48,88)
    student_model04 = StudentModel("青翼蝠王",49,89)
    student_model05 = StudentModel("白眉鹰王",50,90)
    student_model06 = StudentModel("紫衫龙王",51,91)
    print("*********************")
    print("********** add_student ***********")
    print("*********************")
    student_manager_controller = StudentManagerController()
    student_manager_controller.add_student(student_model01)
    student_manager_controller.add_student(student_model02)
    student_manager_controller.add_student(student_model03)
    student_manager_controller.add_student(student_model04)
    student_manager_controller.add_student(student_model05)
    student_manager_controller.add_student(student_model06)
    for item in student_manager_controller.stu_list:
        print(item.name,item.id,item.age,item.score)
    print("*********************")
    print("********** remove_student ***********")
    print("*********************")
    print(student_manager_controller.remove_student(1003))
    for item in student_manager_controller.stu_list:
        print(item.name,item.id,item.age,item.score)
    print("*********************")
    print("********** update_student ***********")
    print("*********************")
    print(student_manager_controller.update_student(StudentModel("迪丽热巴",25,98,1002)))
    for item in student_manager_controller.stu_list:
        print(item.name,item.age,item.score,item.id)
    print("*********************")
    print("*********************")


main()