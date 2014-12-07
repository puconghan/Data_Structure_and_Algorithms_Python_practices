'''
Given a array of positive integers, find all possible triangle triplets that can be formed from this array.
eg: 9 8 10 7
'''

#least parent = floor(n-1)/2
#left node = 2*n + 1
#right node = 2*n + 2
def heap_sort(lst):
    length = len(lst) - 1
    leastp = length // 2
    for i in xrange(leastp, -1, -1):
        movedown(lst, i, length)
    for i in xrange(length, 0, -1):
        if lst[0] > lst[i]:
            swap(lst, 0, i)
            movedown(lst, 0, i-1)
    return lst

def movedown(lst, i, j):
    l = i*2 + 1
    while l <= j:
        if l < j and lst[l] < lst[l+1]:
            l += 1
        if lst[l] > lst[i]:
            swap(lst, l, i)
            i = l
            l = i*2 + 1
        else:
            return

def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

#test for heap sort | average run time and worst run time O(nlog(n))
#print heap_sort([5,1,3,8,0,2,7])

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = len(lst) // 2
        return merge(merge_sort(lst[:pivot]), merge_sort(lst[pivot:]))

def merge(lst1, lst2):
    count1, count2 = 0, 0
    temp = []
    while count1 < len(lst1) and count2 < len(lst2):
        if lst1[count1] < lst2[count2]:
            temp.append(lst1[count1])
            count1 += 1
        else:
            temp.append(lst2[count2])
            count2 += 1
    while count1 < len(lst1):
        temp.append(lst1[count1])
        count1 += 1
    while count2 < len(lst2):
        temp.append(lst2[count2])
        count2 += 1
    return temp

#Test for merge sort | avarage run time and worst run time O(nlog(n))
#print merge_sort([8,2,4,0,1,4,7,5,6])

