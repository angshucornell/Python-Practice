n = 5
for cl in range(2, n+1):
	for i in range(n-cl+1):
		j = i + cl - 1
#		print i, j


for i in range(0,n):
	for j in range(i+1, n):
		print i,j

def f4(seq): 
   # order preserving
   noDupes = []
   a = set()
#   [noDupes.append(i) for i in seq if not noDupes.count(i)]
   for x in seq:
	if x not in a:
		a.add(x)
		noDupes.append(x)
   return noDupes
		          
	
#print f4([2,1,2,1,3,4,2,1,1])	


def f5(seq): 
   # order preserving
   noDupes, a = [], set()
   n,j = len(seq), 0

   for i in range(n):
        x = seq[i]
	if x not in a:
		a.add(x)
                seq[j] = x
                j = j + 1
   return seq[:j]
print f5([2,1,2,1,3,4,2,1,1])	
