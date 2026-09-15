def reverse (a, l=0, r=None):
    if not r :
        r = len (a)-1
    if l>=r:
        return 
     
    a[r], a[l] = a[l], a[r]
    reverse( a, l+1, r-1)

arr = [ 1, 2, 3, 4 ]

reverse (arr)

print (arr)
