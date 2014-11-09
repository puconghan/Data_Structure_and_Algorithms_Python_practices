class Stack:
	def __init__(self):
		self.stack = []
		self.count = 0
	def push(self, value):
		self.stack.append(value)
		self.count += 1
	def pop(self, value):
		if self.count == 0 or len(self.stack) == 0:
			return None
		else:
			self.count -= 1
			return self.stack.pop()
	def size(self):
		return self.count
	def isEmpty(self):
		return self.count == 0 		