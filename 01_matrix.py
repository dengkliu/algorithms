# https://leetcode.com/problems/01-matrix/

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat:
            return []
        
        if not mat[0]:
            return [[]]
        
        m = len(mat)
        n = len(mat[0])
        result = [row[:] for row in mat]
        queue = collections.deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (next_row, next_col) not in seen and next_row in range(m) and next_col in range(n):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                    result[next_row][next_col] = steps + 1
                    
        
        return result