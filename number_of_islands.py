# https://leetcode.com/problems/number-of-islands/description/

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def bsf(row, col, grid, queue, visited):
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                cur_row, cur_col = queue.popleft()
                directions=[(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in directions:
                    next_row, next_col = cur_row + dr, cur_col + dc
                    if next_row in range(len(grid)) and next_col in range(len(grid[0])) and grid[next_row][next_col] == '1' and (next_row, next_col) not in visited:
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))


        queue = collections.deque()
        visited = set()
        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bsf(row, col, grid, queue, visited)
                    result += 1
 
        return result