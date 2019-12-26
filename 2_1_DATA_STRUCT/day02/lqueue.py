"""
链式队列：链式存储（重点代码）
"""
# 自定义异常类
class QueueError(Exception):
    pass

# 自定义节点类
class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class LQueue:
    def __init__(self):
        """
        将链表的第一个元素作为队头，效率高
        将链表的最后一个元素作为队尾，效率高

        当队头和队尾重叠时，队列空
        """
        self._front = self._rear = Node(None) # 初始化一个空节点

    def is_empty(self):
        """
        判断队列是否为空(难点)
        """
        return self._front == self._rear

    def enqueue(self,value):
        """
        队尾入队,高效
        """
        self._rear.next = Node(value) # 入队的值
        self._rear = self._rear.next # 后移指针

    def dequeue(self):
        """
        队头出队,高效
        """
        if self.is_empty():
            raise QueueError("Queue is empty")

        self._front = self._front.next # 后移指针
        return self._front.value # 出队的值

if __name__ == "__main__":
    lqueue = LQueue()
    lqueue.enqueue(10)
    lqueue.enqueue(20)
    lqueue.enqueue(30)
    while not lqueue.is_empty():
        print(lqueue.dequeue())
