def binSearch(arr, x):
	if not len(arr):
		return False
	hi = len(arr) - 1
	lo = 0
	while hi > lo:
		mid = (hi+lo)/2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			lo = mid+1	
	 	else:
			hi = mid-1
	return False

# Test Cases: 
print binSearch([3, 5 , 12, 15, 16, 20], 7)
print binSearch([3, 5 , 12, 15, 16, 20], 20)
print binSearch([3, 5 , 12, 15, 16, 20], 3)
print binSearch([3, 5 , 12, 15, 16, 20], 12)
