# https://www.lintcode.com/problem/573

# Given a 2D grid, each cell is either a wall 2, 
# an house 1 or empty 0 (the number zero, one, two), 
# find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

# Returns the sum of the minimum distances from all houses to the post office. Return -1 if it is not possible.

# You cannot pass through wall and house, but can pass through empty.
# You only build post office on an empty.

# Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
# Output：8
# Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.

# Shortest distance on 2D array - BFS

# 1. Enumerate the empty places and for each do bfs to get shortest distance to each house. 
# 2. Enumerate the houses and get distances to this house for all empty places.

# 2 is better than 1 if there are many empty places and a few house.


class Solution:

    DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    HOUSE = 1
    WALL = 2
    EMPTY = 0   

    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        col_cnt = len(grid[0])
        row_cnt = len(grid)
        
        distance_sum = [[0 for i in range(col_cnt)] for j in range(row_cnt)]
        reachable_houses_cnt = [[0 for i in range(col_cnt)] for j in range(row_cnt)]

        total_houses_cnt = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == self.HOUSE:
                    total_houses_cnt += 1
                    self.__bfs((row, col), grid, distance_sum, reachable_houses_cnt)

        result = float('inf')

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == self.EMPTY and reachable_houses_cnt[row][col] == total_houses_cnt:
                    result = min(result, distance_sum[row][col])

        return -1 if result == float('inf') else result

    def __bfs(self, position, grid, distance_sum, reachable_houses_cnt):
        queue = collections.deque()

        # add start position to queue 
        queue.append(position)
        visited = {}
        visited[position] = 0

        while queue: 
            curr_pos = queue.popleft()
            for next_pos in self.__find_next(curr_pos):

                # 不在界外，不是房子或者墙，只能是空地
                if not self.__is_valid(next_pos, grid, visited):
                    continue

                # 空地到该房子距离
                visited[next_pos] = visited[curr_pos] + 1

                next_row = next_pos[0]
                next_col = next_pos[1]
                
                # 更新distance
                distance_sum[next_row][next_col] += visited[next_pos]
                reachable_houses_cnt[next_row][next_col] += 1

                queue.append(next_pos)

    def __find_next(self, curr_pos):

        next_positions = []

        curr_row = curr_pos[0]
        curr_col = curr_pos[1]

        for direction in self.DIRECTIONS:
            next_row = curr_row + direction[0]
            next_col = curr_col + direction[1]
            next_positions.append((next_row, next_col))
        
        return next_positions

    def __is_valid(self, position, grid, visited):

        if position in visited:
            return False

        row = position[0]
        col = position[1]

        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False

        if grid[row][col] == self.WALL or grid[row][col] == self.HOUSE:
            return False
        
        return True