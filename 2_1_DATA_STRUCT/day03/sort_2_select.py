"""
选择排序：

i : 0
    index_min = 0
j : 1 2 3 4 5 6 7 8 9
    1⇌index_min 2⇌index_min 3⇌index_min 4⇌index_min 5⇌index_min 6⇌index_min 7⇌index_min 8⇌index_min 9⇌index_min
    结果：第一小的数排到了顺数第一
i : 1
    index_min = 1
j : 1 2 3 4 5 6 7 8
    1⇌index_min 2⇌index_min 3⇌index_min 4⇌index_min 5⇌index_min 6⇌index_min 7⇌index_min 8⇌index_min
    结果：第二小的数排到了顺数第二
i : 2
    index_min = 2
j : 1 2 3 4 5 6 7
    1⇌index_min 2⇌index_min 3⇌index_min 4⇌index_min 5⇌index_min 6⇌index_min 7⇌index_min
    结果：第三小的数排到了顺数第三
i : 3
    index_min = 3
j : 1 2 3 4 5 6
    1⇌index_min 2⇌index_min 3⇌index_min 4⇌index_min 5⇌index_min 6⇌index_min
    结果：第四小的数排到了顺数第四
i : 4
    index_min = 4
j : 1 2 3 4 5
    1⇌index_min 2⇌index_min 3⇌index_min 4⇌index_min 5⇌index_min
    结果：第五小的数排到了顺数第五
i : 5
    index_min = 5
j : 1 2 3 4
    1⇌index_min 2⇌index_min 3⇌index_min 4⇌index_min
    结果：第六小的数排到了顺数第六
i : 6
    index_min = 6
j : 1 2 3
    1⇌index_min 2⇌index_min 3⇌index_min
    结果：第七小的数排到了顺数第七
i : 7
    index_min = 7
j : 1 2
    1⇌index_min 2⇌index_min
    结果：第八小的数排到了顺数第八
i : 8
    index_min = 8
j : 1
    1⇌index_min
    结果：第九小的数排到了顺数第九
"""

def select(list_number):
    n = len(list_number)
    for i in range(n - 1):
        index_min = i         # 初始台主
        for j in range(i + 1,n):
            if list_number[j] < list_number[index_min]:
                index_min = j # 更换台主
        if index_min != i:
            list_number[i],list_number[index_min] = list_number[index_min],list_number[i]

if __name__ == "__main__":
    list_number = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
    select(list_number)
    print(list_number)
