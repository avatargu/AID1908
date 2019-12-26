"""
题目：
    一球从100米的高度自由落下,每次落地后反弹回原高度的一半,再落下...
    求它在第10次落地时,共经过多少米?
    第10次反弹多高?
"""
def rebound_height(times):
    """
    第times次反弹的高度
    :param times: 第times次反弹
    :return: 反弹的高度
    """
    height = 100
    return height * 0.5 ** times

def go_by(times):
    """
    第times次落地时共经过多少米
    :param times: 第times次落地
    :return: 共经过多少米
    """
    height = 100

    distance = 0
    for i in range(times):
        distance += rebound_height(i) * 2

    return distance - height

if __name__ == "__main__":
    print(rebound_height(10))
    print(go_by(10))
