
# https://www.lintcode.com/problem/440/

# Given n kinds of items, and each kind of item has an infinite number available. 
# The i-th item has size A[i] and value V[i].
# Also given a backpack with size m. What is the maximum value you can put into the backpack?

# Input: A = [2, 3, 5, 7], V = [1, 5, 2, 4], m = 10
# utput: 15
# Explanation: Put three item 1 (A[1] = 3, V[1] = 5) into backpack.

class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        if not A or len(A) == 0:
            return 0
        
        n = len(A)
        
        dp = [[0 for _ in range(m +1 )] for _ in range(n + 1)]

        for item in range(1, n + 1):
            for size in range(1, m + 1):
                # 完全不装这个item
                dp[item][size] = dp[item - 1][size]
                # 如果可以装的话，就试试，而且可以反复装 
                # 所以是 dp[item][size - A[item - 1]] 而不是 dp[item-1][size - A[item - 1]]
                if (size >= A[item - 1]):
                    dp[item][size] = max(dp[item][size], dp[item][size - A[item - 1]] + V[item - 1])
        return dp[n][m]