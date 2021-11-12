# https://www.lintcode.com/problem/149/

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Input: [3, 2, 3, 1, 2]
# Output: 1
# Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1

# Greedy - buy at the previous minimum prices and try sell at current day
# If more profit, update the result, otherwise hold. 

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        
        maximum_profit = 0
        minimum_price = float('inf')

        for i in range(len(prices)):
            maximum_profit = max(maximum_profit, prices[i] - minimum_price)
            minimum_price = min(minimum_price, prices[i])
        
        return maximum_profit
