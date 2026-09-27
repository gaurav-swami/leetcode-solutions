class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = prices[0]
        for sell in prices:
            max_profit = max( sell-buy, max_profit)
            buy = min(buy,sell)
        
        return max_profit


#time complexity - O(n)
#space complexity - O(1)

#for faster solution using if else 
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
