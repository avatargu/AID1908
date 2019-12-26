# globals() 函数
# locals()　函数
a = 1
b = 2
c = 3


def function01(c, d):
    e = 500
    print("locals()返回", locals())
    print("globals()返回", globals())
    print(c)
    print(globals()["c"])

function01(300,400)





































