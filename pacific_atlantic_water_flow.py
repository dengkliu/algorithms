# https://leetcode.com/problems/pacific-atlantic-water-flow/

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights)
        n = len(heights[0])
        DIRECTIONS = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        result = []

        p_visited = set()
        a_visited = set()

        p_queue = collections.deque()
        a_queue = collections.deque()

        for row in range(m):
            p_queue.append((row, 0))
            a_queue.append((row, n - 1))

        for col in range(n):
            p_queue.append((0, col))
            a_queue.append((m - 1, col))

        while p_queue:
            r, c = p_queue.popleft()
            p_visited.add((r, c))
            for dr, dc in DIRECTIONS:
                r_new, c_new = r + dr, c + dc
                if r_new in range(m) and c_new in range(n) and \
                 heights[r][c] <= heights[r_new][c_new] and \
                 (r_new, c_new) not in p_visited:
                    p_visited.add((r_new, c_new))
                    p_queue.append((r_new, c_new))

        while a_queue:
            r, c = a_queue.popleft()
            a_visited.add((r, c))
            for dr, dc in DIRECTIONS:
                r_new, c_new = r + dr, c + dc
                if r_new in range(m) and c_new in range(n) and \
                 heights[r][c] <= heights[r_new][c_new] and \
                 (r_new, c_new) not in a_visited:
                    a_visited.add((r_new, c_new))
                    a_queue.append((r_new, c_new))
                
        return p_visited.intersection(a_visited)