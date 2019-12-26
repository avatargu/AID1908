"""
    列表助手模块
"""
class ListHelper:
    """
        列表助手类
    """
    @staticmethod
    def get_all(list_target, func_condition):
        """
            在列表中查找符合某个条件的所有元素
        :param list_target: 列表
        :param func_condition: 条件
        :return: 元素
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def get_one(list_target, func_condition):
        """
            在列表中查找符合某个条件的第一个元素
        :param list_target: 列表
        :param func_condition: 条件
        :return: 元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_quantity(list_target, func_condition):
        """
            统计列表里符合某个条件的元素数量
        :param list_target: 列表
        :param func_condition: 条件
        :return: 数量
        """
        counter = 0
        for item in list_target:
            if func_condition(item):
                counter += 1
        return counter

    @staticmethod
    def is_in(list_target, func_condition):
        """
            判断某个符合某个条件的元素是否在列表中
        :param list_target: 列表
        :param func_condition: 条件
        :return: 真假
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def get_sum(list_target, func_property):
        """
            求列表里所有元素某个属性的和
        :param list_target: 列表
        :param func_property: 属性
        :return: 和
        """
        sum_result = 0
        for item in list_target:
            sum_result += func_property(item)
        return sum_result

    @staticmethod
    def get_max(list_target, func_property):
        """
            求列表里某个属性最大的元素
        :param list_target: 列表
        :param func_property: 属性
        :return: 元素
        """
        max_result = list_target[0]
        for item in range(1,len(list_target)):
            if func_property(max_result) < func_property(list_target[item]):
                max_result = list_target[item]
        return max_result

    @staticmethod
    def get_min(list_target, func_property):
        """
            求列表里某个属性最小的元素
        :param list_target: 列表
        :param func_property: 属性
        :return: 元素
        """
        max_result = list_target[0]
        for item in range(1,len(list_target)):
            if func_property(max_result) > func_property(list_target[item]):
                max_result = list_target[item]
        return max_result

    @staticmethod
    def get_property(list_target, func_property):
        """
            获得列表里所有元素的某个属性
        :param list_target: 列表
        :param func_property: 属性
        :return: 属性
        """
        for item in list_target:
            yield func_property(item)

    @staticmethod
    def sorted_by_property(list_target, func_property):
        """
            根据属性升序排列列表
        :param list_target: 列表
        :param func_property: 属性
        """
        for row in range(len(list_target) - 1):
            for column in range(row + 1,len(list_target)):
                if func_property(list_target[row]) > func_property(list_target[column]):
                    list_target[row],list_target[column] = list_target[column],list_target[row]

    @staticmethod
    def sorted_reverse(list_target, func_property):
        """
            根据属性降序排列列表
        :param list_target: 列表
        :param func_property: 属性
        """
        for row in range(len(list_target) - 1):
            for column in range(row + 1,len(list_target)):
                if func_property(list_target[row]) < func_property(list_target[column]):
                    list_target[row],list_target[column] = list_target[column],list_target[row]

    @staticmethod
    def remove_all(list_target, func_condition):
        """
            删除列表里所有满足条件的元素
        :param list_target: 列表
        :param func_condition: 条件
        :return: 操作后的列表
        """
        for i in range(len(list_target) - 1,-1,-1):    # 正索引，倒删除，
            if func_condition(list_target[i]):
                # list_target.remove(list_target[i])
                del list_target[i]
















