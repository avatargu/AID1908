# 导入方式１---------------------------------

# import module01
#
# module01.function01()
#
# module01._function02()
#
# abc03 = module01.Abc()
# abc03.function03()

# import module01 as m
#
# m.function01()
#
# m._function02()
#
# abc01 = m.Abc()
# abc01.function03()

# 导入方式２---------------------------------

# from module01 import function01
# from module01 import _function02
# from module01 import Abc
#
# function01()
#
# _function02()
#
# abc03 = Abc()
# abc03.function03()

# 导入方式３---------------------------------

from module01 import *

function01()
_function02()

abc03 = Abc()
abc03.function03()
Abc.function04()








