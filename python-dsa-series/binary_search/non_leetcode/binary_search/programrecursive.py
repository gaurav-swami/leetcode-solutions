def binarysearch(nums,low,high,target):
    if low>high:
        return -1

    mid = (low+high)//2

    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return binarysearch(nums,mid+1,high,target)
    else:
        return binarysearch(nums,low,mid-1,target)
    

nums = [1,2,3,4,5,6,7,8,9]
print(binarysearch(nums,0,len(nums)-1,6))
