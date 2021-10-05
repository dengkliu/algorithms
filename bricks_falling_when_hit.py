# https://www.lintcode.com/problem/1014/

# We have a grid of 1 and 0; the 1 in a cell represent bricks. 
# A brick will not drop if and only if it is directly connected to the bottom of the grid, or at least one of its (4-way) adjacent bricks will not drop.
# We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, 
# and then some other bricks may drop because of that erasure.
# Return an array representing the number of bricks that will drop after each erasure in sequence.

# The number of rows and columns in the grid will be in the range of [1, 200].
# It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
# An erasure may refer to a location with no brick - if it does, no bricks drop.
# It's lower when the row index is smaller - the cell whose row index is 0 connects to the bottom of the grid.

# Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# Output: [2]
# Explanation: If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.


class UnionFind:
    
    def __init__(self):
        self.father = {}
        self.size_of_sets = {}

    def add(self, x):
        if x in self.father:
            return 
        self.father[x] = None
        self.size_of_sets[x] = 1
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        while x != root:
            curr_father = self.father[x]
            self.father[x] = root
            x = curr_father
        return root
    
    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            self.size_of_sets[root_y] += self.size_of_sets[root_x]

    def get_size_of_set(self, x):
        return self.size_of_sets[self.find(x)]

class Solution:

    def __init__(self):
        self.uf = UnionFind()
        self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    """
    @param grid: a grid
    @param hits: some erasures order
    @return: an array representing the number of bricks that will drop after each erasure in sequence
    """
    def hitBricks(self, grid, hits):

        WALL = (-1, -1)

        self.uf.add(WALL)

        for i in range(len(hits)):
            row = hits[i][0]
            col = hits[i][1]
            grid[row][col] -= 1
           
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.uf.add((i, j))
                    if i == 0:
                        self.uf.merge((i, j), WALL)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.merge_neighbors(i, j, grid, self.uf)
       
        result = []
        
        for i in range(len(hits), 0, -1):

            original_set_size = self.uf.get_size_of_set(WALL)
            print("original_set_size")
            print(original_set_size)

            row = hits[i-1][0]
            col = hits[i-1][1]
            grid[row][col] += 1
            
            # 如果不是砖块 不会有改变
            if grid[row][col] != 1:
                result.insert(0, 0)
                continue

            # 先把砖块加到uf里
            self.uf.add((row, col))
            self.merge_neighbors(row, col, grid, self.uf)

            if row == 0:
                self.uf.merge((row, col), WALL)
        
            new_set_size = self.uf.get_size_of_set(WALL)


            if new_set_size > original_set_size:
                result.insert(0, new_set_size - original_set_size - 1)
            else:
                result.insert(0, 0)

        return result
    
    def merge_neighbors(self, row, col, grid, uf):
        
        for dx, dy in self.DIRECTIONS:
            next_row = row + dx
            next_col = col + dy

            if next_row < 0 or next_row >= len(grid) \
                or next_col < 0 or next_col >= len(grid[0]) or grid[next_row][next_col] != 1:
                continue
            
            self.uf.merge((row, col), (next_row, next_col))