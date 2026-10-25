nums = [5,7,7,8,8,10]

def searchRange(nums, target):
    l,r = 0, len(nums)-1   
    ans2 = -1
    ans = -1
    while l<=r:
        m = l+(r-l)//2

        if nums[m] == target:
            ans = m
            l = m+1
        elif nums[m]<target:
            l = m + 1 
        
        else:
            r = m - 1   
        
    l,r = 0, len(nums)-1
    while l<=r:
        m = l+(r-l)//2

        if nums[m] == target:
            ans2 = m 
            r = m- 1
        elif nums[m] > target:
            r = m- 1
        else:
            l = m+ 1
    return (ans2,ans)

print(searchRange(nums,12))

#time complexity = O(2logn)
#space complexity = O(1)


#okay so these lower and upper bound solution


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
