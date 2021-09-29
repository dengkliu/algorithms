# https://www.lintcode.com/problem/1798/
# There are N piles of stones arranged in a row. The i-th pile has stones[i] stones.
# A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.
# Find the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

# Input: stones = [3,2,4,1], K = 2
# Output: 20
# Explanation: 
# We start with [3, 2, 4, 1].
# We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
# We merge [4, 1] for a cost of 5, and we are left with [5, 5].
# We merge [5, 5] for a cost of 10, and we are left with [10].
# The total cost was 20, and this is the minimum possible.

# 典型的interval dp
# 比起之前的问题，又多了一个变量，那就是每次合并的数量
# 把这个也放到dp矩阵里去
# dp[i][j][k] --> 把区间[i, j]合并为k堆石子的最小代价
# dp[i][i][1] = 0
# dp[i][j][1] = dp[i][j][K] + sum[i:j]
# 对 k 从 2 到 K --
# 先把这些合成K堆
# dp[i][j][k] = min(dp[i][mid][k-1] + dp[mid+1][j][1])

class Solution:
    """
    @param stones: 
    @param K: 
    @return: return a integer 
    """
    def mergeStones(self, stones, K):
        # write your code here

        n = len(stones)

        if (n-1)%(K-1) != 0:
            return -1

        prefix_sum = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i-1] + stones[i-1]  

        dp = [
            [[float('inf') for _ in range(K + 1)] for _ in range(n)]
            for _ in range(n)
        ]

        # 每个石子自己就是一堆
        for i in range(n):
            dp[i][i][1] = 0

        for _len in range(2, n + 1):
            for start in range (0, n - _len + 1):
                end = start + _len - 1
                # 试着两边分
                for mid in range(start, end):
                    for k in range(2, K + 1):
                        dp[start][end][k] = min(dp[start][end][k], dp[start][mid][k-1] + dp[mid+1][end][1]) 
                dp[start][end][1] = dp[start][end][K] + prefix_sum[end + 1] - prefix_sum[start]
                
        return -1 if dp[0][n-1][1] == float('inf') else dp[0][n-1][1]