# https://www.lintcode.com/problem/1447/

# Enter a matrix of length L, width W and three points that must pass through. 
# How many ways can you walk from the upper left corner to the lower right corner？
# (Each step can only go right or down). The input is guaranteed that there is at least one legal path. 
# You only need to return the solution number mod 1000000007.

# 1 <= l,w <= 2000

# Given `l=1`, `w=5`. The three points are `[1,2],[1,3],[1,4]`. Return `1`.
# Input:
# 1
# 5
# [[1,2],[1,3],[1,4]]
# Output:
# 1
# Explanation:
# [1,1]->[1,2]->[1,3]->[1,4]->[1,5]
# The sum is 1.

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l: The length of the matrix
    @param w: The width of the matrix
    @param points: three points 
    @return: The sum of the paths sum
    """
    # The index is 1 based!!!
    def calculationTheSumOfPath(self, l, w, points):

        MOD = 10**9 + 7

        # 技巧1: 对object进行排序
        # sorted(iterables, key = lambda object: (object.attribute1, object.attribute2)
        points = sorted(points, key = lambda point: (point.x, point.y))

        result = 1

        if points[0].x != 1 and points[0].y != 1:
            points = [Point(1, 1)] + points
        
        if points[2].x != l and points[2].y != 1:
            points = points + [Point(l, w)]

        for i in range(1, len(points)):
            result *= self.get_path_sum(points[i].x - points[i-1].x, points[i].y - points[i-1].y)
            result %= MOD

        return result

    def get_path_sum(self, l, w):

        MOD = 10**9 + 7
        
        dp = [[0 for c in range(w + 1)] for r in range(l + 1)]

        # 初始化, 第一行都可以从右边来，第一行全部为1
        for i in range(0, w + 1):
            dp[0][i] = 1

        for j in range(0, l + 1):
            dp[j][0] = 1

        for i in range(1, l + 1):
            for j in range(1, w + 1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                dp[i][j] %= MOD

        return dp[l][w]

