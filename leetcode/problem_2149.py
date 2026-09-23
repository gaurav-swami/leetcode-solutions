class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p,n = 0,1
        result = [0] * len(nums)

        for i in nums:
            if i < 0:
                result[n] = i
                n+=2
            else:
                result[p] = i
                p+=2
