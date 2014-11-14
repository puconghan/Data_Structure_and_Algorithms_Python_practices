'''
1.1 Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
'''

#O(n^2) Using two loops without additional data structures
def has_all_unique_char(inputstring):
    for char1 in inputstring:
        count = 0
        for char2 in inputstring:
            if char1 == char2:
                count += 1
        if count > 1:
            return False
    return True

def has_all_unique_char(inputstring):
    lenth = len(inputstring)
    for i in xrange(lenth):
        for j in xrange(i, lenth+1, 1):
            if inputstring[i] == inputstring[j]:
                return False
    return True

#O(n^2) Using a list data structure
def has_all_unique_char(inputstring):
    list = []
    #checking if char is in the list is O(n) according to http://wiki.python.org/moin/TimeComplexity
    for item in inputstring:
        if item in list:
            return False
        list.append(item)
    return True

#O(n) Using a list data structure with assumption of ASCII input string
def has_all_unique_char(inputstring):
    if len(inputstring) > 256:
        return False
    else:
        charlist = [False]*256
        for char in inputstring:
            if charlist[ord(char)]:
                return False
            else:
                charlist[ord(char)] = True
        return True

#O(n) Using a hash table (dictionary)
def has_all_unique_char(inputstring):
    char_table = {}
    for char in char_table:
        if char in char_table:
            return False
        else:
            char_table[char] = True
    return True

def has_all_unique_char(inputstring):
    if len(inputstring) > 256: return False
    else: return len(set(inputstring)) == len(inputstring)

'''
1.2 Implement a function that reverses a string
'''

# O(n) Using a stack
def reverse_string(inputstring):
    stack = []
    output = ''
    for char in inputstring:
        stack.append(char)
    while len(stack) > 0:
        output += stack.pop(-1)
    return output

# O(n) Recursive solution
def reverse_string(inputstring):
    if len(inputstring) == 0:
        return ''
    else:
        return inputstring[-1:] + reverse_string(inputstring[:-1])

'''
1.3 Given two strings, write a method to decide if one is a permutation of the other
'''

#O(n^2)
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        for char in str1:
            if str2.find(char) != -1:
                return False
            else:
                str2.pop(-1)
        return True

#Run time depend of sorting algorithm
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)

#O(n) Use a hash table
def check_permutation(str1, str2):
    dict1, dict2 = {}, {}
    for char in str1:
        dict1[char] = char
    for char in str2:
        dict2[char] = char
    if len(str1) != len(str2):
        return False
    for key in dict1:
        if not (key in dict2 and dict1[key] == dict2[key]):
            return False
    return True

'''
1.4 Write a method to replace all space in a string with '%20'
'''

#O(n) Using a list
def replace_space(inputstring):
    result_list = []
    for char in inputstring:
        if char == ' ':
            result_list.append('%20')
        else:
            result_list.append(char)
    return ''.join(result_list)

#O(n) Using a queue
def replace_space(inputstring):
    queue = []
    for char in inputstring:
        if char == ' ':
            queue.append('%')
            queue.append('2')
            queue.append('0')
        else:
            queue.append(char)
    outputstring = ''
    while len(queue) > 0:
        outputstring += queue.pop(0)
    return outputstring

'''
1.5 Implement a method to perform basic string compression using the counts of repeated characters
    aabcccccaaa would become a2blc5a3.
    Do nothing if this would not make the string smaller.
'''

def simple_compress(inputstring):
    outputlist = []
    prevchar = ''
    count = 1
    for char in inputstring:
        if prevchar == char:
            count += 1
        else:
            if prevchar != '':
                outputlist.append(char + str(count))
            count = 1
        prevchar = char
    outputlist.append(char + str(count))
    outputstring = ''.join(outputlist)
    if len(inputstring) <= len(outputstring):
        return inputstring
    else:
        return outputstring

'''
1.6 Rotate a NxN matrix 90 degrees
    (assuming clockwise rotation)
1.7 Write an algorithm such that if an element in an MxN matrixis 0, its entire row and column are set to 0.
'''

class MatrixProcessor:
    def __init__(self, matrix):
        self.r = len(matrix)
        self.c = len(matrix[0])
        self.matrix = matrix
    def __str__(self):
        rowstring = ''
        for row in self.matrix:
            rowstring += '['
            for cell in row:
                rowstring += (' '+str(cell)+' ')
            rowstring += ']\n'
        return rowstring
    def rotate90degree(self):
        newmatrix = []
        for i in xrange(self.c):
            tempcolumn = []
            for j in xrange(self.r):
                tempcolumn.append(self.matrix[j][i])
            newmatrix.append(tempcolumn)
        self.r = len(newmatrix)
        self.c = len(newmatrix[0])
        self.newmatrix = newmatrix
    def zerorowcolumn(self):
        zeroraw, zerocolumn = [], []
        for i in xrange(self.r):
            for j in xrange(self.c):
                if self.matrix[i][j] == 0:
                    zeroraw.append(i)
                    zerocolumn.append(j)
        for index in zeroraw:
            for c in xrange(self.c):
                self.matrix[index][c] = 0
        for index in zerocolumn:
            for c in xrange(self.r):
                self.matrix[c][index] = 0

'''
1.8 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of "erbottlewat").
'''

def check_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        return s1.find(s2) > -1

def check_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        str1dic, str2dic = {}, {}
        for char in str1:
            if char in str1dic:
                str1dic[char] += 1
            else:
                str1dic[char] = 1
        for char in str2:
            if char in str2dic:
                str2dic[char] += 1
            else:
                str2dic[char] = 1
        if cmp(str1dic, str2dic) == 0:
            return True
        else:
            return False
