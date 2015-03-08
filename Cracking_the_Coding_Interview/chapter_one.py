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

#Test case
'''
print has_all_unique_char('abcdefg'), True
print has_all_unique_char('abcdefgg'), False
'''

def has_all_unique_char(inputstring):
    length = len(inputstring)
    for i in xrange(length):
        for j in xrange(i+1, length, 1):
            if inputstring[i] == inputstring[j]:
                return False
    return True

#Test case
'''
print has_all_unique_char('abcdefg'), True
print has_all_unique_char('abcdefgg'), False
'''

#O(n^2) Using a list data structure
def has_all_unique_char(inputstring):
    list = []
    #checking if char is in the list is O(n) according to http://wiki.python.org/moin/TimeComplexity
    for item in inputstring:
        if item in list:
            return False
        list.append(item)
    return True

#Test case
'''
print has_all_unique_char('abcdefg'), True
print has_all_unique_char('abcdefgg'), False
'''

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

#Test case
'''
print has_all_unique_char('abcdefg'), True
print has_all_unique_char('abcdefgg'), False
'''

#O(n) Using a hash table (dictionary)
def has_all_unique_char(inputstring):
    char_table = {}
    for char in inputstring:
        if char in char_table:
            return False
        else:
            char_table[char] = True
    return True

#Test case
'''
print has_all_unique_char('abcdefg'), True
print has_all_unique_char('abcdefgg'), False
'''

def has_all_unique_char(inputstring):
    if len(inputstring) > 256: return False
    else: return len(set(inputstring)) == len(inputstring)

#Test case
'''
print has_all_unique_char('abcdefg'), True
print has_all_unique_char('abcdefgg'), False
'''


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

#Test case
'''
print 'Reverse abc: ', reverse_string('abc')
'''

# O(n) Recursive solution
def reverse_string(inputstring):
    if len(inputstring) == 0:
        return ''
    else:
        return inputstring[-1:] + reverse_string(inputstring[:-1])

#Test case
'''
print 'Reverse abc: ', reverse_string('abc')
'''

'''
1.3 Given two strings, write a method to decide if one is a permutation of the other
'''

#O(n^2)
def check_permutation(str1, str2):
    tmp1, tmp2 = str1, str2
    if len(tmp1) != len(tmp2):
        return False
    else:
        for char in tmp1:
            if tmp2.find(char) == -1:
                return False
            else:
                import re
                tmp2 = re.sub(char, '', tmp2)
        if tmp2 == '':
            return True
        else:
            return False

#Test case
'''
print check_permutation('abc', 'cba'), True
print check_permutation('acd', 'abc'), False
'''

#Run time depend of sorting algorithm
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)

#Test case
'''
print check_permutation('abc', 'cba'), True
print check_permutation('acd', 'abc'), False
'''

#O(n) Use a hash table
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    dict1, dict2 = {}, {}
    for char in str1:
        dict1[char] = char
    for char in str2:
        dict2[char] = char
    for key in dict1:
        if not (key in dict2 and dict1[key] == dict2[key]):
            return False
    return True

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        dic = {}
        for char in str1:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        for char in str2:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        for val in dic.values():
            if val != 2:
                return False
        return True

#Test case
'''
print check_permutation('abc', 'cba'), True
print check_permutation('acd', 'abc'), False
'''

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

#Test case
'''
print replace_space('abc def')
'''

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

#Test case
'''
print replace_space('abc def')
'''

'''
1.5 Implement a method to perform basic string compression using the counts of repeated characters
    aabcccccaaa would become a2blc5a3.
    Do nothing if this would not make the string smaller.
'''

def simple_compress(inputstring):
    outputlist, prevchar, count = [], '', 0
    for char in inputstring:
        if prevchar == char:
            count += 1
        else:
            if prevchar != '':
                if count > 1:
                    outputlist.append(char + str(count))
                else:
                    outputlist.append(char)
            count = 1
        prevchar = char
    if count > 1:
        outputlist.append(char + str(count))
    else:
        outputlist.append(char)
    outputstring = ''.join(outputlist)
    if len(inputstring) <= len(outputstring):
        return inputstring
    else:
        return outputstring

#Test case
'''
print simple_compress('aabcccccaaa')
'''

def simple_compress(inputstring):
    prev = ''
    count = 0
    newstring = ''
    for i, char in enumerate(inputstring):
        if prev == '' and count == 0:
            prev = char
            count = 0
        if prev == char:
            count += 1
            if i == len(inputstring) - 1:
                newstring = newstring + prev + str(count)
        else:
            newstring = newstring + prev + str(count)
            prev = char
            count = 1
    return newstring

#Test case
'''
print simple_compress('aabcccccaaa')
'''


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
    def printnewmatrix(self):
        rowstring = ''
        for row in self.newmatrix:
            rowstring += '['
            for cell in row:
                rowstring += (' '+str(cell)+' ')
            rowstring += ']\n'
        return rowstring
    def rotate90degree(self):
        newmatrix = []
        for c in xrange(self.c-1, -1, -1):
            temp = []
            for r in xrange(self.r):
                temp.append(self.matrix[r][c])
            newmatrix.insert(0, temp)
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
            for r in xrange(self.r):
                self.matrix[r][index] = 0

#Test cases
matrix= MatrixProcessor([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print matrix
matrix.rotate90degree()
print matrix.printnewmatrix()
zeromatrix= MatrixProcessor([[1,2,3,4],[5,6,7,8],[9,10,0,12],[13,14,15,16]])
zeromatrix.zerorowcolumn()
print zeromatrix

'''
1.8 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of "erbottlewat").
'''

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

'''
print check_rotation('waterbottle', 'erbottlewat'), True
print check_rotation('waterbottle', 'erbottlewag'), False
'''
