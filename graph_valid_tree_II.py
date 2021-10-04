# https://www.lintcode.com/problem/444/
# Please design a data structure which can do the following operations:
# 1. void addEdge(int a, int b):add an edge between node aa and node bb. It is guaranteed that there isn't self-loop or multi-edge.
# 2. bool isValidTree(): Check whether these edges make up a valid tree.

# Valid tree requires :
# 1. Number of nodes is 1 greater than number of edges
# 2. There is no cycle

# It is a valid tree if and only if:
# 1. The number of edges is 1 less than the number of nodes
# 2. 没有 cycle 
class Solution:

    father = {}
    num_of_edges = 0
    has_cycle = False

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root   

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        self.father[root_x] = root_y
    
    """
    @param a: the node a
    @param b: the node b
    @return: nothing
    """
    def addEdge(self, a, b):
        self.add(a)
        self.add(b)
        self.num_of_edges += 1

        if self.is_connected(a, b):
            self.has_cycle = True
        
        self.merge(a, b)

    """
    @return: check whether these edges make up a valid tree
    """
    def isValidTree(self):

        if len(self.father) != self.num_of_edges + 1:
            return False
        
        return not self.has_cycle