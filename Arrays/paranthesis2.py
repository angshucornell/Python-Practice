def evaluate(str):
	stack = []
	pushchars, popchars = "[{(", "]})"
	for ch in str:
		print ch
		if ch in pushchars:
			stack.append(ch)
		elif ch in popchars:
			if not len(stack):
				return False
			else:
			 	stackTop = stack.pop()
				match = pushchars[popchars.index(ch)]
				if stackTop != match:
					return False
		else:
			continue
	return not len(stack)

print evaluate("[(12 + 2)]")	
