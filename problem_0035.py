class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch (arr: List[int],target: int, start:int, end:int)->int:
            mid = start + (end-start)//2
            if start<=end:
                if arr[mid] > target:
                    if mid-1 == -1:
                        return mid
                    elif arr[mid-1]<target:
                        return mid
                    else:
                        return binarySearch(arr,target,start,mid-1)
                
                elif arr[mid]<target:
                    if mid+1 >= len(arr):
                        return mid+1
                    elif arr[mid+1] >target:
                        return mid+1
                    else:
                        return binarySearch(arr,target,mid+1,end)
                
                else:
                    return mid
            return -1



            
        
        return binarySearch(nums,target,0,len(nums)-1)