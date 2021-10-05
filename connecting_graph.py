# https://www.lintcode.com/problem/589/

# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
# You need to support the following method:
# connect(a, b), add an edge to connect node a and node b.
# query(a, b), check if two nodes are connected

# Input:
# ConnectingGraph(5)
# query(1, 2)
# connect(1, 2)
# query(1, 3) 
# connect(2, 4)
# query(1, 4) 
# Output:
# [false,false,true]

class UnionFind:

    def __init__(self):
        self.father = {}
    
    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        self.father[root_x] = root_y
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

class ConnectingGraph:

    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.uf = UnionFind()
        for i in range(1, n+1):
            self.uf.add(i)
        # do intialization if necessary

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        self.uf.merge(a, b)


    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        return self.uf.is_connected(a, b)
