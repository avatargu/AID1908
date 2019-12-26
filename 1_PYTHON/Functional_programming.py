list_fibonacci = [1,1,2,3,5,8,13,21,34,55]

def get_numbers(list_target,func_condition):
    for item in list_target:
        if func_condition(item):
            yield item

def func_condition_even(item):
    return item % 2 == 0
def func_condition_ten_plus(item):
    return item > 10
def func_condition_ten_fifty(item):
    return 10 < item < 50

for item in get_numbers(list_fibonacci,func_condition_even):
    print(item)
for item in get_numbers(list_fibonacci,func_condition_ten_plus):
    print(item)
for item in get_numbers(list_fibonacci,func_condition_ten_fifty):
    print(item)
































