# You are climbing a stair case. 
# It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# n = 3
# 3

# 最简单的dp 把当前问题分解为若干个之前的子问题

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n == 0:
            return 0

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n] 