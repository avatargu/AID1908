# 用两个栈形成一个队列
from lstack import *

class DoubleStackQueue:
    def __init__(self):
        """
        将第一个栈的栈顶作为队尾，负责入队
        将第二个栈的栈顶作为队头，负责出队

        两栈皆空，队列空
        """
        self.in_stack = LStack()
        self.out_stack = LStack()

    def is_empty(self):
        """
        判断队列是否为空
        """
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def enqueue(self, value):
        """
        队尾入队
        """
        while not self.out_stack.is_empty(): # 入队先后退
            self.in_stack.push(self.out_stack.pop())

        self.in_stack.push(value)

    def dequeue(self):
        """
        队头出队
        """
        while not self.in_stack.is_empty(): # 出队先前进
            self.out_stack.push(self.in_stack.pop())

        return self.out_stack.pop()

if __name__ == "__main__":
    double_stack_queue01 = DoubleStackQueue()

    print(double_stack_queue01.is_empty())
    double_stack_queue01.enqueue(10)
    double_stack_queue01.enqueue(20)
    double_stack_queue01.enqueue(30)
    print(double_stack_queue01.is_empty())

    print(double_stack_queue01.dequeue())
    print(double_stack_queue01.dequeue())
    print(double_stack_queue01.dequeue())
