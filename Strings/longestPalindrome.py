# a b c d a b 
def lps(str):
    n = len(str)
    print str
    print range(n)
    print range(2, n)
 
    # Create a table to store results of subproblems
#    L = [[0 for x in range(n)] for x in range(n)]
    L = [ [0] * n for x in range(n) ]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
    
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # cl is length of substring
    for cl in range(2, n+1):
        print 'n-cl+1'
       
        print n-cl+1
        for i in range(n-cl+1):
            j = i+cl-1
            print 'cl = ', cl , ' i = ', i , ' j = ',   j
            if str[i] == str[j] and cl == 2:
                print 'case 1'
                L[i][j] = 2
            elif str[i] == str[j]:
                print 'case 2'
                L[i][j] = L[i+1][j-1] + 2
            else:
                print 'case 3'
                L[i][j] = max(L[i][j-1], L[i+1][j]);
 
#    print L
    return L[0][n-1]
 
# Driver program to test above functions
#seq = "GEEKS FOR GEEKS"
seq = "GEEKS"
n = len(seq)
print("The length of the LPS is " + str(lps(seq)))




