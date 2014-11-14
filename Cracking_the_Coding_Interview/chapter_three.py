'''
3.1 Describe how you could use a single array to implement three stacks
'''

class MultiStack:
    def __init__(self, stacksize, numofstack):
        self.stacksize = stacksize
        self.numofstack = numofstack
        self.array = [None]*self.stacksize*self.numofstack
        self.pointers = [-1]*self.numberofstack
    def push(self, stacknum, value):
        if self.pointers[stacknum] + 1 >= self.stacksize:
            return False, 'Out of space'
        else:
            self.pointers[stacknum] += 1
            self.array[stacktop(stacknum)] = value
    def pop(self, stacknum):
        if self.pointers[stacknum] < 0:
            return False, 'Stack is empty'
        else:
            data = self.array[stacktop(stacknum)]
            self.array[stacktop(stacknum)] = None
            self.pointers[stacknum] -= 1
            return data
    def isempty(self, stacknum):
        return self.pointers[stacknum] < 0
    def stacktop(self, stacknum):
        return self.stacksize * stacknum + self.pointers[stacknum]

'''
3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time
'''

#Solution1: Using a tuple to store data in every stack element
class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0
    def push(self, value):
        if self.stack is None or value < self.stack[-1][1]:
            self.stack.append((value, value))
        else:
            self.stack.append((value, self.stack[-1][1]))
        self.count += 1
    def pop(self, value):
        if self.count == 0 or len(self.stack) == 0:
            return None
        else:
            self.count -= 1
            return self.stack.pop()[0]
    def size(self):
        return self.count
    def isEmpty(self):
        return self.count == 0
    def getmin(self):
        return self.stack[-1][1]

#Solution2: Using an additional python variable/list (save space)
class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0
        self.minimum = None
    def push(self, value):
        self.stack.append(value)
        self.count += 1
        if self.minimum is None or value < self.minimum:
            self.minimum = value
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
    def getmin(self):
        return self.minimum

'''
3.3 Imagine a (literal) stack of plates If the stack gets too high, it might topple Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold Implement a data structure SetOfStacks that mimics this SetOf- Stacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity SetOfStacks push() and SetOfStacks pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack)
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack
'''

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if len(self.stacks) == 0 or len(self.stacks[-1] == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            return None
        else:
            data = self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
            return data
    def popAt(self, index):
        if len(self.stacks) == 0 or index < 1 or index > len(self.stacks) or len(self.stacks[index-1]) == 0:
            return None
        else:
            data = self.stacks[index-1].pop()
            if len(self.stacks[index-1]) == 0:
                self.stacks.pop(index-1)
            return data

'''
3.4 In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizeswhichcanslideontoanytower Thepuzzlestartswithdiskssortedinascending order of size from top to bottom (e g , each disk sits on top of an even larger one) You have the following constraints:
    (A) Only one disk can be moved at a time
    (B) A disk is slid off the top of one rod onto the next rod
    (C) A disk can only be placed on top of a larger disk
    Write a program to move the disks from the first rod to the last using Stacks
'''

class Hanoi:
    def __init__(self, size):
        self.towers = [[],[],[]]
        self.size = size
        self.towers[0] = [x for x in xrange(size, 0, -1)]
    def playHanoi(self):
        self.printTowers()
        self.moveLevel(self.size, 1, 2, 3)
        self.printTowers()
    def moveLevel(self, size, fr, helper, to):
        if size == 1:
            data = self.towers[fr-1].pop()
            self.towers[to-1].append(data)
            print data, fr, '--->', to
        else:
            self.moveLevel(size-1, fr, to, helper)
            self.moveLevel(1, fr, helper, to)
            self.moveLevel(size-1, helper, fr, to)
    def printTowers(self):
        for tower in self.towers:
            print tower

'''
3.5 Implement a MyQueue class which implements a queue using two stacks
'''

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, value):
        self.stack1.append(value)
    def dequeue(self):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        data = self.stack2.pop()
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        return data

'''
3.6 Write a program to sort a stack in ascending order You should not make any assumptions about how the stack is implemented The following are the only functions that should be used to write this program: push | pop | peek | isEmpty
'''

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
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        return self.count == 0
def sortStack(targetstack):
    newstack = Stack()
    while !targetstack.isEmpty():
        tmp = targetstack.pop()
        while not newstack.isEmpty() and newstack.peek() > tmp:
            targetstack.push(newstack.pop())
        newstack.push(tmp)
        while not targetstack.isEmpty() and targetstack.peek() >= newstack.peek():
            newstack.push(targetstack.pop())
    return newstack

