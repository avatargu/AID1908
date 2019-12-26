"""
二分查找：有序数列（列表，元组）
"""

def search(list_number,key):
    """
    在有序数列中查找目标数字的索引
    :param list_number: 有序数列
    :param key:         待查数字
    :return:            待查数字在有序数列中的索引
    """
    low,high = 0,len(list_number)-1 # 获取最小索引和最大索引
    while low <= high:              # 注意等号不能少
        middle = (low + high) // 2  # 获取中间索引
        if list_number[middle] < key:
            low = middle + 1
        elif list_number[middle] > key:
            high = middle - 1
        else:
            return middle

if __name__ == "__main__":
    list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("key index:", search(list_number, 0))

    tuple_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("key index:", search(tuple_number, 9))





