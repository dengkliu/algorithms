# https://leetcode.com/problems/unique-paths/description/

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        memo = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                memo[row][col] = memo[row-1][col] + memo[row][col-1]
        
        return memo[m-1][n-1]