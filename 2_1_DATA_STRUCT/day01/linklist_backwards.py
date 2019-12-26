"""
单链表（重点代码）
"""
class Node:
    """
    抽象的 Node 类
    具体的 Person 类
    """
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self):
        """
        头节点：
            value 永远为 None
            next  永远指向第一个有效节点
        """
        self.head = Node(None)

    def init_list(self,list_init):
        """
        从列表到链表
        """
        p = self.head # 指向头节点 ****************
        for item in list_init:
            p.next = Node(item)
            p = p.next

    def show(self):
        """
        遍历链表
        """
        p = self.head.next # 指向第一个有效节点 ****************
        while p is not None: # 判断对象用 is,判断值用 ==
            print(p.value)
            p = p.next

    def is_empty(self):
        """
        判断链表是否为空
        """
        if self.head.next is None:
            return True
        return False

    def clear(self):
        """
        清空链表
        """
        self.head.next = None

    def append(self,value): ###### 增 1 ######
        """
        尾部插入
        """
        # p = self.head # 头节点法 ****************
        # while p.next is not None:
        #     p = p.next
        # p.next = Node(value)

        p = self.head.next # 第一个有效节点法 ****************
        while p is not None:
            p = p.next
        p = Node(value)

    def head_insert(self,value): ###### 增 2 ######
        """
        头部插入
        """
        # 三步法：
        # node = Node(value)
        # node.next = self.head.next
        # self.head.next = node

        # 一步法：
        self.head.next = Node(value,self.head.next)

    def insert(self,index,value): ###### 增 3 ######
        """
        指定位置插入：
            负数则头插
            大数则尾插
        """
        p = self.head # 头节点法 ****************
        for i in range(index): # 负数则头插
            if p.next is None: # 大数则尾插
                break
            p = p.next

        # 三步法：
        node = Node(value)
        node.next = p.next
        p.next = node

    def remove(self,value): ###### 删 ######
        """
        删除节点：
            按值删除(YES)
            按索引删除(NO)
        """
        p = self.head
        while p.next and p.next.value != value: # 两个条件：只有当第一个条件为真时，第二个条件才不报错
            p = p.next

        if p.next is None:                      # 第一个条件
            raise ValueError("value not in linklist")
        else:                                   # 第二个条件
            p.next = p.next.next

    def set(self,index,value): ###### 改 ######
        """
        修改节点
        """
        p = self.head.next
        if p is None:
            raise IndexError("linklist index out of range")

        for i in range(index):
            if p.next is None:
                raise IndexError("linklist index out of range")
            p = p.next

        p.value = value

    def get(self,index): ###### 改 ######
        """
        获取节点：
            负数则头值
            大数则尾值
        """
        p = self.head.next
        if p is None:
            raise IndexError("linklist index out of range")

        for i in range(index):
            if p.next is None:
                raise IndexError("linklist index out of range")
            p = p.next

        return p.value

if __name__ == "__main__":
    # 创建链表
    linklist01 = LinkList()
    linklist01.init_list([0,1,2,3,4,5,6,7,8,9])

    # 转为列表
    list_tmp = []
    for i in range(10):
        list_tmp.append(linklist01.get(i))

    # 输出链表倒数第k个节点的值
    k = int(input("Please input your index:"))
    print(list_tmp[-k])
