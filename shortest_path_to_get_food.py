# https://leetcode.com/problems/shortest-path-to-get-food/description/

# You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

# You are given an m x n character matrix, grid, of these different types of cells:

# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        BLOCK = 'X'
        SPACE = 'O'
        FOOD = '#'
        DIRECTIONS = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        if not grid or not grid[0]:
            return -1

        queue = collections.deque()
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '*':
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, step = queue.popleft()
            for dr, dc in DIRECTIONS:
                r_new, c_new = r + dr, c + dc
                if r_new in range(len(grid)) and c_new in range(len(grid[0])) and (r_new, c_new) not in visited:
                    visited.add((r_new, c_new))
                    if grid[r_new][c_new] == FOOD:
                        return step + 1
                    if grid[r_new][c_new] == BLOCK:
                        continue
                    if grid[r_new][c_new] == SPACE:
                        queue.append((r_new, c_new, step + 1))
        
        return -1