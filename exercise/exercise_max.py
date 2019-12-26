"""
题目：使用迭代查询一个list中的最大值和最小值，也就是自己实现max()和min()函数
"""
def max(list_argument):
    num_max = list_argument[0]
    iterator = list_argument.__iter__()
    while True:
        try:
            item = iterator.__next__()
            if item > num_max:
                num_max = item
        except StopIteration:
            return num_max

def min(list_argument):
    num_min = list_argument[0]
    iterator = list_argument.__iter__()
    while True:
        try:
            item = iterator.__next__()
            if item < num_min:
                num_min = item
        except StopIteration:
            return num_min

if __name__ == "__main__":
    list_target = [1,0,2,9,3,8,4,7,5,6]
    print(max(list_target))
    print(min(list_target))
