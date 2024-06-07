# https://leetcode.com/problems/shortest-distance-from-all-buildings/

# You are given an m x n grid grid of values 0, 1, or 2, where:

# each 0 marks an empty land that you can pass by freely,
# each 1 marks a building that you cannot pass through, and
# each 2 marks an obstacle that you cannot pass through.
# You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

# Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

# The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        sum_dist = [[0] * n for _ in range(m)]
        house_cnt = [[0] * n for _ in range(m)]

        total_house_cnt = 0
        max_houses_reach = [0]
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c, house_explored):
            queue = collections.deque()
            queue.append((r, c, 0))
            seen = set()
            seen.add((r, c))

            while queue:
                x, y, dist = queue.popleft()
                for dx, dy in DIRECTIONS:
                    x_n, y_n = x + dx, y + dy
                    if x_n in range(m) and y_n in range(n) and (x_n, y_n) not in seen and grid[x_n][y_n] == -house_explored:
                        sum_dist[x_n][y_n] += dist + 1
                        house_cnt[x_n][y_n] += 1
                        grid[x_n][y_n] -= 1
                        queue.append((x_n, y_n, dist + 1))
                        seen.add((x_n, y_n))

        house_explored = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:                    
                    total_house_cnt += 1
                    bfs(r, c, house_explored)
                    house_explored += 1
        
        min_dist_to_houses = float('inf')
    
        for r in range(m):
            for c in range(n):
                if house_cnt[r][c] == total_house_cnt:
                    min_dist_to_houses = min(min_dist_to_houses, sum_dist[r][c])

        return min_dist_to_houses if min_dist_to_houses != float('inf') else -1