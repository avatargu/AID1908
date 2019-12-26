# 经典排序

list_number = [1,0,2,9,3,8,4,7,5,6]

for x in range(len(list_number)-1):
    for y in range(x + 1,len(list_number)):
        if list_number[x] < list_number[y]:
            list_number[x],list_number[y] = list_number[y],list_number[x]
print(list_number)
