"""
    问题：原有代码函数参数不统一则无法包装
"""

# 新功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper

# 原有代码
@verify_permissions
def enter_background():
    print("进入后台")
@verify_permissions
def delete_order():
    print("删除订单")

# 函数调用
enter_background()
delete_order()









