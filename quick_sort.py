#pivot is the first element
def quick_sort(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return lst
	else:
		first = lst[0]
		left, right = [], []
		rest = lst[1:]
		for item in rest:
			if item < first:
				left.append(item)
			elif item > first:
				right.append(item)
		return quick_sort(left) + first + quick_sort(right)

#pivot is the element in the middle
def quick_sort(lst, l, r):
	if len(lst) > 2 and r > l:
		left, right = l, r
		pivot = (left + right) // 2
		while left <= right:
			while lst[left] < lst[pivot]:
				left += 1
			while lst[right] > lst[pivot]:
				right -= 1
			if left <= right:
				temp = lst[left]
				lst[left] = lst[right]
				lst[right] = temp
				left += 1
				right -= 1
		if left < r:
			quick_sort(lst, left, r)
		if right > l:
			quick_sort(lst, l, right)

