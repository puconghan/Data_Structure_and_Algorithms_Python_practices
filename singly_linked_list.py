'''
Dynamic size | Ease of insertion/deletion | Sequentially access | Extra memory space for a pointer
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
        else:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
    def insert(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            if value < self.head.data:
                newnode.next = self.head
                self.head = newnode
            else:
                prev = self.head
                curr = prev.next
                while curr is not None and value > curr.data:
                    prev = curr
                    curr = curr.next
                prev.next = newnode
                if curr is not None:
                    newnode.next = curr
                else:
                    self.tail = newnode
    def remove(self, value):
        if self.head is None:
            return False, "List is empty"
        else:
            if self.head.data == value:
                self.head = self.head.next
            else:
                prev = self.head
                curr = prev.next
                while curr is not None:
                    if curr.data == value:
                        prev.next = curr.next
                        #If the value is stored in the list for more than one times, remove the next return
                        return True, "Deleted"
                    prev = curr
                    curr = curr.next
                return False, "Not found"
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
    def printlist(self):
        if self.head is None:
            return False, "List is emtpy"
        else:
            currnode = self.head
            while currnode != None:
                print currnode.data
                currnode = currnode.next

#Test cases
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
linkedlist.insert(10)
linkedlist.insert(11)
print 1,2,3,4,5,6,7,8,9,10,11
linkedlist.printlist()
print linkedlist.getsequence()
linkedlist.remove(3)
print 1,2,4,5,6,7,8,9,10,11
linkedlist.printlist()
print linkedlist.getsequence()
'''
