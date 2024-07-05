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
        # [0 1 2 3 4 5 6 7]
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        coin_cnt = {}
        coin_cnt[0] = [0] * len(coins)

        for n in range(amount + 1):
            for index, coin in enumerate(coins):
                if coin <= n:
                    # If using this coin can help
                    if dp[n - coin] + 1 < dp[n]:
                        dp[n] = dp[n - coin] + 1
                        coin_cnt[n] = list(coin_cnt[n - coin])
                        coin_cnt[n][index] += 1                      

        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
