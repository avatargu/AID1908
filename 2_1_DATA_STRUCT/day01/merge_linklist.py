"""
合并两个有序链表
"""
from linklist import *

def merge_linklist(linklist01,linklist02):
    """
    将第二个有序链表合并到第一个有序链表中，结果仍然是有序链表
    :param linklist01: 第一个有序链表
    :param linklist02: 第二个有序链表
    :return: None
    """
    p = linklist01.head # 初始指向结果有序链表的头结点
    q = linklist02.head.next

    """
    思想：
        ================================
         p
         ↓
        None → 0 → 1 → 2       6 → 7 → 8
                       ↓       ↑       ↓
                None → 3 → 4 → 5       9
                       ↑
                       q
        ================================    
                       p       q
                       ↓
        None → 0 → 1 → 2       6 → 7 → 8
                       ↓       ↑       ↓
                None → 3 → 4 → 5       9
                       ↑
                       p  
        ================================                         
    """
    while p.next is not None:
        if p.next.value < q.value:
            p = p.next   # 前进一步
        else:
            t = p.next   # 保存 linklist01 的下半段
            p.next = q   # linklist01 的上半段连接 linklist02
            q = t        # linklist01 的下半段当做 linklist02

            p = p.next   # 前进一步
    else:
        p.next = q       # linklist01 连接 linklist02

if __name__ == "__main__":
    linklist01 = LinkList()
    linklist02 = LinkList()
    linklist01.init_list([0,1,2,6,7,8])
    linklist02.init_list([3,4,5,9])

    print(" ----------before merge---------- ")
    print(" linklist01: ")
    linklist01.show()
    print(" linklist02: ")
    linklist02.show()

    print(" ----------after merge---------- ")
    merge_linklist(linklist01,linklist02)
    print(" linklist01: ")
    linklist01.show()
    print(" linklist02: ")
    linklist02.show()
