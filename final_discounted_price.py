# https://www.lintcode.com/problem/1852/

# A shopkeeper needs to complete a sales task. He arranges the items for sale in a row.
# Starting from the left, the shopkeeper subtracts the price of the first lower or the same price item on the right side of the item from its full price.
# If there is no item to the right that costs less than or equal to the current item's price, the current item is sold at full price.
# You should return the actual selling price of each item.

# Input:
# Prices = [2, 3, 1, 2, 4, 2]
# Output: 
# [1, 2, 1, 0, 2, 2]
# Explanation: 
# The item 0 and 1 are each discounted by 1 unit, The item 3 at 2 units, is discounted 2 units, as would the item 4 at 4 units. 

class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """
    def FinalDiscountedPrice(self, prices):
        
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop(-1)
            stack.append(i)
        
        return prices            