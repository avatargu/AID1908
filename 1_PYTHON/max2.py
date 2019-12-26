# 经典排序！
# for x in range(len(list_number)-1):
#     for y in range(x + 1,len(list_number)):
#         if list_number[x] < list_number[y]:
#             list_number[x],list_number[y] = list_number[y],list_number[x]
# print(list_number)

# 求第二大的数：方法１
"""
5 9 8 -> 5 8 9
5 9 2 -> 5 2 9 -> 2 5 9
"""
# if list_number[0] > list_number[1]:
#     max1 = list_number[0]
#     max2 = list_number[1]
#     list_number[0],list_number[1] = list_number[1],list_number[0]
# else:
#     max1 = list_number[1]
#     max2 = list_number[0]
#
# for x in range(1,len(list_number)-1):
#     if list_number[x] < list_number[x + 1]:
#         max1 = list_number[x + 1]
#         max2 = list_number[x]
#     else:
#         if list_number[x - 1] < list_number[x + 1]:
#             max2 = list_number[x + 1]
#             list_number[x],list_number[x + 1] = list_number[x + 1],list_number[x]
#         else:
#             list_number[x],list_number[x + 1] = list_number[x + 1],list_number[x]
#             list_number[x - 1],list_number[x] = list_number[x],list_number[x - 1]
# print(list_number)
# print(list_number[-2])

# list_number = [1,0,2,8,3,9,4,7,5,6]
list_number = [-1,0,-2,-8,-3,-9,-4,-7,-5,-6]

# 求第二大的数：方法２
largest = list_number[0]
second = list_number[1]
for i in range(1,len(list_number)):
    if largest < list_number[i]:
        second = largest
        largest = list_number[i]
    elif second < list_number[i] < largest:
        second = list_number[i]

print(largest)
print(second)














