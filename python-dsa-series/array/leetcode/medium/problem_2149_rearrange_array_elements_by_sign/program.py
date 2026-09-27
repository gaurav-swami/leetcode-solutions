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

        return result

#so the time complexity is o(n) for creating that array but we are not counting that array for now we can explain that to interviewer
#and also that the auxilary spacer complexity is o(1) as the space that is taken is used to return the output not the operation so

#time complexity = O(n)
#space complexity = O(1) (auxilary)
#actual space complexity = O(n)
