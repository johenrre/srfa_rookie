import random
import linkedlist2
import linkedlist1


"""
需要你自己补全其他的个测试
"""
def test_length():
    List = linkedlist2.LinkedList()
    linkedlist2.append(List, 4)
    linkedlist2.append(List, 3)
    linkedlist2.append(List, 1)
    linkedlist2.append(List, 5)
    linkedlist2.append(List, 8)
    linkedlist2.append(List, 9)

    l = linkedlist2.rearrange(List, 7)
    # linkedlist2.log(l)
    # 5 1 3 4 9 8
    # s = 'test_length1 failed ({})'.format(a)
    # assert str(1) == str(a), s

def test_circle_head():
    List = linkedlist2.LinkedList()
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '2')
    linkedlist2.append(List, '3')
    linkedlist2.append(List, '4')
    linkedlist2.append(List, '5')
    linkedlist2.append(List, '6')
    linkedlist2.append(List, '7')
    linkedlist2.append(List, '8')

    a = linkedlist2.circle_head(List)
    s = 'test_length1 failed ({})'.format(a)
    assert str(None) == str(a), s
    #制造环形链表
    node8 = linkedlist1.last_node(List)
    node5 = linkedlist1.kth_node(List, 5)
    node8.next = node5
  #             6
  #           7    5
  # 1  2  3   4  8
    a = linkedlist2.circle_head(List).value
    s = 'test_length1 failed ({})'.format(a)
    assert str(5) == str(a), s

def test_reorder():
    List = linkedlist2.LinkedList()
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '2')
    linkedlist2.append(List, '3')
    linkedlist2.append(List, '4')
    linkedlist2.append(List, '5')
    linkedlist2.append(List, '6')

    a = linkedlist2.reorder(List)
    #linkedlist1.log(a)
    # 1 2 6 3 5 4

def test_rotate_list():
    List = linkedlist2.LinkedList()
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '2')
    linkedlist2.append(List, '3')
    linkedlist2.append(List, '4')
    linkedlist2.append(List, '5')

    a = linkedlist2.rotate_list(List, 6)
    # linkedlist1.log(a)
    # 4 5 1 2 3

def test_rotate_list():
    List = linkedlist2.LinkedList()
    linkedlist2.append(List, '4')
    linkedlist2.append(List, '2')
    linkedlist2.append(List, '5')
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '3')
    linkedlist2.append(List, '6')

    a = linkedlist2.sort_list(List)
    # linkedlist1.log(a)
    # 1 2 3 4 5 6

def test_reverse_mn():
    List = linkedlist2.LinkedList()
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '2')
    linkedlist2.append(List, '3')
    linkedlist2.append(List, '4')
    linkedlist2.append(List, '5')
    linkedlist2.append(List, '6')

    a = linkedlist2.reverse_mn(List, 2, 5)
    # linkedlist2.log(a)
    # 1 2 5 4 3 6

def test_deduplication():
    List = linkedlist2.LinkedList()
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '2')
    linkedlist2.append(List, '2')
    linkedlist2.append(List, '5')
    linkedlist2.append(List, '5')
    linkedlist2.append(List, '1')
    linkedlist2.append(List, '2')

    a = linkedlist2.deduplication(List)
    # linkedlist2.log(a)
    # 1 2 5

def test_add_number():
    List1 = linkedlist2.LinkedList()
    List2 = linkedlist2.LinkedList()
    linkedlist2.append(List1, 2)
    linkedlist2.append(List1, 4)
    linkedlist2.append(List1, 3)
    linkedlist2.append(List2, 5)
    linkedlist2.append(List2, 6)
    linkedlist2.append(List2, 4)

    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    a = linkedlist2.add_number(List1, List2)
    # linkedlist2.log(a)
    # 7 -> 0 -> 8

def test_merge_list_k():
    List1 = linkedlist2.LinkedList()
    List2 = linkedlist2.LinkedList()
    List3 = linkedlist2.LinkedList()

    linkedlist2.append(List1, 1)
    linkedlist2.append(List1, 2)
    linkedlist2.append(List1, 3)

    linkedlist2.append(List2, 8)
    linkedlist2.append(List2, 9)
    linkedlist2.append(List2, 10)

    linkedlist2.append(List3, 5)
    linkedlist2.append(List3, 6)
    linkedlist2.append(List3, 7)

    a = linkedlist2.merge_list_k(List1, List2, List3)
    # linkedlist2.log(a)
    #1 2 3 5 6 7 8 9 10


def test_reverse_list_k():
    l = linkedlist2.LinkedList()
    linkedlist2.append(l, 1)
    linkedlist2.append(l, 2)
    linkedlist2.append(l, 3)
    linkedlist2.append(l, 4)
    linkedlist2.append(l, 5)

    l = linkedlist2.reverse_list_k(l, 2)
    # linkedlist2.log(l)
    # 2->1->4->3->5
    l = linkedlist2.reverse_list_k(l, 2)
    l = linkedlist2.reverse_list_k(l, 3)
    # linkedlist2.log(l)
    # 3->2->1->4->5

if __name__ == '__main__':
    test()
