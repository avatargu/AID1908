"""
冒泡排序：

i : 0
j : 0 1 2 3 4 5 6 7 8
    0⇌1 1⇌2 2⇌3 3⇌4 4⇌5 5⇌6 6⇌7 7⇌8 8⇌9
    结果：第一大的数排到了倒数第一
i : 1
j : 0 1 2 3 4 5 6 7
    0⇌1 1⇌2 2⇌3 3⇌4 4⇌5 5⇌6 6⇌7 7⇌8
    结果：第二大的数排到了倒数第二
i : 2
j : 0 1 2 3 4 5 6
    0⇌1 1⇌2 2⇌3 3⇌4 4⇌5 5⇌6 6⇌7
    结果：第三大的数排到了倒数第三
i : 3
j : 0 1 2 3 4 5
    0⇌1 1⇌2 2⇌3 3⇌4 4⇌5 5⇌6
    结果：第四大的数排到了倒数第四
i : 4
j : 0 1 2 3 4
    0⇌1 1⇌2 2⇌3 3⇌4 4⇌5
    结果：第五大的数排到了倒数第五
i : 5
j : 0 1 2 3
    0⇌1 1⇌2 2⇌3 3⇌4
    结果：第六大的数排到了倒数第六
i : 6
j : 0 1 2
    0⇌1 1⇌2 2⇌3
    结果：第七大的数排到了倒数第七
i : 7
j : 0 1
    0⇌1 1⇌2
    结果：第八大的数排到了倒数第八
i : 8
j : 0
    0⇌1
    结果：第九大的数排到了倒数第九
"""

def bubble(list_number):
    n = len(list_number)
    for i in range(n - 1):         # 一共比较多少轮
        for j in range(n - 1 - i): # 每轮比较多少次
            if list_number[j] > list_number[j + 1]:
                list_number[j],list_number[j + 1] = list_number[j + 1],list_number[j]

if __name__ == "__main__":
    list_number = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
    bubble(list_number)
    print(list_number)
