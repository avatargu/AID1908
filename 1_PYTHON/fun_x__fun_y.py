"""
    内存图
"""
def fun_x():
    x = 5

    def fun_y():
        nonlocal x
        x += 1
        return x

    return fun_y

a = fun_x()

print(a())
print(a())
print(a())




