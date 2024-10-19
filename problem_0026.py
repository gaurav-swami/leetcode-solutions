class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newLen = len(nums)-2
        i=0
        while i <=  len(nums)-2:
            if i>newLen:
                break
            elif nums[i]==nums[i+1]:
                del nums[i]
                newLen -= 1
            else:
                i+=1

        return len(nums)


















