a = [1,2,3,4]

l = 0
r = 3
print(a)
while l<=r:
    a[l],a[r] = a[r], a[l]
    l+=1
    r-=1

print (a)
