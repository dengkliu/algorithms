# https://www.lintcode.com/problem/593

# There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.
# The goal is to merge the stones in one pile observing the following rules:
# At each step of the game,the player can merge two adjacent piles to a new pile.
# The score is the number of stones in the new pile.
# You are to determine the minimum of the total score.

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    # 典型的区间型dp 详情参见 stone game 
    # 因为是环形的，所以A[0]和A[n-1]也应该是一段可以合并的连续区间
    # 这里有个小技巧, 我们把原来的数组按照顺序延长一倍，比如[1, 2, 1]变成[1, 2, 1, 1, 2, 1]
    # 这样首尾就接上了
    # 而且起点和终点就不确定了
    # 这样我们最后得到的dp[i][i+n-1]就是以第i个数为起点得到的解 我们可以比较每一种可能然后得出解
    def stoneGame2(self, A):
        # write your code here
        if not A or len(A) == 0:
            return 0

        size = len(A)

        # dp[i][j] -- 从 [i, j]的最小代价 
        dp = [[0 for _ in range(2*size)] for _ in range(2*size)]

        prefix_sum = [0] * (2 * size + 1)

        for i in range(1, 2 * size + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i%size - 1]

        # _len -- 合并的石子数量，当_len = 1时 合并一个石头cost是0, 最多可以合并size个石头
        # 所以直接从2开始算起，最多可以合并n个石子
        for _len in range(2, size + 1):
            # left最多可以到 2*size - _len
            for left in range(2*size - _len + 1): 
                right = left + _len - 1
                # 开始打擂台 初始化为最大值
                dp[left][right] = float('inf')
                for mid in range(left, right):
                    range_sum = prefix_sum[right + 1] - prefix_sum[left]
                    dp[left][right] = min(dp[left][right], \
                            dp[left][mid] + dp[mid+1][right] + range_sum)

        result = float('inf')

        # 枚举起始点位置, i 从 0 到 n - 1
        for i in range(size):
            result = min(result, dp[i][i + size - 1])
        
        return result