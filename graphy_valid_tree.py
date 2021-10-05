# https://www.lintcode.com/problem/178/
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.

class UnionFind:

    def __init__(self):
        self.father = {}

    def add(self, x):
        if x in self.father:
            return 
        self.father[x] = None
    
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

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:

    def __init__(self):
        self.uf = UnionFind()
        self.has_cycle = False

    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):

        if n != len(edges) + 1:
            return False
        
        for i in range(n):
            self.uf.add(i)

        for i in range(len(edges)):
            x = edges[i][0]
            y = edges[i][1]

            if self.uf.is_connected(x, y):
                return False

            self.uf.add(x)
            self.uf.add(y)
            self.uf.merge(x, y)
        
        return True