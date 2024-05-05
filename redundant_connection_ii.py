# https://leetcode.com/problems/redundant-connection-ii/

# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

# The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

# Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def getParent(parent, u):
            p_u = parent[u]
            while p_u != parent[p_u]:
                p_u = parent[p_u]
            return p_u

        def isValidWithoutEdge(redundant, edges):
            # why do we initialize the parent to be each node itself
            parent = [i for i in range(len(edges) + 1)]
            
            for u, v in edges:
                if u == redundant[0] and v == redundant[1]:
                    continue
                p_u = getParent(parent, u)
                p_v = getParent(parent, v)

                parent[p_v] = parent[p_u]
            
            for u, v in zip(parent[1:], parent[2:]):
                if getParent(parent, u) != getParent(parent, v):
                    return False
            
            return True
        
        # don't need to define the uf class
        # we basically want to cache the parents info
        # but why we initialize a list of list?
        parents = [[] for i in range(len(edges) + 1)]

        result = []

        for u, v in edges:
            parents[v].append(u)
            # The first use case, one node has 2 parents
            if len(parents[v]) == 2:
                for i in parents[v]:
                    if isValidWithoutEdge([i, v], edges):
                        result.append([i, v])

        if result:
            return result[-1]

        parent = [i for i in range(len(edges) + 1)]

        for u, v in edges:
            p_u = getParent(parent, u)
            p_v = getParent(parent, v)

            # if these two nodes already connected
            if p_u == p_v :
                return [u, v]

            parent[p_v] = p_u
        
        return edges[-1]