"""
    2048游戏核心算法
"""

def zeros_to_end(list_merge):
    """
        将一行中的零元素移动到末尾
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

def merge(list_merge):
    """
        将一行中相同的数字合并
    """
    zeros_to_end(list_merge)
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)

# map_move = [
#     [2,0,0,2],
#     [4,4,2,2],
#     [2,4,0,4],
#     [0,0,2,2]
# ]

def move_left(map_move):
    """
        地图向左移动
    """
    for line in map_move:
        merge(line)

def move_right(map_move):
    """
        地图向右移动
    """
    for line in map_move:
        line.reverse()
        merge(line)
        line.reverse()

def transpose(map_move):
    """
        矩阵转置
    """
    for row in range(len(map_move) - 1):
        for column in range(row + 1, len(map_move)):
            map_move[row][column],map_move[column][row] = map_move[column][row],map_move[row][column]

def move_up(map_move):
    """
        地图向上移动
    """
    transpose(map_move)
    move_left(map_move)
    transpose(map_move)

def move_down(map_move):
    """
        地图向下移动
    """
    transpose(map_move)
    move_right(map_move)
    transpose(map_move)

