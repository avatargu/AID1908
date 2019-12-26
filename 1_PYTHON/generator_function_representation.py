list01 = [100,1.41,"hello",3.14,"world",2.72,200]
# 获取列表中所有的字符串
# １，生成器函数
def get_str(list_target):
    for item in list_target:
        if type(item) == str:
            yield item
# re = get_str(list01)
for item in get_str(list01):
    print(item)
# ２，生成器表达式
# re = (item for item in list01 if type(item) == str)
for item in (item for item in list01 if type(item) == str):
    print(item)
# ３，列表推导式
# re = [item for item in list01 if type(item) == str]
print([item for item in list01 if type(item) == str])
# 获取列表中所有的浮点数
# １，生成器函数
def get_float(list_target):
    for item in list_target:
        if type(item) == float:
            yield item
# re = get_float(list01)
for item in get_float(list01):
    print(item)
# ２，生成器表达式
# re = (item for item in list01 if type(item) == float)
for item in (item for item in list01 if type(item) == float):
    print(item)
# ３，列表推导式
# re = [item for item in list01 if type(item) == float]
print([item for item in list01 if type(item) == float])























