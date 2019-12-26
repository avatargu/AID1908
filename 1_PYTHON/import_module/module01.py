"""
    模块相关概念
"""

__all__ = ["function01","Abc","_function02"] # 定义可导出成员，仅对from module01 import *有效

print("module01")

def function01():
    print("module01的function01")

def _function02(): # 定义隐藏成员，仅对from module01 import *有效
    print("module01的function02")

class Abc:
    def function03(self):
        print("module01的Abc的function03")

    @staticmethod
    def function04():
        print("module01的Abc的function04")

print(__doc__)
print(__file__)
print(__name__)