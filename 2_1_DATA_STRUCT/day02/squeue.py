"""
顺序队列：顺序存储（重点代码）
"""
# 自定义异常类
class QueueError(Exception):
    pass

class SQueue:
    def __init__(self):
        """
        将列表的第一个元素作为队头，效率低
        将列表的最后一个元素作为队尾，效率高
        """
        self._elements = []

    def is_empty(self):
        """
        判断队列是否为空
        """
        return self._elements == []

    def enqueue(self,value):
        """
        队尾入队,高效
        """
        self._elements.append(value)

    def dequeue(self):
        """
        队头出队,低效
        """
        if self.is_empty():
            raise QueueError("Queue is empty")
        return self._elements.pop(0)

if __name__ == "__main__":
    squeue = SQueue()
    squeue.enqueue(10)
    squeue.enqueue(20)
    squeue.enqueue(30)
    while not squeue.is_empty():
        print(squeue.dequeue())
