'''
FILO | LIFO
'''

class Stack:
	def __init__(self):
		self.stack = []
		self.count = 0
	def push(self, value):
		self.stack.append(value)
		self.count += 1
	def pop(self):
		if self.count == 0 or len(self.stack) == 0:
			return None
		else:
			self.count -= 1
			return self.stack.pop(-1)
	def peel(self):
		if self.count == 0 or len(self.stack) == 0:
			return None
		else:
			return self.stack[-1]
	def size(self):
		return self.count
	def isEmpty(self):
		return self.count == 0

'''
#Test cases
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.push(6)
stack.push(8)
stack.push(10)
stack.push(12)
stack.push(14)
print stack.pop(), 14
print stack.size(), 6
print stack.pop(), 12
print stack.pop(), 10
print stack.pop(), 8
print stack.pop(), 6
print stack.pop(), 4
print stack.pop(), 2
print stack.peel(), 1
print stack.size(), 1
print stack.isEmpty(), True
'''
