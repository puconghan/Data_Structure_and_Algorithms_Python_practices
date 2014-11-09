#While loop solution
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

#Traditional recursive solution
def binary_search(lst, item, first = 0, last = 0):
	if len(lst) == 0 or item is None:
		return False
	elif (len(lst) == 1 and item != lst[0]) or first == last:
		return False
	else:
		pivot = (first + last) // 2
		if item == lst[pivot]:
			return True
		elif item < lst[pivot]:
			return binary_search(lst, item, first, pivot - 1)
		else:
			return binary_search(lst, item, pivot + 1, last)

#Python list recursive solution
def binary_search(lst, item):
	if len(lst) == 0:
		return False
	elif len(lst) == 1 and item != lst[0]:
		return False
	else:
		pivot = len(lst) // 2
		if lst[pivot] == item:
			return True
		elif item < lst[pivot]:
			return binary_search(lst[:pivot], item)
		else:
			return binary_search(lst[pivot+1:], item)
