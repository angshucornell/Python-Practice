def preprocess(seq):
	cumulative = []
	sumSoFar = 0
	for x in seq:	
		sumSoFar = sumSoFar + x
		cumulative.append( sumSoFar )
	return cumulative			

def sum(seq, i, j):
	cumulative = preprocess(seq)
	return cumulative[j] - cumulative[i] + seq[i] 


print sum([1,2,3,4,5,6] , 1, 4) 	
