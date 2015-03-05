'''
Comparison based sorting technique based on Binary Heap data structure.
[A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node is greater(or smaller) than the values in its two children nodes]
Average run time O(n*log(n))
Parent: 		floor(i - 1) / 2
Left Child:		2 * i + 1
Right Child:	2 * i + 2
'''

def heap_sort(lst):
    size = len(lst) - 1
    leastparent = size / 2
    for i in xrange(leastparent, -1, -1):
        move_down(lst, i, size)
    for i in xrange(size, 0, -1):
        if lst[0] > lst[i]:
            swap(lst, i, 0)
            move_down(lst, 0, i-1)
    return lst

def move_down(lst, parent, last):
    child = parent * 2 + 1
    while child <= last:
        if child < last and lst[child] < lst[child+1]:
            child += 1
        if lst[child] > lst[parent]:
            swap(lst, child, parent)
            parent = child
            child = child * 2 + 1
        else:
            return

def swap(lst, l, r):
    temp = lst[l]
    lst[l] = lst[r]
    lst[r] = temp

#Test cases
print heap_sort([2,9,3,6,1,8,0,4])
