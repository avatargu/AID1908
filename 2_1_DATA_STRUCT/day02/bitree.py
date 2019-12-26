"""
二叉树的链式存储

递归
"""
from lqueue import *

class BitreeError(Exception):
    pass

# 二叉树节点类
class Node:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left   # 左连接
        self.right = right # 右连接

# 二叉树遍历类
class Bitree:
    def __init__(self,root = None):
        self.root = root

    # 先序遍历：根左右
    def preOrder(self,node):
        if node is None:
            return
        
        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历：左根右
    def inOrder(self,node):
        if node is None:
            return
        
        self.inOrder(node.left)
        print(node.value)
        self.inOrder(node.right)

    # 后序遍历：左右根
    def sufOrder(self,node):
        if node is None:
            return
        
        self.sufOrder(node.left)
        self.sufOrder(node.right)
        print(node.value)

    """
    层次遍历思想：
    
        A 入队
        A 出队 B 入队 C 入队
        B 出队 C 出队 D 入队 E 入队
        D 出队 F 入队 G 入队 E 出队 H 入队 I 入队
        F 出队 G 出队 H 出队 I 出队 
        
        根节点先入队，
        谁出队遍历谁，
        左右孩子入队，
        直到队列为空。
    """
    def levelOrder(self,node):
        lq = LQueue()

        lq.enqueue(node) # 根节点先入队

        while not lq.is_empty():       # 直到队列为空
            node = lq.dequeue()        # 谁出队
            print(node.value)          # 遍历谁

            if node.left:
                lq.enqueue(node.left)  # 左孩子入队
            if node.right:
                lq.enqueue(node.right) # 右孩子入队

if __name__ == "__main__":
    """
    二叉树：
        =================       
            A
        ↓       ↓
        B       C
            ↓       ↓
            D       E
         ↓     ↓ ↓      ↓
         F     G H      I           
        =================              
    """

    # 根据后续遍历构建二叉树
    b = Node("B")
    f = Node("F")
    g = Node("G")
    d = Node("D",f,g)
    i = Node("I")
    h = Node("H")
    e = Node("E",h,i)
    c = Node("C",d,e)
    a = Node("A",b,c)

    bi_tree = Bitree(a)

    print("先序遍历：")
    bi_tree.preOrder(bi_tree.root)
    print("中序遍历：")
    bi_tree.inOrder(bi_tree.root)
    print("后序遍历：")
    bi_tree.sufOrder(bi_tree.root)
    print("层次遍历：")
    bi_tree.levelOrder(bi_tree.root)
