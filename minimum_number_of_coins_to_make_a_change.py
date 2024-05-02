# https://leetcode.com/problems/coin-change/description/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[amount + 1] - the minimum number of coins needed for amount 
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for n in range(amount + 1):
            for coin in coins:
                if coin <= n:
                    dp[n] = min(dp[n], dp[n - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1