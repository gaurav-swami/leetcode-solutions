from typing import List

def rotate( nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        r = len(nums)-1
        while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        l=0
        r=k-1
        
        while l<r and r<len(nums):
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        l=k
        r=len(nums)-1
        while l<=r and r<len(nums):
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1

       
        
        print(nums)



nums = [1,2,3]
k = 4
rotate(nums,k)