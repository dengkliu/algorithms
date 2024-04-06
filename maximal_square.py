# https://leetcode.com/problems/maximal-square/description/

# Given a 2D binary matrix filled with 0's and 1's, 
# find the largest square containing all 1's and return its area.

# Input:
# [
#  [1, 0, 1, 0, 0],
#  [1, 0, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 0, 0, 1, 0]
# ]
# Output: 4

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or len(matrix) == 0:
            return 0

        result = 0

        n = len(matrix)
        m = len(matrix[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            dp[0][i] = matrix[0][i]
            result = max(result, dp[0][i])

        for i in range(n):
            dp[i][0] = matrix[i][0]
            result = max(result, dp[i][0])
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    result = max(result, dp[i][j])
        
        result = result*result
        
        return result