def quick_sort(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    else:
        first = lst[0]
        rest = lst[1:]
        left, right = [], []
        for item in rest:
            if item < first:
                left.append(item)
            else:
                right.append(item)
        return quick_sort(left) + [first] + quick_sort(right)

#Test for quick sort | avarage run time O(nlog(n)) | worst run time O(n^2)
#print quick_sort([3,6,9,1,4,5,2,0])

def triangle_triplets(lst):
    results = []
    length = len(lst)
    #lst = quick_sort(lst)
    #lst = merge_sort(lst)
    lst = heap_sort(lst)
    for i in xrange(length-2):
        for j in xrange(i+1, length-1):
            k = j+1
            while (k <= length-1) and (lst[i]+lst[j] > lst[k]):
                results.append((lst[i],lst[j],lst[k]))
                k = k + 1
    return results

#Test for triangle_triplets
#print triangle_triplets([9,8,10,7])

'''
Write an function to judge whether the input String is a number
'''

#Solution using regular expression
import re
def isNumber(inputs):
    m = re.search('(^-)?d*(\.)?d*', inputs)
    if m:
        return True
    else:
        return False

#Solution using ascii
def isNumber(inputs):
    if len(inputs) == 0:
        return False
    else:
        first = ord(inputs[0])
        dotflag = False
        if first == 45:
            inputs = inputs[1:]
        for char in inputs:
            char = ord(char)
            if char == 46 and dotflag == False:
                dotflag == True
            if char == 46 and dotflag == True:
                return False
            if (char < 48 or char > 57) and char != 46:
                return False
        return True

#Test for isNumber
#print isNumber('1.this'), False
#print isNumber('1'), True
#print isNumber('-1'), True
#print isNumber('1.1'), True
#print isNumber('-1.1'), True
#print isNumber('-1.11'), True
#print isNumber('1.12'), True

'''
Write a function to compute the maximum length palindromic sub-sequence of an array.
A palindrome is a sequence which is equal to its reverse.
A sub-sequence of an array is a sequence which can be constructed by removing elements of the array.
'''

#Solution: O(N2) time and O(1) space
def expandFromCenter(s, l, r):
    length = len(s)
    while l>0 and r<length-1 and s[l-1] == s[r+1]:
        l = l-1
        r = r+1
    return s[l:r+1]

#Test for expandFromCenter
#print expandFromCenter('abcba', 2, 2), 'abcba'
#print expandFromCenter('abccba', 2, 2), 'c'
#print expandFromCenter('acccb', 2, 2), 'ccc'

def longestPalindromic(s):
    if len(s) == 0:
        return False
    else:
        longest = s[:1]
        for i in xrange(len(s)-1):
            str1 = expandFromCenter(s, i, i)
            if(len(str1) > len(longest)):
                longest = str1
            str2 = expandFromCenter(s, i, i+1)
            if(len(str2) > len(longest)):
                longest = str2
        return longest

#Test for longestPalindromic
#print longestPalindromic('41234565434444444')
#print longestPalindromic('4123456544444444')
#print longestPalindromic('asdfghjklqwertyytuiop')

'''
Given a nested list of integers, returns the sum of all integers in the list weighted by their depth.
For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
'''

def computeList(lst, i):
    if len(lst) == 0:
        return 0
    levelsum = 0
    for item in lst:
        if type(item) is list:
            levelsum += computeList(item, i+1)
        else:
            levelsum += item*i
    return levelsum

#Test for computeList
#print computeList([[1,1],2,[1,1]], 1), 10
#print computeList([1,[4, [6]]], 1), 27

'''
There is a particular sequence that only uses numbers 1, 2, 3, 4 and no two adjacent numbers are the same.
Write a program that given n1 1s, n2 2s, n3 3s, n4 4s will output the number of such sequences using all these numbers.
Output your answer modulo 1000000007 (1 + 0^9 + 7).
'''

def numberSequence(num):
    if len(num) == 0:
        return None
    else:
        result = ""
        count = 1
        digit = num[0]
        for i in xrange(1, len(num)):
            if num[i] == digit:
                count += 1
            else:
                if result == "":
                    result += str(num[i])
                else:
                    result += ' + ' + str(num[i])
                if count != 1:
                    result += '^' + str(count)
                count = 1
                digit = str(num[i])
        result += ' + ' + str(digit)
        if count != 1:
            result += '^' + str(count)
        return result

#Test for numberSequence
#print numberSequence('10000000007')
#print numberSequence('10000000007776666666')

'''
URL abbreviation aabbbcc -> 2a3b2c
'''

def urlAbbr(url):
    if len(url) == 0:
        return None
    else:
        result = ''
        count = 0
        digit = ''
        for char in url:
            if count == 0 and digit == '':
                count = 1
                digit = char
            else:
                if digit == char:
                    count += 1
                else:
                    result += (str(count) + digit)
                    count = 1
                    digit = char
        result += (str(count) + digit)
        return result

#Test for urlAbbr
#print urlAbbr('aabbbcc')

'''
Given a binary tree where all the right nodes are leaf nodes, flip it upside down and turn it into a tree with left leaf nodes.
Keep in mind: ALL RIGHT NODES IN ORIGINAL TREE ARE LEAF NODE.

/* for example, turn these:
 *
 *        1                 1
 *       / \               / \
 *      2   3             2   3
 *     / \
 *    4   5
 *   / \
 *  6   7
 *
 * into these:
 *
 *        1               1
 *       /               /
 *      2---3           2---3
 *     /
 *    4---5
 *   /
 *  6---7
 *
 * where 6 is the new root node for the left tree, and 2 for the right tree.
 * oriented correctly:
 *
 *     6                   2
 *    / \                 / \
 *   7   4               3   1
 *        / \
 *       5   2
 *            / \
 *          3   1
 */
'''

def reverseTree(node):
    if node == None:
        return None
    if node.left is None and node.right is None:
        return node
    newRoot = reverseTree(node.left)
    node.left.left = node.right
    node.left.right = node
    node.left = None
    node.right = None
    return newRoot


'''
Print a tree in Level Order with a newline after each depth

/**
 * Sample input:
 *
 *          1
 *         / \
 *        3   5
 *       / \   \
 *      2   4   7
 *     /     \
 *    9       8
 *
 * Expected output:
 *    1
 *    3 5
 *    2 4 7
 *    9 8
 *    ==========
 */
'''

#Recursive solution
def getDepth(node):
    if node == None:
        return 0
    return max(getDepth(node.left), getDepth(node.right)) + 1

def printLevel(node, i, lst):
    if i == 0:
        lst.append(node.data)
    else:
        if node.left is not None:
            printLevel(node.left, i-1, lst)
        if node.right is not None:
            printLevel(node.right, i-1, lst)

def printLevelDown(node):
    level = getDepth(node)
    for i in xrange(level+1):
        lst = []
        printLevel(node, i, lst)
        print ''.join(lst)

#BFS solution
def printLevelDown(node):
    if node is None:
        return None
    queue = [(node, 1)]
    result = ""
    level = 1
    while len(queue) > 0:
        (curr, currlevel) = queue.pop(0)
        if currlevel == level:
            result += str(curr.data)
        else:
            print ''.join(result)
            level = currlevel
            result = ""
        if curr.left is not None:
            queue.append((curr.left, level+1))
        if curr.right is not None:
            queue.append((curr.right, level+1))

'''
Write a program that gives count of common characters presented in an array of strings..(or array of character arrays)
For eg.. for the following input strings..

aghkafgklt
dfghako
qwemnaarkf

The output should be 3. because the characters a, f and k are present in all 3 strings.
Note: The input strings contains only lower case alphabets
'''

#Solution using a hashmap
def findCommon(lst):
    num = len(lst)
    hashmap = {}
    for string in lst:
        temp = []
        for char in string:
            if char not in hashmap:
                hashmap[char] = 1
                temp.append(char)
            else:
                if char not in temp:
                    hashmap[char] += 1
                    temp.append(char)
    return [key for key, value in hashmap.iteritems() if value >= 3]

#Test for findCommon
#print findCommon(['aghkafgklt', 'dfghako', 'qwemnaarkf'])

'''
Given a string array ex: [1, 2, 3], find the permutation/power set in best time.
'''

def powerset(lst):
    power = [[]]
    for item in lst:
        newset = [p + [item] for p in power]
        power.extend(newset)
    return power

#Test for power set
#print powerset([1,2,3,4])

def permutation(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        temp = []
        for i in xrange(len(lst)):
            pivot = lst[i]
            rest = lst[:i] + lst[i+1:]
            for j in permutation(rest):
                temp.append([pivot] + j)
        return temp

#Test for permutation
#print permutation([1,2,3])

'''
Given two nodes of a tree, method should return the deepest common ancestor of those nodes.
   A
  / \
  B C
 / \ \
 D E M
/   \
G    F

commonAncestor(D, F) = B
commonAncestor(C, G) = A
'''

def commonAncestor(node1, node2):
    curr1, curr2 = node1, node2
    temp = []
    while(curr1 is not None):
        temp.append(curr1)
        curr1 = curr1.parent
    while(curr2 is not None):
        if curr2 in temp:
            return curr2
        curr2 = curr2.parent
    return None
