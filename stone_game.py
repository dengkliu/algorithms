# https://www.lintcode.com/problem/476/

# There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
# The goal is to merge the stones in one pile observing the following rules:
# At each step of the game,the player can merge two adjacent piles to a new pile.
# The cost of each combination is the sum of the weights of the two piles of stones combined.
# Please find out the minimum cost of merging.

# Input: [4, 1, 1, 4]
# Output: 18
# Explanation:
#  1. Merge second and third piles => [4, 2, 4], score = 2
#  2. Merge the first two piles => [6, 4]，score = 8
#  3. Merge the last two piles => [10], score = 18

# 典型的区间型动态规划 --> 区间 最值
# 思路 -> 先求出小区间的解，在求大区间的解
# dp[i][j] --> 从i到j merge stones的最值
# for loop里面，应该loop不是i和j，每次loop，处理的是长度一样的小区间
# 因此, for loop的外围是区间长度，for loop的内部是区间起始的地方，然后用隔板法，在区间内部进行分割，枚举分割点

# for len in range(2, n + 1):
#     for start in range(1, n - len + 1):
#         end = start + len - 1
#         for mid in range(start, end):
#             dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + someting)

# dp[i][j] = min(dp[i][k] + dp[k+1][j]) + range sum from i to j
# 用前缀和 range_sum from i to j = prefix_sum[j+1] - prefix_sum[i]

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    # dp[i][j] -- 从 [i, j]的最小代价 
    # dp[i][j] = min(dp[i][k] + dp[k+1][j]) + sum[i][j]
    # dp[0][len(A) - 1]
    def stoneGame(self, A):
        # write your code here

        if not A or len(A) == 0:
            return 0

        size = len(A)

        # dp[i][j] -- 从 [i, j]的最小代价 
        dp = [[0 for _ in range(size)] for _ in range(size)]

        prefix_sum = [0] * (size + 1)

        for i in range(size):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]

        # _len -- 合并的石子数量，当_len = 1时 合并一个石头cost是0
        # 所以直接从2开始算起，最多可以合并n个石子
        for _len in range(2, size + 1):
            # start最多可以取到 size - _len
            for left in range(size - _len + 1): 
                right = left + _len - 1
                # 开始打擂台 初始化为最大值
                dp[left][right] = float('inf')
                for mid in range(left, right):
                    range_sum = prefix_sum[right + 1] - prefix_sum[left]
                    dp[left][right] = min(dp[left][right], \
                            dp[left][mid] + dp[mid+1][right] + range_sum)

        # 合并整个区间 从0到n
        return dp[0][size-1]  

