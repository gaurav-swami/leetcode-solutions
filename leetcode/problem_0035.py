class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:
            mid = left + (right-left)//2

            if target==nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else: 
                left = mid + 1        
        return left




    # space complexity = O(1)

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums)

        while l<r:
            mid = l+(r-l)//2

            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
        
        return l
