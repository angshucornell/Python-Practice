def Evaluate(str):
  stack = []
  pushChars, popChars = "<({[", ">)}]"
  for c in str :
    if c in pushChars :
      stack.append(c)
    elif c in popChars :
      if not len(stack) :
        return False
      else :
        stackTop = stack.pop()
        balancingBracket = pushChars[popChars.index(c)]
        if stackTop != balancingBracket :
          return False
    else :
#      return False
      continue 
  return not len(stack)

print len([])
#print Evaluate("[(2+3)*1]")
print Evaluate("[(2+3) * 1 ]")
#print Evaluate("[()]")
