'''
4.1 Implement a function to check if a tree is balanced.
    For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one
'''

def maxDepth(leaf):
    if leaf is None:
        return 0
    else:
        return 1 + max(maxDepth(leaf.left), maxDepth(leaf.right))

def minDepth(leaf):
    if leaf is None:
        return 0
    else:
        return 1 + min(minDepth(leaf.left), minDepth(leaf.right))

def isBalanced(leaf):
    return (maxDepth(leaf) - minDepth(leaf)) <= 1

'''
4.2 Given a directed graph, design an algorithm to find out whether there is a route between two nodes
'''

#Direct Graph
class DirectGraph:
    def __init__(self, content):
        self.content = content
        self.neighbours = []

#Dynamic programming recursion + cache
def dynamic_traversal(node1, node2, visited, results):
    if node1 == node2:
        return True
    else:
        if (str(hash(node1)) + "," + str(hash(node2))) in results:
            return results[(str(hash(node1)) + "," + str(hash(node2)))]
        nodefound = False
        for neighbour in node1.neighbours:
            if neighbour in visited:
                continue
            visited.append(neighbour)
            nodefound = dynamic_traversal(neighbour, node2, visited, results)
            if nodefound:
                break
        results[(str(hash(node1)) + "," + str(hash(node2)))] = nodefound
        return nodefound

#BFS solution
def BFS_traversal(node1, node2):
    if node1 is node2:
        return True
    elif node1 is None and node2 is None:
        return False
    visited = set([node1, node2])
    queue = [node1]
    while len(queue) > 0:
        node = queue.pop(0)
        for child in node.neighbours:
            if child is node2:
                return True
            else:
                visited.append(child)
                queue.append(child)
    return False

'''
4.3 Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

def ArrayToBinaryTree(inputarray):
    if len(inputarray) == 0:
        return None
    elif len(inputarray) == 1:
        return BinaryTree(inputarray[0])
    else:
        pivot = len(inputarray) // 2
        return BinaryTree(inputarray[pivot], inputarray[:pivot], inputarray[pivot+1:])

'''
4.4 Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
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
        else:
            self.tail.next = newnode
        self.tail = newnode

#Solution1: Level by level
def nodelevelorder(leaf, level, results = []):
    if level == 0:
        results.append(leaf.value)
    else:
        if leaf.left is not None:
            nodelevelorder(leaf.left, level-1, results)
        if leaf.right is not None:
            nodelevelorder(leaf.right, level-1, results)

def getLevel(leaf):
    if leaf is None:
        return 0
    else:
        return 1 + max(getLevel(leaf.left), getLevel(leaf.right))

def generate_linedlist(leaf):
    temp = []
    result = []
    level = getLevel(leaf)
    for i in xrange(level+1):
        nodelevelorder(leaf, i, temp[i])
    for nodelist in temp:
        linkedlist = LinkedList()
        for node in nodelist:
            linkedlist.insert(node)
        results.append(linkedlist)
    return results

#Solution2: Using BFS
def generate_linkedlist(leaf):
    result = []
    temp = [[]]*getLevel(leaf)
    queue = []
    queue.append((leaf, 1))
    while len(queue) != 0:
        (node,level) = queue.pop(0)
        temp[level].append(node)
        if node.left is not None:
            queue.append((node.left, level+1))
        if node.right is not None:
            queue.append((node.right, level+1))
    for nodelist in temp:
        linkedlist = LinkedList()
        for node in nodelist:
            linkedlist.insert(node)
        results.append(linkedlist)
    return results

'''
4.5 Write an algorithm to find the next node (e g , in-order successor) of a given node in a binary search tree where each node has a link to its parent
'''

def find_next_node(leaf):
    if leaf is None:
        return None
    if leaf.right is None:
        if leaf.parent is None:
            curr = leaf.parent
            if leaf.parent.left == leaf:
                return curr
            else:
                return leaf
        else:
            return leaf.parent
    else:
        return find_min_node(leaf)

def find_min_node(leaf):
    if leaf.left is None:
        return leaf
    else:
        curr = leaf.left
        while curr.right is not None:
            curr = curr.right
        return curr

'''
4.6 Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree Avoid storing additional nodes in a data structure NOTE: This is not necessarily a binary search tree
'''

#Solution1: O(n^2)
def common_ancestor(node1, node2):
    curr1 = node1
    while curr1.parent is not None:
        curr2 = node2
        while curr2.parent is not None:
            if curr1 == curr2:
                return curr1
            curr2 = curr2.parent
        curr1 = curr1.parent

#check if a decendent of a root
def is_decendent(root, leaf):
    if root is None:
        return False
    elif root is leaf:
        return True
    else:
        return is_decendent(root.left, leaf) or is_decentdent(root.right, leaf)

#Solution2: O(n^2)
def common_ancestor(node1, node2):
    curr = node1
    while curr.parent is not None:
        if is_decendent(curr.parent, node2):
            return True
        curr = curr.parent
    return False


'''
4.7 You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
    Create an algorithm to decide if T2 is a subtree of T1
'''

def matchtree(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.value != node2.value:
        return False
    return matchtree(node1.left, node2.left) and matchtree(node1.right, node2.right)

def is_subtree(leaf1, leaf2):
    if leaf2 is None:
        return True
    else:
        if leaf1 is None:
            return False
        if leaf1.value == leaf2.value:
            if matchtree(leaf1, leaf2):
                return True
        return is_subtree(leaf1.left, leaf2) or is_subtree(leaf2.right, leaf2)

'''
4.8 You are given a binary tree in which each node contains a value Design an algorithm to print all paths which sum up to that value Note that it can be any path in the tree - it does not have to start at the root
'''

#Bottom up summation
def sumup(leaf):
    temp = leaf.value
    templist = [leaf]
    if leaf.parent is not None:
        temp += leaf.parent.value
        templist = [leaf.parent] + templist
        leaf = leaf.parent
    return temp, templist

def sumall(leaf, givensum, results=[]):
    value, valuelist = sumup(leaf)
    if value == givensum:
        results.append(valuelist)
    if leaf.left is not None:
        sumall(leaf.left, givensum, results)
    if leaf.right is not None:
        sumall(leaf.right, givensum, results)
    return results

