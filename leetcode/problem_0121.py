class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = prices[0]
        for sell in prices:
            profit =  sell - buy
            if profit > max_profit:
                max_profit = profit
            if sell < buy:
                buy = sell
        
        return max_profit
