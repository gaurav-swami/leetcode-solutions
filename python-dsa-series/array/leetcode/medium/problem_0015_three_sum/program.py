class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        n = len(nums)
        for i in range(n):
            search = 0-nums[i]
            track = set()
            for j in range(i+1,n):
                ele_j = nums[j]
                if search - ele_j in track:
                    new_comb = tuple(sorted([ nums[i], search-ele_j, ele_j ] ))
                    res.add(new_comb)
                else:
                    track.add(ele_j)

        res = list(res)
        return res

