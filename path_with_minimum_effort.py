# https://leetcode.com/problems/path-with-minimum-effort/

# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        queue = collections.deque()
        min_effort = {}

        queue.append((0, 0))
        min_effort[(0, 0)] = 0

        DIRECTIIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        m = len(heights)
        n = len(heights[0])

        while queue:
            r, c = queue.popleft()
            for dr, dc in DIRECTIIONS:
                r_n, c_n = r + dr, c + dc
                if r_n in range(m) and c_n in range(n):
                    diff = abs(heights[r][c] - heights[r_n][c_n])
                    # what's the maximum path diff so far
                    path_diff = max(diff, min_effort[(r, c)])
                    # If we found a path with smaller max path diff, we update the max path
                    # and we re-insert the node to the queue
                    if (r_n, c_n) in min_effort:
                        if path_diff < min_effort[(r_n, c_n)]:
                            min_effort[(r_n, c_n)] = path_diff
                            if not (r_n == m -1  and c_n == n - 1):
                                queue.append((r_n, c_n))
                    else:
                        min_effort[(r_n, c_n)] = path_diff
                        queue.append((r_n, c_n))
            
        return min_effort[(m - 1, n - 1)]