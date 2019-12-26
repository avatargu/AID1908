"""
哈夫曼编码(Huffman Code)：

目标字符串：
string = "aaaabbbccd"

权值：
a 的权值是 4
b 的权值是 3
c 的权值是 2
d 的权值是 1

权值替换字符：
[4,3,2,1]

建立哈夫曼树：
第一步：取1,2构造树，根节点为1+2=3
第二步：取3,3构造树，根节点为3+3=6
第三步：取6,4构造树，根节点为6+4=10

哈夫曼树(Huffman Tree)：
给定N个权值作为N个叶子结点，
构造一棵二叉树，
若该树的带权路径长度达到最小，
称这样的二叉树为最优二叉树，
也称为哈夫曼树。
                (10)
            0↓       1↓
            (6)      (4)
        0↓       1↓
        (3)      (3)
    0↓      1↓
    (1)     (2)
哈夫曼树是带权路径长度最短的树，
权值较大的结点离根较近。

字符替换权值：
                (10)
            0↓       1↓
            (6)      (a)
        0↓       1↓
        (3)      (b)
    0↓      1↓
    (d)     (c)

哈夫曼编码：
a 1
b 01
c 001
d 000

结果：
1111010101001001000

优点：
从10个字节到3个字节
"""

from bitree import *

class HTNode(Node):
    def __lt__(self, other): # 比较 HTNode 实例对象就是比较 HTNode 实例对象的属性 value
        return self.value < other.value

def huffman_tree(weights):
    trees = [HTNode(w) for w in weights]

    while len(trees) > 1:
        trees.sort() # 改变原列表

        t1 = trees.pop(0)
        t2 = trees.pop(0)
        new_w = t1.value + t2.value
        trees.append(HTNode(new_w,t1,t2))

    return trees[0]

if __name__ == "__main__":
    # a = HTNode(3)
    # b = HTNode(4)
    # print(a < b)
    weights = [12,27,33,18,10] # 优占12%,良占27%,中占33%,差占18%,不及格占10%
    root = huffman_tree(weights)
    print("先序遍历：")
    Bitree(root).preOrder(root)
