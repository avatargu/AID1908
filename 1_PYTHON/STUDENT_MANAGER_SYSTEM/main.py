"""
    程序入口
"""

from ui import *

if __name__ == "__main__":
    student_manager_view = StudentManagerView()
    student_manager_view.main()

""" # 测试添加学生功能
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
"""