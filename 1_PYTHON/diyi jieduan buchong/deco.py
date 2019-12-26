


def mydeco(fn)   :
    def verify(x):
        print("正在验证权限")
        fn(x)
    return verify




# def savemoney(x):
#     s = input("请输入密码：")
#     if s != "123456":
#         print("密码错误")
#         return
#     print("正在存钱",x,"元")
#
# def withdraw(x):
#     print("正在取钱",x,"元")

@mydeco
def savemoney(x):
    print("正在存钱",x,"元")

# savemoney = mydeco(savemoney)

def withdraw(x):
    print("正在取钱",x,"元")

withdraw = mydeco(withdraw)

savemoney(100)
savemoney(200)
withdraw(150)





















