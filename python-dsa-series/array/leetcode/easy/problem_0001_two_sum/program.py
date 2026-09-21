class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicta = {}
        n = len(nums)
        for i in range(n):
            search = target-nums[i]
            if search in dicta:
                return [i,dicta[search]]
            dicta[nums[i]] = i

#time complexity = O(n)
#space complexity : O(n)
