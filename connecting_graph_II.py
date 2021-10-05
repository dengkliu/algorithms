# https://www.lintcode.com/problem/590/

# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
# You need to support the following method:
# connect(a, b), an edge to connect node a and node b
# query(a), Returns the number of connected component nodes which include node a.

# Input:
# ConnectingGraph2(5)
# query(1)
# connect(1, 2)
# query(1)
# connect(2, 4)
# query(1)
# connect(1, 4)
# query(1)
# Output:[1,2,3,3]


class UnionFind:

    def __init__(self):
        self.father = {}
        self.size_of_set = {}
    
    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.size_of_set[x] = 1

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        self.father[root_x] = root_y
        self.size_of_set[root_y] += self.size_of_set[root_x]
        del self.size_of_set[root_x]
        return

    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]

        while x != root:
            old_father = self.father[x]
            self.father[x] = root
            x = old_father
        
        return root

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.uf = UnionFind()
        for i in range(1, n + 1):
            self.uf.add(i)
        # do intialization if necessary

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        self.uf.merge(a, b)
        # write your code here

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        return self.uf.size_of_set[self.uf.find(a)]
        # write your code here