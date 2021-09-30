# https://www.lintcode.com/problem/92/

# Given n items with size A[i] and 
# an integer m denotes the size of a backpack. How full you can fill this backpack?

# array = [3,4,8,5]
# backpack size = 10

# 最基本的backpack题目
# dp[i][j] -- 对于前i个item, 容量为i的背包，最多能装多少
# dp[i][j] = 1. 如果当前的size能装下， 装进去的话, 空间还剩下j - size[i-1], 最多能装dp[i-1][j-size[i-1]]
#               所以装的话 是dp[i-1][j-size[i-1]] + size[i-1]不装的话是dp[i-1][j]
#               选其中一个大的 是 max(dp[i-1][j-size[i-1]] + size[i-1], dp[i-1][j])
#            2. 如果装不下，只能是dp[i-1][j])
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        
        if not A or len(A) == 0:
            return 0

        n = len(A)

        dp = [[0 for _ in range(m +1 )] for _ in range(n + 1)]
        # write your code here

        for item in range(1, n + 1):
            for size in range(1, m + 1):
                # 如果能装下，就试着装进去，但是会挤占之前的Item的空间
                if (size >= A[item - 1]):
                    dp[item][size] = max(dp[item - 1][size], dp[item - 1][size - A[item - 1]] + A[item - 1])
                # 不然就只能装之前的item
                else:
                    dp[item][size] = dp[item - 1][size]
        
        return dp[n][m]

