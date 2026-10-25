arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 12 


def lower_bound(arr,target):
    n = len(arr)
    l,r = 0, n - 1
    bound = n 
    while l<=r:
        m = l + (r-l)//2

        if arr[m] >=  target:
            bound = m
            r = m-1
        else:
            l = m+1

    return bound

def upper_bound(arr,target):
    n = len(arr)
    l,r = 0, n - 1
    bound = n 
    while l< r:
        m = l + (r-l)//2

        if arr[m] >  target:
            bound = m
            r = m-1
        else:
            l = m+1

    return bound
print(lower_bound(arr,target))

