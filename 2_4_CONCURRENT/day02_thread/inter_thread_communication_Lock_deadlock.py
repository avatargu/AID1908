from threading import Thread,Lock
from time import sleep

# 账户类
class Account:
    def __init__(self,name,balance,lock):
        self.name = name
        self.balance = balance # 余额
        self.lock = lock 

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount # 金额

    # 存钱
    def deposit(self,amount):
        self.balance += amount # 金额

    # 查看余额
    def get_balance(self):
        return self.balance

# 马云
Jack = Account("Mayun",800,Lock())
# 马化腾
Pony = Account("Mahuateng",600,Lock())

# 转账
def transfer(account_from,account_to,amount):
    if account_from.lock.acquire(): # account_from账户上锁
        account_from.withdraw(amount)
        # sleep(1) # 增加一句话带来死锁
        if account_to.lock.acquire(): # account_to账户上锁
            account_to.deposit(amount)
            account_to.lock.release() # account_to账户解锁
        account_from.lock.release() # account_from账户解锁，上移一句话去掉死锁
    print("'%s'给'%s'转账%d"%(account_from.name,account_to.name,amount))

t1 = Thread(target = transfer,args = (Jack,Pony,100))
t2 = Thread(target = transfer,args = (Pony,Jack,50))

t1.start()
t2.start()

t1.join()
t2.join()
