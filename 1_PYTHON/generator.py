"""
    生成器：
        定义：能够动态（循环一次，计算一次，返回一次）提供数据的可迭代对象．
        作用：在循环过程中，按照某种算法推算数据，不必创建容器存储完整的结果，
            从而节省内存空间．数据量越大，优势越明显．
            以上作用也称之为延迟操作或惰性操作，
            通俗地讲就是在需要的时候才计算结果，
            而不是一次构建出所有结果．
    生成器函数：
        定义：含有yield语句的函数，返回值为生成器对象．
        语法：
            创建：
                def 函数名（）：
                    ．．．
                    yield　数据
                    ．．．
            调用：
                for 变量名　in 函数名（）：
                    语句

"""

list_all = [0,1,4,9,16,25,36,49,64,81]

# list_even = []
# for item in list_all:
#     if item % 2 == 0:
#         list_even.append(item)
# print(list_even)


# 普通函数（return）
def list_even01(list_all):
    list_even = []
    for item in list_all:
        if item % 2 == 0:
            list_even.append(item)
    return list_even
list_even = list_even01(list_all)
print(list_even)


# 生成器函数（yield）
def list_even02(list_all):
    for item in list_all:
        if item % 2 == 0:
            yield item  # yield　不就是多次　return　嘛
# 调用生成器函数
list_even = list_even02(list_all)
# 执行生成器函数
for item in list_even:
    print(item)







