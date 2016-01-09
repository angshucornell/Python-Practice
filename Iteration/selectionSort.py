def selectionSort(alist):
   l = len(alist)
   print l
   for fillslot in range(l -1 , 0 , -1 ):
       positionOfMax=0
       print range(1, fillslot+1)
       for location in range(1,fillslot+1):
           if alist[location] > alist[positionOfMax]:
               positionOfMax = location
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
       print alist

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

