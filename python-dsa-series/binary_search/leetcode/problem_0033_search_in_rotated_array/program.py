class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l,r = 0,len(nums)-1
        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m
            if nums[l]<=nums[m]:
                if nums[l]<=target<=nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m]<=nums[r]: 
                if nums[m]<=target<=nums[r]:
                    l = m+1
                else:
                    r = m - 1
        
        return -1 
# to solve this remove check which part is sorted by breaking array from l to m and m to r and check in that if not in that then eliminate that part 

# time complexity = O(logn)
# space complexity = O(1)
            

        
