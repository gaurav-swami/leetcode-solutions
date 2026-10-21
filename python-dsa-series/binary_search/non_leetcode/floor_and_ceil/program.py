def getFloorAndCeil(a, n, x):
    floor,ceil = -1,-1

    l,r = 0,n-1

    while l<=r:

        m = l+(r-l)//2

        if a[m]==x:
            return [a[m],a[m]]

        elif a[m]>x:
            ceil = a[m]
            r = m - 1
        else:
            floor = a[m]
            l = m + 1

    return [floor,ceil]
#time complexity = O(log2n)
#space complexity = O(1)
