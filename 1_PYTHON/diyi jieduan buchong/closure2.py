class Bank:
    def __init__(self,money = 0):
        self.__money = money
    def save(self,x):
        self.__money += x
        print("账户有",self.__money,"元")
    def withdraw(self,x):
        if x > self.__money:
            print("余额不足")
        else:
            self.__money -= x
            print("账户剩余",self.__money,"元")

c1 = Bank(10)
c1.save(200)
c1.withdraw(105)


# def create_counter(money = 0):
#     def save(x):
#         nonlocal money
#         money += x
#         print("账户有",money,"元")
#     def withdraw(x):
#         nonlocal money
#         if x > money:
#             print("余额不足")
#         else:
#             money -= x
#             print("账户剩余",money,"元")
#     return save,withdraw


# save_money1,withdraw1 = create_counter(100)
# save_money1(200)
# withdraw1(300)
# withdraw1(1)


# save_money2,withdraw2 = create_counter(0)
# save_money2(50)
# withdraw2(100)

