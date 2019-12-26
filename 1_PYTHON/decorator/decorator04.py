"""
    问题：增加新功能，改变函数调用
"""

# 原有代码
def enter_background():
    print("进入后台")
def delete_order():
    print("删除订单")

# 新功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper

# 函数调用
enter_background = verify_permissions(enter_background)
delete_order = verify_permissions(delete_order)
enter_background()
delete_order()









