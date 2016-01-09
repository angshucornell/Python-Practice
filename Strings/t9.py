n2l={ 2:'abc',
      3:'def',
      4:'ghi',
      5:'jkl',
      6:'mno',
      7:'pqrs',
      8:'tuv',
      9:'wxyz'}

def generate(str):
	for i in range(len(str)):
		index = 1+ ord(str[i]) - ord('1')
	   	print n2l[index]	

generate("237")
