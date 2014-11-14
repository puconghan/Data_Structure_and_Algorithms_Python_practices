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
                if currnode.next.value == walknode.value:
                    walknode.next = walknode.next.next
                else:
                    walknode = walknode.next
            currnode = currnode.next

# O(n) Using a hash table
def remove_duplication(linkedlist):
    if linkedlist.head is not None:
        currnode = linkedlist.head
        hashtable = {currnode.value: True}
        while currnode.next is not None:
            if currnode.next.value in hashtable:
                currnode.next = currnode.next.next
            else:
                hashtable[currnode.next.value] = True
                currnode = currnode.next

'''
2.2 Implement an algorithm to find the nth to last element of a singly linked list
'''

#O(n) Using two pointers
def nth_to_last(linkedlist, n):
    if n <= 0:
        return 'Invalid n'
    if linkedlist.head is not None:
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
2.4 Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node
'''

def delete_node(node):
    if node.next is not None:
        node.value = node.next.value
        node.next = node.next.next
    else:
        node.value = None

'''
2.4 You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list EXAMPLE Input: (3 -> 1 -> 5), (5 -> 9 -> 2) Output: 8 -> 0 -> 8
'''

def add_num_linkedlist(node1, node2):
    if node1 is None and node2 is None:
        return None
    else:
        carry = 0
        newlist = LinkedList()
        while node1.next is not None or node2.next is not None:
            addition += carry
            if node1 is not None:
                addition += node1.value
                node1 = node1.next
            if node2 is not None:
                addition += node2.value
                node2 = node2.next
            digit = addition % 10
            if addition >= 10:
                carry = 1
            else:
                carry = 0
            newlist.add(digit)
            addition, digit = 0, 0


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
    while pointer2.next is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
        if pointer1 == pointer2:
            break
    if pointer2.next is None:
        return None, 'Linked list is not corrupted/circular'
    pointer1 = linkedlist.head
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1
