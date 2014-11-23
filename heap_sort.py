'''
Parent: 		floor(i - 1) / 2
Left Child:		2 * i + 1
Right Child:	2 * i + 2
'''

def heap_sort(lst):
	length = len(lst) - 1
	leastparent = length // 2
	for i in xrange(leastparent, -1, -1):
		move_down(lst, i, length)
	for i in xrange(length, 0, -1):
		if lst[0] > lst[i]:
			swap(lst, 0, i)
			move_down(lst, 0, i - 1)
	return lst

def move_down(lst, parent, last):
	largest = parent * 2 + 1
	while largest <= last:
		if largest < last and lst[largest] < lst[largest+1]:
			largest += 1
		if lst[largest] > lst[parent]:
			swap(lst, largest, parent)
			parent = largest
			largest = largest * 2 + 1
		else:
			return

def swap(lst, l, r):
	temp = lst[l]
	lst[l] = lst[r]
	lst[r] = temp

#Test cases
print heap_sort([2,9,3,6,1,8,0,4])
