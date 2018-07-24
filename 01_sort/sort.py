import math

def bubble(list):
    '''
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
    '''
    length = len(list)

    while length > 0:

        for i in range(length - 1):

            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

        length -= 1
    pass

def insertion(list):
    '''
    插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
    算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：
    直接插入排序基本思想是每一步将一个待排序的记录，插入到前面已经排好序的有序序列中去，直到插完所有元素为止。
    '''
    length = len(list)

    for i in range(1, length):
        a = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > a:
                list[j + 1] = list[j]
                list[j] = a
            j -= 1
    pass

def selection(list):
    length = len(list)

    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if list[min] > list[j]:
                min = j
        list[min], list[i] = list[i], list[min]
    pass

def maxHeap(list, length, root):


    left = 2*root + 1
    right = left + 1
    larger = root
    if left < length and list[larger] < list[left]:
        larger = left
    if right < length and list[larger] < list[right]:
        larger = right
    if larger != root:
        list[larger],list[root] = list[root],list[larger]
        maxHeap(list, length, larger)

def buildMaxHeap(list):
    length = len(list)
    for i in range((length -2)//2,-1,-1):
        maxHeap(list, length, i)

def heap(list):
    '''
    链表形式, 具体看算法导论的88
    - 实现一个最大堆 或者 最小堆的函数（比如最大堆意思就是父元素大于 左右子元素）
    - 遍历
    '''
    buildMaxHeap(list)
    for i in range(len(list) -1, -1, -1):
        list[0],list[i] = list[i],list[0]
        maxHeap(list, i, 0)
    pass

def quick(list):
    '''
    （1）在数据集之中，选择一个元素作为"基准"（pivot）。

　　（2）所有小于"基准"的元素，都移到"基准"的左边；所有大于"基准"的元素，都移到"基准"的右边。

　　（3）对"基准"左边和右边的两个子集，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。
    '''
    length = len(list)
    if length <= 1:
        return list

    pivotIndex = math.floor(length / 2)
    pivot = list[pivotIndex]

    left = []
    right = []

    for i in range(length):
        if list[i] < pivot:
            left.append(list[i])
        elif list[i] > pivot:
            right.append(list[i])
            pass

    ll = quick(left)
    ll.append(pivot)

    return ll + quick(right)
    pass


"""
注意:
以后算法相关的所有的作业都放在 srfa 目录中


本作业需要安装 2 个库
pip3 install watchdog nose

nose 是 py 用于测试的库, 具体用法可以:
-1, 群/slack 内讨论
0, 群/slack 内讨论
1, 参考下面的链接
2, 自行搜索
3, 群/slack 内讨论
4, 群/slack 内讨论
http://pythontesting.net/framework/nose/nose-introduction/


在终端中运行 watcher.py
它会自动检测当前文件夹下 py 文件的改动
如果文件修改了它会自动运行测试, 具体见 watcher.py
这样你只需要写 sort.py test_sort.py 就可以了
你想的话还可以加个语音/音乐提示




本次作业目录结构
srfa/01_sort/sort.py
srfa/01_sort/test_sort.py
srfa/01_sort/watcher.py


作业内容:
本文件包含以下 5 个函数, 函数签名见测试文件
直接看算法导论, 不要看证明, 最重要的是理解原理并实现
多用纸笔勾画好逻辑再代码
insertion
selection
bubble
list
quick
"""
