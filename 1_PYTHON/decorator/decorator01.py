"""
    问题：增加新功能，改变函数调用
"""

# 原有代码
def enter_background():
    print("进入后台")
def delete_order():
    print("删除订单")

# 新功能
def verify_permissions():
    print("权限验证")

# 函数调用
verify_permissions()
enter_background()
verify_permissions()
delete_order()












