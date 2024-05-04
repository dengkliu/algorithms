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

        def dfs(r, c, visited):
            for dr, dc in DIRECTIONS:
                r_new, c_new = r + dr, c + dc
                if r_new in range(m) and c_new in range(n):
                    if heights[r][c] <= heights[r_new][c_new] and (r_new, c_new) not in visited:
                        visited.add((r_new, c_new))
                        dfs(r_new, c_new, visited)
                

        for c in range(n):
            p_visited.add((0, c))
            dfs(0, c, p_visited)
            a_visited.add((m-1, c))
            dfs(m-1, c, a_visited)
        
        for r in range(m):
            p_visited.add((r, 0))
            dfs(r, 0, p_visited)
            a_visited.add((r, n-1))
            dfs(r, n-1, a_visited)
 
        return p_visited.intersection(a_visited)
