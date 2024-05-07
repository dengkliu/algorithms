# https://leetcode.com/problems/making-a-large-island/description/

# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        parent = {}
        max_island_size = 0
        island_size = collections.defaultdict(int)

        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        def add_island(x):
            if x in parent:
                return
            parent[x] = x
            island_size[x] = 1

        def find_parent(x):
            result = x
            while parent[result] != result:
                result = parent[result]
            cur = x

            # flat the tree
            while cur != result:
                cur_father = parent[cur]
                parent[cur] = result
                cur = cur_father

            return result

        def merge_island(x, y):
            if is_same_island(x, y):
                return
            f_x = find_parent(x)
            f_y = find_parent(y)
            if island_size[f_x] > island_size[f_y]:
                parent[f_y] = f_x
                island_size[f_x] += island_size[f_y]
            else:
                parent[f_x] = f_y
                island_size[f_y] += island_size[f_x]

        def is_same_island(x, y):
            if find_parent(x) == find_parent(y):
                return True
            return False

        if not grid:
            return 0

        n = len(grid)
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    add_island(r * n + c)
                    for dr, dc in directions:
                        r_new, c_new = r + dr, c + dc
                        if r_new in range(n) and c_new in range(n) and grid[r_new][c_new] == 1:
                            add_island(r_new * n + c_new)
                            merge_island(r * n + c, r_new * n + c_new)
        
        if island_size:
            max_island_size = max(island_size.values())
        
        # If there is no island just return it
        if max_island_size == 0:
            return 1
        elif max_island_size == n * n:
            return n * n

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    # why do we need a dictionary?
                    p_to_size = {}
                    for dr, dc in directions:
                        r_new, c_new = r + dr, c + dc
                        if r_new in range(n) and c_new in range(n) and grid[r_new][c_new] == 1:
                            new_p = find_parent(r_new * n + c_new)
                            if  new_p not in p_to_size:
                                p_to_size[new_p] = island_size[new_p]
                    
                    new_island_size = 1 + sum(p_to_size.values())    
                    max_island_size = max(max_island_size, new_island_size)

        return max_island_size