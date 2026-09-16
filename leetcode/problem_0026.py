class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 1
        for i in range (1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left+=1
        return left 
        
 #time complexity is O(n)
 #space comlexity is O(1) 
 #mistake don't use set or dictionary to check you can check using the previous value as the array is sorted 
