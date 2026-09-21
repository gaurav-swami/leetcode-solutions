class Solution(object):
    def missingNumber(self, nums):
       
        n = len(nums)
        return n*(n+1)/2 - sum(nums)


#space complexity = O(1)
#time complexity = O(n)

#just subtract the sum of nums from sum of 0-n to get the missing number
