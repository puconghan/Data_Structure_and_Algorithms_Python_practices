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
		else:
			self.tail.next = newnode
		self.tail = newnode
	def remove(self, value):
		if self.head is None:
			return False, "List is empty"
		else:
			if self.head.data == value:
				self.head = self.head.next
			else:
				prevnode = self.head
				currnode = self.head.next
				while currnode is not None:
					if currnode.data == value:
						prevnode.next = currnode.next
						#If the value is stored in the list for more than one times, remove the next return
						return True, "Deleted"
					prevnode = currnode
					currnode = currnode.next
				return False, "Not found"
	def printlist(self):
		if self.head is None:
			return False, "List is emtpy"
		else:
			currnode = self.head
			while currnode != None:
				print currnode.data
				currnode = currnode.next
