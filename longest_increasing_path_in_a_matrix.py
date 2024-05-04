# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# DFS + memorization
# Why cannot we use dp here?
# Why BFS is not an efficient option here?
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        m = len(matrix)
        n = len(matrix[0])
        
        cache = [[1 for _ in range(n)] for _ in range(m)]

        def dfs(r, c):
            # no need to calculate it again
            if cache[r][c] != 1:
                return cache[r][c]
            for dr, dc in DIRECTIONS:
                next_r, next_c = r + dr, c + dc
                if next_r in range(m) and next_c in range(n):
                    if matrix[r][c] < matrix[next_r][next_c]:
                        cache[r][c] = max(cache[r][c], 1 + dfs(next_r, next_c))
            return cache[r][c]

        result = 0
        for r in range(m):
            for c in range(n):
                result = max(result, dfs(r, c))

        return result

