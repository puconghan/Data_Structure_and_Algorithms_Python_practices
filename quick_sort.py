'''
Divide-and-Conquer algorithm
Average run time O(n*log(n))
Worst case run time O(n^2)
To avoid worst case run time, select middle element as the pivot
'''

#Pivot is the element in the middle.
def quick_sort(lst):
    size = len(lst)
    if size == 0:
        return []
    elif size == 1:
        return lst
    else:
        pivot = size / 2
        left, right = [], []
        element = lst.pop(pivot)
        for item in lst:
            if item <= element:
                left.append(item)
            else:
                right.append(item)
        return quick_sort(left) + [element] + quick_sort(right)

#Test case
'''
print quick_sort([2,6,7,3,9,1,5])
'''

#Pivot is the element in the middle. Pointers moved from both ends.
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
'''
lst = [2,6,7,3,9,1,5];
quick_sort(lst, 0, len(lst)-1)
print lst
'''
