'''
Divide-and-Conquer algorithm
Average run time O(n*log(n))
'''

def merge_sort(lst):
    size = len(lst)
    if size < 2:
        return lst
    else:
        pivot = size / 2
        return merge(merge_sort(lst[:pivot]), merge_sort(lst[pivot:]))

def merge(lst1, lst2):
    count1, count2, size1, size2 = 0, 0, len(lst1), len(lst2)
    temp = []
    while count1 < size1 and count2 < size2:
        if lst1[count1] < lst2[count2]:
            temp.append(lst1[count1])
            count1 += 1
        else:
            temp.append(lst2[count2])
            count2 += 1
    while count1 < size1:
        temp.append(lst1[count1])
        count1 += 1
    while count2 < size2:
        temp.append(lst2[count2])
        count2 += 1
    return temp

#Test case
'''
print merge_sort([2,6,7,3,9,1,5]);
'''
