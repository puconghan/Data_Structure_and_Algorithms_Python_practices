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

'''
Test case
print divide_and_conquer([9,3,5,1,0,3,6])
'''

'''
CSV parser
'''

def csv_parser(inputs):
    for line in inputs:
        chunks = line.split(',')
        for chunk in chunks:
            print chunk.replace('\n', '').strip()

'''
Test case
csv_parser(['hello, world, this, is, test', 'hello2, world2, this2, is2, test2'])
'''


'''
Find all the combinations of a string in lowercase and uppercase
"ab" -> ["ab", "Ab", "aB", "AB"]
'''
def allset(string):
    charlist = []
    charlist.extend([char.lower() for char in string])
    charlist.extend([char.upper() for char in string])
    return charlist

def combinations(charlist):
    if len(charlist) == 0:
        return []
    if len(charlist) == 1:
        return [charlist]
    else:
        results = []
        for i in xrange(len(charlist)):
            pivot = charlist[i]
            rest = charlist[:i] + charlist[i+1:]
            for comb in combinations(rest):
                results.append([pivot] + comb)
        return results

'''
Test case
allchar = allset('ab')
print combinations(allchar)
'''

'''
Parsing cvs file
inputs = [
'Pucong,Han,puconghan@gmail.com,San Francisco,1',
'Jie,Zou,jiezou@gmail.com,"San Francisco, CA",0',
'"Yao, ""Huang""",Huang,yaohuang@gmail.com,New York,1',
'Shiye,"""Hu"",""Shiye""",shiyehu@gmail.com,New York,"Two"'
]
'''

def input_parser(inputs):
    for line in inputs:
        counter = 0
        mode = 0
        result = ''
        while counter < len(line)-1:
            if line[counter] == '"':
                if line[counter + 1] == '"':
                    result += '"'
                    counter += 2
                else:
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
                    counter += 1
            else:
                if mode == 0:
                    if line[counter] == ',':
                        result += '|'
                    else:
                        result += line[counter]
                    counter += 1
                if mode == 1:
                    result += line[counter]
                    counter += 1
        print result

'''
#Test case
inputs = [
'Pucong,Han,puconghan@gmail.com,San Francisco,1',
'Jie,Zou,jiezou@gmail.com,"San Francisco, CA",0',
'"Yao, ""Huang""",Huang,yaohuang@gmail.com,New York,1',
'Shiye,"""Hu"",""Shiye""",shiyehu@gmail.com,New York,"Two"'
]
input_parser(inputs)
'''

'''
You are given a 2D Array that contains only 0s and 1s in sorted order. i.e. First Os and then 1s.
Array:
    0 0 0 1
    1 1 1 1
    0 0 1 1
    0 1 1 1
You have to figure out the row that contains maximum number of 1s.
'''

def maximum_one(lst):
    r, c = len(lst), len(lst[0])
    for col in xrange(c):
        for row in xrange(r):
            if lst[row][col] == 1:
                return lst[row]

'''
Test case
lst = [
[0,0,0,1],
[1,1,1,1],
[0,0,1,1],
[0,1,1,1]
]
print maximum_one(lst)
'''

'''
Given a list of jobs with their dependencies, identify a list of job execution which respects all dependencies.
Example:
A-->B, C, F
B-->C
C-->E
Output: [E,C,B,F,A]

Input: {("B", set(["C"])), ("C", set(["E"])), ("A", set(["B", "C", "F"]))}
'''

result = []
def dependency(inputs, result):
    for key in inputs:
        for val in inputs[key]:
            if val not in inputs:
                if val not in result:
                    result.append(val)
            else:
                newdict = {}
                for newkey in inputs:
                    if newkey != key:
                        newdict[newkey] = inputs[newkey]
                dependency(newdict, result)
        if key not in result:
            result.append(key)

#Test case
'''
inputs = {"B": ("C"), "C": ("E"), "A": ("B", "C", "F")}
dependency(inputs, result)
print result
should return ['E', 'C', 'B', 'F', 'A']
'''

def dependency(inputs):
    result = []
    stack = []
    for key in inputs:
        if key not in stack:
            stack.append(key)
        for val in inputs[key]:
            if val not in stack:
                stack.append(val)
            while stack[-1] not in inputs and stack[-1] not in result:
                result.append(stack.pop(-1))
    while len(stack) > 0:
        result.append(stack.pop(-1))
    return result

#Test case
'''
inputs = {"B": ("C"), "C": ("E"), "A": ("B", "C", "F")}
print dependency(inputs)
'''
