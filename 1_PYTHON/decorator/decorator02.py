"""
问题：增加新功能，改变原有代码
"""

# 原有代码
def enter_background():
    verify_permissions()
    print("进入后台")
def delete_order():
    verify_permissions()
    print("删除订单")

# 新功能
def verify_permissions():
    print("权限验证")

# 函数调用
enter_background()
delete_order()

