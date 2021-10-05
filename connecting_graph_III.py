# https://www.lintcode.com/problem/591/

# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
# You need to support the following method:
# connect(a, b), an edge to connect node a and node b
# query(), Returns the number of connected component in the graph

# Input:
# ConnectingGraph3(5)
# query()
# connect(1, 2)
# query()
# connect(2, 4)
# query()
# connect(1, 4)
# query()
# Output:[5,4,3,3]

class UnionFind:

    def __init__(self):
        self.father = {}
        self.num_of_set = 0
    
    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.num_of_set += 1

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        self.father[root_x] = root_y
        self.num_of_set -= 1
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

class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.uf = UnionFind()
        for i in range(1, n+1):
            self.uf.add(i)
        # initialize your data structure here.
    
    def connect(self, a, b):
        self.uf.merge(a, b)
        # write your code here

    """
    @return: An integer
    """
    def query(self):
        return self.uf.num_of_set
        # write your code here