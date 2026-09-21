class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bigger = float("-inf")
        summ = 0 
        for i in nums:
            if summ<0:        
                summ = 0
            summ+=i
            bigger = max(summ,bigger)
        
        return bigger

#time complexity = O(n)
#space complexity = O(1)
