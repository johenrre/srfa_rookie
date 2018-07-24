import math

"""
本次作业周四晚上 22:00 回收

本次作业目录结构
srfa/04_stackqueue/stackqueue.py
srfa/04_stackqueue/test_stackqueue.py
srfa/04_stackqueue/watcher.py



本次作业是 stack queue 相关的初步题目，下次是高级题目
这些题目得用 OOP 的方式做

最重要的一点：
有问题多讨论！
自己想出解法是基本没有意义的，最重要的是把这道题的解法过一遍有个印象
想着独创的人最终都学得不太好，因为抓不住重点
我会把一些我认为难的题目直接写出解题思路，不要自己强行硬刚不看思路

由于 s q 的实现都很简单大家可以不用浪费时间，内部用 list 外面暴露相应的接口就好
"""
class Stack2:
    def __init__(self, n):     #constructor
        self.size = n
        self.data = [None] * n
        self.top1 = -1
        self.top2 = self.size
        #  为了节省空间，  push1 push2分别从收尾开始

    def push1(self, x):

        if self.top1 < self.top2 - 1 :
            self.top1 = self.top1 + 1
            self.data[self.top1] = x

        else:
            print("上溢")

    def push2(self, x):

        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.data[self.top2] = x

        else :
           print("上溢")

    def pop1(self):
        if self.top1 >= 0:
            x = self.data[self.top1]
            self.top1 = self.top1 -1
            return x
        else:
            print("下溢 ")

    def pop2(self):
        if self.top2 < self.size:
            x = self.data[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("下溢 ")


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

    def top(self):
        index = len(self.data) - 1
        return this.data[index]
        pass
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
class Double_Deque:
    def __init__(self):
        self.data = []
        #实现就是双向链表，  或者在class上增加头部和尾部指针， 这里简单的用输出的insert pop append实现

    def push_front(self, element):
        self.data.insert(0, element)
        pass

    def pop_frontD(self):
        p = self.data[0]
        self.data = self.data[1:]
        return p
        pass

    def push_back(self, element):
        self.data.append(element)
        pass

    def pop_back(self):
        index = len(self.data) - 1
        p = self.data[index]
        self.data = self.data[:index]
        return p
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

    def length(self):
        return len(self.data)
        pass


"""
3, 用两个 stack 实现一个 queue, 并分析 dequeue 和 enqueue 的时间复杂度
dequeue 和 enqueue的 时间复杂相同操作的第一次是O(n), 之后同样操作是O(1).
"""
class Queue_stack2:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        #思路， stack1专门用来进队， stack2用来出队，  出队的时候要把stack1全部pop到stack2里
        #      判断上溢： stack1 和 stack2都满了    判断下溢： stack2是空

    def enqueue(self, element):
        length2 = len(self.stack2.data)
        length1 = len(self.stack1.data)
        if length1 != 0:
            self.stack1.push(element)
        else:
            self.stack2_to_stack1()
            self.stack1.push(element)
            pass
        pass

    def dequeue(self):
        # 把第一个元素删除并返回
        length2 = len(self.stack2.data)
        length1 = len(self.stack1.data)
        if length2 != 0:
            return self.stack2.pop()
        elif length2 == 0 and length1 != 0:
            self.stack1_to_stack2()
            return self.stack2.pop()
        else:
            print('下溢')
            pass
        pass

    def stack1_to_stack2(self):
        length = len(self.stack1.data)
        for i in range(length):
            el = self.stack1.pop()
            self.stack2.push(el)
            pass
        pass

    def stack2_to_stack1(self):
        length = len(self.stack2.data)
        for i in range(length):
            el = self.stack2.pop()
            self.stack1.push(el)
            pass
        pass
"""
4, 用两个 queue 实现一个 stack, 并分析 push 和 pop 的时间复杂度
    push是O(1), pop永远是O(n), 空间复杂度也翻倍
"""
class Stack_queue2:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        #思路就是不断倒一杯水， 软后push 和pop 都是O(n)

    def push(self, element):
        length1 = self.queue1.length()
        length2 = self.queue2.length()

        if length2 != 0:
            self.queue2.enqueue(element)
        else:
            self.queue1.enqueue(element)
            pass
        pass

    def pop(self):
        #pop 删除并返回最新添加的元素
        length1 = self.queue1.length()
        length2 = self.queue2.length()
        if length1 == 0 and length2 != 0:
            return self.Last_node(self.queue2, self.queue1)
        elif length1 != 0 and length2 ==0:
            return self.Last_node(self.queue1, self.queue2)
        else:
            print('下溢')
            pass
        pass

    def Last_node(self, q1, q2):
        length = q1.length()
        while length > 1:
            el = q1.dequeue()
            q2.enqueue(el)
            length -= 1
            pass
        return q1.dequeue()
        pass
"""
6, 实现 StackSet, 它内部由多个容量为 3 的 stack 组成, 并且在前一个栈填满时新建一个 stack
接口如下
s = StackSet(n)
s.push
s.pop
"""
class StackSet:
    def __init__(self):
        self.data = [None]
        self.data[0] = Stack()

    def push(self, element):
        stackLength = len(self.data)
        s = self.data[stackLength - 1]

        if self.isFullStack(s):
            s = Stack()
            self.data.append(s)
            pass

        s.push(element)
        pass

    def isFullStack(self, stack):
        return len(stack.data) >= 3
        pass

    def pop(self):
        index = len(self.data) - 1
        s = self.data[index]

        if self.isEmptyStack(s):
            self.data = self.data[:index]
            s = self.data[index]
            pass

        return s.pop()
        pass

    def isEmptyStack(self, stack):
        return len(stack.data) <= 0
        pass

    def pop_from(self, index):
        """
        7, 为 StackSet 添加一个 pop_from(index) 方法
        index 是指定的子栈下标
        """
        return self.data[index - 1]
        pass

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
class Stack_Min:
    def __init__(self):
        self.data = []
        self.min = Stack()

    def push(self, element):
        self.data.append(element)
        self.push_minStack(element)
        pass

    def push_minStack(self, element):
        length = len(self.min.data)
        if length == 0 or self.data[length - 1] > element:
            self.min.push(element)
            pass
        pass

    def pop(self):
        index = len(self.data) - 1
        res = self.data[index]
        self.data = self.data[:index]
        self.pop_minStack(res)
        return res
        pass

    def pop_minStack(self, element):
        index = len(self.min.data) - 1
        last_n = self.min.data[index]
        if last_n == element:
            self.min.pop()
            pass
        pass

    def minElement(self):
        index = len(self.min.data) - 1
        last_n = self.min.data[index]
        return last_n
        pass
"""
9, 给定一个字符串其中包含无数个圆括号和其他字符，使用栈来确定圆括号是匹配的
本题不理解题意的话要在 slack、群 中问清楚
思路：  进zai， 出zai问题。 做过
"""

def bracket_matching(c, left, right):
    s = Stack()
    length = len(c)
    for i in range(length):
        value = c[i]
        if value == left:
            s.push(left)
        elif value == right:
            s.pop()
            pass
        pass

    if len(s.data) == 0:
        return True
    else:
        return False
        pass
    pass

def ymbol_matching(c):
    return bracket_matching(c, '(', ')') and bracket_matching(c, '{', '}')
    pass

# class ymbol_matching:
#     def __init__(self):
#         self.ymbol = {}
#
#     def matching(self, *args):
#         chars = args[0]
#
#         print('test args', args)
#         pass
#
#     def addYmbol(self, ymbol):
#         self.ymbol[ymbol] = Stack()
#         pass
