#!/usr/bin/env python


# OPTIMIZE by perhaps choosing from middle 3 elements
# In case the list is partially sorted
def select_pivot(a):
	if len(a) >= 3:
		first_three = a[:3]
		return sorted(first_three)[1]
	else:
		return a[0]

def quickSort(a):
	lesser, equal, greater = [],[],[]
	print(a)
	if len(a) > 1:
		pivot = select_pivot(a)
		for x in a:
			if x < pivot:
				lesser.append(x)
			elif x > pivot:
				greater.append(x)
			else:
				equal.append(x)
		print(lesser, equal, greater)
		return quickSort(lesser) + equal + quickSort(greater) # joins 3 sorted arrays
	
	# Base case len(a) == 1
	else:
		return a 

alist = [54,26,93,17,77,31,44,55,20]
print(quickSort(alist))