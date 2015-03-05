'''
Binary Search: half-interval search algorithm finds the position of a key within a sorted array.
Average Runtime O(log(n))
'''

#Implementation using recursion and list data structure
def binary_search(lst, item):
    if len(lst) == 0:
        return False
    else:
        pivot = len(lst) / 2
        if lst[pivot] == item:
            return True
        elif item < lst[pivot]:
            return binary_search(lst[:pivot], item)
        else:
            return binary_search(lst[pivot+1:], item)

#Test case
'''
print binary_search([1,2,3,4,5,6,7,8], 4), True
print binary_search([1,2,3,5,6,7,8,9], 4), False
'''

#Implementation using recursion

def binary_search(lst, item, first, last):
    if len(lst) == 0 or item is None or first >= last:
        return False
    else:
        pivot = (first + last) / 2
        if item == lst[pivot]:
            return True
        elif item < lst[pivot]:
            return binary_search(lst, item, first, pivot-1)
        else:
            return binary_search(lst, item, pivot+1, last)

#Test case
'''
print binary_search([1,2,3,4,5,6,7,8], 4, 0, 7), True
print binary_search([1,2,3,5,6,7,8,9], 4, 0, 7), False
'''

#Implementation using while-loop
def binary_search(lst, item):
	first = 0
	last = len(lst) - 1
	found = False
	while first < last and not found:
		midpoint = (first + last) // 2
		if lst[midpoint] == item:
			found = True
		else:
			if item < lst[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

'''
#Test case
print binary_search([1,2,3,4,5,6,7,8], 4), True
print binary_search([1,2,3,5,6,7,8,9], 4), False
'''
