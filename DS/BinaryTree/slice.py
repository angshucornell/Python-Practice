arr = [1, 2, 3, 4 ,5, 6 , 7, 8]
root = 4
ind = arr.index(root)


left = arr[:ind]
right = arr[ind+1:]

print root
print left
print right
