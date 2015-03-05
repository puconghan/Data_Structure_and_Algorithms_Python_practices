'''
Bucket sort is mainly useful when input is uniformly distributed over a range.
One version: each bucket stores a linked list of elements that were hashed to that bucket.
Worst case runtime: O(n^2)
Average case and best case runtime: O(n + k)
'''

from singly_linked_list import LinkedList

def bucket_sort(lst, n, l, r):
    #Set up an array of initially empty buckets. Each bucket stores an empty linkedlist.
    bucket = {}
    for i in xrange(n):
        bucket[i] = LinkedList()
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
        lst = lst + bucket[i].getsequence()
    return lst


#Test for bucket sort
print bucket_sort([0.5,0.51,0.58,0.1,0.11,0.19,0.9,0.91,0.98,0.2,0.21,0.29,0.8,0.81,0.88,0.3,0.36,0.74,0.45,0.62], 10, 0, 1)
