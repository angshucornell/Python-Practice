def MinHeapify(A, T):
    def heapify(i):
        left = i*2
	right = i+2 + 1 
	smallest = i
        if ( T[left] < T[right]) 
		smallest = T[left]
	else if (T[right] < T[left] ) 
		smallest = T[right] 
	if (smallest != i )
		temp = T[smallest]
		T[smallest] = T[i]
		T[i] = temp	
		heapify(smallest)	
    def insertKey(A, k):
	A.append(k)
	index = len(A) - 1
	
		
    def siftDown(A, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and T.count(A[child]) < T.count(A[child + 1]):
                child += 1
            if child <= end and T.count(A[root]) < T.count(A[child]):
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return

    heapify(A)

    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        siftDown(A, 0, end - 1)
        end -= 1


if __name__ == '__main__':
    array = [5, 6, 9, 3, 2, 1, 7, 12, 8]
    print array 

    HeapSort(heap, array)
    print heap
