# https://www.lintcode.com/problem/150/

# Given an array prices, which represents the price of a stock in each day.

# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 

# However, you may not engage in multiple transactions at the same time (ie, if you already have the stock, you must sell it before you buy again).

# Design an algorithm to find the maximum profit.
    
# Always sell if you find a profit 

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        
        if not prices:
            return 0
        
        maximum_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                maximum_profit += (prices[i] - prices[i-1])
        
        return maximum_profit
