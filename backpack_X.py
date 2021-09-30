# https://www.lintcode.com/problem/801

# You have a total of n yuan. 
# Merchant has three merchandises and their prices are 150 yuan, 250 yuan and 350 yuan. 
# And the number of these merchandises can be considered as infinite. 
# After the purchase of goods need to be the remaining money to the businessman as a tip, finding the minimum tip for the merchant.

# Input:  n = 900
# Output:  0

class Solution:
    """
    @param n: the money you have
    @return: the minimum money you have to give
    """
    def backPackX(self, n):
        prices = [150, 250, 300]

        dp = [[0 for _ in range(n + 1)] for _ in range(4)]

        for i in range(1, 4):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j]
                if (j >= prices[i - 1]):
                    dp[i][j] = max(dp[i][j], dp[i][j - prices[i-1]] + prices[i-1])
        
        return n - dp[3][n]
