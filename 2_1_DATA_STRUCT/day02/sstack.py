"""
顺序栈：顺序存储（重点代码）
"""
# 自定义异常类
class StackError(Exception):
    pass

class SStack:
    def __init__(self):
        """
        将列表的最后一个元素作为栈顶，效率高
        """
        self._elements = [] # 初始化一个空列表

    def is_empty(self):
        """
        判断栈是否为空
        """
        return self._elements == []

    def push(self,value):
        """
        入栈
        """
        self._elements.append(value)

    def pop(self):
        """
        出栈
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elements.pop()

    def set_top(self,value):
        """
        修改栈顶元素
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        self._elements[-1] = value

    def get_top(self):
        """
        查看栈顶元素
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elements[-1]

if __name__ == "__main__":
    sstack = SStack()
    sstack.push(10)
    sstack.push(20)
    sstack.push(30)
    while not sstack.is_empty():
        print(sstack.pop())

    print("==========")

    sstack.push(10)
    sstack.push(20)
    sstack.push(30)
    print(sstack.get_top())
    sstack.set_top(300)
    print(sstack.get_top())
