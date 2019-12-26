# 延迟销毁
# 动态生成函数
# 封装
# 资源的概念

def make_power(y):
    def pow(x):
        return x ** y
    return pow

pow2 = make_power(2)
print(pow2(3))
del pow2

pow5 = make_power(5)
print(pow5(3))
del pow5








