def partition(nums,l,h):
    pivot = nums[l]
    i,j = l,h
    while i < j:
        while nums[i] <= pivot and i<h:
            i+=1
        while nums[j] > pivot and j>l:
            j-=1

        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[l],nums[j] = nums[j],nums[l]

    return j

def quick_sort(nums,low,high):
    if low<high:
        part = partition(nums,low,high)
        quick_sort(nums, low, part-1)
        quick_sort(nums,part+1,high)

nums = [4,1,7,6,3,2,8]
quick_sort(nums,0,6)
print(nums)

