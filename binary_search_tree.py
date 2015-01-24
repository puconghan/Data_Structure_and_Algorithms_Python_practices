class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None
	def getValue(self):
		return self.data
	def hasLeft(self):
		return self.left is not None
	def hasRight(self):
		return self.right is not None

class BinarySearchTree:
	def __init__(self):
		self.root = None
	def insert(self, value):
		if not self.root:
			self.root = Node(value)
		else:
			self._insert(value, self.root)
	def _insert(self, value, leaf):
		if value < leaf.getValue():
			if leaf.hasLeft():
				self._insert(value, leaf.left)
			else:
				leaf.left = Node(value)
		else:
			if leaf.hasRight():
				self._insert(value, leaf.right)
			else:
				leaf.right = Node(value)
	def delete(self, value):
		self.root = self._delete(value, self.root)
	def _delete(self, value, leaf=None):
		if leaf is not None:
			if value == leaf.getValue():
				if not leaf.hasLeft() and not leaf.hasRight():
					leaf = None
				elif leaf.hasLeft() and not leaf.hasRight():
					leaf = leaf.left
				elif not leaf.hasLeft() and leaf.hasRight():
					leaf = leaf.right
				else:
					successor = leaf.left
					parent = None
					while successor and successor.hasRight():
						parent = successor
						successor = successor.right
					if successor:
						leaf.data = successor.data
					if parent:
						parent.right = None
			elif value < leaf.getValue() and leaf.hasLeft():
				leaf.left = self._delete(value, leaf.left)
			elif value > leaf.getValue() and leaf.hasRight():
				leaf.right = self._delete(value, leaf.right)
		return leaf
	def treesize(self):
		return self._treesize(self.root)
	def _treesize(self, leaf=None):
		if leaf is None:
			return 0
		else:
			return self._treesize(leaf.left) + 1 + self._treesize(leaf.right)
	def treedepth(self):
		return self._treedepth(self.root)
	def _treedepth(self, leaf=None):
		if leaf is None:
			return 0
		else:
			return max(self._treedepth(leaf.left), self._treedepth(leaf.right)) + 1
	def getmax(self, leaf=None):
		if leaf is None:
			return None
		else:
			curr = leaf
			while curr.hasRight():
				curr = curr.right
			return curr.getValue()
	def getmin(self, leaf=None):
		if leaf is None:
			return None
		else:
			curr = leaf
			if curr.hasLeft():
				return self.getmin(curr.left)
			else:
				return curr.getValue()
	#Print level by level from top to the bottom
	def BreadthFirstTraversal(self, leaf):
		if leaf is not None:
			queue = [leaf]
			output = []
			while len(queue) > 0:
				curr = queue.pop(0)
				output.append(curr.getValue())
				if curr.hasLeft():
					queue.append(curr.left)
				if curr.hasRight():
					queue.append(curr.right)
			print output
	def DepthFirstTraversal_preorder(self, leaf):
		if leaf is not None:
			stack = [leaf]
			output = []
			while len(stack) > 0:
				curr = stack.pop(-1)
				output.append(curr.getValue())
				if curr.hasLeft():
					stack.append(curr.left)
				if curr.hasRight():
					stack.append(curr.right)
			print output
	def DepthFirstTraversal_inorder(self, leaf):
		if leaf is not None:
			stack = [leaf]
			output = []
			while len(stack) > 0:
				curr = stack.pop(-1)
				if curr.hasLeft():
					stack.append(curr.left)
				output.append(curr.getValue())
				if curr.hasRight():
					stack.append(curr.right)
			print output
	def DepthFirstTraversal_postorder(self, leaf):
		if leaf is not None:
			stack = [leaf]
			output = []
			while len(stack) > 0:
				curr = stack.pop(-1)
				if curr.hasLeft():
					stack.append(curr.left)
				if curr.hasRight():
					stack.append(curr.right)
				output.append(curr.getValue())
			print output
	def printlevel(self, leaf, level):
		if level == 0:
			print leaf.data
		else:
			if leaf.hasLeft():
				self.printlevel(leaf.left, level - 1)
			if leaf.hasRight():
				self.printlevel(leaf.right, level - 1)
	def printleveldown(self, leaf):
		for i in xrange(self.treedepth()):
			self.printlevel(leaf, i)
	def printlevelup(self, leaf):
		for i in xrange(self.treedepth(), -1, -1):
			self.printlevel(leaf, i)
	def printdeepestlevel(self, leaf):
		queueone = [leaf]
		queuetwo = []
		printlist = []
		while len(queueone) != 0:
			node = queueone.pop(0)
			if node.left:
				queuetwo.append(node.left)
			if node.right:
				queuetwo.append(node.right)
			if len(queueone) == 0:
				if len(queuetwo) != 0:
					printlist = []
					for item in queuetwo:
						queueone.append(item)
						printlist.append(item.getValue())
					queuetwo = []
				else:
					print printlist

'''
#Test cases
tree = BinarySearchTree()
tree.insert(8)
tree.insert(5)
tree.insert(12)
tree.insert(4)
tree.insert(6)
tree.insert(15)
tree.insert(11)
tree.insert(29)
tree.insert(1)
print 'Print Level Up'
tree.printlevelup(tree.root)
print 'Print Level Down'
tree.printleveldown(tree.root)
print 'Print the deepest Level'
tree.printdeepestlevel(tree.root)
print 'Print level 2'
tree.printlevel(tree.root, 2)
print 'Get Max'
print tree.getmax(tree.root)
print 'Get Min'
print tree.getmin(tree.root)
print 'Get Tree Size, Depth'
print tree.treesize(), tree.treedepth()
print 'Delete 6'
tree.delete(6)
tree.DepthFirstTraversal_inorder(tree.root)
'''
