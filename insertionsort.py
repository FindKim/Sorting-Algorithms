def insertion_sort(data):
	if len(data) < 2:
		return
	for r in range(1, len(data)):
		for l in range(0, r):
			if data[l] > data[r]:
				temp = data[r]
				data[l+1:r+1] = data[l:r]
				data[l] = temp
				break