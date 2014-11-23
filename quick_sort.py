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
		return quick_sort(left) + [first] + quick_sort(right)

#Test case
print quick_sort([2,6,7,3,9,1,5])

#pivot is the element in the middle
def quick_sort(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    else:
        pivot = len(lst) // 2
        left, right = [], []
        element = lst.pop(pivot)
        for item in lst:
            if item < element:
                left.append(item)
            else:
                right.append(item)
        return quick_sort(left) + [element] + quick_sort(right)

#Test case
print quick_sort([2,6,7,3,9,1,5])

#pivot is the element in the middle. Pointers moved from both ends [Improved version]
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

#Test case
lst = [2,6,7,3,9,1,5];
quick_sort(lst, 0, len(lst)-1)
print lst
