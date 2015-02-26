'''
You have a user-submitted review. Design and write an algorithm to break up the review into sentences, and put it in a list/array data structure.
'''


def text_processing(inputs):
    import re
    result = [i.strip() for i in re.split("[.?!]", inputs) if i != '']
    return result

#Test case
'''
input = 'This is test string. The goal is to break this input by eliminators. Do you know how to do it? In particular, I do not want comma to be one of the eliminators. Other special charactors should be count. Please make this happen!'
print text_processing(input)
'''

'''
Given
{
    #"Restaurant Types"."[categoryNames]"
    "American" : "[Burger, French fries, Potato Chips]",
    "Italian":"[Pizza,Bread Sticks, Potato Chips]"
}
Assume this kind of data is given as input and loaded into your choice of Data Structure.
Using Category name return the no of resturarnt type. Ex: if i/p is Potato Chips, O/P should be : 2 (American and Italian).

Please mention your Data structure and logic.
Hash table/dictionary -> access run time is O(1)
'''

def load_data(restaurants):
    if isinstance(restaurants, dict):
        foods = {}
        for key, value in restaurants.iteritems():
            for food in value:
                if food in foods:
                    foods[food].append(key)
                else:
                    foods[food] = [key]
        return foods

#Test case
'''
restaurants = {
"American": ["Burger", "French fries", "Potato Chips"],
"Italian": ["Pizza", "Bread Sticks", "Potato Chips"],
}
print load_data(restaurants)
'''

'''
Implement the 'cd' command. Given a function cd('a/b','c/../d/e/../f'), where 1st param is current directory and 2nd param is the sequence of operations, find the final directory that the user will be in when the cd command is executed
'''

def cd_command(currdir, operations):
    result = ''
    stack = currdir.split('/')
    operators = operations.split('/')
    for op in operators:
        if op == '..':
            if len(stack) > 0:
                stack.pop(-1)
        else:
            stack.append(op)
    while len(stack) > 0:
        if result == '':
            result = stack.pop(0)
        else:
            result += ('/' + stack.pop(0))
    return result

#Test case
'''
print cd_command('a/b','c/../d/e/../f')
'''

'''
Write code to generate all possible case combinations of a given lower-cased string.
'''

def combinations(prefix, inputs):
    if len(inputs) == 0:
        return [prefix]
    elif len(inputs) == 1:
        return [prefix+inputs.lower(), prefix+inputs.upper()]
    else:
        result = []
        last = inputs[-1]
        inputs = inputs[:-1]
        for item in combinations('', inputs):
            result.append(prefix+item+last.lower())
            result.append(prefix+item+last.upper())
        return result

#Test case
'''
print combinations('0', 'abc')
'''

'''
If we're given a set of integers such that S = {1, 2, 3}, how can we find all the subsets of that set? For example, given S, the subsets are {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, and {1, 2, 3}.
'''

def subset(inputs):
    result = []
    num_of_subset = 1 << len(inputs)
    for i in xrange(num_of_subset):
        bitmask = i
        pos = len(inputs) - 1
        temp = []
        while bitmask > 0:
            if bitmask & 1 == 1:
                temp.append(inputs[pos])
            pos -= 1
            bitmask >>= 1
        result.append(temp)
    return result

#Test case
'''
print subset([1,2,3])
'''

'''
Dynamic programming find the nth fibonacci number
'''

fib = {}
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n in fib:
        return fib[n]
    else:
        fib[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib[n]

#Test case
'''
print fibonacci(6)
'''

'''
Print the matrix in spiral form
'''

#Solution using loops
def move_right_down(start, matrix, visited):
    (r, c) = start
    c += 1
    while c < len(matrix[0]):
        if matrix[r][c] not in visited:
            visited.append(matrix[r][c])
        else:
            break
        c += 1
    c -= 1
    r += 1
    while r < len(matrix):
        if matrix[r][c] not in visited:
            visited.append(matrix[r][c])
        else:
            break
        r += 1
    r -= 1
    return (r, c)

def move_left_up(start, matrix, visited):
    (r, c) = start
    c -= 1
    while c >= 0:
        if matrix[r][c] not in visited:
            visited.append(matrix[r][c])
        else:
            break
        c -= 1
    c += 1
    r -= 1
    while r >= 0:
        if matrix[r][c] not in visited:
            visited.append(matrix[r][c])
        else:
            break
        r -= 1
    r += 1
    return (r, c)

def print_spiral(matrix):
    visited = []
    point = (0, -1)
    while len(matrix)*len(matrix[0]) > len(visited):
        point = move_right_down(point, matrix, visited)
        point = move_left_up(point, matrix, visited)
    print visited

#Test case
'''
print_spiral([[1,2],[3,4]])
print_spiral([[1,2,3],[4,5,6],[7,8,9]])
print_spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
'''

#Solution using recursive functions
def move_right(point, matrix, visited):
    (r, c) = point
    if matrix[r][c] not in visited:
        while c < len(matrix[0]):
            if matrix[r][c] not in visited:
                visited.append(matrix[r][c])
            else:
                break
            c += 1
        c -= 1
        if len(matrix)*len(matrix[0]) > len(visited):
            r += 1
            point = (r, c)
            move_down(point, matrix, visited)

def move_down(point, matrix, visited):
    (r, c) = point
    if matrix[r][c] not in visited:
        while r < len(matrix):
            if matrix[r][c] not in visited:
                visited.append(matrix[r][c])
            else:
                break
            r += 1
        r -= 1
        if len(matrix)*len(matrix[0]) > len(visited):
            c -= 1
            point = (r, c)
            move_left(point, matrix, visited)

def move_left(point, matrix, visited):
    (r, c) = point
    if matrix[r][c] not in visited:
        while c >= 0:
            if matrix[r][c] not in visited:
                visited.append(matrix[r][c])
            else:
                break
            c -= 1
        c += 1
        if len(matrix)*len(matrix[0]) > len(visited):
            r -= 1
            point = (r, c)
            move_up(point, matrix, visited)

def move_up(point, matrix, visited):
    (r, c) = point
    if matrix[r][c] not in visited:
        while r >= 0:
            if matrix[r][c] not in visited:
                visited.append(matrix[r][c])
            else:
                break
            r -= 1
        r += 1
        if len(matrix)*len(matrix[0]) > len(visited):
            c += 1
            point = (r, c)
            move_right(point, matrix, visited)

def print_spiral(matrix):
    point = (0, 0)
    visited = []
    move_right(point, matrix, visited)
    print visited


#Test case
'''
print_spiral([[1,2],[3,4]])
print_spiral([[1,2,3],[4,5,6],[7,8,9]])
print_spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
'''
