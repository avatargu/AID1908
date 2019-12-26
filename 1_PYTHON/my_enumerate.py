list01 = [0,1,4,9,16,25,36,49,64,81]

for item in enumerate(list01):
    print(item)
for index,element in enumerate(list01):
    print(index,element)

print(enumerate(list01))
print(list(enumerate(list01)))
print(list(enumerate(list01,start = 1)))

print("##########################################")


def my_enumerate(my_iterable):
    i = 0
    for item in my_iterable:
        yield i,item
        i += 1

list01 = [0,1,4,9,16,25,36,49,64,81]
for item in my_enumerate(list01):
    print(item)
for index,element in enumerate(list01):
    print(index,element)










