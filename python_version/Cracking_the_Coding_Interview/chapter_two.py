def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

load_src('singly_linked_list', '../singly_linked_list.py')
from singly_linked_list import LinkedList

'''
2.1 Write code to remove duplicates from an unsorted linked list
'''

# O(n^2) Without a data structure
def remove_duplication(linkedlist):
    if linkedlist.head is not None:
        currnode = linkedlist.head
        while currnode is not None:
            walknode = currnode
            while walknode.next is not None:
                if currnode.data == walknode.next.data:
                    #linkedlist.remove(walknode.next.data)
                    walknode.next = walknode.next.next
                walknode = walknode.next
            currnode = currnode.next

'''
#Test case
linkedlist = LinkedList()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(6)
linkedlist.insert(7)
linkedlist.insert(8)
print 'Before remove duplication'
linkedlist.printlist()
remove_duplication(linkedlist)
print 'After remove duplication'
linkedlist.printlist()
'''

# O(n) Using a hash table
def remove_duplication(linkedlist):
    if linkedlist.head is not None:
        currnode = linkedlist.head
        hashtable = {currnode.data: True}
        while currnode.next is not None:
            if currnode.next.data in hashtable:
                currnode.next = currnode.next.next
            else:
                hashtable[currnode.next.data] = True
                currnode = currnode.next

'''
#Test case
linkedlist = LinkedList()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(6)
linkedlist.insert(7)
linkedlist.insert(8)
print 'Before remove duplication'
linkedlist.printlist()
remove_duplication(linkedlist)
print 'After remove duplication'
linkedlist.printlist()
'''

'''
2.2 Implement an algorithm to find the nth to last element of a singly linked list
'''

#O(n) Using two pointers
def nth_to_last(linkedlist, n):
    if n <= 0:
        return 'Invalid n'
    if linkedlist.head is None:
        return 'Empty linkedlist'
    pointer2 = linkedlist.head
    for i in xrange(n-1):
        if pointer2.next is not None:
            pointer2 = pointer2.next
        else:
            return 'n exceeds the length of linkedlist'
    pointer1 = linkedlist.head
    while pointer2.next is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

'''
#Test case
linkedlist = LinkedList()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(6)
linkedlist.insert(7)
linkedlist.insert(8)
print nth_to_last(linkedlist, 2).data
'''

'''
2.4 Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node
'''

def delete_node(node):
    if node.next is not None:
        node.data = node.next.data
        node.next = node.next.next
    else:
        node.data = None

'''
#Test case
linkedlist = LinkedList()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(6)
linkedlist.insert(7)
linkedlist.insert(8)
node = linkedlist.head.next.next
print 'Delete: ',node.data
delete_node(node)
linkedlist.printlist()
'''

'''
2.4 You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list EXAMPLE Input: (3 -> 1 -> 5), (5 -> 9 -> 2) Output: 8 -> 0 -> 8
'''

def add_num_linkedlist(node1, node2):
    if node1 is None and node2 is None:
        return None
    else:
        carry = 0
        newlist = LinkedList()
        while node1 is not None or node2 is not None:
            addition = 0
            addition += carry
            if node1 is not None:
                addition += node1.data
                node1 = node1.next
            if node2 is not None:
                addition += node2.data
                node2 = node2.next
            digit = addition % 10
            if addition >= 10:
                carry = 1
            else:
                carry = 0
            newlist.insert(digit)
            digit = 0
        return newlist

'''
#Test case
linkedlist = LinkedList()
linkedlist.insert(3)
linkedlist.insert(1)
linkedlist.insert(5)
linkedlist1 = LinkedList()
linkedlist1.insert(5)
linkedlist1.insert(9)
linkedlist1.insert(2)
node1 = linkedlist.head
node2 = linkedlist1.head
newlist = add_num_linkedlist(node1, node2)
newlist.printlist()
'''

'''
2.5 Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
    DEFINITION: Circular linked list: A (corrupt) linked list in which a node next pointer points to an earlier node, so as to make a loop in the linked list.
    SOLUTION EXAMPLE Input: A -> B -> C -> D -> E -> C [the same C as earlier] Output: C
'''
# Speed         -> n - k
# Slow one      -> 1(n - k) = n - k
# Faster one    -> 2(n - k) = 2n - 2k
# First meet    -> k + 2n - 2k = 2n - k
def find_circular(linkedlist):
    if linkedlist.head is not None:
        return None, 'Linked list is empty'
    pointer1, pointer2 = linkedlist.head, linkedlist.head
    #Find meeting point.
    while pointer2.next is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
        if pointer1 == pointer2:
            break
    #Break if the faster pointer reach the end.
    if pointer2.next is None:
        return None, 'Linked list is not corrupted/circular'
    #Move one pointer to head. Making them move at same speed, they will meet at the beginning of the loop.
    pointer1 = linkedlist.head
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1
