
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r = 0,len(num  s)-1
        
        while l<=r:
            m = l + (r-l)//2
            if nums[l]<=nums[m]<=nums[r]:  # if we already in the sorte dpart then just return first element 
                return nums[l]                                           # so that we can save time and memoery
            elif nums[m]>nums[r]:          # if nums[m] > nums[r] that mean the first element will be on the right of m so l = m+1
                l = m + 1
            else:
                r = m                      # but if the nums[m]  > nums[r] then the first element can be at m or  before m so r = m


#time complexity = O(logn)
#space complexity = O(1)
