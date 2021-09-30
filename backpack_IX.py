# https://www.lintcode.com/problem/800

# You have a total of n thousand yuan, hoping to apply for a university abroad. 
# The application is required to pay a certain fee. 
# Give the cost of each university application and the probability of getting the University's offer, 
# and the number of university is m. If the economy allows, you can apply for multiple universities. 
# Find the highest probability of receiving at least one offer.

class Solution:
    """
    @param n: Your money
    @param prices: Cost of each university application
    @param probability: Probability of getting the University's offer
    @return: the  highest probability
    """

    # dp[i][j] -- given i universities, 
    # what is the possiblity of getting at least 1 offer
    def backpackIX(self, n, prices, probability):
        # write your code here
        
        if not prices or len(prices) == 0:
            return 0
        
        m = len(prices)
        
        dp = [[0.00 for _ in range(n + 1)] for _ in range(2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i%2][j] = dp[(i-1)%2][j]
                if j >= prices[i-1]:
                    dp[i%2][j] = max(dp[i%2][j], 1.00 - (1.00 - dp[(i-1)%2][j - prices[i-1]]) * (1.00 - probability[i-1]))
        
        return dp[m%2][n]