import math

import linkedlist1

"""
本次作业周日晚上 18:00 回收

本次作业目录结构
srfa/03_linkedlist2/linkedlist2.py
srfa/03_linkedlist2/test_linkedlist2.py
srfa/03_linkedlist2/watcher.py



本次作业是链表相关的更多题目
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

def log(node):
    n = node.head.next
    while n != None:
        print(' > ', n.value)
        n = n.next
        pass
    print('end')

def append(node, x):
    # 7, 给单链表末尾插入一个元素
    node._length += 1
    lastNode = linkedlist1.last_node(node)
    lastNode.next = ListNode(x)
    return node

def prependNode(List, node):
    h = List.head
    List._length += 1
    node.next = h.next
    h.next = node
    return List


def rearrange(node, x):
    # 1
    # 给一个单链表和一个值 x, 对它进行分割, 使得所有小于 x 的节点都在节点大于或等于 x 之前,
    # 新建俩个链表，一个存放小于x的节点，另一个存放大于等于x的节点。最后将链表和在一起。就得到结果
    l1 = LinkedList() #大于x的链表
    l2 = LinkedList()

    h = node.head
    n = node.head.next
    while h.next != None:
        h.next = n.next
        v = n.value
        if v >= x:
            prependNode(l1, n)
        else:
            prependNode(l2, n)
            pass
        n = h.next
        pass

    l1._length += l2._length
    ln = linkedlist1.last_node(l2)
    ln.next = l1.head.next
    l1.head.next = l2.head.next
    return l1

def circle_head(node):
    # 2
    # 给一个链表, 返回环形链表中环形开始的节点, 如果没有环形, 返回 None
    # <1> 定义两个指针p1和p2，在初始化时都指向链表的头节点。
    # <2> 如果链表中的环有n个节点，指针p1先在链表上向前移动n步。
    # <3> 然后指针p1和p2以相同的速度在链表上向前移动直到它们相遇。
    # <4> 它们相遇的节点就是环的入口节点。
    # 那么如何得到环中的节点数目？可使用上述方法（1），即通过一快一慢两个指针来解决这个问题。当两个指针相遇时，表明链表中存在环。
    # 两个指针相遇的节点一定是在环中。可以从这个节点出发，一边继续向前移动一边计数，当再次回到这个节点时，即可得到环中的节点数了。

    #1. 判断是不是环形
    p1 = node.head.next
    p2 = p1.next

    jd = {}  # p1和p2的交点

    while p2.next != None:
        v1 = p1.value
        v2 = p2.value
        if v1 == v2:
            jd = p1
            break
            pass
        p1 = p1.next
        p2 = p2.next.next
        pass

    if jd == {}:
        return None
        pass

    hSize = 1  #环的长度
    n = jd.next
    while jd.value != n.value:
        hSize += 1
        n = n.next
        pass

    hNode = {}   #环开始节点\

    p1 = linkedlist1.kth_node(node, hSize + 1)
    p2 = node.head.next
    while hSize > 0:
        p1 = p1.next
        p2 = p2.next
        if p1.value == p2.value:
            hNode = p1
            pass
        hSize -= 1
        pass
    return hNode


def reorder(node):
    # 3
    # 给一个链表, 将原链表 L0 -> L1 -> L2 -> ... -> Ln-1 -> ln 排序为
    # L0 -> L1 -> Ln -> L2 -> Ln-1 -> ...
    # 要求: 不能修改节点的值
    l = linkedlist1.length(node)
    if (l % 2) == 0:
        l -= 1
        pass
    count = math.floor(l / 2)    #插入次数
    # 1 3, 2 5, 3 7, 4 8
    index = 2
    for i in range(count):
        #得到最后一个node， 删除他
        sn = linkedlist1.n_last(node, 2)  #返回倒数第二个
        ln = sn.next                       #最后一个node
        #插入到 node 【index】 后面
        iNode = linkedlist1.kth_node(node, index)
        ln.next = iNode.next
        iNode.next = ln

        index += 2
        pass

    return node


def rotate_list(node, k):
    # 4
    # 给一个链表, 将列表向右旋转 k 个下标, 其中 k 是非负数
    # 例子:
    #     Input: 1->2->3->4->5->NULL, k = 2
    #     Output: 4->5->1->2->3->NULL
    #     Input: 0->1->2->NULL, k = 4
    #     Output: 2->0->1->NULL
    l = linkedlist1.length(node)
    if l < k:
        k = k % l
        pass

    i = l - k
    iNode = linkedlist1.kth_node(node, i)
    lNode = linkedlist1.last_node(node)

    h = node.head

    lNode.next = h.next
    h.next = iNode.next
    iNode.next = None

    return node

def sort_list(node):
    # 5
    # 给一个链表, 将链表排序
    # 要求: 时间复杂度为 O(n log n)
    l = linkedlist1.length(node)
    if l <= 1:
        return node
        pass

    pivotIndex = math.floor(l / 2)
    pivot = linkedlist1.kth_node(node, pivotIndex)

    left = LinkedList()  #xiao
    right = LinkedList()  #da

    h = node.head
    n = h.next
    while n != None:
        h.next = n.next
        if n.value > pivot.value:
            prependNode(right, n)
        else:
            prependNode(left, n)
            pass
        n = h.next
        pass

    #递归排序2个链表
    left = sort_list(left)
    right = sort_list(right)
    #合并2个链表
    nn = linkedlist1.merge_list(left, right)
    return nn

def reverse_mn(node, m, n):
    # 6
    # 给一个单链表和正整数 m, n(m < n), 从 m 到 n 开始反转
    mNode = linkedlist1.kth_node(node, m)
    nNode = linkedlist1.kth_node(node, n)
    l1 = LinkedList()
    l2 = LinkedList()

    l1.head.next = mNode.next
    l2.head.next = nNode.next
    nNode.next = None

    l1 = linkedlist1.reverse(l1)
    mNode.next = l1.head.next
    return linkedlist1.merge_list(node, l2)

def sort_repeat(List, node):
    # 如果node.value不包含在List里， append到List后面
    n = List.head.next
    v2 = node.value
    while n != None:
        v1 = n.value
        if v1 == v2:
            return List
            pass
        n = n.next
        pass

    linkedlist1.append(List, v2)
    return List

def deduplication(node):
    # 7
    # 给一个有序的单链表, 删除所有有重复 value 的节点, 只留下原始列表中不同的 value
    n = node.head.next
    list = LinkedList()

    while n != None:
        list = sort_repeat(list, n)
        n = n.next
        pass

    return list

def add_number(a, b):
    # 8
    # 给两个非空且长度不一定相同的单链表, 表示两个非负整数
    # 数字以相反的顺序存储(个位在前), 每个节点都包含一个 value, 将两个 value 相加并返回链表
    l = LinkedList()
    n1 = a.head.next
    n2 = b.head.next
    jinwei = False
    while n1 != None or n2 != None:
        v1 = 0
        v2 = 0
        if n1 != None:
            v1 = n1.value
            pass

        if n2 != None:
            v2 = n2.value
            pass

        v = (v1 + v2)

        if jinwei:
            v += 1
            jinwei = False
            pass

        if v >= 10:
            jinwei = True
            pass

        v = v % 10

        n = linkedlist1.append(l, v)

        n1 = n1.next
        n2 = n2.next
        pass

    return l

def merge_list_k(*args):
    # 9
    # 合并 k 个有序链表并保证有序，要求时间复杂度最优，不会就讨论，乱写没价值
    # args 是一个包含 k 个链表的数组
    # print('test', args[1], args[0], args[2])
    l = args[0]
    length = len(args)
    for i in range(length - 1):
        l = linkedlist1.merge_list(l, args[i + 1])
        pass

    return l

def reverse_list_k(node, k):
    # 10
    # k 个一组反转链表(25)
    #     给一个链表, 以每 k 个为一组来翻转链表
    #     例子:
    #         Given this linked list: 1->2->3->4->5
    #
    #         k = 2, return: 2->1->4->3->5
    #
    #         k = 3, return: 3->2->1->4->5
    ln = linkedlist1.kth_node(node, k)
    l = LinkedList()
    l._length = k
    n = node.head.next
    l.head.next = n

    node.head.next = ln.next
    ln.next = None

    l = linkedlist1.reverse(l)

    ln = linkedlist1.last_node(l)
    ln.next = node.head.next

    return l
