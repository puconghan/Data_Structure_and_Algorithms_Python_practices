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

#Test case
print merge_sort([2,6,7,3,9,1,5]);
