'''
Bucket sort is mainly useful when input is uniformly distributed over a range.
One version: each bucket stores a linked list of elements that were hashed to that bucket.
Worst case runtime: O(n^2)
Average case and best case runtime: O(n + k)
'''

#Implementation for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if data <= self.root.data:
                temp = self.root
                self.root = Node(data)
                self.root.next = temp
            else:
                currnode = self.root
                nextnode = currnode.next
                while nextnode is not None and nextnode.data < data:
                    currnode = nextnode
                    nextnode = nextnode.next
                currnode.next = Node(data)
                if nextnode is not None:
                    currnode.next.next = nextnode
    def getsequence(self):
        if self.root is None:
            return []
        else:
            result = []
            curr = self.root
            while curr is not None:
                result.append(curr.data)
                curr = curr.next
            return result

def bucket_sort(lst, n, l, r):
    #Set up an array of initially empty buckets. Each bucket stores an empty linkedlist.
    bucket = {}
    for i in xrange(n):
        bucket[i+1] = LinkedList()
    #Go over the original array, putting each object in its bucket.
    num_range = float(r - l)
    each_range = num_range / n
    import math
    for val in lst:
        hashnum = math.floor(val / each_range)
        bucket[hashnum].insert(val)
    lst = []
    #Visit the buckets in order and put all elements back into the original array.
    for i in xrange(n):
        lst = lst + bucket[i+1].getsequence()
    return lst

#Test for linked list
'''
lst = LinkedList()
lst.insert(5)
lst.insert(1)
lst.insert(9)
lst.insert(2)
lst.insert(8)
lst.insert(3)
lst.insert(7)
lst.insert(4)
lst.insert(10)
lst.insert(20)
lst.insert(14)
lst.insert(13)
lst.insert(18)
lst.insert(16)
print lst.getsequence()
'''

#Test for bucket sort
'''
print bucket_sort([0.5,0.51,0.58,0.1,0.11,0.19,0.9,0.91,0.98,0.2,0.21,0.29,0.8,0.81,0.88,0.3,0.36,0.74,0.45,0.62], 10, 0, 1)
'''
