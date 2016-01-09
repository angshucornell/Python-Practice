def qsort(A):
	less = []
	equal = []
	great = []
	if len(A) > 1:
		pivot = A[0]
		for x in A:
			if x > pivot:
				great.append(x)
			elif x == pivot:
				equal.append(x)
			else:
				less.append(x)
		return qsort(less) + equal + qsort(great)
	else:
		return A

print qsort([2,2,3,4,5,6,1]) 
