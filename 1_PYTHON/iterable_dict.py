dict01 = {"a":1,"b":2,"c":3,"d":4,"e":5}
# １，获取迭代器
iterator = dict01.__iter__()
# ２，循环获取下一个元素
while True:
    try:
        key = iterator.__next__()
        print(key,dict01[key])
    # ３，遇到异常停止迭代
    except StopIteration:
        break