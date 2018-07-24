import math

"""
本次作业周四晚上 22:00 回收

本次作业目录结构
srfa/02_linkedlist1/linkedlist1.py
srfa/02_linkedlist1/test_linkedlist1.py
srfa/02_linkedlist1/watcher.py



本次作业是链表相关的题目
由于面试和很多地方都不是用的 OOP 方式，所以我们的作业也不是用 OOP（融入 群总是必要的）
这里的 class ListNode 只是定义一个结构
所有的函数都是接受一个 ListNode 作为参数，请注意这一点

例外情况自行处理，这里列出常见例外：
    1，传过来的 node 可能是个 None，但不会是其他类型
测试自行编写，每个函数至少 3 个测试用例


最重要的一点：
有问题多讨论！
自己想出解法是基本没有意义的，最重要的是把这道题的解法过一遍有个印象
想着独创的人最终都学得不太好，因为抓不住重点
我会把一些我认为难的题目直接写出解题思路，不要自己强行硬刚不看思路
"""


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode('head')
        self._length = 0

def length(node):
    # 1, 求单链表中节点的个数
    return node._length

def log(node):
    n = node.head.next
    l = length(node)
    while l > 0:
        print(' > ', n.value)
        l -= 1
        n = n.next
        pass

def last_node(node):
    # 2, 返回单链表的最后一个节点
    n = node.head.next
    if n == None:
        return node.head
        pass

    while n != None:
        if n.next == None:
            break
            pass
        n = n.next
        pass
    return n

def kth_node(node, i):
    # 3, 返回单链表第 n 个节点
    n = node.head.next
    while i > 1:
        n = n.next
        i -= 1
        pass
    return n


def n_last(node, i):
    # 4, 返回单链表倒数第 n 个节点
    return kth_node(node, length(node) - i + 1)

def has_x(node, x):
    # 5, 判断单链表中是否有值为 x 的节点
    n = node.head.next
    while n != None:
        if n.value == x:
            return True
            pass
        n = n.next
        pass
    return False

def middle(node):
    # 6, 查找单链表的中间节点, 长度为偶数则返回 None
    l = length(node)
    if l % 2 == 0:
        return None
    else:
        midIndex = math.ceil(l / 2)
        return kth_node(node, midIndex)
        pass

def append(node, x):
    # 7, 给单链表末尾插入一个元素
    node._length += 1
    lastNode = last_node(node)
    lastNode.next = ListNode(x)
    return node

def prepend(node, x):
    # 8, 给单链表头部插入一个元素
    node._length += 1
    n = node.head.next
    newNode = ListNode(x)
    newNode.next = node.head.next
    node.head.next = newNode
    return node

def insert_after(node, n, x):
    # 9, 给单链表第 n 个节点后插入一个元素
    node._length += 1

    newNode = ListNode(x)

    if n < 1:
        newNode.next = node.head.next
        node.head.next = newNode
    else:
        kth_n = kth_node(node, n)
        newNode.next = kth_n.next
        kth_n.next = newNode
        pass
    return node

def insert_last_n(node, n, x):
    # 10, 给单链表倒数第 n 个节点前插入一个元素
    l = length(node)
    i = l - n
    insert_after(node, i, x)
    return node

def delete_n(node, i):
    # 11, 删除单链表第 n 个节点
    if length(node) == 0:
        return
        pass

    node._length -= 1
    n = node.head.next

    if n == 1:
        node.head.next = n.next
    else:
        kth_n = kth_node(node, i - 1)
        kth_n.next = kth_n.next.next
        pass
    return node

def delete_x(node, x):
    # 12, 删除单链表中值为 x 的节点
    index = []
    n = node.head.next
    i = 1
    while n != None:
        if n.value == x:
            index.append(i)
            pass
        i += 1
        n = n.next
        pass

    for item in index:
        delete_n(node, item)

    return node

def delete_last_n(node, n):
    # 13, 删除单链表倒数第 n 个节点
    l = length(node)
    delete_n(node, l - n)

def prependNode(List, node):
    List._length += 1

    n = List.head.next
    List.head.next = node
    node.next = n

def reverse(List):
    # 14, 返回反转后的单链表
    # 从第2个节点到第N个节点，依次逐节点插入到第1个节点(head节点)之后，最后将第一个节点挪到新表的表尾。

    #元素链表第一个节点
    p1 = List.head.next
    head = List.head

    while p1.next != None:
        p2 = p1.next
        p1.next = p2.next

        p2.next = head.next
        head.next = p2
        pass
    return List


def is_palindrome(node):
    # 15, 判断一个链表是否是回文链表
    #该方法时间复杂度O(n)、空间复杂度O(1).
    #另想办法，找到链表中点，
    minNode = middle(node)
    if minNode == None:
        return False
        pass

    #然后一个将后半部分就地反转，
    leftList = LinkedList()
    leftList.head.next = minNode.next
    leftList = reverse(leftList)
    #分别再从头、中点遍历判断是否相等，
    l = math.floor(length(node) / 2)

    for i in range(1, l - 1):
        a = kth_node(node, i)
        b = kth_node(leftList, i)
        if a != b:
            return False
            pass
        pass

    return True

def is_circle(node):
    # 16, 判断一个链表是否是环形链表
    # 本题用双指针, a 一次走一格 b 一次走两格，如果相遇说明有环形
    n = node.head.next
    a = n.next
    b = n.next.next

    while b != None:
        if a.value == b.value:
            return True
            pass

        if b.next == None:
            return False
            pass

        a = a.next
        b = b.next.next
        pass
    return False



def copy(node):
    # 17, 返回一个单链表的复制
    cList = LinkedList()
    n = node.head.next

    while n != None:
        append(cList, n.value)
        n = n.next
        pass

    return cList

def power_copy(node):
    # 18, 返回一个环形链表的复制
    # 判断环形链表的开始：
    # <1> 定义两个指针p1和p2，在初始化时都指向链表的头节点。
    # <2> 如果链表中的环有n个节点，指针p1先在链表上向前移动n步。
    # <3> 然后指针p1和p2以相同的速度在链表上向前移动直到它们相遇。
    # <4> 它们相遇的节点就是环的入口节点。
    n = node.head.next
    hSize = 4   #环的大小
    p1 = kth_node(node, hSize + 1)
    p2 = n
    hNode = {}   #环开始节点

    while hSize > 0:
        p1 = p1.next
        p2 = p2.next
        if p1.value == p2.value:
            hNode = p1
            pass
        hSize -= 1
        pass

    cList = LinkedList()
    in_circle = False

    while n != None:
        append(cList, n.value)
        if n.value == hNode.value:
            if in_circle == False:
                in_circle = True
            else:
                return cList
                pass
            pass
        n = n.next
        pass

# def appendNode(List, node):


def merge_list(node1, node2):
    # 19, 合并两个有序链表并保持有序
    n1 = node1.head.next
    n2 = node2.head.next

    while n1 != None:
        i = 0
        while n2 != None:
            v1 = n1.value
            v2 = n2.value
            if v1 < v2 :
                insert_after(node2, i, v1)
                break
                pass
            i += 1
            n2 = n2.next
            pass
        n1 = n1.next
        n2 = node2.head.next
        i = 0
        pass

    return node2

def joseph_list(node, m):
    # 20, 本题是约瑟夫环问题
    # 1, 2, 3 ..., n 这 n 个数字排成一个圆圈, 所以 node 是一个环形链表的表头
    # 从数字 1 开始每次从这个圆圈里删除第 m 个数字
    # 求出这个圆圈里剩下的最后一个数字
    for i in range(1, m):
        delete_n(node, i)
        pass

    return node
