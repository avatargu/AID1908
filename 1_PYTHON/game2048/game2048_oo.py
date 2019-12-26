"""
    2048项目
"""
import random
import copy


class MapController:
    """
        地图控制器
    """

    def __init__(self):
        self.list_map = []
        for i in range(4):
            list_map1 = []
            for j in range(4):
                list_map1.append(0)
            self.list_map.append(list_map1)

    @staticmethod
    def zero_to_end(list_targer):
        """
            列表中零元素移动到末尾
        :param list_targer:列表元素
        """
        for i in range(len(list_targer) - 1, -1, -1):
            if list_targer[i] == 0:
                del list_targer[i]
                list_targer.append(0)

    @staticmethod
    def zero_to_start(list_targer):
        """
            列表中零元素移动到前端
        :param list_targer:列表元素
        """
        for i in range(0, len(list_targer)):
            if list_targer[i] == 0:
                del list_targer[i]
                list_targer.insert(0, 0)

    @staticmethod
    def merge(list_targer):
        """
            列表中相同元素相加，只加一次
        :param list_targer:列表元素
        """
        # 列表中零元素移动到末尾
        MapController.zero_to_end(list_targer)
        # 对比相邻的数据，如果相同就相加
        for i in range(0, len(list_targer) - 1):
            if list_targer[i] == list_targer[i + 1]:
                list_targer[i] *= 2
                del list_targer[i + 1]
                list_targer.append(0)

    def move_left(self):
        """
            矩形列表左移
        :param list_map: 矩形列表元素
        """
        for i in range(len(self.list_map)):
            MapController.merge(self.list_map[i])

    def move_right(self):
        """
            矩形列表右移
        :param list_map: 矩形列表元素
        """
        for i in range(len(self.list_map)):
            MapController.merge(self.list_map[i])
            # 列表中零元素移动到前端
            MapController.zero_to_start(self.list_map[i])

    @staticmethod
    def rectangle_change(list_map_tar):
        """
            矩形列表行列互换
        :param list_map:     矩形列表元素
        """
        for i in range(0, len(list_map_tar) - 1):
            for j in range(i + 1, len(list_map_tar)):
                list_map_tar[i][j], list_map_tar[j][i] = list_map_tar[j][i], list_map_tar[i][j]

    def move_up(self):
        """
            矩形列表上移
        :param list_map: 矩形列表元素
        """
        # 矩形列表行列互换
        MapController.rectangle_change(self.list_map)
        # 矩形列表左移
        MapController.move_left(self)
        # 矩形列表行列互换
        MapController.rectangle_change(self.list_map)

    def move_down(self):
        """
            矩形列表右移
        :param list_map: 矩形列表元素
        """
        # 矩形列表行列互换
        MapController.rectangle_change(self.list_map)
        # 矩形列表右移
        MapController.move_right(self)
        # 矩形列表行列互换
        MapController.rectangle_change(self.list_map)

    def find_zero(self):
        """
            查找界面中所有为0的数据，并存入列表中
        :return: 0数据坐标的列表
        """
        list01 = []
        # 将所有为0的元素存入列表中
        for i in range(len(self.list_map)):
            for j in range(len(self.list_map)):
                if self.list_map[i][j] == 0:
                    list01.append([i, j])
        return list01

    def random_map(self):
        """
            随机将一个是0的位置变成2（95%的概率）或者4（5%概率）
        :param list_map: 矩形列表元素
        """
        list01 = self.find_zero()
        # 当还有0位置的时候，随机抽中其中一个0变成2（95%的概率）或者4（5%概率）
        if len(list01) > 0:
            random01 = random.randint(0, len(list01) - 1)
            self.list_map[list01[random01][0]][list01[random01][1]] = (
                2 if random.randint(1, 100) < 95 else 4)

    def contrast_map(self, list_map_tar):
        """
            对比上一次界面是否一致
        :param list_map: 矩形列表元素
        """
        for i in range(len(list_map_tar)):
            for j in range(len(list_map_tar)):
                if list_map_tar[i][j] != self.list_map[i][j]:
                    return False
        return True

    @staticmethod
    def __confirmation(list_map_tar):
        adding = True
        for i in range(len(list_map_tar)):
            for j in range(0, len(list_map_tar) - 1):
                if list_map_tar[i][j] == list_map_tar[i][j + 1]:
                    adding = False
        return adding

    def add_confirmation(self, list_map_tar):
        """
            测试在没有0位置的情况下，是否有相邻相同数字
        :param list_map_tar:
        :return: 输出是否有相同的数字
        """
        list_map_tar = copy.deepcopy(self.list_map)
        # 判断行中是否有相邻相邻的数字
        adding = MapController.__confirmation(list_map_tar)
        # 判断列中是否有相邻相邻的数字
        MapController.rectangle_change(list_map_tar)
        adding1 = MapController.__confirmation(list_map_tar)
        MapController.rectangle_change(list_map_tar)
        # 行与列都没有为True，否则False
        return True if adding and adding1 else False


class MapView:
    """
        游戏图像界面
    """
    # 控制退出图像界面
    quit_tar = 0

    def __init__(self):
        self.__map = MapController()
        self.__map.random_map()
        self.__map.random_map()

    def print_map(self):
        """
            打印矩形数据
        :param list_map: 矩形列表元素
        """
        for i in self.__map.list_map:
            for j in i:
                print(j, end="\t")
            print("")

    def __map_menu(self):
        """
            界面输出到屏幕
        """
        print("1).上移，2).下移，3).左移，4).右移")

    def __select_menu(self):
        """
            根据需求选择界面选项
        """
        i = input("请输入菜单编号：")
        if i == "1":
            self.__move_map(1)
        elif i == "2":
            self.__move_map(2)
        elif i == "3":
            self.__move_map(3)
        elif i == "4":
            self.__move_map(4)
        else:
            self.quit_tar = 1

    def __move_map(self, value):
        """
            游戏结束规则
        :param value:判断移动方向
        """
        list01 = copy.deepcopy(self.__map.list_map)
        # 判断是否没有0，并且所有相邻的数字也没有
        if len(self.__map.find_zero()) == 0 and self.__map.add_confirmation(list01):
            self.quit_tar = 1
        else:
            if value == 1:
                self.__map.move_up()
            elif value == 2:
                self.__map.move_down()
            elif value == 3:
                self.__map.move_left()
            elif value == 4:
                self.__map.move_right()
        # 如果移动后，上一个界面于下一个界面没有变化，则不会多出数字
        if not self.__map.contrast_map(list01):
            self.__map.random_map()
        self.print_map()

    def main(self):
        """
            程序入口
        """
        self.print_map()
        while True:
            if self.quit_tar == 1:
                print("游戏结束！")
                break
            self.__map_menu()
            self.__select_menu()


# 游戏开始
MapView().main()
