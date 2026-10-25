class Solution:
    def search(self, nums: list[int], target: int) -> bool:

        l,r = 0,len(nums)-1
        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target:
                return True
            if nums[m] == nums[l] == nums[r]: # when all the three pointers are equal which can happen in this case we have to decrease the search space 
                                              # because we can't find which part is sorted part so decreasing the search space we will eventually get the
                                              # different elment in one of the pointers and we can continue to elemenate the wrong part 
                r-=1
                l+=1
            elif nums[l]<=nums[m]:
                if nums[l]<=target<=nums[m]:
                    r = m-1
                else:
                    
                    l = m+1
            else:
                if nums[m]<=target<=nums[r]:
                    l = m+1
                else:
                    
                    r = m-1
        
        return False
        
            

#time complexity 
#average case = O(log n)
#worst case = O(n//2) = O(n)
#space complexity = O(1)
