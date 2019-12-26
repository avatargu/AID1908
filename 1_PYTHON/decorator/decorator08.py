import time

def print_execution_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        stop_time = time.time()
        print("执行时间是：",stop_time - start_time)
        return result
    return wrapper

@print_execution_time
def func01():
    print("func01执行开始")
    time.sleep(2)
    print("func01执行结束")

@print_execution_time
def func02(a):
    print("func02执行开始，参数是：",a)
    time.sleep(1)
    print("func02执行结束，参数是：",a)

func01()
func02(100)




































