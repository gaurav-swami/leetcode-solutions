class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        maxi = 0
        count = 0
        
        for ele in s:
            if ele-1 not in s:
                count = 1
                x = ele
                while x+1 in s:
                    count+=1
                    x+=1
                
                maxi = max(maxi,count)

        return maxi 

#time complexity
#worst case = O(3n) as one is for creating set and second and third for iterating through set 2 times if all are in squence
# so O(n)

#space complexity
#O(n)
