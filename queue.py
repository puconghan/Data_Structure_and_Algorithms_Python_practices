'''
FIFO | LILO
'''

class Queue:
	def __init__(self):
		self.queue = []
		self.count = 0
	def enqueue(self, value):
		self.queue.append(value)
		self.count += 1
	def dequeue(self):
		if self.count == 0 or len(self.queue) == 0:
			return None
		else:
			item = self.queue[0]
			self.queue = self.queue[1:]
			self.count -= 1
			return item
	def size(self):
		return self.count
	def isEmpty(self):
		return self.count == 0

'''
#Test cases
queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(9)
print queue.size(), 5
print queue.isEmpty(), False
print queue.dequeue(), 1
print queue.dequeue(), 3
print queue.dequeue(), 5
print queue.dequeue(), 7
print queue.dequeue(), 9
'''
