"""
快速排序：

[1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
[0, 1, 2, 9, 3, 8, 4, 7, 5, 6]
[0, 1, 2, 9, 3, 8, 4, 7, 5, 6]
[0, 1, 2, 9, 3, 8, 4, 7, 5, 6]
[0, 1, 2, 9, 3, 8, 4, 7, 5, 6]
[0, 1, 2, 6, 3, 8, 4, 7, 5, 9]
[0, 1, 2, 5, 3, 4, 6, 7, 8, 9]
[0, 1, 2, 4, 3, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def sub_sort(list_number,low,high):
    """
    将比第一个数小的数放在第一个数的左边，
    将比第一个数大的数放在第一个数的右边，
    第一个数在有序列表中的位置也就确定了，
    同时形成两个子列表
    :param list_number:目标列表
    :param low:        待排序的第一个数在列表中的位置
    :param high:       待排序的最后一个数在列表中的位置
    :return:           第一个数在有序列表中的位置
    """

    x = list_number[low] # 在第一个数的位置生成第一个空位

    # 外层while 循环左移每个比第一个数小的数，右移每个比第一个数大的数
    while low < high: # 若 low 等于 high, 则完成列表分割

        # 内层 while 循环左移一个比第一个数小的数
        while list_number[high] >= x and high > low: # 遇到比第一个数小的数
            high -= 1                                # 从后往前遍历
        list_number[low] = list_number[high]         # 填补旧空位生成新空位

        # 内层 while 循环右移一个比第一个数大的数
        while list_number[low] < x and low < high: # 遇到比第一个数大的数
            low += 1                               # 从前往后遍历
        list_number[high] = list_number[low]       # 填补旧空位，生成新空位

    list_number[low] = x # 用第一个数填补最后一个空位

    return low # 第一个数在有序列表中的位置

def quick(list_number,low,high):
    """
    快速排序
    :param list_number:目标列表
    :param low:        待排序的第一个数在列表中的位置
    :param high:       待排序的最后一个数在列表中的位置
    """

    # print(list_number)

    if low < high: # 若 low 等于 high, 则完成快速排序

        key = sub_sort(list_number,low,high) # 函数调用，分割列表并返回列表分割位置

        quick(list_number,low,key - 1) # 递归调用，列表分割位置减一作为左子列表的最后一个数的位置
        quick(list_number,key + 1,high) # 递归调用，列表分割位置加一作为右子列表的第一个数的位置

if __name__ == "__main__":
    list_number = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
    quick(list_number, 0, len(list_number) - 1)
    print("快速排序结果：",list_number)
