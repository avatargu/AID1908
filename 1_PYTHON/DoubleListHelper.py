class Vector2:
    """
        二维向量：表示位置或方向
    """
    # 位置
    def __init__(self,row,column):
        self.row = row
        self.column = column

    # 方向：左
    @staticmethod
    def left():
        return Vector2(0,-1)

    # 方向：右
    @staticmethod
    def right():
        return Vector2(0,1)

    # 方向：上
    @staticmethod
    def up():
        return Vector2(-1,0)

    # 方向：下
    @staticmethod
    def down():
        return Vector2(1,0)

    # 方向：左上
    @staticmethod
    def left_up():
        return Vector2(-1,-1)

    # 方向：右上
    @staticmethod
    def right_up():
        return Vector2(-1,1)

    # 方向：左下
    @staticmethod
    def left_down():
        return Vector2(1,-1)

    # 方向：右下
    @staticmethod
    def right_down():
        return Vector2(1,1)


class DoubleListHelper:
    @staticmethod
    def get_elements(target,vect_pos,vect_dir,count):
        """
            在二维列表中，获取指定位置，指定方向，指定数量的元素
        :param target: 二维列表
        :param vect_pos: 位置
        :param vect_dir: 方向
        :param count: 数量
        :return: 元素列表
        """
        list_result = []
        for i in range(count):
            # 新位置 = 旧位置 + 方向
            vect_pos.row += vect_dir.row
            vect_pos.column += vect_dir.column
            element = target[vect_pos.row][vect_pos.column]
            list_result.append(element)
        return list_result

if __name__ == "__main__":
    list01 = [
        ["00", "01", "02", "03"],
        ["10", "11", "12", "13"],
        ["20", "21", "22", "23"],
        ["30", "31", "32", "33"]
    ]
    re = DoubleListHelper.get_elements(list01,Vector2(1,3),Vector2.left(),3)
    print(re)
    re = DoubleListHelper.get_elements(list01,Vector2(2,2),Vector2.up(),2)
    print(re)
    re = DoubleListHelper.get_elements(list01,Vector2(0,3),Vector2.down(),2)
    print(re)