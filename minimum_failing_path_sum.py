# https://www.lintcode.com/problem/1711/

# Given a square array of integers A, we want the minimum sum of a falling path through A.
# A falling path starts at any element in the first row, and chooses one element from each row. 
# The next row's choice must be in a column that is different from the previous row's column by at most one.

class Solution:
    """
    @param A: the given array
    @return: the minimum sum of a falling path
    """

    # dp[i][j] -> 从第i行，第j列落下来的最小路径是多少
    # dp[i][j] -> A[i][j] + min([dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]])

    def minFallingPathSum(self, A):
        # Write your code here
        n = len(A)

        dp = [[0] * (n) for _ in range(2)]

        for i in range(n):
            dp[0][i] = A[0][i]

        for i in range (1, n):
            # The first number
            dp[i%2][0] = A[i][0] + min([dp[(i-1)%2][0], dp[(i-1)%2][1]])
            # The last number
            dp[i%2][n-1] = A[i][n-1] + min([dp[(i-1)%2][n-2], dp[(i-1)%2][n-1]])

            for j in range (1, n-1):
                dp[i%2][j] = A[i][j] + min([dp[(i-1)%2][j], dp[(i-1)%2][j-1], dp[(i-1)%2][j+1]])
        
        return min(dp[(n-1)%2])