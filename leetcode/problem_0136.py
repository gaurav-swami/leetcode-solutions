class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i

        return ans

# ^ is XOR and it has some properties
# a ^ 0 = a 
# a ^ a = 0
# a ^ b  = b ^ a 
# a ^ b ^ c = a ^ c ^ b

#time complexity is O(n)
#space complexity is O(1)
