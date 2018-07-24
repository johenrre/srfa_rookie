import random
import linkedlist1


"""
需要你自己补全其他的个测试
"""

def test_length():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    a = linkedlist1.length(List)
    s = 'test_length1 failed ({})'.format(a)
    assert str(1) == str(a), s

    linkedlist1.append(List, '2')
    a = linkedlist1.length(List)
    s = 'test_length2 failed ({})'.format(a)
    assert str(2) == str(a), s

    linkedlist1.append(List, '3')
    a = linkedlist1.length(List)
    s = 'test_length3 failed ({})'.format(a)
    assert str(3) == str(a), s

def test_last_node():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    value = linkedlist1.last_node(List).value
    s = 'test_last_node1 failed ({})'.format(value)
    assert str(1) == str(value), s

    linkedlist1.append(List, '2')
    value = linkedlist1.last_node(List).value
    s = 'test_last_node2 failed ({})'.format(value)
    assert str(2) == str(value), s

    linkedlist1.append(List, '3')
    value = linkedlist1.last_node(List).value
    s = 'test_last_node3 failed ({})'.format(value)
    assert str(3) == str(value), s

def test_kth_node():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')

    value = linkedlist1.kth_node(List, 1).value
    s = 'test_last_node1 failed ({})'.format(value)
    assert str(1) == str(value), s

    value = linkedlist1.kth_node(List, 2).value
    s = 'test_last_node2 failed ({})'.format(value)
    assert str(2) == str(value), s

    value = linkedlist1.kth_node(List, 3).value
    s = 'test_last_node3 failed ({})'.format(value)
    assert str(3) == str(value), s

def test_n_last():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')

    value = linkedlist1.n_last(List, 1).value
    s = 'test_n_last1 failed ({})'.format(value)
    assert str(3) == str(value), s

    value = linkedlist1.n_last(List, 2).value
    s = 'test_n_last2 failed ({})'.format(value)
    assert str(2) == str(value), s

    value = linkedlist1.n_last(List, 3).value
    s = 'test_n_last3 failed ({})'.format(value)
    assert str(1) == str(value), s

def test_has_x():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')

    value = linkedlist1.has_x(List, '1')
    s = 'test_has_x1 failed ({})'.format(value)
    assert str(True) == str(value), s

    value = linkedlist1.has_x(List, '2')
    s = 'test_has_x2 failed ({})'.format(value)
    assert str(True) == str(value), s

    value = linkedlist1.has_x(List, '4')
    s = 'test_has_x3 failed ({})'.format(value)
    assert str(False) == str(value), s

def test_middle():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')

    value = linkedlist1.middle(List).value
    s = 'test_middle1 failed ({})'.format(value)
    assert str(1) == str(value), s

    linkedlist1.append(List, '2')
    value = linkedlist1.middle(List)
    s = 'test_middle2 failed ({})'.format(value)
    assert str(None) == str(value), s

    linkedlist1.append(List, '3')
    value = linkedlist1.middle(List).value
    s = 'test_middle3 failed ({})'.format(value)
    assert str(2) == str(value), s

def test_append():
    List = linkedlist1.LinkedList()

    linkedlist1.append(List, '2')
    value = linkedlist1.last_node(List).value
    s = 'test_append1 failed ({})'.format(value)
    assert str(2) == str(value), s

    linkedlist1.append(List, '4')
    value = linkedlist1.last_node(List).value
    s = 'test_append2 failed ({})'.format(value)
    assert str(4) == str(value), s

    linkedlist1.append(List, '3')
    value = linkedlist1.last_node(List).value
    s = 'test_append3 failed ({})'.format(value)
    assert str(3) == str(value), s

def test_prepend():
    List = linkedlist1.LinkedList()
    linkedlist1.prepend(List, '1')
    linkedlist1.prepend(List, '2')
    linkedlist1.prepend(List, '3')

    value = linkedlist1.kth_node(List, 1).value
    s = 'test_test_prepend1 failed ({})'.format(value)
    assert str(3) == str(value), s

    value = linkedlist1.kth_node(List, 2).value
    s = 'test_test_prepend2 failed ({})'.format(value)
    assert str(2) == str(value), s

    value = linkedlist1.kth_node(List, 3).value
    s = 'test_test_prepend3 failed ({})'.format(value)
    assert str(1) == str(value), s

