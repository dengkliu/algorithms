# https://www.lintcode.com/problem/434/

# Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). 
# Originally, the 2D matrix is all 0 which means there is only sea in the matrix. 
# The list pair has k operator and each operator has two integer 
# A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island.
# Return how many island are there in the matrix after each operator.You need to return an array of size K.

# Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]
# Output: [1,1,2,2]

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class UnionFind:

    def __init__(self):
        self.father = {}
        self.num_of_sets = 0

    def add(self, x):
        if x in self.father:
            return 
        self.father[x] = None
        self.num_of_sets += 1
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        while x != root:
            old_father = self.father[x]
            self.father[x] = root
            x = old_father
        return root

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        self.father[root_x] = root_y
        self.num_of_sets -= 1

class Solution:

    def __init__(self):
        self.uf = UnionFind()
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):

        DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        result = []

        if not operators or len(operators) == 0:
            return result

        for i in range(len(operators)):
            row = operators[i].x
            col = operators[i].y

            curr = row * m + col

            self.uf.add(curr)

            for direction in DIRECTIONS:
                neighbor_row = row + direction[0]
                neighbor_col = col + direction[1]

                if neighbor_row < 0 or neighbor_row >= n \
                    or neighbor_col < 0 or neighbor_col >= m:
                    continue

                neighbor = neighbor_row * m + neighbor_col
                
                if neighbor not in self.uf.father:
                    continue
                
                self.uf.merge(curr, neighbor)
            
            result.append(self.uf.num_of_sets)
        
        return result
