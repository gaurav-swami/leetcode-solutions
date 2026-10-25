def binarysearch(nums,target):
    n = len(nums)
    l,r = 0,n-1

    while l<=r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    

    return -1


lista = [1,2,3,4,5,6,7,8,9]
print(binarysearch(lista,6)) 
