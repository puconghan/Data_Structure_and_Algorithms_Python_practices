'''
Implementation for regular expression pattern matching for '.' and '*'
'''

def pattern_matching(string, pattern):
    if len(pattern) == 0:
        return len(string) == 0
    if len(pattern) == 1:
        if pattern[0] != '.':
            return (string[0] == pattern[0] and len(string) == 1)
        else:
            return pattern_matching(string[1:], pattern[1:])
    else:
        if pattern[1] == '*':
            if string[0] != pattern[0] and pattern[0] != '.':
                return False
            else:
                pattern = pattern[2:]
                while len(string) >= 2 and string[0] == string[1]:
                    string = string[1:]
                string = string[1:]
                return pattern_matching(string, pattern)
        else:
            if string[0] != pattern[0] and pattern[0] != '.':
                return False
            else:
                return pattern_matching(string[1:], pattern[1:])

#Test cases for pattern matching
#print pattern_matching('a', 'a'), True
#print pattern_matching('a', 'b'), False
#print pattern_matching('aa', 'aa'), True
#print pattern_matching('aa', 'ab'), False
#print pattern_matching('aa', 'a.'), True
#print pattern_matching('aaa', 'a.'), False
#print pattern_matching('aaa', 'a*'), True
#print pattern_matching('aa', '.*'), True
#print pattern_matching('aaa', '.*'), True
#print pattern_matching('aabbcc', 'a*c*'), False
#print pattern_matching('abc', 'a*b*c*'), True

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
    m = re.match(r'(^-)?\d*(\.)?\d*', inputs)
    return True if m.group() else False

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
        if isinstance(item, list):
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
                digit = num[i]
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
                    if count != 1:
                        result += (str(count) + digit)
                    else:
                        result += digit
                    count = 1
                    digit = char
        if count != 1:
            result += (str(count) + digit)
        else:
            result = digit
        return result

#Test for urlAbbr
#print urlAbbr('abbbccccddddd')
#print urlAbbr('abcd')

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
            result = str(curr.data)
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

'''
This class will be given a list of words (such as might be tokenized from a paragraph of text), and will provide a method that takes two words and returns the shortest distance (in words) between those two words in the provided text.
Example:
    WordDistanceFinder finder = new WordDistanceFinder(Arrays.asList("the", "quick", "brown", "fox", "quick"));
    assert(finder.distance("fox","the") == 3);
    assert(finder.distance("quick", "fox") == 1);
'''

class WordDistanceFinder:
    def __init__(self):
        self.dictionary = ["the", "quick", "brown", "fox", "quick"]
    def distance(self, str1, str2):
        length = len(self.dictionary)
        index1, index2 = None, None
        for i in xrange(length):
            if self.dictionary[i] == str1:
                index1 = i
            if self.dictionary[i] == str2:
                index2 = i
        if index1 is None or index2 is None:
            return False, 'Word not in dictionary'
        else:
            return abs(index1-index2)

#Test for WordDistanceFinder class
#finder = WordDistanceFinder()
#print finder.distance('fox', 'the')
#print finder.distance('quick', 'fox')

'''
Find the maximum sum subset in an array with negative integers
[-2, 1, -3, 4, -1, 2, 1, -5, 4] => [4, -1, 2, 1]
Kadane's algorithm
'''

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

#Test for max subarray
#print max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

'''
find the Maximum product subset with negative and positive integer
Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -3, 0, -2, -40}
Output:   80  // The subarray is {-2, -40}
'''

def max_product_subset(lst):
    if len(lst) == 0:
        return None
    max_product, min_product, max_so_far = 1, 1, 1
    for x in lst:
        if x > 0:
            max_product *= x
            min_product = min(min_product*x, 1)
        elif x == 0:
            max_product, min_product = 1, 1
        else:
            temp = max_product
            max_product = max(min_product*x, 1)
            min_product = temp*x
        if max_product > max_so_far:
            max_so_far = max_product
    return max_so_far

#Test for max_product_subset
#print max_product_subset([6, -3, -10, 0, 2]), 180
#print max_product_subset([-1, -3, -10, 0, 60]), 60
#print max_product_subset([-2, -3, 0, -2, -40]), 80

'''
Given a list of tuples representing intervals, return the range of unique intervals.
e.g:
[(1,3), (2,5),(8,9)] should return 5
'''

def unique_interval(lst):
    temp, num = {}, 0
    for (l, r) in lst:
        while l <= r:
            if l not in temp:
                temp[l] = 1
            else:
                temp[l] += 1
            l += 1
    for key, elem in temp.items():
        if elem == 1:
            num += 1
    return num

#Test for unique interval
#print unique_interval([(1,3), (2,5), (8,9)]), 5

'''
Given a sorted array with duplicates and a number, find the range in the
form of (startIndex, endIndex) of that number. For example,

find_range({0 2 3 3 3 10 10}, 3) should return (2,4).
find_range({0 2 3 3 3 10 10}, 6) should return (-1,-1).
The array and the number of duplicates can be large.
'''

def modified_binary_search(lst, l, r, num):
    if r < l:
        return (-1, -1)
    if r == l and lst[l] != num:
        return (-1, -1)
    length = r - l
    if length == 1:
        if lst[l] != num or lst[l+1] != num:
            return (-1, -1)
    pivot = length // 2 + l
    if lst[pivot] == num:
        return expand(lst, pivot)
    elif num < lst[pivot]:
        return modified_binary_search(lst, l, pivot, num)
    else:
        return modified_binary_search(lst, pivot, r, num)

def expand(lst, pivot):
    left, right = pivot, pivot
    while lst[left-1] == lst[pivot]:
        left -= 1
    while lst[right+1] == lst[pivot]:
        right += 1
    return (left, right)

#Test for modified_binary_search
#print modified_binary_search([0,2,3,3,3,4,5,6,7,8,9,10,10], 0, 12, 3)
#print modified_binary_search([0,2,3,3,3,4,5,6,7,8,9,10,10], 0, 12, 1)

'''
Word Wrap / String Justification algorithm.
Given a set of words and a length.
You are required to print the words such that the words on each line end almost on the same column and the number of trailing spaces at the end is minimized.

Given aaa bb cc ddddd and length is 5 print the following output.

aaa
bb cc
ddddd
'''

def word_wrap(string, l):
    if len(string) <= 5:
        print string
    else:
        if string[l-1] != string[l]:
            print string[:l]
            string = string[l:]
        else:
            while string[l-1] == string[l-2]:
                l -= 1
            if string[:l-1] != ' ':
                print string[:l-1]
            string = string[l-1:]
        word_wrap(string, l)

#Test for word_wrap
#word_wrap('aaa bb cc ddddd', 5)

'''
Returns a^b, as the standard mathematical exponentiation function
public double pow(double a, int b) {}
'''

#Runtime O(n)
def _pow(curr, a, b):
    if b == 1:
        return curr
    else:
        return _pow(curr*a, a, b-1)

def pow(a, b):
    return _pow(a, a, b)

#Runtime O(log(n))
def pow(a, b):
    if b < 0:
        return 1 // pow(a, -b)
    elif b == 0:
        return 1
    else:
        halfpow = pow(a, b//2)
        if b%2 == 0:
            return halfpow * halfpow
        else:
            return halfpow * halfpow * a

#Test for pow
#print pow(2, 3), 8
#print pow(3, 2), 9
