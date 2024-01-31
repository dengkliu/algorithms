# https://leetcode.com/problems/island-perimeter/

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        perimeter = [0]

        def bsf(row, col, grid, perimeter):
            queue = collections.deque()
            visited = set()
            queue.append((row, col))
            visited.add((row, col))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                cur_row, cur_col = queue.popleft()
                for dr, dc in directions:
                    next_row, next_col = cur_row + dr, cur_col + dc
                    if next_row not in range(len(grid)) or next_col not in range(len(grid[0])) or grid[next_row][next_col] == 0:
                        perimeter[0] += 1
                    elif grid[next_row][next_col] == 1 and (next_row, next_col) not in visited:
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    bsf(row, col, grid, perimeter)
                    return perimeter[0]