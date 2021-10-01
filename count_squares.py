# https://www.lintcode.com/problem/1869/

# Given a m * n matrix of ones and zeros, please count and return the number of square submatrix completely composed of 1.

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300

# Input: 
# matrix =
# [
#  [0,1,1,1],
#  [1,1,1,1],
#  [0,1,1,1]
# ]
# Output: 
# 15

class Solution:
    """
    @param matrix: a matrix
    @return: return how many square submatrices have all ones
    """
    def countSquares(self, matrix):
        
        if not matrix or len(matrix) == 0:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0 for i in range(m)] for i in range(n)]

        for i in range(n):
            dp[i][0] = matrix[i][0]

        for i in range(m):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        square_cnt = 0

        for i in range(n):
            for j in range(m):
                square_cnt += dp[i][j]
        

        return square_cnt