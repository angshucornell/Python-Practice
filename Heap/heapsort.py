def HeapSort(A,T):
    def heapify(A):
        start = (len(A) - 2) / 2
        while start >= 0:
            siftDown(A, start, len(A) - 1)
            start -= 1

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
    print 'After Heapify'
    print A 

    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        siftDown(A, 0, end - 1)
        end -= 1


if __name__ == '__main__':
    text = "the quick brown fox jumped over the the quick brown quick log log"
    heap = list(set(text.split()))
    print heap

    HeapSort(heap,text)
#    print heap
