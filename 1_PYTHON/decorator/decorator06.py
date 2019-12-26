"""
    问题：无
"""

# 新功能
def verify_permissions(func):
    def wrapper(*args,**kwargs):    #    合
        print("权限验证")
        return func(*args,**kwargs)        #    分
    return wrapper

# 原有代码
@verify_permissions    #    随时增删
def enter_background(account_number,password):
    print(account_number,password,"进入后台")
@verify_permissions    #    随时增删
def delete_order(id):
    print("删除订单",id)

# 函数调用
enter_background("abc",123)
delete_order(101)

