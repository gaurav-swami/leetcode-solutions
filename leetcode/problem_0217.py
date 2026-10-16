#solution 
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()

        for i in nums:
            if i in s:
                return True
            s.add(i)

        return False

#time complexity = O(n)
#space complexity = O(n)

#solution2 

class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
#time complexity = O(n*logn)
#space complexity = O(1)
