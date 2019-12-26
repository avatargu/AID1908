def verify_account(func):
    def wrapper(*args,**kwargs):
        print("验证帐号")
        return func(*args,**kwargs)
    return wrapper

@verify_account
def deposit(money):
    print("存%d元钱"%money)
@verify_account
def withdraw(account_number,password):
    print(account_number,password,"取钱")

deposit(10000)
withdraw("abc",123)