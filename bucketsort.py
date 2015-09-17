#!/usr/bin/env python

def select_pivot(a):
	if len(a) >= 3:
		first_three = a[:3]
		return sorted(first_three)[1]
	else:
		return a[0]

def quickSort(a):
	lesser, equal, greater = [],[],[]
	if len(a) > 1:
		pivot = select_pivot(a)
		for x in a:
			if x < pivot:
				lesser.append(x)
			elif x > pivot:
				greater.append(x)
			else:
				equal.append(x)
		return quickSort(lesser) + equal + quickSort(greater) # joins 3 sorted arrays
	
	# Base case len(a) == 1
	else:
		return a 

# a list of values, k num of buckets
def bucketSort(a, k):
	buckets = [[] for x in range(k)]
	largest_value = max(a)
	bucket_range = largest_value//k+1
	print k, largest_value, bucket_range

	# Place value in proper bucket
	for x in a:
		buckets[x//bucket_range].append(x)
		print x, buckets

	# Sort buckets and merge
	a_sorted = []
	for b in buckets:
		a_sorted += quickSort(b)
	return a_sorted

alist = [5,54,26,93,17,77,31,44,55,20]
print(bucketSort(alist,5))