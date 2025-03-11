from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit =  prices[r]-prices[l]
                maxP = max(profit,maxP)
            else:
                l = r
            r+=1
        return maxP

x = Solution()
print(x.maxProfit([7,1,5,3,6,4]))

