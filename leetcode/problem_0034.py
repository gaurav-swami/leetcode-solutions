
class Solution:
    def lowerbound(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        return l

    def upperbound(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return l

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lowerbound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = self.upperbound(nums, target)

        return [lb, ub - 1]
