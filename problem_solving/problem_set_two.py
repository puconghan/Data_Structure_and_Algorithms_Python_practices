'''
You have a binary tree on client machine, how will u send this info to server and how will you again maintain the  tree over the server.
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.left, self.right = None, None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
        else:
            self._insert(value, self.root)
    def _insert(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
    def printleveldown(self, node=None):
        if node is None:
            queue = [(self.root, 1)]
        else:
            queue = [(node, 1)]
        level = 1
        result = ""
        while len(queue) > 0:
            (node, currlevel) = queue.pop(0)
            if level == currlevel:
                result += str(node.data)
            else:
                print result
                level = currlevel
                result = str(node.data)
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        if result != "":
            print result

#Solution using in order format
def inorderformat_send(node):
    temp = []
    if node.left is None:
        temp.append(None)
    else:
        temp.append(inorderformat_send(node.left))
    temp.append(node.data)
    if node.right is None:
        temp.append(None)
    else:
        temp.append(inorderformat_send(node.right))
    return temp

def inorderformat_receive(lst):
    if lst is None:
        pass
    else:
        tempnode = Node(lst[1])
        tempnode.left = inorderformat_receive(lst[0])
        tempnode.right = inorderformat_receive(lst[2])
        return tempnode

'''
Test case for inorderformat solution
binarytree = BinaryTree()
binarytree.insert(8)
binarytree.insert(4)
binarytree.insert(15)
binarytree.insert(3)
binarytree.insert(5)
binarytree.insert(12)
binarytree.insert(18)
binarytree.printleveldown()
newlist = inorderformat_send(binarytree.root)
print newlist
newtree = inorderformat_receive(newlist)
binarytree.printleveldown(newtree)
print inorderformat_send(newtree)
'''

#Solution using BFS
def bfs_send(node):
    lst, queue = [], [node]
    while len(queue) > 0:
        curr = queue.pop(0)
        lst.append(curr.data)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return lst

def bfs_receive(lst):
    newtree = BinaryTree()
    for val in lst:
        newtree.insert(val)
    return newtree

'''
#Test case for bfs solution
binarytree = BinaryTree()
binarytree.insert(8)
binarytree.insert(4)
binarytree.insert(15)
binarytree.insert(3)
binarytree.insert(5)
binarytree.insert(12)
binarytree.insert(18)
binarytree.printleveldown()
lst = bfs_send(binarytree.root)
tree = bfs_receive(lst)
tree.printleveldown()
'''

'''
Find the min and max in an array in minimum no of operations with complexity.
'''

#Divide and conquer solution
def divide_and_conquer(lst):
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        minval, maxval = lst[0], lst[0]
    if len(lst) == 2:
        if lst[0] > lst[1]:
            minval, maxval = lst[1], lst[0]
        else:
            minval, maxval = lst[0], lst[1]
    elif len(lst) > 2:
        pivot = len(lst) // 2
        left = lst[:pivot]
        right = lst[pivot:]
        min1, max1 = divide_and_conquer(left)
        min2, max2 = divide_and_conquer(right)
        minval = min(min1, min2)
        maxval = max(max1, max2)
    return minval, maxval

print divide_and_conquer([9,3,5,1,0,3,6])
