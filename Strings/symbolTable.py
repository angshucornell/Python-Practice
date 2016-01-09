def reverse(str):
	ans = ''
	n = len(str)
	for i in range(n-1, -1 ,-1):
		ans = ans + str[i]
	return ans

def tokenize(str, delimiters):
	list = [] 
	para = ''
	tmp = '' 
	for x in str:
		if(x in delimiters):
			list.append(reverse(tmp))
			tmp = tmp + x
			para = para + reverse(tmp) 
			tmp = '' 
		else:
			tmp = tmp + x
        
	list.append(reverse(tmp))
	para = para + reverse(tmp) 
	
	return list, para	


print tokenize("abc saasf sadg sdfg dsfg ds,fg dsfg dsfg,dfsgdsfgdsf dfs, dsfg", [' ', ',', '\n'])
print tokenize("abc", " ")

