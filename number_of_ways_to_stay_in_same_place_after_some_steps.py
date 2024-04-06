# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/description/

# You have a pointer at index 0 in an array of size arrLenarrLen.
# At each step, you can move 1 position to the left, 1 position to the right in the array 
# or stay in the same place (The pointer should not be placed outside the array at any time).
# Given two integers steps and arrLen, return the number of ways such that your pointer still 
# at index 0 after exactly steps steps.

# Since the answer may be too large, return it modulo 10^9 + 7

# 坐标型动态规划

class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    # dp[i][j] -- at step i, number of ways staying at index j
    def numWays(self, steps, arrLen):
        # write your code here
        if arrLen == 1:
            return 1
        
        # 10 to 9 power
        MOD = 10**9 + 7

        right_bound = min(steps//2 + 1, arrLen)

        dp = [[0] * right_bound for _ in range(steps + 1)]

        dp[0][0] = 1

        for step in range(1, steps + 1):
            # 停在0这个位置 
            dp[step][0] = (dp[step - 1][0] + dp[step - 1][1])% MOD
            # 停在最后一个位置
            dp[step][right_bound - 1] = (dp[step - 1][right_bound - 1] + dp[step - 1][right_bound - 2])%MOD
            for index in range(1, right_bound - 1):
                dp[step][index] = sum([
                    dp[step - 1][index], 
                    dp[step - 1][index - 1], 
                    dp[step - 1][index + 1]
                    ])%MOD

        return dp[steps][0]
