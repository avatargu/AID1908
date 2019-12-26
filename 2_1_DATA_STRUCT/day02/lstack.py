"""
链式栈：链式存储（重点代码）
"""
# 自定义异常类
class StackError(Exception):
    pass

# 自定义节点类
class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class LStack:
    def __init__(self):
        """
        将链表的第一个元素作为栈顶，效率高
        """
        self._top = None # 初始化一个空指针

    def is_empty(self):
        """
        判断栈是否为空
        """
        return self._top is None

    def push(self,value):
        """
        入栈
        """
        # 三步法：
        # node = Node(value)
        # node.next = self._top
        # self._top = node
        # 一步法：
        self._top = Node(value,self._top)

    def pop(self):
        """
        出栈
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        result = self._top.value
        self._top = self._top.next
        return result

    def set_top(self,value):
        """
        修改栈顶元素
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        self._top.value = value

    def get_top(self):
        """
        查看栈顶元素
        """
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._top.value
    
if __name__ == "__main__":
    lstack = LStack()
    lstack.push(10)
    lstack.push(20)
    lstack.push(30)
    while not lstack.is_empty():
        print(lstack.pop())

    print("==========")

    lstack.push(10)
    lstack.push(20)
    lstack.push(30)
    print(lstack.get_top())
    lstack.set_top(300)
    print(lstack.get_top())