def test_insert_after():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '5')

    linkedlist1.insert_after(List, 1, '2')
    value = linkedlist1.kth_node(List, 2).value
    s = 'test_insert_after failed ({})'.format(value)
    assert str(2) == str(value), s

    linkedlist1.insert_after(List, 3, '4')
    value = linkedlist1.kth_node(List, 4).value
    s = 'test_insert_after2 failed ({})'.format(value)
    assert str(4) == str(value), s

def test_insert_last_n():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '4')

    linkedlist1.insert_last_n(List, 2, '2')
    value = linkedlist1.kth_node(List, 2).value
    s = 'test_insert_after failed ({})'.format(value)
    assert str(2) == str(value), s

def test_delete_n():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '4')

    List = linkedlist1.delete_n(List, 3)
    value = linkedlist1.last_node(List).value
    s = 'test_delete_n failed ({})'.format(value)
    assert str(3) == str(value), s

def test_delete_x():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '4')

    linkedlist1.delete_x(List, '3')
    value = linkedlist1.kth_node(List, 2).value
    s = 'test_delete_x failed ({})'.format(value)
    assert str(4) == str(value), s

def test_delete_last_n():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '4')

    linkedlist1.delete_last_n(List, 2)
    value = linkedlist1.kth_node(List, 2).value
    s = 'test_delete_last_n failed ({})'.format(value)
    assert str(4) == str(value), s

def test_reverse():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '4')

    rList = linkedlist1.reverse(List)
    # linkedlist1.log(rList)
    # 4 3 2 1

def test_is_palindrome():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '1')

    value = linkedlist1.is_palindrome(List)
    s = 'test_has_x1 failed ({})'.format(value)
    assert str(True) == str(value), s

    linkedlist1.append(List, '3')
    value = linkedlist1.is_palindrome(List)
    s = 'test_has_x1 failed ({})'.format(value)
    assert str(False) == str(value), s

    linkedlist1.append(List, '4')
    value = linkedlist1.is_palindrome(List)
    s = 'test_has_x1 failed ({})'.format(value)
    assert str(False) == str(value), s

def test_is_circle():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')

    value = linkedlist1.is_circle(List)
    s = 'test_has_x1 failed ({})'.format(value)
    assert str(False) == str(value), s

    node = linkedlist1.last_node(List)
    node.next = List.head.next
    value = linkedlist1.is_circle(List)
    s = 'test_has_x1 failed ({})'.format(value)
    assert str(True) == str(value), s

def test_copy():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')

    # cList = linkedlist1.copy(List)
    # linkedlist1.log(cList)
    # 1 2 3

def test_power_copye():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '4')
    linkedlist1.append(List, '5')
    linkedlist1.append(List, '6')
    linkedlist1.append(List, '7')
    linkedlist1.append(List, '8')

    node8 = linkedlist1.last_node(List)
    node5 = linkedlist1.kth_node(List, 5)

    node8.next = node5
  #             6
  #           7    5
  # 1  2  3   4  8
    cList = linkedlist1.power_copy(List)

    value = linkedlist1.kth_node(List, 11).value
    s = 'test_has_x1 failed ({})'.format(value)
    assert str(7) == str(value), s

def test_merge_list():
    List1 = linkedlist1.LinkedList()
    linkedlist1.append(List1, '1')
    linkedlist1.append(List1, '3')
    linkedlist1.append(List1, '5')

    List2 = linkedlist1.LinkedList()
    linkedlist1.append(List2, '2')
    linkedlist1.append(List2, '4')
    linkedlist1.append(List2, '6')

    List3 = linkedlist1.merge_list(List1, List2)
    # linkedlist1.log(List3)
    # 1 2 3 4 5 6

def test_joseph_list():
    List = linkedlist1.LinkedList()
    linkedlist1.append(List, '1')
    linkedlist1.append(List, '2')
    linkedlist1.append(List, '3')
    linkedlist1.append(List, '4')
    linkedlist1.append(List, '5')
    linkedlist1.append(List, '6')
    linkedlist1.append(List, '7')
    linkedlist1.append(List, '8')
    linkedlist1.append(List, '9')

    lNode = linkedlist1.last_node(List)
    lNode.next = List.head
    ######创建环链表
    l = linkedlist1.joseph_list(List, 9)
    # linkedlist1.log(l)
    # least  4










if __name__ == '__main__':
    test()
