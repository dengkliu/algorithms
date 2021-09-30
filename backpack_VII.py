# https://www.lintcode.com/problem/798/

# Assume that you have n yuan. There are many kinds of rice in the supermarket. 
# Each kind of rice is bagged and must be purchased in the whole bag. 
# Given the weight, price and quantity of each type of rice, find the maximum weight of rice that you can purchase.

# Input:  n = 8, prices = [3,2], weights = [300,160], amounts = [1,6]
# Output:  640
# Explanation:  Buy the second rice(price = 2) use all 8 money.

class Solution:
    """
    @param n: the money of you
    @param prices: the price of rice[i]
    @param weight: the weight of rice[i]
    @param amounts: the amount of rice[i]
    @return: the maximum weight
    """
    # dp[i][j] -- for first i kinds of rice, what is the maximum weight you can get with n yuan
    def backPackVII(self, n, prices, weight, amounts):
        # write your code here

        if n == 0:
            return 0

        if not prices or len(prices) == 0:
            return 0

        item_count = len(prices)

        dp = [[0 for _ in range(n + 1)] for _ in range(2)]

        for item in range(1, item_count + 1):
            for price in range(1, n + 1):
                dp[item%2][price] = dp[(item - 1)%2][price]
                for item_cnt in range(1, amounts[item - 1] + 1):
                    if (item_cnt * prices[item - 1] <= price):
                        dp[item%2][price] = max(dp[item%2][price], \
                            dp[(item - 1)%2][price - item_cnt * prices[item - 1]] + item_cnt * weight[item - 1])

# 想想这种写法错误在哪里                    
#                   if (prices[item - 1] <= price):
#                       if item_cnt == 1:
#                            dp[item][price] = max(dp[item][price], \
#                                dp[item - 1][price - prices[item - 1]] + weight[item - 1])
#                        else:
#                            dp[item][price] = max(dp[item][price], \
#                                dp[item - 1][price - prices[item - 1]] + weight[item - 1])
#
        return dp[item_count%2][n]           


