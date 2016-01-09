def reverse(str):
	ans = ''
	n = len(str)
	for i in range(n-1, -1, -1):
		ans = ans + str[i]
	return ans


print reverse ('abcd')
		
