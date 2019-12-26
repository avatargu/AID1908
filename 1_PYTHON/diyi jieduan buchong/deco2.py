


def mydeco(fn)   :
    def verify(*args,**kwargs):
        print("正在验证权限")
        fn(*args,**kwargs)
    return verify

def mydeco2(fn)   :
    def sendmessage(*args,**kwargs):
        fn(*args,**kwargs)
        print("正在发送短信")
    return sendmessage

@mydeco
def savemoney(x):
    print("正在存钱",x,"元")

# savemoney = mydeco(savemoney)

@mydeco
def withdraw(x):
    print("正在取钱",x,"元")

# withdraw = mydeco(withdraw)

@mydeco2
@mydeco
def vip_savemoney(name,x):
    print("VIP:",name,"正在存钱",x,"元")



vip_savemoney = mydeco(vip_savemoney)



vip_savemoney("马云",99999999)



savemoney(100)
savemoney(200)
withdraw(150)


