# https://www.lintcode.com/problem/1607/

# There are G criminals are going to plan a series of criminal activity.
# Given two arrays named groups and profit represent the i-th criminal activity needs groups[i] members and it will get a profit profit[i].
# A member can only participate in one criminal activity at the same time.
# The purpose of the gang is to get at least p profit. Your task is to calculate how many options are available.
# You need to return the answer module 10^9 + 7

# Input: G = 5, P = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: 
# To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.

# 典型的背包类DP问题
# dp[i][j][k] --> 当有i个activity的时候，刚好用了k个人，达到>= j的profit有多少中方法    
# dp[i][j][k] = 假如做这个activity, dp[i-1][j-profit[i]][k-group[i]] --- 这里注意 当 j <= profit[i] 或者 k <= group[i]  等价于 0
#               假如不做这个activity, dp[i-1][j][k]

class Solution:
    """
    @param G: The people in a gang.
    @param P: A profitable scheme any subset of these crimes that generates at least P profit.
    @param group: The i-th crime requires group[i] gang members to participate.
    @param profit: The i-th crime generates a profit[i].
    @return: Return how many schemes can be chosen.
    """

    def profitableSchemes(self, G, P, group, profit):

        MOD = 10**9 + 7
        
        dp = [
            [[0] * (G + 1) for _ in range(P + 1)] 
            for row in range(len(group) + 1)
        ]

        # 背包问题的初始化尽量简单一点吧 只考虑第一个元素
        dp[0][0][0] = 1

        for i in range(1, len(group) + 1):
            for j in range(P + 1):
                for k in range(G + 1):
                    # 可以不做
                    dp[i][j][k] += dp[i-1][j][k]
                    
                    # 人数不够 没法做
                    if k < group[i-1]:
                        continue

                    # 人数够，那就做
                    prev_profit = max(0, j - profit[i-1])
                    dp[i][j][k] += dp[i-1][prev_profit][k-group[i-1]]
        
        total_options = 0
        # 可以用0到G个人
        for i in range(G+1):
            total_options += dp[len(group)][P][i]

        return total_options%MOD
