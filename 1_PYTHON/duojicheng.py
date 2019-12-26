"""
多继承
无重叠的多继承
有重叠的多继承：父类中出现同名方法，看子类继承父类的顺序(就近原则)
算法：深度优先，广度优先
"""

class A:
    def say(self):
        print("sayA")

class B:
    def talk(self):
        print("talk")

    def say(self):
        print("sayB")

# class Children(A,B):
#     pass

class Children(B,A):
    pass

child = Children()
child.say()
child.talk()















