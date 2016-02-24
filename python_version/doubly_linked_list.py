class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
        else:
            self.head = None
            self.tail = None
    def insert(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if value < self.head.data:
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            else:
                prev = self.head
                curr = prev.next
                while curr is not None and value > curr.data:
                    prev = curr
                    curr = curr.next
                if curr is not None:
                    prev.next = newnode
                    newnode.prev = prev
                    newnode.next = curr
                    curr.prev = newnode
                else:
                    prev.next = newnode
                    newnode.prev = prev
                    self.tail = newnode
    def remove(self, value):
        if self.head is None:
            return False, "The linkedlist is empty"
        else:
            if self.head.data == value:
                self.head = self.head.next
            else:
                prevnode = self.head
                currnode = prevnode.next
                while currnode is not None:
                    if currnode.data == value:
                        prevnode.next = currnode.next
                        currnode.next.prev = prevnode
                        #If the value is stored in the list for more than one times, remove the next return
                        return True, 'Deleted'
                    prevnode = currnode
                    currnode = currnode.next
                return False, 'Not found'
    def getsequence(self):
        if self.head is None:
            return []
        else:
            result = []
            curr = self.head
            while curr is not None:
                result.append(curr.data)
                curr = curr.next
            return result
    def printlist(self, direction='Forward'):
        if self.head is None:
            return None
        else:
            if direction == 'Forward':
                currnode = self.head
                while currnode is not None:
                    print currnode.data
                    currnode = currnode.next
            elif direction == 'Backward':
                currnode = self.tail
                while currnode is not None:
                    print currnode.data
                    currnode = currnode.prev

#Test case
'''
linkedlist = LinkedList()
linkedlist.insert(9)
linkedlist.insert(1)
linkedlist.insert(8)
linkedlist.insert(2)
linkedlist.insert(7)
linkedlist.insert(3)
linkedlist.insert(6)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(12)
linkedlist.insert(11)
print 1,2,3,4,5,6,7,8,9,10,11,12
print linkedlist.getsequence()
linkedlist.printlist()
linkedlist.remove(3)
print 1,2,4,5,6,7,8,9,10,11,12
print linkedlist.getsequence()
linkedlist.printlist()
'''
