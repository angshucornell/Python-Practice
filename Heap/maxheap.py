def max_heapify(A, i, heap_len):
#	print 'Before: ', A
	left = 2*i
	right = 2*i + 1
	largest = i
#	print 'heap_len = ', heap_len, ' left = ', left, ' right = ', right, ' i = ', i, ' largest = ', largest

	if left < heap_len:
		if A[left] > A[largest]:
			largest = left	
	if (right < heap_len):
		if (A[right] > A[largest]): 
			largest = right

	
	if largest != i :
		temp = A[i]
		A[i] = A [largest]
		A [ largest] = temp
		
		max_heapify(A, largest, heap_len)
#	print 'After: ', A
#	print '--------'
	return A

def build_heap(A):
	heap_len = len(A)
	for index in range ( heap_len/2, -1, -1):
		max_heapify(A, index, heap_len)

def extract(A):
	ans = A[0]
	n = len(A)
	A[0] = A[n-1]
	A.pop()
	print A
	return ans

list = [1, 2, 3, 4 , 5, 6 , 7, 8 , 9]
print build_heap(list)

#print (extract(build_heap(list)))

# [ 20, 26, 32, 45, 81, 42, 
#    81
# 45      32
