'''
5.1 You are given two 32-bit numbers, N and M, and two bit positions, i and j Write a method to set all bits between i and j in N equal to M (e g , M becomes a substring of N located at i and starting at j)
EXAMPLE: Input: N = 10000000000, M = 10101, i = 2, j = 6 Output: N = 10001010100
'''

def bit_replace(n, m, i, j):
    length = len(n) - 1
    new_i, new_j = length - i, length - j
    new_n = list(n)
    new_m = list(m)
    for index in xrange(new_j, new_i + 1, 1):
        new_n[index] = new_m.pop(0)
    return ''.join(new_n)

def bit_replace(n, m, i, j):
    stack = []
    n = list(n)
    m = list(m)
    while len(n) != 0:
        if i != 0 and j != 0:
            stack.append(n.pop(-1))
            i -= 1
            j -= 1
        elif i == 0 and j != -1:
            stack.append(m.pop(-1))
            j -= 1
        elif i == 0 and j == -1 and len(m) == 0:
            stack.append(n.pop(-1))
    output = ''
    while len(stack) != 0:
        output += stack.pop(-1)
    return output

'''
5.2 Given a (decimal - eg 3.72) number that is passed in as a string, print the binary representation If the number can not be represented accurately in binary, print ERROR
'''

def binary_convertor(decimal):
    result = ''
    numlist = str(decimal).split('.')
    if len(numlist) == 1:
        integer = int(numlist[0])
        while integer != 0:
            digit = integer % 2
            integer = integer / 2
            result = str(digit) + result
    elif len(numlist) == 2:
        integer = int(numlist[0])
        decimal = float('0.' + numlist[1])
        while integer != 0:
            digit = integer % 2
            integer = integer / 2
            result = str(digit) + result
        result += '.'
        image = ''
        stack = [decimal]
        while decimal != 1:
            decimal = decimal * 2
            if decimal in stack:
                return 'ERROR'
            else:
                stack.append(decimal)
                if decimal < 1:
                    image = '0' + image
                if decimal == 1:
                    image = '1' + image
                if decimal > 1:
                    image = '1' + image
        result = result + image
    return result

'''
5.3 Given an integer, print the next smallest and next largest number that have the same number of 1 bits in their binary representation
'''

def find_larger(binary):
    binary = list(str(binary))
    length = len(binary)
    flag = False
    pivot = 0
    for index in xrange(length - 1, -1, -1):
        if flag is False:
            if binary[index] == '1':
                flag = True
        if flag is True:
            if binary[index] == '0':
                binary[index] = '1'
                binary[index+1] = '0'
                pivot = index
                break
    zero = []
    one = []
    while len(binary) > pivot + 1:
        digit = binary.pop(pivot+1)
        if digit == '1':
            one.append('1')
        if digit == '0':
            zero.append('0')
    binary = binary + zero + one
    return ''.join(binary)

def find_smaller(binary):
    binary = list(str(binary))
    length = len(binary)
    flag = False
    pivot = 0
    for index in xrange(length - 1, -1, -1):
        if flag is False:
            if binary[index] == '0':
                flag = True
        if flag is True:
            if binary[index] == '1':
                binary[index] = '0'
                binary[index+1] = '1'
                pivot = index
                break
    zero = []
    one = []
    while len(binary) > pivot + 1:
        digit = binary.pop(pivot+1)
        if digit == '1':
            one.append('1')
        if digit == '0':
            zero.append('0')
    binary = binary + one + zero
    return ''.join(binary)

#print '11111100000000011111'
#print find_larger('11111100000000011111')
#print find_smaller('11111100000000011111')

'''
5.4 Explain what the following code does: ((n & (n-1)) == 0)

abcde1000
abcde0111

checks if n is a power of 2 (or 0)
'''

'''
5.5 Write a function to determine the number of bits required to convert integer A to integer B
Input: 31, 14 Output: 2
'''
def convert_to_binary(num):
    binary = ''
    while num != 0:
        bit = num % 2
        num = num // 2
        binary = str(bit) + binary
    return binary

def num_of_bit(num1, num2):
    bits = 0
    binary1 = convert_to_binary(num1)
    binary2 = convert_to_binary(num2)
    for i in xrange(-1, -max(len(binary1), len(binary2))-1, -1):
        try:
            if binary1[i] != binary2[i]:
                bits += 1
        except IndexError:
            bits += 1
    print binary1, binary2, bits

'''
5.6 Write a program to swap odd and even bits in an integer with as few instructions as possible (e g , bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc)
'''

def swap_odd_even(binary):
    binary = list(str(binary))
    for i in xrange(-1, -len(binary)-1, -2):
        try:
            swap(binary, i, i-1)
        except IndexError:
            break
    print binary


def swap(inputs, i, j):
    temp = inputs[i]
    inputs[i] = inputs[j]
    inputs[j] = temp

#swap_odd_even('1010101010')

'''
5.7 An array A[1 to n] contains all the integers from 0 to n except for one number which is missing. In this problem, we cannot access an entire integer in A with a single operation. The elements of A are represented in binary, and the only operation we can use to access them is [fetch the jth bit of A[i]], which takes constant time Write code to find the missing integer Can you do it in O(n) time?
'''
def fetch_jth_bit_ai(blist, j, i):
    return blist[j][i]

#Binary addition
def binary_add(bin1, bin2):
    result = ''
    carry = '0'
    for i in xrange(-1, -len(bin1), -1):
        if carry == '0':
            if bin1[i] == '0' and bin2[i] == '0':
                result = '0' + result
            elif (bin1[i] == '1' and bin1[i] == '0') or (bin1[i] == '0' and bin1[i] == '1'):
                result = '1' + result
            else:
                carry = '1'
                result = '0' + result
        if carry == '1':
            if bin1[i] == '0' and bin2[i] == '0':
                result = '1' + result
            elif (bin1[i] == '1' and bin1[i] == '0') or (bin1[i] == '0' and bin1[i] == '1'):
                carry = '1'
                result = '0' + result
            else:
                carry = '1'
                result = '1' + result
    return result

def find_missing_binary(blist):
    size = len(blist)
    flag = 1
    for j in xrange(size):
        if fetch_jth_bit_ai(blist, j, -1) == '1' and flag == 1:
            flag = 0
        elif fetch_jth_bit_ai(blist, j, -1) == '0' and flag == 0:
            flag = 1
        else:
            one = ''
            for i in xrange(len(blist[j-1])-1):
                one += '0'
            one += '1'
            return binary_add(blist[j-1], one)

#print find_missing_binary(['001','010','011','100','101','111'])
