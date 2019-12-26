"""
插入排序：

i : 1
    x = list_number[1]
j : 0
    0⇌1
    结果：前二个排好了序
i : 2
    x = list_number[2]
j : 1 0
    1⇌2 0⇌2
    结果：前三个排好了序
i : 3
    x = list_number[3]
j : 2 1 0
    2⇌3 1⇌3 0⇌3
    结果：前四个排好了序
i : 4
    x = list_number[4]
j : 3 2 1 0
    3⇌4 2⇌4 1⇌4 0⇌4
    结果：前五个排好了序
i : 5
    x = list_number[5]
j : 4 3 2 1 0
    4⇌5 3⇌5 2⇌5 1⇌5 0⇌5
    结果：前六个排好了序
i : 6
    x = list_number[6]
j : 5 4 3 2 1 0
    5⇌6 4⇌6 3⇌6 2⇌6 1⇌6 0⇌6
    结果：前七个排好了序
i : 7
    x = list_number[7]
j : 6 5 4 3 2 1 0
    6⇌7 5⇌7 4⇌7 3⇌7 2⇌7 1⇌7 0⇌7
    结果：前八个排好了序
i : 8
    x = list_number[8]
j : 7 6 5 4 3 2 1 0
    7⇌8 6⇌8 5⇌8 4⇌8 3⇌8 2⇌8 1⇌8 0⇌8
    结果：前九个排好了序
i : 9
    x = list_number[9]
j : 8 7 6 5 4 3 2 1 0
    8⇌9 7⇌9 6⇌9 5⇌9 4⇌9 3⇌9 2⇌9 1⇌9 0⇌9
    结果：前十个排好了序
"""

def insert(list_number):
    n = len(list_number)
    for i in range(1,n):
        x = list_number[i] # 待插入对象
        j = i - 1
        while j >= 0 and list_number[j] > x:
            list_number[j + 1] = list_number[j] # 比待插入对象大则后移
            j -= 1
        list_number[j + 1] = x # 比待插入对象小则插入

if __name__ == "__main__":
    list_number = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
    insert(list_number)
    print(list_number)
