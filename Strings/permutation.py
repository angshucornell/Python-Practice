# Python program to print all permutations with
# duplicates allowed
 
# Function to swap values
def swap(a,l,r):
    t = a[l]
    a[l] = a[r]
    a[r] = t
    return a
 
def toList(string):
    List = []
    for x in string:
        List.append(x)
    return List
 
def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.

def permute(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in xrange(l,r+1):
            a = swap(a,l,i)
            permute(a, l+1, r)
            a = swap(a,l,i) # backtrack
 
# Driver program to test the above function
string = "ABC"
n = len(string)
a = toList(string)
permute(a, 0, n-1)
 
