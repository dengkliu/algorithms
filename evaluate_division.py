# https://leetcode.com/problems/evaluate-division/

# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

class UnionFind:
    
    def __init__(self):
        # why do we need a dictionary of list?
        # parent[x][0] -- the parent value
        # parent[x][1] -- parent/x
        self.parent = collections.defaultdict(list)

    def add(self, x):
        if x not in self.parent:
            # why do we want to initialize an array here
            # why do we set the division parent/x as 1 here
            self.parent[x] = [x, 1]

    def merge(self, x, y, div):
        parent_x, div_x = self.find(x)
        parent_y, div_y = self.find(y)

        # div = x/y
        # so parent_x/parent_y = (parent_x/x) / (parent_y/y) * x/y
        if parent_x != parent_y:
            self.parent[parent_y] = [parent_x, (div_x / div_y) * div]

    def find(self, x):
        root = x
        div = 1

        while self.parent[root][0] != root:
            # why do we first do multiplication and then move upward the root?
            div =  div * self.parent[root][1]
            root = self.parent[root][0]
        
        # why do we need to flat the tree here?
        multiplier = 1
        while x != root:
            old_parent = self.parent[x][0]
            old_div = self.parent[x][1]
            self.parent[x] = [root, div/multiplier]
            multiplier = multiplier * old_div
            x = old_parent

        return root, div

    def isConnected(self, x, y):
        return self.find(x)[0] == self.find(y)[0]

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        uf = UnionFind()

        for [u, v], div in zip(equations, values):
            uf.add(u)
            uf.add(v)
            print(uf.parent)
            uf.merge(u, v, div)
            print(uf.parent)

        print(uf.parent)
        
        result = []
        for u, v in queries:
            if u not in uf.parent or v not in uf.parent:
                result.append(-1.0)
            elif not uf.isConnected(u, v):
                result.append(-1.0)
            else:
                # to get u/v, we want (parent/v)/(parent/u)
                parent_u = uf.parent[u]
                parent_v = uf.parent[v]
            
                result.append(parent_v[1]/parent_u[1])

        return result 