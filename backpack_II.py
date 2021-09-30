# There are n items and a backpack with size m. 
# Given array A representing the size of each item and array V representing the value of each item.
# What's the maximum value can you put into the backpack?

# A[i], V[i], n, m are all integers.
# You can not split an item.
# The sum size of the items you want to put into backpack can not exceed m.
# Each item can only be picked up once
# m <= 1000 len(A),len(V)<=100

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        
        if not A or len(A) == 0:
            return 0

        n = len(A)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(2)]

        for item in range(1, n + 1):
            for size in range(1, m + 1):
                dp[item%2][size] = dp[(item -1)%2][size]
                if A[item - 1] <= size:
                    dp[item%2][size] = max(dp[item%2][size], dp[(item - 1)%2][size - A[item - 1]] + V[item - 1])
        
        return dp[n%2][m]