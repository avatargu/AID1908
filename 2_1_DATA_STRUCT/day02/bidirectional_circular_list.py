"""
双向循环链表

环
"""
class Node:
    def __init__(self,value,prior=None,next=None):
        self.value = value
        self.prior = prior
        self.next = next

class LinkList:
    def __init__(self):
        """
        单节点环
        """
        self.head = Node(None)
        self.head.prior = self.head.next = self.head

    def init_list(self,list_init):
        """
        从列表到链表
        """
        p = self.head
        for item in list_init:
            # ====================
            # 生成新节点
            node = Node(item)

            # 新节点连接后节点
            node.next = p.next
            # 后节点连接新节点
            p.next.prior = node

            # 头节点连接新节点
            p.next = node
            # 新节点连接头节点
            node.prior = p
            # ====================
            p = p.next

    def show_forward(self):
        """
        正向遍历
        """
        p = self.head.next
        while p != self.head:
            print(p.value)
            p = p.next

    def show_reverse(self):
        """
        反向遍历
        """
        p = self.head.prior
        while p != self.head:
            print(p.value)
            p = p.prior

    def insert(self):
        pass

if __name__ == "__main__":
    link = LinkList()
    link.init_list([1,2,3])
    print("正向遍历：")
    link.show_forward()
    print("反向遍历：")
    link.show_reverse()
