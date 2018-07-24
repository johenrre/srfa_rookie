import random
import stackqueue

'''
2, 实现如下接口
s = Stack2(n)
s.push1
s.pop1
s.push2
s.pop2

s 包含 2 个 stack
内部是用一个长度为 n 的数组实现的
2 个 stack 个数之和不为 n 时, 两者都不会出错
要求 push 和 pop 的时间复杂度都是 O(1)
'''
def test_Stack2():
    q = stackqueue.Stack2(5)
    q.push1(4)
    q.push1(2)
    q.push1(3)
    q.push1(1)
    q.push1(5)
    a = q.data
    s = 'test_Stack2 failed ({})'.format(a)
    assert str([4, 2, 3, 1, 5]) == str(a), s
"""
3, 用两个 stack 实现一个 queue, 并分析 dequeue 和 enqueue 的时间复杂度
dequeue 和 enqueue的 时间复杂相同操作的第一次是O(n), 之后同样操作是O(1).
"""
def test_Queue_stack2():
    q = stackqueue.Queue_stack2()
    q.enqueue(4)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(1)
    q.enqueue(5)
    a = q.dequeue()
    s = 'test_Queue_stack2 failed ({})'.format(a)
    assert str(4) == str(a), s
    # 时间复杂相同操作的第一次是O(n), 之后同样操作是O(1).
"""
4, 用两个 queue 实现一个 stack, 并分析 push 和 pop 的时间复杂度
    push是O(1), pop永远是O(n), 空间复杂度也翻倍
"""
def test_Stack_queue2():
    q = stackqueue.Stack_queue2()
    q.push(4)
    q.push(2)
    q.push(3)
    q.push(1)
    q.push(5)
    a = q.pop()
    s = 'test_Stack_queue2 failed ({})'.format(a)
    assert str(5) == str(a), s

"""
5, 双端队列(deque)是一种插入和删除都可以在两端进行的数据结构,
写出 4 个时间复杂度均为 O(1) 的函数
分别实现双端队列的两端插入和删除的操作
该队列是用一个数组实现的
deque.push_front
deque.pop_frontD
deque.push_back
deque.pop_back
"""
def test_Double_Deque():
    q = stackqueue.Double_Deque()
    q.push_front(4)
    q.push_front(2)
    q.push_back(3)
    q.push_back(1)
    a = q.pop_frontD()
    b = q.pop_back()
    s = 'test_Double_Deque failed ({})'.format(a)
    assert str(2) == str(a), s

    s = 'test_length1 failed ({})'.format(b)
    assert str(1) == str(b), s

"""
6, 实现 StackSet, 它内部由多个容量为 3 的 stack 组成, 并且在前一个栈填满时新建一个 stack
接口如下
s = StackSet(n)
s.push
s.pop
"""
def test_StackSet():
    q = stackqueue.StackSet()
    q.push(4)
    q.push(2)
    q.push(3)
    q.push(1)
    a = q.pop()
    s = 'test_StackSet failed ({})'.format(a)
    assert str(1) == str(a), s

"""
7, 为 StackSet 添加一个 pop_from(index) 方法
index 是指定的子栈下标
"""
def test_pop_from():
    q = stackqueue.StackSet()
    q.push(4)
    q.push(2)
    q.push(3)
    q.push(1)
    q.push(8)
    q.push(7)
    q.push(6)
    a = q.pop_from(2).pop()
    s = 'test_pop_from failed ({})'.format(a)
    assert str(7) == str(a), s

"""
8, 设计一个符合下面复杂度的栈
push    O(1)
pop     O(1)
min     O(1) 返回栈中的最小元素

思路： 链表的栈在有头和尾指针的情况，push和pop复杂度本来就是O(1)
考虑2 4 3 1 四个依次入栈的数字。在我们维护的min数据中，我们不需要保存1 2 3 4， 事实上，
由于栈只能按照1 3 4 2的顺序出栈，4和3永远也不会成为最小的数。也就是说，我们在维护min数据时，
只需在遇到一个新的最小数据（即比当前的最小数据更小或相等）时，
我们就将遇到的最小数据放在当前的最小数据前面(这个数据结构可用栈来维护)。
这样我们在以上入栈序列2 4 3 1中，先保存最小数据2 遇到4 3时不改变，遇到1时，将1 放在2的前面。这样在弹出序列1 3 4 2时，
如果弹出的数据是当前最小数据，我们就将该数据在min维护的数据结构中删除掉，例如在弹出1时，min序列就只剩下2，
而由于2永远在3 4之后弹出，因此它理所当然在弹出它本身之前是最小的。另外还要注意重复最小数，比如入栈序列1 3 2 1。
在弹出1之后，最小元素仍然是1，也就是说，最小栈在遇到与当前最小元素相等的元素时，也应该更新。
"""
def test_Stack_Min():
    q = stackqueue.Stack_Min()
    q.push(2)
    q.push(4)
    q.push(3)
    q.push(1)
    a = q.minElement()
    s = 'Stack_Min1 failed ({})'.format(a)
    assert str(1) == str(a), s

    q.pop()
    b = q.minElement()
    s = 'Stack_Min2 failed ({})'.format(b)
    assert str(2) == str(b), s
"""
9, 给定一个字符串其中包含无数个圆括号和其他字符，使用栈来确定圆括号是匹配的
本题不理解题意的话要在 slack、群 中问清楚
思路：  进zai， 出zai问题。 做过
"""
def test_parentheses_matching():
    c = '(fsfdfs(fsfsdf(fsdfs()fff)ww)fff(fsfa)(fsdf))fwqw'
    a = stackqueue.bracket_matching(c, '(', ')')
    s = 'test_parentheses_matching failed ({})'.format(a)
    assert str(True) == str(a), s

    # m.matching(c, 2)

"""
10, 给定一个字符串其中包含无数个圆括号、方括号和其他字符，使用栈来确定圆括号和方括号是匹配的
本题不理解题意的话要在 slack、群 中问清楚
思路就是多个zai把
"""
def test_ymbol_matching():
    c = '(fsfdfs(fs{}fs{df(fsdfs()fff)ww)fff(fsfa)(fsdf))fwqw'
    a = stackqueue.ymbol_matching(c)
    s = 'test_ymbol_matching failed ({})'.format(a)
    assert str(False) == str(a), s

if __name__ == '__main__':
    test()
