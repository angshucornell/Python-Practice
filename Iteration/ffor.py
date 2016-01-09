import sys
print range(10)


def  StairCase(t):
    n = t+1
    for i in range(n):
        for j in range (n):
            if i + j >= n :
#                print "#",
                 sys.stdout #
	    else:
                sys.stdout " "
#		print " ",        
        print "\n"  
       
StairCase(6)
