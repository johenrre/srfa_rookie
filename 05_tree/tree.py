import math

"""
本次作业周日晚上 22:00 回收

本次作业目录结构
srfa/05_tree/tree.py
srfa/05_tree/test_tree.py
srfa/05_tree/watcher.py



本次作业是 tree 相关的题目和 stack queue 相关的应用题目

有问题多讨论！
自己想出解法是基本没有意义的，最重要的是把这道题的解法过一遍有个印象
想着独创的人最终都学得不太好，因为抓不住重点
我会把一些我认为难的题目直接写出解题思路，不要自己强行硬刚不看思路

本次使用下面的结构，和 List 一样是只有节点没有主类
你应该写几个辅助函数方便你写代码和测试
具体哪些辅助函数，不懂就问

Class TreeNode:
    def __init__(n):
        self.value = n
        self.left = None
        self.right = None

参考：
https://blog.csdn.net/Bone_ACE/article/details/46718683

1, 用递归实现二叉树的中序遍历算法

2, 用递归实现二叉树的后序遍历算法

3, 用递归实现二叉树的前序遍历算法

4, 用队列实现广度优先算法，注明时空复杂度

5, 用栈实现深度优先算法，注明时空复杂度

6, 用非递归算法实现二叉树的中序遍历

7, 递归翻转二叉树

8, 检查二叉树是否是镜像对称的

9, 给定一个二叉树，找出其最大深度

10, 对于一棵有 n 个节点的二叉树, 请设计在 θ(n) 时间内完成先序遍历算法和后序遍历算法
    θ(n) 的含义是，去除了常数的 O(n), 也就是说 θ(n) 就是确定的 n
    在这里意思是一次遍历得到先序和后序的结果

11, 选做，能否用栈实现广度优先？优势是什么？
"""
class TreeNode:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)
        pass

    def pop(self):
        #pop 删除并返回最新添加的元素
        index = len(self.data) - 1
        r = self.data[index]
        self.data = self.data[:index]
        return r
        pass

class Queue:
    def __init__(self):
        self.data = []
        self.capacity = 999

    def enqueue(self, element):
        length = self.length()
        if length < self.capacity:
            self.data.append(element)
        else:
            return '上溢'
            pass
        pass

    def dequeue(self):
        # 把第一个元素删除并返回, splice 返回的是数组
        length = self.length()
        if length > 0:
            r = self.data[0]
            self.data = self.data[1:]
            return r
        else:
            return '下溢'
            pass
        pass

class Tree:
    def __init__(self):
        self.root = Node(-1)
        self.myQueue = []

    def add(self, value):
        """为树添加节点"""
        node = Node(value)
        if self.root.value == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print root.elem,
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print root.elem,
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print root.elem,

    def DFS(self, value):
        """
        https://zh.wikipedia.org/zh-hans/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2
        Depth-First-Search, 用栈实现深度优先算法，注明时空复杂度
        1 首先将根节点放入队列中。
        2 从队列中取出第一个节点，并检验它是否为目标。
            如果找到目标，则结束搜寻并回传结果。
            否则将它某一个尚未检验过的直接子节点加入队列中。
        3 重复步骤2。
        4 如果不存在未检测过的直接子节点。
            将上一级节点加入队列中。
            重复步骤2。
        5 重复步骤4。
        6 若队列为空，表示整张图都检查过了——亦即图中没有欲搜寻的目标。结束搜寻并回传“找不到目标
        """
        stack = Stack()
        stack.push(self.root)
        while len(stack.data) != 0:
            n = stack.pop()
            v = n.value
            if v == value:
                return n
                pass


            pass
       pass

    def BFS(self, node):
        """
        https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2
        readth-First-Search, 用队列实现广度优先算法，注明时空复杂度
        1 首先将根节点放入队列中。
        2 从队列中取出第一个节点，并检验它是否为目标。
            如果找到目标，则结束搜索并回传结果。
            否则将它所有尚未检验过的直接子节点加入队列中。
        3 若队列为空，表示整张图都检查过了——亦即图中没有欲搜索的目标。结束搜索并回传“找不到目标”。
        4 重复步骤2。
        """
        pass
