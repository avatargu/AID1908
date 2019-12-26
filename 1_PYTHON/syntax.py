# a = 1
# help("__main__")


# class Person:
#     pass
# class Teacher(Person):
#     pass
# person01 =Person()
# teacher01 = Teacher()
# print(isinstance(person01,Person))
# print(issubclass(Teacher,Person))


# re = eval("1 + 2 * 5");print(re)
# re = eval(input("请输入："));print(re)
# exec("a = 1");print("a",a)
# exec(input('请输入：'));print("b",b)


# # __str__
# # __repr__
# class StudentModel:
#     def __init__(self,name = "",age = 0,score = 0,id = 0):
#         self.name = name
#         self.age = age
#         self.score = score
#         self.id = id
#     def __str__(self):
#         return "我叫%s，编号是%d，今年%d岁了，成绩是%d"%(self.name,self.id,self.age,self.score)
#     def __repr__(self):
#         return "StudentModel('%s',%d,%d,%d)"%(self.name,self.age,self.score,self.id)
# student_model = StudentModel("孙悟空",500,100,101)
# print("__str__")
# print(student_model)
# str_student_model = str(student_model);print(str_student_model)
# print("__repr__")
# repr_student_model = repr(student_model);print(repr_student_model)
# eval_repr_student_model = eval(repr(student_model));print(eval_repr_student_model)
# eval_repr_student_model.name = "猪八戒";print(student_model.name,end = " ");print(eval_repr_student_model.name,end = " ")











