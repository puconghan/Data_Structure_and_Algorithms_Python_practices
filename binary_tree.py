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

class BinaryTree:
	def __init__(self):
		self.root = None
	def insert(self, value):
		if not self.root:
			self.root = Node(value)
		else:
			self._insert(value, self.root)
	def _insert(self, value, leaf=None):
		if value < leaf.getValue():
			if leaf.hasLeft:
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
		if leaf:
			if value == leaf.getValue():
				if not leaf.hasLeft() and not leaf.hasRight():
					leaf = None
				if leaf.hasLeft() and not leaf.hasRight():
					leaf = leaf.left
				if not leaf.hasLeft() and leaf.hasRight():
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
			if value < leaf.getValue() and leaf.hasLeft():
				leaf.left = self._delete(value, leaf.left)
			if value > leaf.getValue() and leaf.hasRight():
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
			if curr.hasRight():
				return self.getmin(curr.right)
			else:
				return curr.getValue()
	#Print level by level from top to the bottom
	def BreadthFirstTraversal(leaf):
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
	def DepthFirstTraversal_preorder(leaf):
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
	def DepthFirstTraversal_inorder(leaf):
		if leaf is not None:
			stack = [leaf]
			output = []
			while len(stack) > 0:
				if curr.hasLeft():
					stack.append(curr.left)
				curr = stack.pop(-1)
				output.append(curr.getValue())
				if curr.hasRight():
					stack.append(curr.right)
			print output
	def DepthFirstTraversal_postorder(leaf):
		if leaf is not None:
			stack = [leaf]
			output = []
			while len(stack) > 0:
				if curr.hasLeft():
					stack.append(curr.left)
				if curr.hasRight():
					stack.append(curr.right)
				curr = stack.pop(-1)
				output.append(curr.getValue())
			print output
	def printlevel(leaf, level):
		if level == 0:
			print leaf.data
		else:
			if leaf.hasLeft():
				self.printlevel(leaf.left, level - 1)
			if leaf.hasRight():
				self.printlevel(leaf.right, level - 1)
	def printleveldown(leaf):
		for i in xrange(self.treedepth()):
			self.printlevel(leaf, i)
	def printlevelup(leaf):
		for i in xrange(self.treedepth(), -1, -1):
			self.printlevel(leaf, i)
	def printdeepestlevel(leaf):
		queueone = [leaf]
		queuetwo = []
		printlist = []
		while len(queueone) != 0:
			node = queueone.pop(0)
			printlist.append(node.getValue())
			if node.left:
				queuetwo.append(node.left)
			if node.right:
				queuetwo.append(node.right)
			if len(queueone) == 0:
				if len(queuetwo) != 0:
					queueone = queuetwo
				else:
					print printlist
