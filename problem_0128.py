class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num =  set(nums)
        max_sub = 0
        for i in num:
            if (i-1) not in num:
                j=i
                sub = 0
                while j in num:
                    sub+=1
                    j=j+1
            
                max_sub = max(sub,max_sub)
        return max_sub

                



        


                
        